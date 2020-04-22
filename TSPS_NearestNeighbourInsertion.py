#Import Numpy
import math
import random
import os
#random.seed(12345)


#------------------------------------------------------------------------------

#file importer
def importInst(fileName):
    file = open(fileName, 'r')
    size = int(file.readline())  
    inst = {}
    for i in range(size):   
        line=file.readline()        
        (myid, x, y) = line.split()        
        inst[int(myid)] = (int(x), int(y))    
    file.close()    
    return(inst)


#------------------------------------------------------------------------------

#distance calculator
def euclidean(cityA, cityB):
    distance = round(math.sqrt((cityA[0] - cityB[0])**2 
                               + (cityA[1] - cityB[1])**2))
    return(distance)


#------------------------------------------------------------------------------

def tsp(inst):
    
    cities = list(inst.keys())
    startIndex = random.randint(0, len(inst)-1)
    route = [cities[startIndex]]
    del cities[startIndex]
    
    totalDist = 0
    currentCity = route[0]

    while len(cities) > 0:
        city = cities[0]
        index = 0
        dist = euclidean(inst[currentCity], inst[city] )
        
        for newIndex in range(1, len(cities)):
            #print(newIndex)
            newCity = cities[newIndex]
            newDist = euclidean(inst[currentCity], inst[newCity])
            if newDist < dist:
                dist = newDist
                city = newCity
                index = newIndex
        currentCity = city
        route.append(currentCity)
        totalDist += dist
        del cities[index]
        #print(len(cities))
    totalDist += euclidean(inst[currentCity], inst[route[0]])    
    return route, totalDist          
 
    
#------------------------------------------------------------------------------    

def saveOutput(outFile, solution, distance):
    file = open(outFile, 'w')    
    file.write(str(distance)+"\n")    
    for city in solution:        
        file.write(str(city)+"\n")    
    file.close()
 
    
#------------------------------------------------------------------------------
    
def runBatch(dirInput, dirOutput):
    fileList = os.listdir(dirInput)
    
    for file in fileList:
        filePath = filePath = dirInput + filefile
        instance = importInst(filePath)
        solution = tsp(instance)
        
        outFile = dirOutput + file
        saveOutput(outFile, solution[0], solution[1])
    

dirInput  = "C:\\Users\\James\\Desktop\\CIT\\2_MetaHeauristic Optimisation\\LabWork\\Lab1\\TSP dataset\\"
dirOutput = "C:\\Users\\James\\Desktop\\CIT\\2_MetaHeauristic Optimisation\\Python\\TSP output\\"
runBatch(dirInput, dirOutput)

filePath = dirInput + "inst-4.tsp"
inst = importInst(filePath)
print(tsp(inst))


