cubes = [i**3 for i in range(1, 1001) if i % 2 != 0]
sum = 0
for numbers in cubes:
    sum = 0
    caunt = numbers
    while caunt !=0:
        sum += caunt % 10
        caunt //= 10
    if not sum % 7:
        sum += numbers
print(sum)
sum = 0
for numbers in cubes:
    sum = 0
    caunt = numbers + 17
    while caunt !=0:
        sum += caunt % 10
        caunt //= 10
    if not sum % 7:
        sum += numbers
print(sum)