import re
import os



class HeuristicCheck:
    @staticmethod
    def CheckForStuff(LookForArr, filename):
        num = 0
        filesize = os.path.getsize(filename)
        if filesize > 1000000000:
            HeuristicCheck.CheckForStuffLargeFile(LookForArr, filename)
        try:
            with open(filename, "r", encoding="utf-8", errors="ignore") as TargetFile:
                contents = TargetFile.read()
                for i in range(len(LookForArr)):
                    res = re.search(LookForArr[i], contents)
                    if res:
                        num += 1
                    else:
                        continue
        except FileNotFoundError:
            print("Could not read As "+filename+" Does not exist")
        except IOError or OSError:
            print("For some reason that i idk i cannot read "+ filename)
        except MemoryError:
            print("Memory Error")
        return num
    
    @staticmethod
    def CheckForStuffLargeFile(LookForArr, filename):
        num = 0
        filesize = os.path.getsize(filename)
        if filesize < 1000000000:
            HeuristicCheck.CheckForStuff(LookForArr, filename)
        try:
            with open(filename, "r", encoding="utf-8", errors="ignore") as TargetFile:
                for line in TargetFile:
                    for i in range(len(LookForArr)):
                        res = re.search(LookForArr[i], line)
                        if res:
                            num += 1
                        else:
                            continue
        except FileNotFoundError:
            print("Could not read As "+filename+" Does not exist")
        except IOError or OSError:
            print("For some reason that i idk i cannot read "+ filename)
        except MemoryError:
            print("Memory Memort Error")
        return num
    
