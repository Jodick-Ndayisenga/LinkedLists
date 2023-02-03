class LinkedList:
    def List(self, firstList:list, secondList:list) -> list:
        myFirstNumber = "".join([str(i) for i in firstList[::-1]])
        mySecondNumber = "".join([str(j) for j in secondList[::-1]])
        somme =[int(i) for i in str(int(myFirstNumber)+int(mySecondNumber))][::-1]
        
        return somme

myFirstInstance = LinkedList()
print(myFirstInstance.List([9,9,9,9,9,9,9], [9,9,9,9]))