def extract_functions(python_filename, output_filename):
    lines = ""
    with open(python_filename, "r") as python_file, open(output_filename, "w") as output_file:
        for line in python_file:
            lines += line
        functions = lines.split("def")
        functions.pop(0)
        for i in range(len(functions)):
            name, contents = functions[i].split(":", 1)
            ds_start = contents.find('"""')
            ds_end = contents.rfind('"""')
            docstring = contents[ds_start + 3:ds_end].strip().strip("\n")
            if docstring[0:4] != "    ":
                docstring = "    " + docstring
            name = f"{i + 1}.{name}"
            output_file.write(f"{name}\n{docstring}\n\n")


extract_functions("python_script.py", "q6_output.txt")
