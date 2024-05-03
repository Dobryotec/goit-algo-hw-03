import os
import shutil

def parse_input(user_input):
    return user_input.strip().lower().split()

def copy_files(source_dir, dest_dir="dist"):
    try:
        if os.path.isdir(source_dir):
            for item in os.listdir(source_dir):
                item_path = os.path.join(source_dir, item)
                if os.path.isdir(item_path):
                    copy_files(item_path, dest_dir)
                else:
                    filename_parts = item.split(".")
                    file_extension = filename_parts[-1]
                    extension_dir = os.path.join(dest_dir, file_extension)
                    os.makedirs(extension_dir, exist_ok=True)
                    dest_file_path = os.path.join(extension_dir, item)
                    shutil.copy(item_path, dest_file_path)
            print("Files copied successfully.")
        else:
            print("Source directory does not exist.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("Welcome!")

    while True:
        user_input = parse_input(input("Enter the path to the source directory and optionally to the destination directory: "))
        if not user_input:
            print("Invalid path specified.")
            break
        
        elif user_input[0] == "exit":
            print("Exiting the program.")
            break 
        elif len(user_input) < 2:
            copy_files(user_input[0], dest_dir='dist')   
        else:    
            copy_files(user_input[0], user_input[1])
                  
if __name__ == "__main__":
    main()