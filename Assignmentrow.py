Data=[["Student","Course","Level","Gender"],
 ["Tobi","Mechanical",400,"Male"], 
["Frank","Electrical","","Female"],
["Emmanuel","Chemistry",200,""],
["John","Petroleum",100,"Male"],
["Jessie","",300,"Female"],
["Opus","Law",500,""],
["Francis","Agric","",""]]

# print(Data[0][0])
# print(Data[1][0])
# print(Data[2][0])
# print(Data[3][0])
# print(Data[4][0])
# print(Data[5][0])
# print(Data[6][0])

# print("--------------------")

# print(Data[0][1])
# print(Data[1][1])
# print(Data[2][1])
# print(Data[3][1])
# print(Data[4][1])
# print(Data[5][1])
# print(Data[6][1])

# print("-------------------")

# print(Data[0][2])
# print(Data[1][2])
# print(Data[2][2])
# print(Data[3][2])
# print(Data[4][2])
# print(Data[5][2])
# print(Data[6][2])

# print("------------------")

# print(Data[0][3])
# print(Data[1][3])
# print(Data[2][3])
# print(Data[3][3])
# print(Data[4][3])
# print(Data[5][3])
# print(Data[6][3])   

for item in Data:
    print(item[1])

from csv import reader
file = open("freshdata.csv","w")

from csv import writer
file = open("freshdata.csv","w")
