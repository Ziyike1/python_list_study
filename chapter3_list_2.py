motocycles = ["honda","yamaha","suzuki"]
print(motocycles)

# motocycles[0] = "ducati"
# print(motocycles)

motocycles.append("ducati")
print(motocycles)

motocycles2 = []
motocycles2.append("honda")
motocycles2.append("yamaha")
motocycles2.append("ducati")
print(motocycles2)

motocycles3 = ["honda","yamaha","suzuki"]
# motocycles3.insert(0,"ducati")
# print(motocycles3)
# motocycles3.insert(3,"other")
motocycles3.insert(100,"other")
# motocycles3.append("xxx")
# motocycles3.insert(-1,"other")
print(motocycles3)

del motocycles3[0]
print(motocycles3)

del motocycles3[0]
print(motocycles3)