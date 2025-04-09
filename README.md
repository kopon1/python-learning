# 🐍 Python Learning Project – Setup Guide
Welcome! This guide will help you get started with Python, set up your own workspace in the project, and understand how to work with virtual environments (`venv`) and Git.

## Tools You'll Need

- [Download VSCode](https://code.visualstudio.com/)
- [Download Git](https://git-scm.com/)
- [Download Python](https://www.python.org/downloads/)

## Why Python?

Python is easy to read if you know English which makes it pretty non-intimidating and beginner-friendly. Key features include:
- Easy-to-learn syntax.
- Large standard library for various tasks.
- Extensive community support and third-party libraries.

## Getting Started

### 1. Clone the Repository
To get the repository on your computer you must clone it from Github.
**Git and Github are not the same!** Git is a program installed on your computer that manages repositories. Github is just a place where they are stored.

Be aware that this will create a new folder named python-learning inside the folder your terminal is at. If you aren't comfortable with the terminal, you can go into a folder using the regular Windows file explorer and type *cmd* on the address bar at the top.
This will open a console on that folder.
```bash
git clone https://github.com/xarop-pa-toss/python-learning
```

### 2. Navigate to the `dev` Folder and create your own folder
After cloning the repository, navigate to the `dev` folder. The *cd* command stands for 'Change Directory':
```bash
cd python-learning/dev
```
Create a folder with your name to organize your programs. Try to not use spaces in your folders and file names. Separate with either - or _
```bash
mkdir your-name
cd your-name
```

### 3. Create a New Subfolder for a Project
Welcome to your own folder! This is where you will create subfolders for each project. For example, to create a folder for a calculator project:
```bash
mkdir your-name/calculator
cd your-name/calculator
```

### 4. What is a Virtual Environment (venv)?
A virtual environment (venv) is a tool that helps manage dependencies for your Python projects. It creates an isolated Python environment for each project, ensuring that library versions don’t conflict between projects.
Initialize a virtual environment inside the folder:
```bash
python -m venv venv
```
Activate the virtual environment:
- On Windows:
  ```bash
  .venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 5. How VSCode Detects and Activates venvs
When you open the project folder in VSCode, it will automatically detect the virtual environment and use it for running your code. Ensure the Python extension is installed in VSCode to take full advantage of this feature.

If you are ever in the command line inside a folder and want to open it in VSCode, you can just type
```bash
code .
```
code is the command for VSCode and . is the shortcut for "current folder". Basically opening the current folder in VSCode :)

### 6. Commit your changes and push them to the repo
After you have made your folder, subfolder and created your Venv (which creates a .venv folder), your file explorer inside VSCode should have a structure kinda like this.
```
├── dev/
│   ├── your-name/
│   │   ├── calculator/
│   │   │   ├── venv/             # Virtual environment folder
│   │   │   ├── your_python_files.py
│   │   └── another-project/      # Example of another project folder
│   │       ├── venv/             # Virtual environment folder
│   │       ├── project_code.py
```
Your code only exists on your computer though, so to keep it safe and traceable, you have to push it to the repo using Git.
You can use VSCode's visual interface for Git, a button on the sidebar called Source Control which should tell you that there are changes to Commit. Add a short message that explains the changes you made, eg. "Create user folder and initialize project Calculator" or something else that feels right and press Commit and then Sync (it **pulls** changes from the repo and then **pushes** your own).
