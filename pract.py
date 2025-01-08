#1 WAP to take input 2 numbers from the user and print the sum of the numbers.
x= int(input("first number :"))
y = int(input("second number:"))
sum = x+y
print(sum)
#2 WAP to take input 1 number from the user and print its square and cube.

x = int(input("any number for square and cube: "))
sq = x**2
cube= x**3
print(sq,cube)

#3 WAP to calculate and print area of circle and circumference of circle.

r= float(input("radius for area of square "))
area = 3.14*r**2
circumstence= 2*3.14*r
print(area,circumstence)
#4 WAP to take input rupees from the user and convert it into paise.
rupee = int(input("input for rupee to paise"))
paise= rupee*100
print(paise,"paise")


#5 WAP to take input days from the user and convert it into years, months, and remaining days.
total_days = int(input("no of days:::: "))
years = total_days // 365
remaining_day = total_days % 365
month = remaining_day // 30
days = remaining_day % 30
print(years, month, days)
# WAP to take input 3 digit numbers from the user and print sum of 1 and 3 digit.
num = int(input("enter a three digit number"))
fst = num//100
thirt = num%10
sum = fst+thirt
print(sum)
# WAP to take input 3 digit numbers from the user and print the square of the middle digit.
num = int(input("enter a three digit number"))
middle = num%100
result = middle//10
sq= result**2
print(sq)
# WAP to take input 4 digit numbers from the user and print its all digits.
num = int(input("enter a four digit number"))
num1 = num//1000
num2= (num%1000)//100
num3 = (num%100)//10
num4 = num%10
print(num1,num2,num3,num4)

#WAP to check whether a number is even or odd.
# WAP to check whether the number is positive, negative or zero.
# WAP to take input two numbers from the user and print the largest of them.
#WAP to take input 2 numbers from the user and print their difference.
# WAP to take input 3 numbers from the user and print the largest number among them.
#WAP to take input 3 numbers and print the 2nd largest number among them.
x = int(input("1st"))
y= int(input("2nd"))
z= int(input("3rd"))
if (x>y and x<z) or (x<y and x>z):
    secondlargest = x
elif (y>x and y<z) or (y<x and y>z):
    secondlargest = y
else:
    secondlargest= z

print(secondlargest)
#WAP to take input a number (range 1 to 7) from the user and print the corresponding week.
# WAP to input year from user and check whether it is a leap year or not.
inp = int(input("checking leap year or not"))
if (inp %400==0 and inp%100 == 0):
    print("it is a leap year")
elif (inp % 4==0 and inp%100!=0):
    print("it is a leap year")
else:
    print("not a leap year")

# WAP to take input 3 numbers from the user and print the numbers in the descending order.
x1= int(input("fst"))
x2= int(input("sec"))
x3= int(input("thrd"))
if x1>=x2 and x1>=x3:
    if x2>=x3:
        print(x1,x2,x3)
    else:
        print(x1,x3,x2)
elif x2>=x1 and x2>=x3:
    if x3>=x1:
        print(x2,x3,x1)
    else:
        print(x2,x1,x3)

elif x3>=x2 and x3>=x1:
    if x1>=x2:
        print(x3,x1,x2)
    else:
        print(x3,x2,x1)
"""
WAP to take input income from the user and calculate the amount of tax to be paid as per rules.
Less or equal to 10,000 -> no tax
Greater than 10,000 and less or equal to 25,000 -> 10% of income above 10,000
Greater than 25,000 and less or equal to 50,000 -> 2500 + 20% income above 25,000
Greater than 50,000 -> 5000 + 30% of income above 50,000 """

income = int(input("user income: "))
if income<=10000:
    print("no tax")
elif income > 10000 and income<=25000 :
    print("10 percent of income above 10,0000")
    print(10/100*(income-10000))
elif income >25000 and income<= 50000:
    print("2500+ 20 percent income")
    print(2500+(20/100*(income-25000)))
elif income > 50000 :
    print("5000 with 30% of income")
    print(5000 + (30/100*(income-50000)))

#WAP to perform arithmetic operations as per user's choice.
option = input("enter any one arithmetic operation +,_,*,/,%..: ")
inp1 = float(input("first num: "))
inp2 = float(input("snd num: "))
if option == "+":
    print(inp1+inp2)
