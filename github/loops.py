#For loop
for i in range (1, 6):
    print(i)
#while loop
i = 1
while i < 6:
    print(i)
    i += 1
#Nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
#break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)
#continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#pass statement
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
#for loop with else
for i in range(1, 6):
    print(i)
else:
    print("Loop completed")
#while loop with else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("Loop completed")
                       
#List comprehension with for loop                         
# List comprehension
# Creating a list of squares
squares = [x**2 for x in range(1, 11)]
print(squares)
# Creating a list of even numbers
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)
# Creating a list of tuples
tuples = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(tuples)
# Creating a list of strings
strings = [str(x) for x in range(1, 11)]      
print(strings)
# Creating a list of characters
chars = [chr(x) for x in range(65, 91)]
print(chars)
# Creating a list of prime numbers
primes = [x for x in range(2, 101) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
print(primes)
# Creating a list of Fibonacci numbers
fibonacci = [0, 1]
for i in range(2, 11):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(fibonacci)
# Creating a list of factorials
factorials = [1]
for i in range(1, 11):
    factorials.append(factorials[i-1] * i)
print(factorials)
# Creating a list of palindromes    
palindromes = [x for x in range(1, 101) if str(x) == str(x)[::-1]]
print(palindromes)
# Creating a list of anagrams
anagrams = [''.join(p) for p in itertools.permutations('abc')]
print(anagrams)
# Creating a list of combinations
combinations = [x for x in itertools.combinations('abc', 2)]
print(combinations)
# Creating a list of permutations
permutations = [x for x in itertools.permutations('abc', 2)]
print(permutations)
# Creating a list of Cartesian product
cartesian_product = [x for x in itertools.product('abc', '123')]
print(cartesian_product)
# Creating a list of powersets
powerset = [x for x in itertools.chain.from_iterable(itertools.combinations('abc', r) for r in range(len('abc') + 1))]
print(powerset)
# Creating a list of combinations with replacement
combinations_with_replacement = [x for x in itertools.combinations_with_replacement('abc', 2)]
print(combinations_with_replacement)
# Creating a list of permutations with replacement
permutations_with_replacement = [x for x in itertools.product('abc', repeat=2)]
print(permutations_with_replacement)
# Creating a list of Cartesian product with replacement
cartesian_product_with_replacement = [x for x in itertools.product('abc', repeat=2)]
print(cartesian_product_with_replacement)
# Creating a list of Fibonacci numbers with memoization
fibonacci_memo = {}
def fibonacci_memoization(n):
    if n in fibonacci_memo:
        return fibonacci_memo[n]
    if n <= 1:
        return n
    fibonacci_memo[n] = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
    return fibonacci_memo[n]
for i in range(10):
    print(fibonacci_memoization(i))
# Creating a list of prime numbers with memoization
prime_memo = {}
def is_prime(n):
    if n in prime_memo:
        return prime_memo[n]
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime_memo[n] = False
            return False
    prime_memo[n] = True
    return True
for i in range(1, 101):
    if is_prime(i):
        print(i)
     