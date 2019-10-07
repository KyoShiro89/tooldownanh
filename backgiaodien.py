from scraper import BrickSetSpider
import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')
print(searchterm)
x = BrickSetSpider
x.parse


