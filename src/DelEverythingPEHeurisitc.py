import pefile
import math
import os

def CalculateEntropy(data):
    if not data:
        return 0
    length = len(data)
    frequency = [0]*256
    for b in data:
        frequency[b] += 1
    result = -sum((f/length) * math.log2(f/length) for f in frequency if f)
    return result

class PEHeuristicCheck:
    def __init__(self, filename):
        self.fileN = filename
        if filename.endswith(".exe") or filename.endswith(".dll") or filename.endswith(".scr"):
            self.PortableExecutableObject = False
            try:
                self.PortableExecutableObject = pefile.PE(filename)
            except pefile.PEFormatError:
                print("pefile.PEFormatError")
            
            self.cleanSections = [".text", ".data", ".rdata", ".rsrc"]
            self.score = 0
            self.badFuncts = ['OpenProcess', 'CreateRemoteThread', 'VirtualAlloc', 'WriteProcessMemory', 'RtlAdjustPrivilige']
        else:
            print("Unsupported file format")
            os._exit(os.EX_OK)
        
    def CheckForScarySections(self):
        try:
            for section in self.PortableExecutableObject:
                DecodeName = section.Name.decode()
                RemoveUnecessary = DecodeName.strip()
                if RemoveUnecessary not in self.cleanSections:
                    print("Bad sign: "+RemoveUnecessary)
                    self.score += 1
                else:
                    continue
        except OSError:
            print("Problem With OS sorry")
        except IOError:
            print("Problem With Input/Output stream")
        except MemoryError:
            print("Seems to be a Segfault")
        except:
            print("Seems to be a problem we are not prepared for :o")
    
    def CheckForEncryption(self):
        try:
            for section in self.PortableExecutableObject.sections:
                data = section.get_data()
                EncryptCheck = CalculateEntropy(data)
                if EncryptCheck > 5:
                    self.score += 5
        except OSError:
            print("Problem With OS sorry")
        except IOError:
            print("Problem With Input/Output stream")
        except MemoryError:
            print("Seems to be a Segfault")
        
    
    def CheckForSuspiciousFunctions(self):
        try:
            if hasattr(self.PortableExecutableObject, 'DIRECTORY_ENTRY_IMPORT'):
                for entry in self.PortableExecutableObject.DIRECTORY_ENTRY_IMPORT:
                    decodedEntry = entry.dll.decode()
                    for imp in entry.imports:
                        name = imp.name
                        decodedName = name.decode()
                        if name and decodedName in self.badFuncts:
                            print("Suspicoius Activity: "+decodedName+" Inside of: "+decodedEntry)
                            self.score += 2
                        else:
                            continue
        except OSError:
            print("Problem With OS sorry")
        except IOError:
            print("Problem With Input/Output stream")
        except MemoryError:
            print("Seems to be a Segfault")
        except:
            print("Seems to be a problem we are not prepared for :o")
    
    def CheckFile(self):
        if self.PortableExecutableObject != False:
            PEHeuristicCheck.CheckForScarySections(self)
            PEHeuristicCheck.CheckForEncryption(self)
            PEHeuristicCheck.CheckForSuspiciousFunctions(self)
        else:
            print(f"pefile.PEFormatError: Skipping {self.fileN}")
        
        return self.score
        