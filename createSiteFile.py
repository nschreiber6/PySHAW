
# Read the file
file_path = "c1_vet.sit"  # Replace with the actual file path
with open(file_path, "rw") as file:
    lines = file.readlines()


# Initialize variables
JSTART, HRSTAR, YRSTAR, JEND, YREND = map(int, lines[0].split()[2:7])  # Line B
ALTDEG, ALTMIN, SLP, ASPEC, HRNOON, ELEV = map(float, lines[1].split()[1:])  # Line C
NPLANT, NSP, NR, NS, NSALT, TOLER, NHRPDT, LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5, LEVEL6 = map(int, lines[2].split()[1:])  # Line D
ZMCM, HEIGHT, PONDMX = map(float, lines[4].split()[1:])  # Line E
ISNOTMP, SNOTMP, ZMSPCM, ISNOPARM = map(int, lines[6].split()[1:])  # Line G
IVLCBC, ITMPBC, ALBDRY, ALBEXP, IWRC, IPHANTOM = map(int, lines[8].split()[1:])  # Line J1

# For Line J2 (Omit if ITMPBC does not equal 1)
if ITMPBC == 1:
    TSAVG = float(lines[9].strip())  # Line J2

# For Line J3-1 to J3-NS when IWRC = 1 (Campbell equation)
if IWRC == 1:
    for i in range(NS):
        ZS, SAND, SILT, CLAY, ROCK, OM, RHOB, SATCON, SATKL, SOILWRC_1, SOILWRC_2, SOILWRC_3, ASALT, DISPER = map(float, lines[10 + i].split())
        print(f"Line J3-{i+1}:", ZS, SAND, SILT, CLAY, ROCK, OM, RHOB, SATCON, SATKL, SOILWRC_1, SOILWRC_2, SOILWRC_3, ASALT, DISPER)


# UPDATE VARIABLES HERE



# Write Line C
file.write(f"{ALTDEG} {ALTMIN} {SLP} {ASPEC} {HRNOON} {ELEV}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLINE C\n")