from urllib.request import urlopen

shakes = urlopen('shakespeare.txt')
text = shakes.read().split()
