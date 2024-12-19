
import os

start_path = os.path.join("/home/lukiwa/Documents/Python/Power_BI", "")

directories = [
    ""
]

for directory in directories : 
    try : 
        # Create the directory
        dir_path = os.path.join(start_path, directory)
        os.mkdir(dir_path)

        # Add the .gitkeep file inside the created directory
        gitkeep_path = os.path.join(dir_path, ".gitkeep")
        with open(gitkeep_path, "w") as f:
            f.write("")
    except FileExistsError : 
        print(f"{directory} already exists")
    except Exception as e : 
        print(f"An error occurred: {e}")
    else : 
        print(f"{directory} created successfully")
    finally : 
        print("End of the loop")