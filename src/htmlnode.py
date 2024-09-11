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
        if not self.props:
            return ""
        attributes = "".join(list(map(lambda x,y: f" {x}=\"{y}\"", self.props.keys(), self.props.values())))
        return attributes

    def __repr__(self):
        string = f"""HTMLNode
        Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}"""
        return string
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        if value:
            super().__init__(tag, value, None, props)
        else:
            raise ValueError("Node Value is required.")

    def to_html(self):
        if not self.value:
            raise ValueError("Node Value is required")
        if not self.tag:
            return self.value
        html_open = f"<{self.tag}{super().props_to_html()}>"
        html_value = f"{self.value}"
        html_close = f"</{self.tag}>"
        return html_open + html_value + html_close
