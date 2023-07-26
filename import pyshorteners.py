# url shortener
import pyshorteners
url = input("enter url: ")
s = pyshorteners.Shortener()
print(s.tinyurl.short(url))