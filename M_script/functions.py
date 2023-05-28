from collections import deque

def merge_files(filenames, output_file):
    try:
        with open(output_file, 'w') as outfile:
            for file in filenames:
                try:
                    with open(file) as infile:
                        for line in infile:
                            outfile.write(line)
                except FileNotFoundError:
                    print(f"Error: File '{file}' not found.")
                except IOError:
                    print(f"Error: Failed to read file '{file}'.")
            print(f"all files merged and saved to '{output_file}'.")  
    except IOError:
        print(f"Error: Failed to create output file '{output_file}'.")


def remove_duplicate_shuffle(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            unique_elements = set(line.strip() for line in infile)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError:
        print(f"Error: Failed to read file '{input_file}'.")

    try:
        with open(output_file, 'w') as outfile:
            for element in unique_elements:
                outfile.write(element + "\n")
            print(f"all duplicate values removed and new file saved to '{output_file}'.")
            
    except IOError:
        print(f"Error: Failed to create output file '{output_file}'.")


def remove_duplicate_order(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            unique_elements = set()
            ordered_elements = deque()

            for line in infile:
                cleaned_line = line.strip()

                if cleaned_line not in unique_elements:
                    unique_elements.add(cleaned_line)
                    ordered_elements.append(cleaned_line)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError:
        print(f"Error: Failed to read file '{input_file}'.")

    try:
        with open(output_file, 'w') as outfile:
            for element in ordered_elements:
                outfile.write(element + '\n')
            print(f"all duplicate values removed and new file saved to '{output_file}'.")

    except IOError:
        print(f"Error: Failed to create output file '{output_file}'.")


def file_intersection(file1, file2, output_file):
    try:
        with open(file1, 'r') as infile1, open(file2, 'r') as infile2:
            lines1 = set(infile1.readlines())
            lines2 = set(infile2.readlines())
            common_lines = lines1 & lines2
    except FileNotFoundError:
        print(f"Error: File '{file1}' or '{file2}' not found.")
        return
    except IOError:
        print(f"Error: Failed to read file '{file1}' or '{file2}'.")
        return

    try:
        with open(output_file, 'w') as outfile:
            outfile.writelines(common_lines)
        print(f"Common lines extracted and saved to '{output_file}'.")
    except IOError:
        print(f"Error: Failed to create output file '{output_file}'.")


def file_difference(file1, file2, output_file):
    try:
        with open(file1, 'r') as infile1, open(file2, 'r') as infile2:
            lines1 = set(infile1)
            lines2 = set(infile2)
            difference = lines1.symmetric_difference(lines2)
    except FileNotFoundError:
        print(f"Error: File '{file1}' or '{file2}' not found.")
        return
    except IOError:
        print(f"Error: Failed to read file '{file1}' or '{file2}'.")
        return

    try:
        with open(output_file, 'w') as outfile:
            outfile.writelines(difference)
        print(f"Difference extracted and saved to '{output_file}'.")
    except IOError:
        print(f"Error: Failed to create output file '{output_file}'.")

