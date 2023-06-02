# firstString = "water"
# secondString = "fall"
# thirdString = firstString + secondString
# print(thirdString)

name = input("What is your name? ")
#print("Hello " + name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name * 3,color,animal))

myFruitList = ["apple", "banana", "cherry"]
# print(myFruitList)
# print(type(myFruitList))

# print(myFruitList[0])
# print(myFruitList[1])
# print(myFruitList[2])

# myFruitList[2] = "orange"
# print(myFruitList[2])

# myFruitList.extend(["mango", "cherry"])
# print(myFruitList[3])
# print(myFruitList)

# myFinalAnswerTuple = ("apple", "banana", "pineapple")
# print(myFinalAnswerTuple)
# print(type(myFinalAnswerTuple))
# print(myFinalAnswerTuple[0])
# print(myFinalAnswerTuple[1])
# print(myFinalAnswerTuple[2])

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    
# for i in range(5, 10, 2):
#     print(myMixedTypeList[i])