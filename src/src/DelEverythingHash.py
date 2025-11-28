import hashlib


class HashChecker:
    @staticmethod
    def FileHash(filename, Alg='md5'):
        print(Alg)
        hashObjDigest = ""
        hashObj = hashlib.new(Alg)
        try:
            with open(filename, "rb") as TargetFile:
                while chunck := TargetFile.read(8192):
                    hashObj.update(chunck)
            hashObjDigest = hashObj.hexdigest()
        except:
            print("Cannot read to generate Hash")
        return hashObjDigest
    @staticmethod
    def CheckFile(hash, Bad_hashes):
        if hash in Bad_hashes:
            return True
        else:
            return False
    