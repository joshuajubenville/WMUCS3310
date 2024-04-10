from a4heap import MinHeap
from a4bst import *
from a4pq import *
import time

# Simple function that formats the data in a way I can use it with my data structures.
def prepData(input):
    with open(input) as openFile:
        temp1 = openFile.readlines()
        temp1 = [string.rstrip() for string in temp1]
        temp1.pop(0)
        temp2 = []
        for value in temp1:
            value = value.split(",")
            temp2.append(value)
        data = []
        for sublist in temp2:
            newSublist = [sublist[0], sublist[1:]]
            data.append(newSublist)
        return data

priorityData = prepData("priority.txt")
patientData = prepData("patient_info.txt")

print(priorityData)

pq = PriorityQueue()
for [x, [y]] in priorityData:
    pq.push(x, y)

pq.traverse()