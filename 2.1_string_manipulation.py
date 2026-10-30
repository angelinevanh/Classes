"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:" hey Everyone from Paris "
# 2. Process:Using strip, lower, upper, swapcase.
# 3. Out:the modified versions, hopefully
# 4. My four transformations, and when each is useful: strip() is to trim unnecessary spaces.
# lower() is to convert text to lowercase, and upper() is to convert to uppercase.
# swapcase() for when you realise you typed blindly. 


# Your code below
sentence = " hey Everyone from Paris"

# Transformation 1
result1 = sentence.strip()
# result to be checked

# Transformation 2
result2 = sentence.lower()
#result to be checked

# Transformation 3
result3 = sentence.upper()
# result to be checked

# Transformation 4
result4 = sentence.swapcase()
# result to be checked

print(result1)
print(result2)
print(result3)
print(result4)