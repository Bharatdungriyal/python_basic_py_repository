"""Shutil is a Python module that provides a higher level interface for working with file and
directories. The name "shutil" is short for shell utility. It provides a convenient and efficient way
to automate tasks that are commonly performed on files and directories"""

import shutil
import os
shutil.copy("shutil_module.py", "main2.py")     #1
"""shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. 
If the destination location already exists, the original file will be overwritten"""

shutil.copy2("shutile_module.py,main2.py")     #2
"""shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata
 about the original file, such as the timestamp."""


shutil.copytree("lib", "my tutorial")           #3
"""shutil.copytree(src, dst): This function recursively copies the directory located at src to a 
new location specified by dst. If the destination location already exists,
 the original directory will be merged with it."""

shutil.move("my tutorial/tut_baby.py","max.max")      #4
"""shutil.move(src, dst): This function moves the file located at src to a new location specified by dst.
 This function is equivalent to renaming a file in most cases."""

shutil.rmtree("my tutorial")          #5  to delete the folder only
"""shutil.rmtree(path): This function recursively deletes the directory located at path, 
along with all of its contents. This function is similar to using the rm -rf command in a shell. """

os.remove("file.file")  # to delete the file
# The os. remove() method in Python is used to remove a file at a specified path