elif option == "-":
    print(inp1-inp2)
elif option == "*":
    print(inp1*inp2)
elif option == "/":
    print(inp1/inp2)
elif option == "%":
    print(inp1%inp2)

# **** WAP to input a character from user and check whether it is an alphabets, digits, or special symbols.
# Input a character from the user
char = input("Enter a character: ")

# Check if the character is an alphabet
if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    print(f"{char} is an alphabet.")
# Check if the character is a digit
elif '0' <= char <= '9':
    print(f"{char} is a digit.")
# If it's neither an alphabet nor a digit, it's a special symbol
else:
    print(f"{char} is a special symbol.")


# find the count of special symbol between an string
# Input a string from the user
input_string = input("Enter a string: ")

# Initialize a counter for special symbols
special_count = 0

# Iterate through each character in the string
for char in input_string:
    # Check if the character is not an alphabet or digit, i.e., it's a special symbol
    if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')):
        special_count += 1

# Output the count of special symbols
print(f"The count of special symbols in the string is: {special_count}")
"""
WAP to input a character from user and check whether it is uppercase and lowercase.
WAP to check whether a character given by user is a vowel or consonant.
"""
# WAP to input a lower limit and an upper limit from user and print all the numbers in between the given limits.

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

# Check if the lower limit is less than or equal to the upper limit
if lower_limit <= upper_limit:
    print(f"Numbers between {lower_limit} and {upper_limit} are:")
    # Loop through the range and print each number
    for num in range(lower_limit + 1, upper_limit):
        print(num, end=" ")
else:
    print("Invalid input: lower limit should be less than or equal to upper limit.")
# WAP to input a lower limit and an upper limit from user and print all the numbers in between the given limits.
# WAP to input a lower limit and an upper limit from user and print all the even numbers in between the given limits.
# WAP to input a number from user and print its factorial.
inp = int(input("number for factorial: "))
fact= 1
if inp<0:
    print("no factorial for negative number")
elif inp==0:
    print(1)
else:
    for i in range(1,inp+1):
        fact = fact*i
    print(fact)


# WAP to input a number from user and print its table.

tabl = int(input("number for table"))
for item in range(1,11):
    print(f"{tabl}X{item} = ",tabl*item)
# WAP to print the sum of the divisors of a number given by user.
number = int(input("enter a number for divide"))
sum = 0
if number<0 :
    print("enter a positive number " )
elif number==0:
    print(0)
else:
    for item in range(1,number+1):
        if number %item ==0:
            sum= sum + item
            
    print(sum)
        

# WAP to check whether a number is perfect or not.
# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
inp= int(input("enter to check for perfect number: "))
demo= 0
for item in range(1,inp):
    if inp % item ==0:
        demo = demo+item
if demo==inp:
    print("it is a perfect number")
else:
    print("not a perfect number")

# WAP to print the reverse of a number given by user.
num = int(input("NUmber : "))
reverse_num= 0
while num>0:
    rev = num%10
    reverse_num = reverse_num*10 + rev
    num= num//10
print(reverse_num)


# making function
def reverse_number(n):
    # Initialize the reversed number as 0
    reversed_num = 0
    
    # Process each digit
    while n > 0:
        digit = n % 10  # Extract the last digit
        reversed_num = reversed_num * 10 + digit  # Append the digit
        n = n // 10  # Remove the last digit
    
    return reversed_num

# Input from the user
number = int(input("Enter a number: "))

# Reverse the number and display the result
reversed_number = reverse_number(number)
print(f"The reverse of {number} is {reversed_number}.")

# A palindrome is a number (or a word) that reads the same backward as forward
num = int(input("check for palidrome"))
org_num= num
rever_num = 0
while num>0:
    revers = num%10
    rever_num = rever_num*10 + revers
    num = num//10
if rever_num == org_num:
    print(" it is a palidrome number")
else:
    print("Not palidrome")

# An Armstrong number (or Narcissistic number) is a number that is equal to the sum of its own digits,-
# -each raised to the power of the number of digits.
num = int(input("Enter a number to check if it's an Armstrong number: "))
original_num = num
num_of_digits = len(str(num))
sum_of_powers = 0
while num > 0:
    digit = num % 10
    sum_of_powers += digit ** num_of_digits
    num = num // 10
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
