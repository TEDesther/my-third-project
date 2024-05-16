# num = 311

# if (num%2 == 0):
#     print("Success")

# else:
#     print("odd number")

Item = ["Nurudeen has a very big head"]

Item = [["Nurudeen has a very big head"],["I am Happy"]]

# Number = [[200],[300],[4000]]

Number = [[200,300,4000]]

from csv import writer

file = open("nurudeenfile.csv", "a")

data = writer(file)

data.writerows(Number)



