import os
import random as rand
data_dir=os.listdir("data/") 
print(data_dir)

color_dict=dict()

f=open("color.txt")
for line in f:
    print(line,end='')
    line_list=line.split(' ')

    color_index=line_list[0]
    color_information_temp=line_list[1]
        
    color_information=color_information_temp[0:-2]

    color_dict[color_index]=color_information

    print("color_index",color_index,"color_information",color_information,"\n")
    
print(color_dict)

for index in data_dir:
    if index not in color_dict:
        with open('color.txt', 'a') as f:
            line=str(index)+" "+str(rand.randint(0,255))+","+str(rand.randint(0,255))+","+str(rand.randint(0,255)) + '\n'
            f.writelines(line)
