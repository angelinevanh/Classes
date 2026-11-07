"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one number
# 2. Process, function by function: main function evaluates the number through if, else and elseif checks.
#   it checks if the number is zero, if it is greater than zero, less than zero, if it is even. if none of the above, it defaults to labelling the number as odd.
# 3. Out: whether the number is positive or negative
# 4. The question my fourth function answers: is_negative checks whether the number is negative.


# Your code below
def is_even(number):
    """True when the number divides by two exactly."""
    return number % 2 == 0

def is_zero(number):
    """True when the number is zero."""
    return number == 0


def is_positive(num):
    return num > 0

def is_negative(num):
    return num < 0


def detailed_message(num):
    if is_zero(num):
        return "The number is zero."
    elif is_positive(num):
        return "The number is positive."
    elif is_negative(num):
        return "The number is negative."
    elif is_even(num):
        return "The number is even."
    else:
        return "The number is odd."

number = 6
print(detailed_message(number))

print(detailed_message(-4))