from a4heap import MinHeap
from a4bst import *
from a4pq import *
import time
import webbrowser

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
            key = int(sublist[0])
            data.append([key] + sublist[1:])
        return data

def testPriorityQueue():
    pq = PriorityQueue()
    for entry in priorityData:
        pq.push(entry[0], entry[1:])

    pq2 = PriorityQueue()
    for entry in patientData:
        pq2.push(entry[0], entry[1:])

    orderedPriority = pq.buildList()
    orderedPatient = pq2.buildList()

    with open("pqResults.txt", "w") as file:
        i = 0
        while i < len(orderedPriority):
            priority = orderedPriority[i][0]
            patientID = orderedPriority[i][1][0]
            file.writelines(f"Priority: {priority}\nID: {patientID}\nName: {pq2.search(int(patientID))[0]}\nPhone: {pq2.search(int(patientID))[1]}\n") # This can probably be made faster by returning both indicies with a single search call, but I'm scared I'll break everything.
            file.writelines("\n")
            i += 1
        print("File (pqResults.txt) write complete!")

def testHeapBST():
    mh = MinHeap(20)
    for entry in priorityData:
        mh.insert(entry[0], entry[1:])

    bst = BinarySearchTree()
    for entry in patientData:
        bst.insert(entry[0], entry[1:])
        
    with open("heapBSTresults.txt", "w") as file:
        while mh.size > 0:
            priority, patientID = mh.remove()
            if isinstance(patientID, list):
                patientID = int(patientID[0])
            patientInfo = bst.search(patientID)
            file.write(f"Priority: {priority}\nID: {patientID}\nName: {patientInfo[1][0]}\nPhone: {patientInfo[1][1]}\n\n")
    print("File (heapBSTresults.txt) write complete!")
    

priorityData = prepData("priority.txt")
patientData = prepData("patient_info.txt")
startTime = time.time()
testPriorityQueue()
time1 = time.time() - startTime
with open("pqResults.txt", "a") as file:
    file.writelines(f"\nExecution Time: {time1} seconds.")

webbrowser.open("pqResults.txt")

nextTime = time.time()
testHeapBST()
time2 = time.time() - nextTime
with open("heapBSTResults.txt", "a") as file:
    file.writelines(f"\nExecution Time: {time2} seconds.")

webbrowser.open("heapBSTresults.txt")


