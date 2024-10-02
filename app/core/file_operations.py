import sys
import os
import tomllib


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

def find_toml():
    home_dir = os.path.expanduser("~")
    for file in os.listdir(home_dir):
        if file == "addcom_config.toml":
            return os.path.join(home_dir,file)
    print("Config File Wasn't Found")
    return None

def read_toml(file: str):
    if not os.path.isfile(file):
        print(f"File not found: {file}", file=sys.stderr)
        return None

    with open(file,"rb") as f:
        data = tomllib.load(f)
        return data
    
def get_config():
    toml_file =find_toml()

    if toml_file:
        config_data = read_toml(toml_file)
        return config_data

    return None
    
    
    


