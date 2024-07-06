import csv

with open('Sort_a_list\hackathon_list.csv',mode = 'r')as file:
    f=csv.reader(file)
    l=[]
    for i in f:
        l.append(i)
#creating dictionary
d={}
for i in range(len(l)):
    d[l[i][0]]=[l[i][1],l[i][2]]

#sorting according name
sort_according_name = sorted(d)

#output
print('Name','Start Date','End Date',sep=' , ')
for i in sort_according_name:
    print(i,d[i][0],d[i][1],sep=' , ')