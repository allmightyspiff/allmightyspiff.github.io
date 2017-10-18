from pprint import pprint as pp

class word_permutation():
    def permutate(self,word):
        print("PERMUTATE: %s" % word)
        if len(word) <= 1:
            return word
        #get all permutations of leCS/Day3/directory_skeleton.pyngth N-1
        perms=self.permutate(word[1:])
        char=word[0]
        result=[]
        #iterate over all permutations of length N-1
        for perm in perms:
            #insert the character into every possible location
            for i in range(len(perm)+1):
                result.append(perm[:i] + char + perm[i:])
        return result

if __name__ == "__main__":
    my_array = "Hello"
    main = word_permutation()
    permutations  = main.permutate(my_array)
    print(permutations)
