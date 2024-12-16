cars = ["bmw","audi","subaru","toyota"]
print(cars)

cars.sort()
print(cars)

cars2 = ["宝马","奥迪","斯巴鲁","丰田"]
print(cars2)

cars2.sort()
print(cars2)

cars.sort(reverse=True)
print(cars)

cars = ["bmw","audi","subaru","toyota"]
print("Here is the original list:")
print(cars)
print("\nHere is the new sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print("\nHere is the new reverserd sorted list:")

#sorted() 方法想要用reverse反转顺序的话，需要使用如下方式
print(sorted(cars,reverse=True))
print(cars)

cars = ["bmw","audi","subaru","toyota"]
print(cars)

cars.reverse()
print(cars)

cars.reverse()
print(cars)

list_length = len(cars)
print(list_length)