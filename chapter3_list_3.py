motocycles = ["honda","yamaha","suzuki"]
print(motocycles)

poped_motocycles = motocycles.pop()
print(motocycles)
print(poped_motocycles)

print(f"The last motorcycle I buught was {poped_motocycles}")

motocycles2 = ["honda","yamaha","suzuki"]
print(motocycles2)
first_poped = motocycles2.pop(0)
print(first_poped)

print(f"The first motorcycle I buught was {first_poped}")

motocycles3 = ["honda","yamaha","suzuki","ducati"]
print(motocycles3)

motocycles3.remove("honda")
print(motocycles3)

too_expansive = "ducati"
motocycles3.remove(too_expansive)
print(motocycles3)
print(f"\nA {too_expansive.title()} is too expansive for me")