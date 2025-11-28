import psutil
import os

class Behaviour:
    def __init__(self, procName=None):
        self.count = 1
        self.score = 0
        self.BadPathArray = {}
        for proc in psutil.process_iter():
            if procName != None:
                if proc.name() == procName:
                    self.processObj = proc
                    self.ProcID = self.processObj.pid
            else:
                self.processObj = proc
                self.ProcID = self.processObj.pid
                print(f"[DelEverything] [{self.count}] Scanning process: {proc.name()}. PID: {self.processObj.pid}")
                self.count += 1
                ProcessBehav = self.CheckProcBehaviour()
                try:
                    NetworkBehav = self.CheckProcNetwork(True)
                except:
                    NetworkBehav = 0
                if (NetworkBehav + ProcessBehav) > 2 and self.score > 2: 
                    self.BadPathArray.update({self.GetProcPath(self.ProcID): self.score})
                else:
                    print("[DelEverything] Passed Tests")
                self.score = 0
        print(f"[DelEverything] Scanned {self.count} processes")
                
                
    def CheckProcBehaviour(self, cpuThresh=50.0, memoryThresh=4000.00, childThresh=10):
        try:
            cpuUsage = self.processObj.cpu_percent(interval=0.1)
            memUsage = self.processObj.memory_percent("rss")
            numChild = self.processObj.children(recursive=False)
            
            if cpuUsage >= cpuThresh:
                print("Bad Process")
                self.score += 1
            else:
                print("Good Process")
            
            if memUsage >= memoryThresh:
                print("Bad Process")
                self.score += 1
            else:
                print("Good Process")
                
            if len(numChild) >= childThresh:
                print("Bad Process")
                self.score += 1
            else:
                print("Good Process")
            
        except MemoryError:
            print("Memory Error")
        except OSError or IOError:
            print("Cannot Scan Process")
        except psutil.NoSuchProcess:
            print(f"Process does not exist. Name: {self.processObj.name()}. PID: {self.processObj.pid}")
        
        return self.score
    
    def CheckProcNetwork(self, OnlyEstablished, NetThresh=10, BlacklistedIPs=[], BlacklistedPorts=[]):
        ConnectDump = self.processObj.net_connections()
        for conn in ConnectDump:
            Status = conn.status
            remoteAddress = conn.raddr.ip
            remotePort = conn.raddr.port
            if Status == "ESATBLISHED" or OnlyEstablished == True:
                if remoteAddress in BlacklistedIPs:
                    self.score += 1
                else:
                    print("Clean")
                
                if remotePort in BlacklistedPorts:
                    self.score += 1
                else:
                    print("Clean")
            else:
                if remoteAddress in BlacklistedIPs:
                    self.score += 1
                else:
                    print("Clean")
                
                if remotePort in BlacklistedPorts:
                    self.score += 1
                else:
                    print("Clean")
        
        return self.score
    
    def GetProcPath(self):
        CMDProcOBJ = self.ProcID
        newProcObj = psutil.Process(CMDProcOBJ).cmdline()
        path = os.path.abspath(newProcObj)
        
        return path
    
    def AccessSuspicousLists(self):
        return self.BadPathArray