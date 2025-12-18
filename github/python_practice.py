#For loop
import itertools


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

# Check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
# Test the function
print(check_number(5))   # Output: Positive
print(check_number(-3))  # Output: Negative
print(check_number(0))   # Output: Zero
# Check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Test the function
print(check_even_odd(4))  # Output: Even
print(check_even_odd(7))  # Output: Odd
# Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# Test the function
print(is_prime(7))   # Output: True
print(is_prime(10))  # Output: False
# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]
# Test the function
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
# Check if a string is an anagram of another string
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
# Test the function
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False
# Check if a string contains only digits
def is_digit(s):
    return s.isdigit()
# Test the function
print(is_digit("12345"))  # Output: True
print(is_digit("123a5"))  # Output: False
# Check if a string contains only letters
def is_alpha(s):
    return s.isalpha()
# Test the function
print(is_alpha("hello"))  # Output: True    
print(is_alpha("hello123"))  # Output: False
# Check if a string contains only alphanumeric characters
def is_alnum(s):
    return s.isalnum()
# Test the function
print(is_alnum("hello123"))  # Output: True
print(is_alnum("hello 123"))  # Output: False
# Check if a string contains only whitespace characters
def is_space(s):
    return s.isspace()
# Test the function
print(is_space("   "))  # Output: True
print(is_space("hello"))  # Output: False
# Check if a string contains only uppercase letters
def is_upper(s):
    return s.isupper()
# Test the function
print(is_upper("HELLO"))  # Output: True
print(is_upper("Hello"))  # Output: False
# Check if a string contains only lowercase letters
def is_lower(s):
    return s.islower()
# Test the function
print(is_lower("hello"))  # Output: True
print(is_lower("Hello"))  # Output: False
# Check if a string contains only printable characters
def is_printable(s):
    return s.isprintable()
# Test the function
print(is_printable("hello"))  # Output: True
print(is_printable("hello\n"))  # Output: False
# Check if a string contains only non-printable characters
def is_non_printable(s):
    return not s.isprintable()
# Test the function
print(is_non_printable("hello"))  # Output: False
print(is_non_printable("hello\n"))  # Output: True  
# Check if a string contains only punctuation characters
def is_punctuation(s):
    return all(c in strings.punctuation for c in s)
# Test the function
print(is_punctuation("!@#$%^&*()"))  # Output: True
print(is_punctuation("hello"))  # Output: False
# Check if a string contains only special characters
def is_special(s):
    return all(not c.isalnum() and not c.isspace() for c in s)
# Test the function
print(is_special("!@#$%^&*()"))  # Output: True
print(is_special("hello"))  # Output: False
# Check if a string contains only hexadecimal characters
def is_hexadecimal(s):
    return all(c in strings.hexdigits for c in s)
# Test the function
print(is_hexadecimal("1a2b3c"))  # Output: True
print(is_hexadecimal("hello"))  # Output: False
# Check if a string contains only octal characters
def is_octal(s):
    return all(c in '01234567' for c in s)
# Test the function
print(is_octal("1234567"))  # Output: True
print(is_octal("hello"))  # Output: False
# Check if a string contains only binary characters
def is_binary(s):
    return all(c in '01' for c in s)
# Test the function 
print(is_binary("101010"))  # Output: True
print(is_binary("hello"))  # Output: False
# Check if a string contains only ASCII characters
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
# Test the function
print(is_ascii("hello"))  # Output: True
print(is_ascii("hello©"))  # Output: False
# Check if a string contains only Unicode characters
def is_unicode(s):
    return all(ord(c) >= 128 for c in s)
# Test the function
print(is_unicode("hello"))  # Output: False
print(is_unicode("hello©"))  # Output: True
# Check if a string contains only Latin characters
def is_latin(s):
    return all(c in strings.ascii_letters for c in s)
# Test the function
print(is_latin("hello"))  # Output: True
print(is_latin("hello©"))  # Output: False
# Check if a string contains only Cyrillic characters
def is_cyrillic(s):
    return all('\u0400' <= c <= '\u04FF' for c in s)
# Test the function
print(is_cyrillic("привет"))  # Output: True
print(is_cyrillic("hello"))  # Output: False
# Check if a string contains only Greek characters
def is_greek(s):
    return all('\u0370' <= c <= '\u03FF' for c in s)
# Test the function
print(is_greek("γειά σου"))  # Output: True
print(is_greek("hello"))  # Output: False
# Check if a string contains only Arabic characters
def is_arabic(s):
    return all('\u0600' <= c <= '\u06FF' for c in s)
# Test the function
print(is_arabic("مرحبا"))  # Output: True
print(is_arabic("hello"))  # Output: False
# Check if a string contains only Hebrew characters
def is_hebrew(s):
    return all('\u0590' <= c <= '\u05FF' for c in s)
