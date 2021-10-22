from html.parser import HTMLParser


class HtmlParser(HTMLParser):
    voidTags = ["area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen",
                "link", "meta", "param", "source", "track", "wbr"]  # Tags don't need closing

    def __init__(self, content=None):
        super().__init__()
        self.topTags = []
        self.positions = []

        if content != None:
            self.feed(content)

    def handle_starttag(self, tag, attrs):
        """
        Method overwritten from superclass: Handles a starttag occurrence in the content
        :param tag: The tag (string)
        :param attrs: The attributes of the tag
        """
        newTag = Tag(tag, attrs)
        if len(self.positions) == 0:
            self.topTags.append(newTag)
            self.positions.append(len(self.topTags) - 1)
        else:
            self.__addTagToCurrentPosition(newTag)
        if tag in self.voidTags:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        """
        Method overwritten from superclass: Handles an endtag occurence in the content
        :param tag:
        """
        self.positions.pop(len(self.positions) - 1)

    def handle_data(self, data):
        """
        Method overwritten from superclass: Handles data in the tags
        :param data: The data in the tag
        """
        if len(self.positions) != 0:
            currentChild = self.topTags[self.positions[0]]
            counter = 1
            while counter < len(self.positions):
                currentChild = currentChild.children[self.positions[counter]]
                counter += 1
            currentChild.data += data

    def getAllTags(self):
        """
        Returns all tags as one array
        :return: All tags as one array
        """
        allTags = self.__getAllTags(self.topTags)
        allTags.reverse()
        return allTags

    def __getAllTags(self, tagArray):
        """
        Simple Recursion Algorithm for getting all the tags (including children in an array)
        :param tagArray: The Array of tags from which to get the tag
        :return: The completed tag array
        """
        result = []
        for i in tagArray:
            if len(i.children) != 0:
                result += self.__getAllTags(i.children)
            temp = i
            temp.children = []
            result.append(temp)
        return result

    def __addTagToCurrentPosition(self, tag):
        """
        Private methode which adds a tag to the current Position of the positions array
        :param tag: The tag (tag-class) which should be added
        """
        currentChild = self.topTags[self.positions[0]]
        counter = 1
        while counter < len(self.positions):
            currentChild = currentChild.children[self.positions[counter]]
            counter += 1
        currentChild.children.append(tag)
        self.positions.append(len(currentChild.children) - 1)



class Tag:
    def __init__(self, tag, attributes):
        self.tag = tag
        self.attributes = attributes
        self.data = ""
        self.children = []
