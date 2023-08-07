# first_term = 0
# secound_term = 1

# for i in range(5):
#     sum = first_term + secound_term
#     first_term = secound_term
#     secound_term = sum
#     i == i + sum
#     print(i)


first_term = 0
secound_term = 1
fib = [0,1]
for i in range(5):
    sum = first_term + secound_term
    first_term = secound_term
    secound_term = sum
    fib.append(sum)
print(fib)

