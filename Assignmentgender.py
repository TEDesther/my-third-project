Data=[["Student","Course","Level","Gender"],
 ["Tobi","Mechanical",400,"Male"], 
["Frank","Electrical","","Female"],
["Emmanuel","Chemistry",200,""],
["John","Petroleum",100,"Male"],
["Jessie","",300,"Female"],
["Opus","Law",500,""],          
["Francis","Agric","",""]]

Gender=[]

for item in Data:
    Gender.append(item[-1])
print(Gender)

# Level=[]

# for levels in Data:
#     Level.append(levels[-2])
# print(Level)

# big_list=[]

# for everyitem in Data:
#     big_list.append(everyitem)

# print(big_list)

big_list=[]

for everyitem in Data:
    for inner in everyitem:
       print(inner,"hello")


  #first loop everyitem = ["student",course,level,gender]

  #secondloop every item= ["tobi,mechanicql,400"]   
  #third

print(big_list)

