# aexr

A Headless Automatic Reader for Pearson eText

### Usage:
Pearson tracks how long a student has spent reading the eText. 
This is a simple solution to automatically read a specified amount of pages, each for a specified range of seconds.
For educational purposes only, of course.

## Getting Started

Download the latest build

### Prerequisites

Here's what you need:

```
Python 3.8 or newer
Modules from requirements.txt
```

### Installing


Download and extract the latest build, and install the requirements.

```
Run Install-Requirements.bat OR

CD into the directory and run:
pip install -r requirements.txt
```

Configure settings.txt

```
1. Open your eText in the browser of your choice and copy the link
2. Paste the link after 
   [Pearson-Settings]
   e_text_link = 
3. Change &pagenumber=1 or whatever page you were on, 
   to &pagenumber=i
4. Add your login credentials to 
   login_username and login_password
5. Configure Settings under [Page-Settings]
```


## Running the program

```
Run AutoETextReader.bat OR 
CD into the directory and run:
aexr.py

Choose whether to load settings from config or configure them new.
Make sure your eText link contains &pagenumber=i
```

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* tartley (colorama)
* SeleniumHQ (selenium)
* myself

