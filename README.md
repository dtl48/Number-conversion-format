# Number-conversion-format

David Ly

Read Me

Calc.py:

In calc.py, the first input is for the operations for num1 and num2. The choices are +,-,m.
“+” Means plus, “-” means minus, and “m” means multiplication. Next two inputs are num1 and
num2. If the number inputted is negative place in front of the number a “-”. The type of the
number is represented by “d” for decimal, “b” for binary, “o” for octal, and “x” for hex. The last
input is for the type that wants to be outputted. The types are “d”, “b”, “o”, “x”.

Examples: python calc.py + d20 -d5 x
answer : xF

In calc.py, num1 and num2 are checked if they are are negative or not and then the next check
would be the type each number is. The negative would be noted and num1 and num2 would be
changed from the type detected and changes it to a decimal. When both num1 and num2 are
changed to decimal, the numbers are changed accordingly to negatives if there was a negative
sign attached to that number. Both numbers are then either added, subtracted or multiplied
based on the operations given (+,-,m). The number will then be changed to the type that was
selected at the output. Challenges i faced was how to handle negative signs for different types of numbers. I
ended up just making the number negative if there was a negative sign in either num1 and num2.

Example: python calc.py m -d5 -xa o
Answer: o62

This would run like this: -5 * -10 = 50. 50 in Decimal is 62 in oct. The answer is o62.
Format.py:

In format.py, a binary number with the length of 32 bits is inputted into the function. Only
one parameter is inputted because it is assumed that the number is a binary number that is an
int. If it is not 32 bits, an error will occur. If the bits in the binary number is not either a 1 or 0, an
error will occur. The binary number first detect the bit at placement [0] to check if there is a 1. If
it is a 1 then the binary number is a negative. The binary number will be flipped and the flipped
binary number would be converted to a decimal. The decimal number will be added by 1 and
the negative sign would be added to show that it is negative. If the binary number is not
negative, it would just be converted to a decimal.

Example: python format.py 11111111111111111111111111110011
Answer: -13

Challenges in this is figuring out how to convert a negative binary number to a decimal. The
solution was to flip the binary number and add 1 to get the correct negative decimal.
