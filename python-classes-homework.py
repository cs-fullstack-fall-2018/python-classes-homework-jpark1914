
# #=====Exercise 1======
#
# class Dog():
#     def __init__(self, name, breed, color, gender):
#         self.name = name
#         self.breed = breed
#         self.color = color
#         self.gender = gender
#
# def main():
#     newDog = Dog("Fido", "Lab", "brown", "male")
#     print(newDog.name)
#     print(newDog.breed)
#     print(newDog.color)
#     print(newDog.gender)
#

#======Exercise 2 ======

class ToDo():
    def __init__(self, name, dueDate, list,):
        self.name = name
        self.dueDate = dueDate
        self.list = list
    def addTask(self, newTask):
        self.list.append(newTask)

def main():
    newToDo = ToDo("Jordan", "Friday", ["Coding Project", "Youtube Video", "laundry"])
    print(newToDo.list)
    newToDo.addTask("game")
    print(newToDo.list)




#=====Exercise 3 ======

if __name__ == '__main__':
    main()


