# Data=[
#     ["Name","Height","Favorite Food"],
#     ["Aisosa", 165, "Rice"],
#     ["Tobi",162,"Beans"],
#     ["Opus", 170,"Yam"],
#     ["APC",164,"Spag"]]




# for item in Data:
#     print("startig")
#     for item2 in item:
#         print(item2)
#     print("Ending")

# item =  ["Name","Height","Favorite Food"] #loop1

# for item2 in item:
#     print(item2,"Happy")


# item = ["Aisosa", 165, "Rice"]  #loop2
# for item2 in item:
#     print(item2,"Sad")


# item = ["Tobi",162,"Beans"]  #loop3
# for item2 in item:
#     print(item2,"Smile")


# Data=[
#     ["Name","Height","Favorite Food"],
#     ["Aisosa", 165, "Rice"],
#     ["Tobi",162,"Beans"],
#     ["Opus", 170,"Yam"],
#     ["APC",164,"Spag"]]


Data=[
    ["Aisosa", 165, "Rice"],
    ["Tobi",162,"Beans"],
    ["Opus", 170,"Yam"],
    ["APC",164,"Spag"]]


num = []
 
for item in Data:
    num.append(item[1])

print(num)