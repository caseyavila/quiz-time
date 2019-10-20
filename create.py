import json

selectedSet = input("Choose a set name: ")

setData = ""
with open("data.json") as f:
    for x in f.readlines():
        setData = setData+x

setData = json.loads(setData)
setData["sets"].update({selectedSet:[]})


while True:
    term = []
    value = input("Enter a question: ")
    term.append(value)
    value = input("Enter the answer: ")
    term.append(value)
    setData["sets"][selectedSet].append([term[0], term[1]])
    additional = input("Continue? Y/N: ")
    if additional == "N" or additional == "n":
        break

with open('data.json', 'w') as outfile:
    json.dump(setData, outfile,indent=2)
