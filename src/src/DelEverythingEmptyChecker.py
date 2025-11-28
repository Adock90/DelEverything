import os

class EmptyCheck:
    @staticmethod
    def CheckIfEmpty(filename):
        isEmpty = False
        filesize = os.path.getsize(filename)
        if filesize == 0:
            print("Empty File")
            isEmpty = True
        else:
            print("Has Content")
            isEmpty = False
        
        return isEmpty

class DirCheck:
    @staticmethod
    def CheckDir(filename):
        if os.path.isdir(filename):
            print("[DelEverything] IS Dir")
            return True
        else:
            return False