import os

def generate_file_list(directory="."):
    file_list = []
    try:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                file_dict = {
                    "file_name": file,
                    "file_path": os.path.abspath(file_path),
                    "file_size": os.path.getsize(file_path)
                }
                file_list.append(file_dict)
    except Exception as e:
        print(f"An error occurred: {e}")
    return file_list

if __name__ == "__main__":
    directory = "."  # You can change this to any directory path
    files = generate_file_list(directory)
    for file in files:
        print(file)
