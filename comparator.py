# a simple python programme that takes a list of comma-separated numbers and returns 
# a list of the numbers from smallest to largest
# define main
def main():
    # get a list of numbers from the user
    user_list = input("List your numbers> ")
    
    # split the numbers using a comma and store them in a list
    user_list = user_list.split(",")

    # convert the string values in the list to integers
    numbers = [int(num) for num in user_list]

    # use the sorted function to sort the numbers
    ordered_numbers = sorted(numbers)

    # print the sorted list
    print("Sorted list:",ordered_numbers)

if __name__ == "__main__":
    main()