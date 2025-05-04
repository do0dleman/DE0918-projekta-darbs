from html.parser import HTMLParser
from html.entities import name2codepoint
import json

class Element:
    def __init__(self, tag, attrs=[], parent=None):
        self.tag = tag
        self.parent = parent
        self.children = []

        # convert attributs from tuple[str, str] to dictionary
        dict_attrs = {}
        for attr in attrs:
            dict_attrs[attr[0]] = attr[1]

        self.attrs = dict_attrs

    @classmethod
    def fromString(cls, string):
        text_node = cls("text", [("value", string)])
        return text_node
    
    def to_dict(self):
        dict_children = list(map(lambda child: child.to_dict(), self.children))
        return {
            "tag": self.tag,
            "attrs": self.attrs,
            "children": dict_children
        }
    
    def get_id(self):
        return self.attrs.get("id")
    
    def print(self):
        print(json.dumps(self.to_dict(),indent=2))
            
        

# example from docs
class HtmlTree(HTMLParser):
    def __init__(self, *, convert_charrefs = True):
        super().__init__(convert_charrefs=convert_charrefs)

        self.root = Element("document")
        self.current = self.root

    def handle_starttag(self, tag, attrs):
        new_element = Element(tag, attrs, self.current)
        self.current.children.append(new_element)
        self.current = new_element

    def handle_endtag(self, tag):
        if self.current.parent:
            self.current = self.current.parent

    def handle_data(self, data):
        self.current.children.append(Element.fromString(data))

    def to_dict(self):
        return self.root.to_dict()
    
    def print(self):
        print(json.dumps(self.to_dict(),indent=2))
    
    def get_by_id(self, id, element=None):
        if element==None:
          element = self.root
        
        if element.get_id() == id:
            return element
        
        for child in element.children:
            foundElement = self.get_by_id(id, element=child)
            if foundElement is not None:
                return foundElement
            