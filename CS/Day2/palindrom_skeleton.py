"""
@package palindrome
@author Christopher Gallo
palindrome
"""
from pprint import pprint as pp
import string

class palindrome():

    def pal_check(self, s):
        s = self.sanitize(s)
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

if __name__ == "__main__":
    my_string = [
    	'Aibohphobia',
    	"Madam, I'm Adam.",
        "testing",
        "Goodbye World"
    ]
    main = palindrome()
    for s in my_string:
        if main.pal_check(s):
            print("%s is a palindrome" % s)
        else:
            print("%s NOT a palindrome" % s)