max_range = 100000

count = 0

for dividend in range(1, max_range + 1):
    is_prime = True
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    count += 1
    
print(count)