# What is this?

A quick and simple service for getting pictures of whatever-you-want for use as placeholders in your designs or code. Just put your image size (width & height) after the URL and you'll get a placeholder. Similar URL as [Placekitten](http://placekitten.com).

There is also a bookmarklet service which works the same as [Horse_ebookmarklet](http://www.heyben.com/horse_ebookmarklet/).

## Installation

Dependencies are handled by [pip](http://pypi.python.org/pypi/pip), install it on your machine (if you use virtualenv, create a new venv).

  1. Go to the code: `cd path/to/holder`
  1. Get dependencies in place: `pip install -r requirements.txt`
  1. Start the app: `python wsgi.py`
  1. Go to [http://localhost:5001](http://localhost:5001) in your web browser.
  1. Done!

## Example calls

    # generates an image, 200px wide and 300px tall
    http://localhost:5001/200/300
    
    # generates an image in grayscale, 200px wide and 300px tall
    http://localhost:5001/g/200/300
    
    # generates an image using a specific theme, 200px wide and 300px tall
    http://localhost:5001/200/300/custom-theme
    
    # generates an image in grayscale using a specific theme, 200px wide and 300px tall
    http://localhost:5001/g/200/300/custom-theme

## Images
  
The images used are stored in `images` in sub directories (themes).
  
You can create your own themes by creating new sub directories and populate it with images. High-res JPGs are recommended.
