from html.parser import HTMLParser
from parser.self_closing_tags import SELF_CLOSING_TAGS
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
    
    def to_dict(self, include_chldren=False):
        dict_element = {       
            "tag": self.tag,
            "attrs": self.attrs,
        }
        if include_chldren:
            dict_element["children"] = list(map(lambda child: child.to_dict(include_chldren), self.children))

        return dict_element
    
    def get_id(self):
        return self.attrs.get("id") or ""
    
    def print(self, include_chldren=False):
        print(json.dumps(self.to_dict(include_chldren),indent=2))
            
        

# example from docs
class HtmlTree(HTMLParser):
    def __init__(self, *, convert_charrefs = True):
        super().__init__(convert_charrefs=convert_charrefs)

        self.root = Element("document")
        self.current = self.root

    @classmethod
    def fromElement(cls, element):
        new_tree = cls()
        new_tree.root = element
        new_tree.current = element

    def handle_starttag(self, tag, attrs):
        new_element = Element(tag, attrs, self.current)
        self.current.children.append(new_element)
        if tag not in SELF_CLOSING_TAGS:
            self.current = new_element

    def handle_endtag(self, tag):
        if self.current.parent:
            self.current = self.current.parent

    def handle_data(self, data):
        self.current.children.append(Element.fromString(data))

    def to_dict(self, include_chldren=True):
        return self.root.to_dict(include_chldren)
    
    def print(self, include_chldren=True):
        print(json.dumps(self.to_dict(include_chldren),indent=2))
    
    def get_by_id(self, id, element=None):
        if element==None:
          element = self.root
        
        if element.get_id() == id:
            return element
        
        for child in element.children:
            foundElement = self.get_by_id(id, element=child)
            if foundElement is not None:
                return foundElement
            
    def get_by_tag(self, tag, element=None):
        foundElements = []
        
        if element==None:
          element = self.root
        

        if element.tag == tag:
            foundElements.append(element)

        for child in element.children:
            moreFoundElement = self.get_by_tag(tag, element=child)
            for element in moreFoundElement:
                foundElements.append(element)

        return foundElements