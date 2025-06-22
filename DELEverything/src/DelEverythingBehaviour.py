import psutil
import os

class Behaviour:
    def __init__(self, procName):
        for proc in psutil.process_iter():
            if proc.name == procName:
                self.processObj = proc
                self.ProcID = self.processObj.pid()
                
    def CheckProcBehaviour(self, cpuThresh=50.0, memoryThresh=4000.00, childThresh=10):
        sus = 0
        try:
            cpuUsage = self.processObj.cpu_percent(interval=0.1)
            memUsage = self.processObj.memory_percent("rss")
            numChild = self.processObj.children(recursive=False)
            
            if cpuUsage >= cpuThresh:
                print("SUS Process")
                sus += 1
            else:
                print("Chill Process")
            
            if memUsage >= memoryThresh:
                print("SUS Process")
                sus += 1
            else:
                print("Chill Process")
                
            if numChild >= childThresh:
                print("SUS Process")
                sus += 1
            else:
                print("Chill Process")
            
        except MemoryError:
            print("Memory Fucked")
        except OSError or IOError:
            print("Cannot Scan Process")
        except:
            print("Unexplained Error")
        
        return sus
    
    def CheckProcNetwork(self, OnlyEstablished, NetThresh=10, BlacklistedIPs=[], BlacklistedPorts=[]):
        sus = 0
        ConnectDump = self.processObj.net_connections()
        for conn in ConnectDump:
            Status = conn.status
            remoteAddress = conn.raddr.ip
            remotePort = conn.raddr.port
            if Status == "ESATBLISHED" or OnlyEstablished == True:
                if remoteAddress in BlacklistedIPs:
                    sus += 1
                else:
                    print("Clean")
                
                if remotePort in BlacklistedPorts:
                    sus += 1
                else:
                    print("Clean")
            else:
                if remoteAddress in BlacklistedIPs:
                    sus += 1
                else:
                    print("Clean")
                
                if remotePort in BlacklistedPorts:
                    sus += 1
                else:
                    print("Clean")
        
        return sus
    def GetProcPath(self):
        CMDProcOBJ = self.ProcID
        newProcObj = psutil.Process(CMDProcOBJ).cmdline()
        path = os.path.abspath(newProcObj)
        
        return path