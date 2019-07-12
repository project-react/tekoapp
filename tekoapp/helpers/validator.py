import re 

class Username:
    value = ''
    def __init__(self, value):
        self.value = value

    def test_length(self):
        return len(self.value) >= 6

    def test_has_space(self):
        result = re.search(r'[^\S+$]+', self.value)
        if result:
            return False
        else:
            return True

    def test_charater(self):
        result = re.search(r'[a-zA-Z0-9]+$', self.value)
        if result:
            return True
        else:
            return False

    def is_valid(self):
        return self.test_length() and self.test_has_space() and self.test_charater()

class Email:
    value = ''
    def __init__(self, value):
        self.value = value
    
    def test_format(self):
        result = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', self.value, re.I)
        if result:
            return True
        else:
            return False

    def is_valid(self):
        return self.test_format()

class Password:
    value = ''
    def __init__(self, value):
        self.value = value

    def test_length(self):
        return len(self.value) >= 8

    def test_format(self):
        result = re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])', self.value)
        if result:
            return True
        else:
            return False

    def is_valid(self):
        return self.test_length() and self.test_format()