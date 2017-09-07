# Droplr Scraper

Scrapes droplr short links by generating random slugs and then checking if they are valid. Sometimes returns juicy links!

## Compatibility

Python 2 or 3

## Usage

Open `DroplrScraper.py` in your text editor of choice and fill in your Droplr.com username and password on lines 20-21.

Then open CMD or Terminal and run the following command to install the dependency:
```
pip install requests
```

To execute the script, run the following command:
```
python DroplrScraper.py {count}
```

**Parameters**

`count` is the number of slugs you want to generate and check, must be an integer.