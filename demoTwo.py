from pprint import PrettyPrinter, pprint
import requests
# r is set as variable
# It's value is set by using requests library and with a get request 
r = requests.get('https://imgs.xkcd.com/comics/python.png')
pprint(r.content)


# here writing files are used. comic.png will be the file's name and will be saved in the same directory
with open('comic.png', 'wb') as f:
    f.write(r.content)
    

    
