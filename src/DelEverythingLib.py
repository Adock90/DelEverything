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
    if DelEverythingEmptyChecker.EmptyCheck.CheckIfEmpty() == True:
        return 0
    
    score = 0
    if virustotal:
        VTObj = DelEverythingVirustotal.VirusTotalCheck(VTPasscode, filepath)
        VTScore = VTObj.SendToVT()
        score += VTScore
    else:
        print("[DelEverything] Skipping virustotal")
    
    Heur = DelEverythingHueristic.HeuristicCheck.CheckForStuff(None, filepath)
    score += Heur
    
    if filepath.endswith(".exe") or filepath.endswith(".dll") or filepath.endswith(".scr"):
        PE = DelEverythingPEHeurisitc.PEHeuristicCheck()
        PEScore = PE.CheckFile(filepath)
        
        score += PEScore
    else:
        pass
     
    return score