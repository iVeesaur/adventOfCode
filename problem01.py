digits = []
searchHits = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5", 
              "six", "6", "seven", "7", "eight", "8", "nine", "9", "zero", "0"]
invertSearch = []
for i in searchHits:
    invertSearch.append("".join(reversed(i)))
digvals = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
    "zero" : "0"
}

with open("problem01.txt") as problemSet:
    for line in problemSet:
        firstNum = ""
        lastNum = ""
        indexes = [line.find(word) for word in searchHits]
        placeLowestNum = min([index for index in indexes if index != -1])
        if line[placeLowestNum].isdigit():
            firstNum = line[placeLowestNum]
        else:
            for key in digvals.keys():
                if key.startswith((line[placeLowestNum]) + line[placeLowestNum+1]):
                    firstNum = digvals[key]
                    break
        
        invertLine = "".join(reversed(line))
        indexes = [invertLine.find(word) for word in invertSearch]
        placeHighestNum = min([index for index in indexes if index != -1])
        if invertLine[placeHighestNum].isdigit():
            lastNum = invertLine[placeHighestNum]
        else:
            for key in digvals.keys():
                if key.endswith(invertLine[placeHighestNum+2] + 
                                invertLine[placeHighestNum+1] + 
                                invertLine[placeHighestNum]):
                    lastNum = digvals[key]
                    break
                
        digits += [int(firstNum + lastNum)]

print(sum(digits))