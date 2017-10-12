"""
@package palindrome
@author Christopher Gallo
palindrome
"""
from pprint import pprint as pp
import string

class palindrome():

    def pal_check(self, s):
        s = self.sanitize_2(s)
        z = list(s)
        z.reverse()
        if list(s) == z:
            return True
        
    def sanitize(self, s):
        s = s.lower()
        chars = list(string.ascii_lowercase)
        clean_s = ''
        for letter in s:
            if letter in chars:
                clean_s = clean_s + letter

        return clean_s

    def sanitize_2(self, s):
        s = s.lower()
        good = string.ascii_lowercase
        bad = string.punctuation + string.whitespace + "'’"
        xlate = s.maketrans(good, good,bad)
        clean = s.translate(xlate)
        return s.translate(xlate)


if __name__ == "__main__":
    my_string = [
    	'Aibohphobia',
    	'Madam, I’m Adam.'
    ]
    main = palindrome()
    for s in my_string:
        if main.pal_check(s):
            print("%s is a palindrome" % s)