# M_script

M_script is a professional script that performs various file operations, such as merging multiple files, removing duplicate elements, extracting intersections, and differences between files. It leverages data structures and software algorithms to handle large files and complex implementations effectively.

## Features

1. Merge Multiple Files
2. Remove Duplicate Elements (shuffle-order is not important)
3. Remove Duplicate Elements (orderly-order is important)
4. Extract Intersection Between two Files
5. Extract Difference Between two Files
6. About M_script

## Requirements

The script requires Python 3.x to be installed on your system.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kasra-z/M_script.git
   
   ```
   
   Change into the project directory and use it
   ```bash
   cd M_script
   python3 main.py
   
   ```


## Usage

    Merge Multiple Files
    
    Merge multiple files into a single file.
    
    Remove Duplicate Elements (shuffle-order is not important)
    
    Remove duplicate elements from a file, regardless of their order.
    
    Remove Duplicate Elements (orderly-order is important)
    
    Remove duplicate elements from a file while preserving their order.
    
    Extract Intersection Between two Files
    
    Extract the common lines between two files.
    
    Extract Difference Between two Files
    
    Extract the unique lines that exist in either of the two files.
    
```bash
   About M_script

   Displays information about M_script.
```
# Instructions
    

   Merge Multiple Files

```bash  
        How many files do you want to merge? 3
        Please enter the path of file 1 (with .txt format): path/to/file1.txt
        Please enter the path of file 2 (with .txt format): path/to/file2.txt
        Please enter the path of file 3 (with .txt format): path/to/file3.txt
        Are you sure you want to merge these files? (yes/no) yes
        OK. Now please enter the final file name (the merged file): merged_files.txt
```

   Remove Duplicate Elements (shuffle-order is not important)

```bash
         Please enter the file path from which you want to remove duplicates: path/to/input.txt
         Please enter the name of the final file: output.txt
```

Remove Duplicate Elements (orderly-order is important)

```bash

         Please enter the file path from which you want to remove duplicates: path/to/input.txt
         Please enter the name of the final file: output.txt
```
Extract Intersection Between two Files

```bash

         Please enter the path of file 1: path/to/file1.txt
         Please enter the path of file 2: path/to/file2.txt
         Please enter the name of the final file (Intersection between file 1 and file 2): intersection.txt
```
Extract Difference Between two Files

```bash

       Please enter the path of file 1: path/to/file1.txt
       Please enter the path of file 2: path/to/file2.txt
       Please enter the name of the final file (Difference between file 1 and file 2): difference.txt
```


## Optimizations

# process bar
To optimize the M_script, you can consider the following improvements:

   Input Validation: Implement robust input validation to handle various edge cases, such as invalid file paths, incorrect file formats, and unexpected user inputs. This will enhance the reliability and usability of the script.

   Error Handling: Improve error handling by providing more informative error messages and handling exceptions gracefully. This will assist users in troubleshooting issues and provide a better user experience.

   Performance Enhancement: Analyze the file processing operations and identify potential performance bottlenecks. Explore efficient algorithms and techniques to optimize file reading, writing, and processing. This could include strategies such as buffering, parallel processing, or memory optimization to handle large files more efficiently.

   Command-Line Arguments: Add support for command-line arguments to allow users to provide input options directly when running the script. This will enable automation and easier integration with other scripts or systems.

   Logging: Implement a logging mechanism to capture and record important events, errors, and progress during script execution. This will aid in debugging, monitoring, and auditing the script's behavior.

   Unit Tests: Develop comprehensive unit tests to ensure the correctness of the script and validate its functionality under various scenarios. This will help maintain code quality and prevent regressions when making changes or adding new features.

   Documentation: Expand the script's documentation by providing detailed explanations of the implemented algorithms, data structures, and techniques. Include examples, use cases, and best practices to assist users in understanding and utilizing the script effectively.



## Contribution

Contributions to the project are welcome. To contribute, follow these steps:

   Fork the repository.
    Create a new branch for your feature or bug fix.
    Make the necessary changes and commit them.
    Push your changes to your forked repository.
    Submit a pull request explaining your changes.

Please follow the contribution guidelines for more details.

## License

This project is licensed under the MIT License.

## Support

If you encounter any issues or have any questions, please create an issue or contact author-name.





Thank you for using M_script! ❤
