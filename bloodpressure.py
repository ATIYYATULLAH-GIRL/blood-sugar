import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

classes=np.array([1,4,3,2,6,7,5,8,11,10,9,12])
plt.hist(classes, bins=[1,7,14], color="black", edgecolor="grey")
plt.show()

#new graph
blood_pressure_men=[113,88,59,90,95,67,70,98,100,190,120]
blood_sugar_women=[150,80,91,47,50,90,96,87,79,67,134]

type=[blood_pressure_men, blood_sugar_women]
color=["r","b"]
label=["Men","Women"]
bins=[60,90,120,150,190]
plt.hist(type, bins=bins, color=color, label=label, orientation="horizontal")
plt.title("Blood Pressure Level Graph")
plt.xlabel("Total no. of patients")
plt.ylabel("Blood Pressure Range")
plt.legend()
plt.show()