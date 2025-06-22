import DelEverythingHash
import DelEverythingHueristic
import os

input("")

Bad = ["549d100e4de2ffc86def96e2df45b08668eaf0ef96f7da9a44d50d2b4d407ff7"]

Even_Badder = [r'print', r'os', r"eval\("]

count = 0
danger = 0

for (dirpath, dirname, filenames) in os.walk("C:\\Users\\Adam\\Documents", topdown=True):
    for i in range(len(filenames)):
        print("["+str(count)+"]"+dirpath+"\\"+str(filenames[i]))
        fileHash = DelEverythingHash.HashChecker.FileHash(dirpath+"\\"+str(filenames[i]), 'sha256')
        print(fileHash)
        checkHash = DelEverythingHash.HashChecker.CheckFile(fileHash, Bad)
        checkHeuristic = DelEverythingHueristic.HeuristicCheck.CheckForStuff(Even_Badder, dirpath+"\\"+str(filenames[i]))
        if checkHeuristic > 1:
            print("Found Danger")
            print(checkHeuristic)
            danger += 1
        else:
            print(checkHeuristic)
        if checkHash == True:
            print("Found")
        else:
            print("Opps")
        count += 1


print(f"\n{count} files: {danger} are dangerous")

input("")