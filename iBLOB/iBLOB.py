class iBLOB():
    def __init__(self):
        pass

    def __str__(self):
        return "Convert any file to/from binary format"

    def __repr__(self):
        return "Convert any file to/from binary format"

    def convert_to_blob(self, in_data):
        """Convert digital data to binary format"""
        with open(in_data, 'rb') as file:
            blob_data = file.read()
        return blob_data

    def convert_from_blob(self, blob_data, out_type):
        """Convert binary data to proper format and write it on Hard Disk"""
        with open(f'output.{out_type}', 'wb') as file:
            file.write(blob_data)


"""
Demo:
driver = iBLOB()
blob = driver.convert_to_blob('file_name.jpg')
print(blob)
driver.convert_from_blob(blob, 'png')
"""
