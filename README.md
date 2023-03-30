This is a Python script that compresses directories into ZIP files. It's a simple but useful tool that can help keep your projects folder organized and save space on your computer.

To use the script, simply download the zip.py file and run it from your terminal using the command python3 zip.py. The script will prompt you to enter the path to the directory you want to compress, and it will then create a ZIP file of that directory inside the original directory.

For example, if you have a directory called my_project located at /Users/username/Documents/projects/, you would enter /Users/username/Documents/projects/my_project when prompted by the script. The resulting ZIP file will be located inside the my_project directory.

The script uses the zipfile module in Python to create the ZIP file. It first checks if the directory exists and if it's not already a ZIP file. If the directory exists and is not already a ZIP file, it creates a new ZIP file with the same name as the directory and adds all the files and subdirectories inside the directory to the ZIP file.

The script is designed to be simple and easy to use, with clear prompts and minimal input required. It's perfect for when you need to quickly compress a directory and don't want to deal with the complexities of other compression tools.

So go ahead and give it a try! And if you have any questions or feedback, feel free to leave a comment or open an issue in the repository. Happy compressing!
