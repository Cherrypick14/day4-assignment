#  dipslaying max and min values in a tuple list
print("Below are the no of fruits and their quantities")

fruits =[("apples",6),("avocados",15),("blueberries",8),("kiwi",4)]

print(fruits)

def max_min(fruits):
    return max(fruits, key=lambda items:items[1])[1], min(fruits, key=lambda items:items[1])[1]
    

print("The maximum and minimum no of fruits is: ")
print(max_min(fruits))


