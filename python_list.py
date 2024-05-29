import os 
def generate_fileList(): 
      fileList = []  
      for file in os.listdir():  
             if os.path.isfile(file):  
                fileDict = {  
                "file_name": file,                     
                "file_path": os.path.abspath(file),    
                "file_size": os.path.getsize(file)      
            }
                fileList.append(fileDict)   
      return fileList    

if __name__ == "__main__":
       files = generate_fileList()  
       for file in files: 
            print(file)