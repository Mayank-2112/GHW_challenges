#importing module
import csv

#reading file
with open('Sort_a_list\hackathon_list.csv',mode = 'r')as file:
    f=csv.reader(file)
    l=[]
    for i in f:
        l.append(i)
#creating dictionary
d={}
for i in range(len(l)):
    d[l[i][1]]=[l[i][2],l[i][0]]

#sorting according date
sort_according_date = sorted(d)

#output
print('Name','Start Date','End Date',sep=' , ')
for i in sort_according_date:
    print(d[i][1],i,d[i][0],sep=' , ')