import sys
from pychad_interpreter import PychadInterpreter

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <pychad_code_file>")
        return
    
    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            pychad_code = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return
    
    interpreter = PychadInterpreter()
    interpreter.interpret(pychad_code)

if __name__ == "__main__":
    main()
def generate_pychad_code():
    # Generate or define your Pychad code here
    pychad_code = """
    rizz lines
    sick lines 5
    rizz up
    treat me like white tees
    princ lines, rizz, sick, treat me like white tees, rizz up
    """
    return pychad_code

def save_to_pycd_file(pychad_code, file_name):
    with open(file_name, 'w') as file:
        file.write(pychad_code)

def main():
    # Generate Pychad code
    pychad_code = generate_pychad_code()
    
    # Save Pychad code to a .pycd file
    file_name = 'test.pycd'
    save_to_pycd_file(pychad_code, file_name)
    print(f"Pychad code saved to {file_name}")

if __name__ == "__main__":
    main()
