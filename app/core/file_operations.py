import sys
import os


def load_contents(file_path: str):
    """
    Read the contents of a file and return it. If the file is not found,
    print an error message and return None.
    """
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}", file=sys.stderr)
        return None
    
    with open(file_path, 'r') as file:
        return file.read()
    

def write_to_output_file(output: str, commented_content: str):
    """
    Append the commented content to the specified output file. 
    """
    try:
        with open(output, 'a') as f:
            f.write(commented_content + "\n\n")
            
    except IOError as e:
        print(f"Error writing to file {output}: {e}", file=sys.stderr)