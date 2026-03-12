import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

age=np.array([10,12,16,6,5,7,12,3,5,7,12,14,13,5,6])
plt.hist(age, bins=[5,10,15], color="red", edgecolor="black")
plt.show()

#new graph
blood_sugar_men=[113,88,59,90,95,67,70,98,100,190,120]
blood_sugar_women=[150,80,91,47,50,90,96,87,79,67,134]

type=[blood_sugar_men, blood_sugar_women]
color=["r","g"]
label=["Men","Women"]
bins=[60,90,120,150,190]
plt.hist(type, bins=bins, color=color, label=label, orientation="horizontal")
plt.title("Blood Sugar Level Graph")
plt.xlabel("Total no. of patients")
plt.ylabel("Blood Sugar Range")
plt.legend()
plt.show()