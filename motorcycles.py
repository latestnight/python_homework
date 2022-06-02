#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

#motorcycles.append('ducati')
#print(motorcycles)

motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

#del motorcycles[0]
#print(motorcycles)
#popped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)
#motorcycles.append('suzuki')
#print(motorcycles)
#last_owned = motorcycles.pop()
#print(f"The last motorcycle i owned was a {last_owned.title()}.")
#first_owned = motorcycles.pop(0)
#print(f"the first motorcycle I owned was a {first_owned.title()}.")
#print(motorcycles)
#motorcycles.remove('yamaha')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")