# Time.com Latest Stories Scraper

This Python script uses Selenium to scrape the latest stories from the Time.com website and saves the results in a JSON file.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Chrome browser
- ChromeDriver (Automatically installed using `chromedriver-autoinstaller`)

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script using Python:

```bash
python script.py
```

2. The script will open the Time.com website, close any pop-up ads, and scrape the titles and links of the latest stories.
3. The results will be saved in a file named `data.json` in the same directory.

## File Description

- `script.py`: Python script to scrape the latest stories from Time.com using Selenium.
- `data.json`: JSON file containing the scraped latest stories.

