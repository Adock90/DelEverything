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