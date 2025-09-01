import pefile
import math
import os

class PEHeuristicCheck:
    def __init__(self, filename):
        if filename.endswith(".exe") or filename.endswith(".dll") or filename.endswith(".scr"):
            self.PortableExecutableObject = pefile.PE(filename)
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
            for section in self.PortableExecutableObject:
                for b in section.get_data():
                    EncryptCheck = -sum((b/len(section.get_data()))*math.log2(b/len(section.get_data())))
                if EncryptCheck > 5:
                    self.score += 5
        except OSError:
            print("Problem With OS sorry")
        except IOError:
            print("Problem With Input/Output stream")
        except MemoryError:
            print("Seems to be a Segfault")
        except:
            print("Seems to be a problem we are not prepared for :o")
    
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
        PEHeuristicCheck.CheckForScarySections()
        PEHeuristicCheck.CheckForEncryption()
        PEHeuristicCheck.CheckForSuspiciousFunctions()
        
        return self.score
        