# Test the function
print(is_hebrew("שלום"))  # Output: True
print(is_hebrew("hello"))  # Output: False
# Check if a string contains only Chinese characters
def is_chinese(s):
    return all('\u4E00' <= c <= '\u9FFF' for c in s)
# Test the function
print(is_chinese("你好"))  # Output: True
print(is_chinese("hello"))  # Output: False
# Check if a string contains only Japanese characters
def is_japanese(s):
    return all('\u3040' <= c <= '\u30FF' for c in s)
# Test the function
print(is_japanese("こんにちは"))  # Output: True
print(is_japanese("hello"))  # Output: False
# Check if a string contains only Korean characters
def is_korean(s):
    return all('\uAC00' <= c <= '\uD7AF' for c in s)
# Test the function
print(is_korean("안녕하세요"))  # Output: True
print(is_korean("hello"))  # Output: False
# Check if a string contains only Thai characters
def is_thai(s):
    return all('\u0E00' <= c <= '\u0E7F' for c in s)
# Test the function
print(is_thai("สวัสดี"))  # Output: True
print(is_thai("hello"))  # Output: False
# Check if a string contains only Vietnamese characters
def is_vietnamese(s):
    return all('\u0100' <= c <= '\u017F' for c in s)
# Test the function
print(is_vietnamese("Xin chào"))  # Output: True
print(is_vietnamese("hello"))  # Output: False                                              
# Check if a string contains only Filipino characters
def is_filipino(s):
    return all('\u1700' <= c <= '\u171F' for c in s)
# Test the function
print(is_filipino("Kamusta"))  # Output: True
print(is_filipino("hello"))  # Output: False
# Check if a string contains only Indonesian characters 
def is_indonesian(s):
    return all('\u1B00' <= c <= '\u1B7F' for c in s)
# Test the function
print(is_indonesian("Halo"))  # Output: True
print(is_indonesian("hello"))  # Output: False
# Check if a string contains only Malay characters
def is_malay(s):
    return all('\u1E00' <= c <= '\u1EFF' for c in s)

# Function to calculate square of a number
def square(num):
    return num ** 2
# Test the function
print(square(5))  # Output: 25
print(square(10))  # Output: 100    
# Function to calculate cube of a number
def cube(num):
    return num ** 3
# Test the function
print(cube(5))  # Output: 125
print(cube(10))  # Output: 1000
# Function to calculate factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
# Test the function
print(factorial(5))  # Output: 120
print(factorial(10))  # Output: 3628800
# Function to calculate power of a number
def power(base, exponent):
    return base ** exponent
# Test the function
print(power(2, 3))  # Output: 8
print(power(5, 2))  # Output: 25
# Function to calculate square root of a number
def square_root(num):
    return num ** 0.5
# Test the function
print(square_root(25))  # Output: 5.0
print(square_root(100))  # Output: 10.0
# Function to calculate cube root of a number
def cube_root(num):
    return num ** (1/3)
# Test the function
print(cube_root(27))  # Output: 3.0
print(cube_root(64))  # Output: 4.0
# Function to calculate logarithm of a number
import math
def logarithm(num, base):
    return math.log(num, base)
# Test the function
print(logarithm(100, 10))  # Output: 2.0
print(logarithm(8, 2))  # Output: 3.0
# Function to calculate sine of an angle
def sine(angle):
    return math.sin(math.radians(angle))
# Test the function
print(sine(30))  # Output: 0.5
print(sine(90))  # Output: 1.0
# Function to calculate cosine of an angle
def cosine(angle):
    return math.cos(math.radians(angle))
# Test the function
print(cosine(0))  # Output: 1.0
print(cosine(60))  # Output: 0.5
# Function to calculate tangent of an angle
def tangent(angle):
    return math.tan(math.radians(angle))
# Test the function
print(tangent(45))  # Output: 1.0
print(tangent(60))  # Output: 1.7320508075688772
# Function to calculate factorial of a number using memoization
factorial_memo = {} 
def factorial_memoization(num):
    if num in factorial_memo:
        return factorial_memo[num]
    if num == 0 or num == 1:
        return 1
    else:
        factorial_memo[num] = num * factorial_memoization(num - 1)
        return factorial_memo[num]
    
import rustworkx as rx
from rustworkx.visualization import mpl_draw as draw_graph # type: ignore
import numpy as np

n = 5

graph = rx.PyGraph()
graph.add_nodes_from(np.arange(0, n, 1))
edge_list = [(0, 1, 1.0), (0, 2, 1.0), (0, 4, 1.0), (1, 2, 1.0), (2, 3, 1.0), (3, 4, 1.0)]
graph.add_edges_from(edge_list)
draw_graph(graph, node_size=600, with_labels=True)
    

 pip install ipykernel -U --user --force-reinstall
   