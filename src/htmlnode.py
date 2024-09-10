class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
        else:
            return False

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        #attributes = ""
        #for prop in self.props:
        #    attributes += " " + prop + "=\"" + self.props[prop] + "\""
        #return attributes
        attributes = "".join(list(map(lambda x,y: f" {x}=\"{y}\"", self.props.keys(), self.props.values())))
        return attributes

    def __repr__(self):
        string = f"""HTMLNode
        Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}"""
        return string
    

