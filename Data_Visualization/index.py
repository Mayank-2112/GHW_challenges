import numpy as np
import matplotlib.pyplot as plt
import csv

Calorie_Goal_Limit = 3500
Protien_Goal = 900
Fat_Goal = 580
Carbs_Goal = 1300




with open('Data_Visualization\data.csv',mode='r')as file:
    today=[]
    f = csv.reader(file)
    for i in f:
        today.append(i)


print(today)
calorie_sum = sum(int(food[1]) for food in today)
protien_sum = sum(int(food[2])  for food in today)
fat_sum = sum(int(food[3])  for food in today)
carb_sum = sum(int(food[4])  for food in today)

fig,axs = plt.subplots(2,2)
axs[0,0].pie([protien_sum,fat_sum,carb_sum], labels=['Protiens','Fats','Carbs'], autopct='%1.1f%%')
axs[0,0].set_title('Macronutrients Distribution')
axs[0,1].bar([0,1,2],[protien_sum,fat_sum,carb_sum], width=0.4, label=['Protien Intake','Fats Intake','Carbs Intake'])
axs[0,1].bar([0.5,1.5,2.5],[Protien_Goal,Fat_Goal,Carbs_Goal], width=0.4, label=['Protien Goal','Fats Goal','Carbs Goal'])
axs[0,1].set_title('Macronutrients Progress')
axs[1,0].plot(list(range(len(today))),np.cumsum([int(food[1]) for food in today]), label='Calories Eaten')
axs[1,0].plot(list(range(len(today))),[Calorie_Goal_Limit] * len(today), label='Calorie Goal')
axs[1,0].legend()
axs[1,0].set_title('Calorie Goal Over Time')
axs[1,1].pie([calorie_sum,Calorie_Goal_Limit - calorie_sum],labels=['Calories','Remaining'], autopct='%1.1f%%')
axs[1,1].set_title('Calories Goal Progress')
fig.tight_layout()
plt.show()

