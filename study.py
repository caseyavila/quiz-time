import json
import random

#Reading the data.json file, and importing all of the sets
setData = ""
with open("data.json") as f:
    for x in f.readlines():
        setData = setData+x

setData = json.loads(setData)

print("Available Sets:")
for x in setData["sets"]:
    print(x)

while True:
    selectedSet = input("Select a set:")
    try:
        print("Cool, selected {}!".format(selectedSet))
        selectedSetData = setData["sets"][selectedSet]
        break
    except:
        print("Please select an actual set")
        for x in setData["sets"]:
            print(x)

random.shuffle(selectedSetData)

correctCount = 0
for term in selectedSetData:
    print("Q: "+term[0])
    answer = input("A: ")
    if answer == term[1]:
        print("Correct!")
        correctCount+=1
    else:
        print('Incorrect, correct answer is: {} \nTry again for half credit!'.format(term[1]))
        print("Q: " + term[0])
        answer = input("A: ")
        if answer == term[1]:
            print("Correct!")
            correctCount+=.5
        else:
            print("Incorrect!")


print("Congrats you've earned {} minutes".format(correctCount))
