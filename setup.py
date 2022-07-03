from setuptools import setup

setup(name='iBLOB',
      version='1.0.3',
      description='Convert any file to/from binary format',
      long_description="""
      Demo:\n
      from iBLOB import iBLOB\n
      driver = iBLOB()\n
      blob = driver.convert_to_blob('file_name.jpg')\n
      print(blob)\n
      driver.convert_from_blob(blob, 'png')\n
      """,
      author='Eden Dadon',
      packages=['iBLOB'],
      zip_safe=False)
