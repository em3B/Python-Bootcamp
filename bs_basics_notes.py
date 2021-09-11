from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
d = soup.select("[data-example]")
print(d)
print(type(soup))
print(soup.body)
print(soup.body.div) #just gives first div
print(soup.find("div"))

print(type(d))
print(soup.find_all("div"))
print(soup.find(id="first"))
print(soup.find_all(class_="special")) #***for BS, us class_ for class. also use find_all for class

print(soup.find_all(attrs={"data-example": "yes"})) #**select based off of attributes

print(soup.select("#first")) #same as soup.find(id="first")
print(soup.select("div"))
print(soup.select("[data-example]"))     #use [] to search for attributes wiht select 

el = soup.select(".special")[0]
print(el.get_text())
print(el.name)

#another way to get text:
# for el in soup.select(".special"):
      #print(el.name)

print(el.attrs)

attr= soup.find("h3")["data-example"] #specifies class of data-ex
print(attr)
