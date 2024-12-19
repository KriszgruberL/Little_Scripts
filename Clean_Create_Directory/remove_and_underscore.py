import re

data = """

"""

lines = data.split("\n")

with open("cleaned_line.txt", "a") as file : 
    for index,line in enumerate(lines) : 
        if line :
            line = re.sub(r"^\s*>\s*-\s*\[\s*\]\s*", "", line).strip()
            line = re.sub(r"\s*:\s*", " ", line)
            line = re.sub(r"\s*,\s*", " ", line)
            line = line.replace(" ", "_")
            if index < 10 : 
                file.write(f"00{index}_" +line + "\n")
            else : 
                file.write(f"0{index}_" +line + "\n")
            
    file.write("+------------------------------------------------------------------+\n")