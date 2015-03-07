import numpy as np
filename="Bolshoi_Cube_Mcut_5E12"
data = np.loadtxt(filename+".csv", skiprows=1, delimiter=",")
outfile = open(filename+".dat", "w")
for item in data:
    outfile.write("%f %f %f\n"%(item[1], item[2], item[3]))
outfile.close()
