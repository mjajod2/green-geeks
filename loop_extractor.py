import ast
import os

class LoopExtractor(ast.NodeVisitor):
    def __init__(self):
        self.loops = []

    def visit_For(self, node):
        # Extract for loops
        self.loops.append(ast.unparse(node))  # Requires Python 3.9+
        self.generic_visit(node)

    def visit_While(self, node):
        # Extract while loops
        self.loops.append(ast.unparse(node))
        self.generic_visit(node)

def wrap_loop_in_function(loop_code, function_name):
    """
    Wrap the loop code inside a function definition.
    
    Args:
    - loop_code: The code of the loop as a string.
    - function_name: The name of the function to wrap the loop in.
    
    Returns:
    A string representing the full function definition with the loop inside.
    """
    # Create the function header
    function_def = f"def {function_name}():\n"
    
    # Indent the loop code and add it inside the function body
    loop_code_indented = "\n".join([f"    {line}" for line in loop_code.splitlines()])
    
    # Combine the function definition and the indented loop code
    full_function_code = function_def + loop_code_indented
    
    return full_function_code

def extract_loops_from_file(file_path):
    """
    Extract all for-loops and while-loops from a Python file.
    """
    with open(file_path, "r") as source:
        try:
            # Parse the file into an AST (Abstract Syntax Tree)
            tree = ast.parse(source.read())
            # Initialize the loop extractor
            extractor = LoopExtractor()
            # Visit the AST nodes and collect loops
            extractor.visit(tree)
            return extractor.loops
        except SyntaxError as e:
            print(f"Error parsing {file_path}: {e}")
            return []

def extract_and_wrap_loops_from_repo(repo_path, max_loops=150):
    """
    Extract loops from Python files in a repository and wrap each loop in a function.
    """
    all_wrapped_loops = []
    
    # Walk through all files in the repository
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):  # Only process Python files
                file_path = os.path.join(root, file)
                loops = extract_loops_from_file(file_path)
                
                # Wrap each loop in a function
                for i, loop in enumerate(loops):
                    function_name = f"extracted_loop_{len(all_wrapped_loops) + 1}"  # Unique function name
                    wrapped_loop = wrap_loop_in_function(loop, function_name)
                    all_wrapped_loops.append(wrapped_loop)
                    
                    # Stop if we've reached the max number of loops
                    if len(all_wrapped_loops) >= max_loops:
                        return all_wrapped_loops

    return all_wrapped_loops[:max_loops]  # Return the loops if fewer than max_loops are found

def save_loops_to_folder(loops, output_folder):
    """
    Saves extracted and wrapped loops into individual Python files in the specified folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist

    # Save each wrapped loop in a separate Python file
    for i, loop in enumerate(loops):
        file_path = os.path.join(output_folder, f"loop_{i + 1}.py")
        with open(file_path, "w") as f:
            f.write(f"# Function containing extracted loop {i + 1}\n")
            f.write(loop)

# Example usage
repo_path = "./Python-master"  # Path to the repository
output_folder = os.path.join("./", "extracted_loops")  # Folder to save extracted loops

# Extract and wrap 100 loops from the repository
wrapped_loops = extract_and_wrap_loops_from_repo(repo_path, max_loops=150)

# Save the wrapped loops to the 'extracted_loops' folder
save_loops_to_folder(wrapped_loops, output_folder)

print(f"Extracted, and saved {len(wrapped_loops)} loops to {output_folder}")
