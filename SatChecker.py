from os import listdir

#Problem importer
#------------------------------------------------------------------------------
def importInst(fileName):
    file = open(fileName, 'r')
    inst = []
    for line in file:
        if not line.startswith("c") \
        and not line.startswith("p") \
        and not line.startswith("0") \
        and line.strip() \
        and not line.startswith("%") :
            line = line.split()
            line = [int(literal) for literal in line]
            inst.append(line)  
    for clause in inst:
        clause.remove(0)    
    file.close()    
    return(inst)
 
#Solution Importer    
#------------------------------------------------------------------------------
def importSol(fileName):
    file = open(fileName, 'r')
    sol = []
    for line in file:
        if not line.startswith("c"):
            sol = sol + line.split()
    file.close()    
    sol = [value for value in sol if value not in ["v", "0"]]
    sol = [int(i) for i in sol]
    return(sol)
    
#SAT CHECKER    
#------------------------------------------------------------------------------
def SAT(instance, solution):
    for clause in instance:
        clauseResult = False
        for literal in clause:
            if literal in solution:    
                clauseResult = True
                break
        if clauseResult == False:
            return False, clause 
    return True, clause

#RUN SAT CHECKER
#------------------------------------------------------------------------------
#set paths to data
inst_path = ".\\Lab-data\\Inst\\"
sol_path = ".\\Lab-data\\sols\\"
instances = [inst_path + i for i in listdir(inst_path)]
solutions = [sol_path + i for i in listdir(sol_path)]

##Simple Test Case
test_instance = [[1,-2, 3, 4], [-2, 3, -4, 1], [4, -2, 3, 1]]
test_solution = [-1,2,-3,4,5]
result, clause = SAT(test_instance, test_solution)
print("TestCase:")
print("The following clause is false:", clause)
print()

#Run all instances
for i in range(len(instances)):
    instance = importInst(instances[i])
    solution  = importSol(solutions[i])
    result, clause = SAT(instance, solution)
    print(instances[i])
    if result == True:
        print(result)
    else:
        print("The following clause is false:", clause)
