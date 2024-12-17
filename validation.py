import bleach
## XSS, Cross site script validation

def sanitize_input(string):
    return bleach.clean(string)

def check_empty(value):
    return True if value is None or value =="" else False

