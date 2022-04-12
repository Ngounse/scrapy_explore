import requests

## download image 

r = requests.get('https://image.slidesharecdn.com/slideshareisjoiningscribd-200811191829/95/slideshare-is-joining-scribd-3-1024.jpg?cb=1597174152')

print(r.content)

with open ('comic.png', 'wb') as f:
    f.write(r.content)

##---------------
