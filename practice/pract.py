num = 200

if(num%2 == 0):
    print("Success")

from csv import writer

file = open("myfile.txt","w")

Data = writer(file)

Data.write(file)