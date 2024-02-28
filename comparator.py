# a simple python programme that takes a list of comma-separated numbers and returns 
# a list of the numbers from smallest to largest
# define main
def main():
    user_list = input("List your numbers> ")
    user_list = user_list.split(",")
    numbers = [int(num) for num in user_list]
    ordered_numbers = sorted(numbers)
    print("Sorted list:",ordered_numbers)

if __name__ == "__main__":
    main()