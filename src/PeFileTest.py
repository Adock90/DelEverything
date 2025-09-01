import pefile

pe = pefile.PE("C:\\Users\\Adam\\Documents\\WinManage\\x64\\Debug\\WinManage.exe")

print(pe.DOS_HEADER)

print("\n\n\n\n")

print(pe.NT_HEADERS)

print("\n\n\n\n")

print(pe.OPTIONAL_HEADER)

print("\n\n\n\n")

for section in pe.sections:
    print(section.Name.decode.strip)