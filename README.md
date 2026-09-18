Wikipedia Article Reader

A simple command-line tool that fetches and displays Wikipedia articles,including infobox data and full article text.
Features

    Search any Wikipedia topic interactively
    Displays infobox caption and key-value table data
    Prints the full article content
    Handles multi-word search queries with URL encoding
    Clear error messages for network failures and 404 pages

Requirements

    Python 3.8+
    requests
    beautifulsoup4

Installation

git clone https://github.com/USERNAME/wikipedia-reader.gitcd wikipedia-readerpip install -r requirements.txt

Usage
bash
 
  
 
 
python main.py
 
 

Then type any topic to read its Wikipedia article:
text
 
  
 
 
Search something (q to exit): artificial intelligence
 
 

