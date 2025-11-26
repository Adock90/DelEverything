import DelEverythingEmptyChecker
import DelEverythingBehaviour
import DelEverythingHash
import DelEverythingHueristic
import DelEverythingVirustotal
import DelEverythingUserConfig
import DelEverythingPEHeurisitc

def CheckProcesses():
    pass

def CheckFile(filepath, virustotal, VTPasscode):
    try:
        if DelEverythingEmptyChecker.DirCheck.CheckDir(filepath) == True or DelEverythingEmptyChecker.EmptyCheck.CheckIfEmpty(filepath) == True:
            return 0
       
    except:
        print("[DelEverything] Failed")
    
    score = 0
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