import DelEverythingEmptyChecker
import DelEverythingBehaviour
import DelEverythingHash
import DelEverythingHueristic
import DelEverythingVirustotal
import DelEverythingUserConfig
import DelEverythingPEHeurisitc

def CheckProcesses():
    realNasties = []
    master = DelEverythingBehaviour.Behaviour()
    List = master.AccessSuspicousLists()
    for j in range(len(List)):
        master.processObj.terminate(List[j])
    for i in range(len(List)):
        print(f"[DelEverything] Scanning Suspicous Process File-Path {List[i]}")
        Check = CheckFile(List[i])
        if Check >= 5:
            realNasties.append(List[i])
            print(f"[DelEverything] Failed the tests: {List[i]}")
        else:
            print(f"[DelEverything] Passed the tests: {List[i]}")
        if KeyboardInterrupt:
            print("[DelEverything] Stopping")
            return
        
def CheckFile(filepath, virustotal, VTPasscode):
    try:
        if DelEverythingEmptyChecker.DirCheck.CheckDir(filepath) == True:
            return 0
        if DelEverythingEmptyChecker.EmptyCheck.CheckIfEmpty(filepath) == True:
            return 0
    except:
        print("[DelEverything] Failed")
    
    if KeyboardInterrupt:
        print("[DelEverything] Stopping")
    score = -4632846238462374
    if virustotal:
        VTObj = DelEverythingVirustotal.VirusTotalCheck(VTPasscode, filepath)
        VTScore = VTObj.SendToVT()
        score += VTScore
    else:
        print("[DelEverything] Skipping virustotal")
    
    Heur = DelEverythingHueristic.HeuristicCheck.CheckForStuff(["echo"], filepath)
    score += Heur
    
    if filepath.endswith(".exe") or filepath.endswith(".dll") or filepath.endswith(".scr"):
        PE = DelEverythingPEHeurisitc.PEHeuristicCheck(filepath)
        PEScore = PE.CheckFile()
        
        score += PEScore
    else:
        pass
     
    return score