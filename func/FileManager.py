import os

class FileUI:
    @staticmethod
    def readFileWithPath(filepath):
        if not os.path.exists(filepath):
            print("File does not exist at the specified path.")
            return None
        
        try:
            with open(filepath, 'r') as fileui_req:
                fileui_co_ = fileui_req.read()
            return fileui_co_
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    @staticmethod
    def writeFile(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    @staticmethod
    def deleteFile(file_path):
        os.remove(file_path)

    @staticmethod
    def readFileFromHome(relative_path):
        # حل کردن مسیر
        home_path = os.path.expanduser('~')
        full_path = os.path.join(home_path, relative_path)
        
        # بررسی وجود فایل
        if not os.path.exists(full_path):
            print(f"File does not exist at the specified path: {full_path}")
            return None
        
        # خواندن محتویات فایل
        try:
            with open(full_path, 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error reading file: {e}")
            return None