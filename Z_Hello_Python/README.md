# Getting Started with Linux, Python and the command line

## Environment Checklist

* UNIX-like command line (Linux, Windows Subsystem for Linux AKA WSL, MacOS Terminal)
* Terminal-based text editor (I like vim) [Best Terminal-based text editors](https://www.linuxfordevices.com/tutorials/linux/terminal-based-text-editors)
* Python and pip installation [How to use pip](https://www.freecodecamp.org/news/how-to-use-pip-install-in-python/)

## Basic terminal commands

### Navigating directories
* ```pwd``` - print working directory, list your current location in the file tree
* ```cd``` - change directory e.g. ```cd myfolder``` to go into myfolder or ```cd ..`` to go back up a level
* ```ls``` - list contents of current directory, you may also list contents of another directory like ```ls /opt```

### Creating and editing files
* ```touch``` - create a file, e.g. ```touch myscript.py```
* ```cp``` - copy a file e.g. ```cp myfile.py myfile_copy.py```
* ```mv``` - move or rename a file ```mv myfile.py flask/app.py```
* ```vim``` - open the vim text editor e.g. ```vim myscript.py``` note, you can use vim to open a file without using ```touch``` first

### Installation and python
* ```sudo apt install python3``` install python in ubuntu
* ```pip3 install pandas``` install the pandas library
* ```python3``` start python in interactive mode
* ```python3 myfile.py``` run myfile.py python script

## Other resources

* [Linux Command Cheat Sheet](https://www.guru99.com/linux-commands-cheat-sheet.html)
* [Book: The Linux Command Line, 2nd Edition](https://www.amazon.com/Linux-Command-Line-2nd-Introduction/dp/1593279523/ref=mp_s_a_1_1?keywords=linux+command+line&qid=1657824089&sr=8-1)
* [Automate the boring stuff with Python](https://automatetheboringstuff.com/)
* [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
