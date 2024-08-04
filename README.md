To use this program you have to setup and virutual enviorment or alternatively install the Python libs on your own. 

Here is the step by step guide:

***Step 1***

Start by creating a new directory where you want the program to reside with
<code>cd 'C:/Enter/Your/Directory/Of/Choice'</code> followed with 
<code>mkdir 'Enter a name for the folder'</code> and 
<code>cd 'Name you just entered'</code>

***Step 2***

Clone the repo and get create the virtual environment
<code>git clone https://github.com/hughu123/BenifitList.git</code>
Enter the newly cloned repo <code>cd BenifitList</code> and create the .venv enviorment with <code>python -m venv .venv</code> 
*(you might need to get python.exe from its program folder in <code>C:\Users\your-name\AppData\Local\Programs\Python\Python310\python.exe</code>)*

***Step 3***

Now there exists a new folder called <code>.venv</code>.

<code>.\.venv\Scripts\activate.bat</code> followed with <code>.\.venv\Scripts\pip.exe install /r .\requirements.txt</code>

After this you can now run the program with <code>.\.venv\Scripts\python.exe .\BenifitList.py</code>

****TL;DR****

Do these comands in order (you need Python on your pc tho)

<code>git clone https://github.com/hughu123/BenifitList.git</code>

<code>cd BenifitList</code>

<code>python -m venv .venv</code>

<code>.\.venv\Scripts\activate.bat</code>

<code>.\.venv\Scripts\pip.exe install /r .\requirements.txt</code>

<code>.\.venv\Scripts\python.exe .\BenifitList.py</code>

And if you're done you can deactivate the virutal enviorment with <code>.\.venv\Scripts\deactivate.bat</code>

Done
