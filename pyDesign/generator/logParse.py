import sys

inname = "C:\\Users\\BaileyRD\\Documents\\GitHub\\pyDesign\\generator\\simple.log"#sys.argv[1]
outname = "C:\\Users\\BaileyRD\\Documents\\GitHub\\pyDesign\\generator\\warning.log" #sys.argv[2]

with open(inname) as infile:
    with open(outname, "w") as outfile:
        for l in infile: 
            if 'WARNING' in l:
                outfile.write(l.replace(' WARNING', ''))