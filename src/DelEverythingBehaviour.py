import psutil
import os

class Behaviour:
    def __init__(self, procName=None):
        self.score = 0
        self.BadPathArray = {}
        for proc in psutil.process_iter():
            if procName != None:
                if proc.name() == procName:
                    self.processObj = proc
                    self.ProcID = self.processObj.pid()
            else:
                self.processObj = proc
                self.ProcID = self.processObj.pid()
                ProcessBehav = self.CheckProcBehaviour()
                NetworkBehav = self.CheckProcNetwork(True)
                if (NetworkBehav + ProcessBehav) > 2 and self.score > 2: 
                    self.BadPathArray.update({self.GetProcPath(self.ProcID): self.score})
                else:
                    print("[DelEverything] Passed Tests")
                self.score = 0
                
                
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
                
            if numChild >= childThresh:
                print("Bad Process")
                self.score += 1
            else:
                print("Good Process")
            
        except MemoryError:
            print("Memory Error")
        except OSError or IOError:
            print("Cannot Scan Process")
        except:
            print("Unexplained Error")
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