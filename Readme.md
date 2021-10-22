**HtmlParser**

HtmlParser is  a simple Python class which can help you interpret
repositories

**How to use:**<br>
First import the parser from its class:
```python
from HtmlParser import HtmlParser
```
Create a new parser object using the following code:
```python
parser = HtmlParser()
```
You can either pass the html file in the constructor:
```python
parser = HtmlParser("<html></html>")
```
Or feed it later:
```python
parser = HtmlParser()
parser.feed("<html></html>")
```

Then you can extract an array of top-level tags from the object by using the following code:
```python
topLevelTags = parser.topTags
```
You can get the children by using the children variable in the tag object:
```python
children = topLevelTags[0].children #Get the children of the first top level tag
myTag = children[0] #Get the first child
```

If you want all the tags in the html in one array use the following code:
```python
allTags = parser.getAllTags()
```

To access information (such as data, attributes and the tag) from the tag type use:
```python
print(myTag.tag)
print(myTag.attributes)
print(myTag.data)
```