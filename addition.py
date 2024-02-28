# a simple python program that gets two integers from the user and returns the sum
# a main function
def main():
    num1 = int(input("First integer> "))
    num2 = int(input("Second integer> "))
    result = addition(num1, num2)
    print("The sum of the two numbers is",result)
# a function called addition
def addition(a,b):
    return a+b

main()