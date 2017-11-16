import re


if __name__ == "__main__":
    input_string = """# Regex in python
https://wiki.python.org/moin/RegularExpression
https://docs.python.org/3/library/re.html
---"""

    regex = r'# ([\w ]+)'
    matches = re.match(regex,input_string)
    print(matches.groups())
