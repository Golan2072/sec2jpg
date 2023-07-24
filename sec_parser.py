#SEC file parser for Traveller
#Uses the "Sunbane" Format
#Will eventually use other formats and auto-detect them.

import stargen
import utility
from collections import defaultdict

def parser_function(sec_file):
    with open(sec_file, "r") as sector_file:
        subsector = defaultdict(dict)
        raw_sector = sector_file.readlines()
        for line in raw_sector:
            if line[0] == "#":
                pass
            elif line == []:
                pass
            elif line[0] == "-":
                pass
            elif line[0] == "H":
                pass
            elif line[0].isnumeric() == True:
                hex_column = int(line[0:2])
                hex_row = int(line[2:4])
                subsector[hex_column][hex_row] = stargen.Star(hex_column, hex_row)
                subsector[hex_column][hex_row].names = line[5:16]
                subsector[hex_column][hex_row].starport = line[26]
                subsector[hex_column][hex_row].size = utility.reverse_hex(line[27])
                subsector[hex_column][hex_row].atmosphere = utility.reverse_hex(line[28])
                subsector[hex_column][hex_row].hydrographics = utility.reverse_hex(line[29])
                subsector[hex_column][hex_row].population = utility.reverse_hex(line[30])
                subsector[hex_column][hex_row].government = utility.reverse_hex(line[31])
                subsector[hex_column][hex_row].law = utility.reverse_hex(line[31])
                subsector[hex_column][hex_row].tl = utility.reverse_hex(line[34])
                subsector[hex_column][hex_row].remarks = line[36:76]
            else:
                pass
        return subsector
# subsector_result = parser_function()
# for hex_column in subsector_result:
#     for hex_row in subsector_result[hex_column]:
#         print("Column: " + str(subsector_result[hex_column][hex_row].column))
#         print("Row: " + str(subsector_result[hex_column][hex_row].row))
#         print("Name: " + str(subsector_result[hex_column][hex_row].names))
#         print("Starport: " +str(subsector_result[hex_column][hex_row].starport))
#         print("Size: " +str(subsector_result[hex_column][hex_row].size))
#         print("Atmosphere: " +str(subsector_result[hex_column][hex_row].atmosphere))
#         print("Hydrographics: " +str(subsector_result[hex_column][hex_row].hydrographics))
#         print("Population: " +str(subsector_result[hex_column][hex_row].population))
#         print("Government: " +str(subsector_result[hex_column][hex_row].government))
#         print("Law Level: " +str(subsector_result[hex_column][hex_row].law))
#         print("World Type: " +str(subsector_result[hex_column][hex_row].startype))
#         print("TL: " +str(subsector_result[hex_column][hex_row].tl))
#         print("Remarks: " +str(subsector_result[hex_column][hex_row].remarks))
#         print("\n")