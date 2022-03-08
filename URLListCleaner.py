# Cleans the URLList outputted from URLgetter.py
# URLList still needs to be manually formated first and surrounded by ""


# Exact date match

# infile_path = r".\URLList.txt" 
# outfile_path = r".\URLListcleaned.txt" 

# i=0
# completed_lines = []
# outfile = open(outfile_path, "w", encoding="utf-8", errors="ignore") 

# for line in open(infile_path, "r", encoding="utf-8", errors="ignore"):
   
#     if len(completed_lines) > 2:
#         lastline = completed_lines[i-1]
#         if line[25:33] != lastline[25:33]:
#             outfile.write(line.rstrip()+"\n")
#             completed_lines.append(line)
#             i=i+1
#     else:
#         completed_lines.append(line)
#         i=i+1

# outfile.close()


# Only one URL per month

infile_path = r".\output\URLgetter\URLList.txt" 
outfile_path = r".\output\URLgetter\URLListOnlyMonth.txt" 

i=0
completed_lines = []
outfile = open(outfile_path, "w", encoding="utf-8", errors="ignore") 

for line in open(infile_path, "r", encoding="utf-8", errors="ignore"):
   
    if len(completed_lines) > 2:
        lastline = completed_lines[i-1]
        if line[25:31] != lastline[25:31]:
            outfile.write(line.rstrip()+"\n")
            completed_lines.append(line)
            i=i+1
    else:
        completed_lines.append(line)
        i=i+1

outfile.close()
