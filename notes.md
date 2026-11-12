Python uses virtual environments to create a dedicated place local to the folder where dependencies can be installed to your local project folder instead of to your machine more broadly. 

Not essential for the project but good practice.

##Y'all may know this, but I always forget how to make them and activate them.

Linux (if you don't have venv installed)
    sudo apt install python3-venv

To create a python virtual environment:
    Linux and Mac CLI "python3 -m venv venv"
    Windows "python -m venv venv" or "py -m venv venv"


To activate the python virtual environment:
    Linux and Mac CLI "source venv/bin/activate"
    Windows PowerShell "venv\Scripts\Activate.ps1"
    Windows Command Prompt "venv\Scripts\activate.bat"