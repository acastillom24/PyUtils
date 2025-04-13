import os

class RemoveFile:
    def __init__(self, path):
        self.path = path

    def removeFile(self):
        if os.path.exists(self.path):
            os.remove(self.path)
        else:
            print("The file does not exist")

    def removeFiles(self):
        if os.path.exists(self.path):
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    os.remove(os.path.join(root, file))
        else:
            print("The file does not exist")

# Example usage
path = "C:\\Users\\User\\Desktop\\Test"
remove_file = RemoveFile(path)
remove_file.removeFile()
