'''
a = [10,20,30,40,50]

a.append(5)
a.append(6)
a.append(7)
print(a)

a.remove(50) # input is element
print(a)
a.pop(2) # input is index place
a.pop() # automatically pops first index if there is no input
print(a)

a.sort()
print(a)

empty=[]
for val in a:
    if val >= 6 and val <= 20:
        empty.append(val)
print(empty)

empty = [0] * 10
print(empty)
empty[5] = 10
print(empty)

dog = 'dog'
dogs = dog * 3
print(dogs)

# Comprehension
squares = [x * x for x in range(1,10)]
print(squares)

animals = ['dog', 'cat', 'dog', 'turtle']
dog = [animal for animal in animals if animal=='dog']
print(dog)
'''

# Dictionaries

fav_foods = {"Kathleen": "pizza", "Yin": "pizza", "Nick": "french fries", 
             "Owen": "burger"}

yin_favfood = fav_foods["Yin"]
print(yin_favfood)

for key in fav_foods:
    print(key, "favorite food is", fav_foods[key])

for key,val in fav_foods.items():
    print (key, "'s favorite food is", val)
