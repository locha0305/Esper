class esper():
    def __init__(self, attributes):
        self.attributes = attributes
    def __repr__(self):
        return '<esper object {}>'.format(self.attributes)
    def __str__(self):
        return '<esper object {}>'.format(self.attributes)
    def __add__(self, other):
        result_attribute = {}
        if isinstance(other, esper):
            for attr in self.attributes:
                try:
                    result_attribute[attr] = self.attributes[attr] + other.attributes[attr]
                except:
                    result_attribute[attr] = self.attributes[attr]
            return esper(result_attribute)
        else:
            return 0
    def __sub__(self, other):
        result_attribute = {}
        if isinstance(other, esper):
            for attr in self.attributes:
                try:
                    result_attribute[attr] = self.attributes[attr] - other.attributes[attr]
                except:
                    result_attribute[attr] = self.attributes[attr]
            return esper(result_attribute)
        else:
            return 0
    def __mul__(self, other):
        result_attribute = {}
        if isinstance(other, esper):
            for attr in self.attributes:
                try:
                    result_attribute[attr] = self.attributes[attr] * other.attributes[attr]
                except:
                    result_attribute[attr] = self.attributes[attr]
            return esper(result_attribute)
        else:
            return 0




a = esper({
    "value":1
})
