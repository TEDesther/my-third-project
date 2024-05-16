Data=[["Student","Course","Level","Gender"],
 ["Tobi","Mechanical",400,"Male"], 
["Frank","Electrical","","Female"],
["Emmanuel","Chemistry",200,""],
["John","Petroleum",100,"Male"],
["Jessie","",300,"Female"],
["Opus","Law",500,""],
["Francis","Agric","",""]]


course =[]




# for item in Data:
#     for item2 in item:
#         course.append(item2)


# row = Data[0]
# for it in row:
#     course.append(it)

# print(course)




for item in Data:
    course.append(item[1])


# print(course)

gender=[]

for gen in Data:
    gender.append(gen[-1])

print(gender)