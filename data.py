import json

class StorageHandler():

    def __init__(self, file):
        self.file = file
    

    def save(self, data):
        try:
            print(data)
            if len(data)>0:
                with open(self.file, 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                print(f"Data saved to {self.file}")
            else:
                print('No data found')
        except Exception as e:
            print(e)
    
    def load(self):
        try:
            with open(self.file, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print(f"File {self.file} not found.")
            return None
        except json.JSONDecodeError:
            print(f"File {self.file} contains invalid JSON.")
            return None



