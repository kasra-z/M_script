from logo import logo
from functions import *

def display_menu():
    print("Welcome to M_script")
    print("0 - EXIT")
    print("1 - Merge Multiple Files")
    print("2 - Remove Duplicate Elements (shuffle-order is not important)")
    print("3 - Remove Duplicate Elements (orderly-order is important)")
    print("4 - Extract Intersection Between two Files")
    print("5 - Extract Difference Between two Files")
    print("6 - About M_script")


def validate_file_extension(filename):
    if not filename.endswith(".txt"):
        return filename + ".txt"
    return filename


def get_user_input(message):
    return input(message).strip().lower()


def merge_files_menu():
    try:
        num_merge = int(input("How many files do you want to merge? "))
        file_names = []

        for n in range(num_merge):
            file_names.append(input(f"Please enter the path of file {n+1} (with .txt format): "))

        for file_name in file_names:
            print(file_name)

        result = get_user_input("Are you sure you want to merge these files? (yes/no) ")
        if result == "yes" or result == "y":
            out_file_name = input("OK. Now please enter the final file name (the merged file): ")
            out_file_name = validate_file_extension(out_file_name)
            merge_files(file_names, output_file=out_file_name)
        elif result == "no" or result == "n":
            print("OK, have a nice day!")
        else:
            print("Wrong input!!!")
    except ValueError:
        print("wrong input!!!")


def remove_duplicates_shuffle_menu():
    input_file = input("Please enter the file path from which you want to remove duplicates: ")
    output_file = input("Please enter the name of the final file: ")
    output_file = validate_file_extension(output_file)
    remove_duplicate_shuffle(input_file=input_file, output_file=output_file)


def remove_duplicates_order_menu():
    input_file = input("Please enter the file path from which you want to remove duplicates: ")
    output_file = input("Please enter the name of the final file: ")
    output_file = validate_file_extension(output_file)
    remove_duplicate_order(input_file=input_file, output_file=output_file)


def intersection_menu():
    file1 = input("Please enter the path of file 1: ")
    file2 = input("Please enter the path of file 2: ")
    output_file = input("Please enter the name of the final file (Intersection between file 1 and file 2): ")
    output_file = validate_file_extension(output_file)
    file_intersection(file1=file1, file2=file2, output_file=output_file)


def difference_menu():
    file1 = input("Please enter the path of file 1: ")
    file2 = input("Please enter the path of file 2: ")
    output_file = input("Please enter the name of the final file (Difference between file 1 and file 2): ")
    output_file = validate_file_extension(output_file)
    file_difference(file1=file1, file2=file2, output_file=output_file)


def about_menu():
    print("\nM_script is a professional script that, according to data structures and software algorithms,")
    print("can perform the best in merging files, removing duplicate values in files,")
    print("and extracting differences and similarities between two files")
    print("in the dimensions of huge files and big implementations.")
    print(logo)



def main():

    display_menu()
    user_answer = get_user_input("Please enter the option you want (0-6): ")

    if user_answer == "0" or user_answer == "exit":
        print("Have a nice day!")
        exit()
    elif user_answer == "1":
        merge_files_menu()
    elif user_answer == "2":
        remove_duplicates_shuffle_menu()
    elif user_answer == "3":
        remove_duplicates_order_menu()
    elif user_answer == "4":
        intersection_menu()
    elif user_answer == "5":
        difference_menu()
    elif user_answer == "6":
        about_menu()
    else:
        print("Wrong input!!!")

if __name__ == '__main__':
    print("Welcome to M_script")
    main()

