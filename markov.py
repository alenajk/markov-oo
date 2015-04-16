import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""
        
        source_string = ""

        for myfile in filenames:
            source_text = open(myfile)
            for line in source_text:
                source_line = line.rstrip()
                source_string += source_line + " "    

        print source_string
        return source_string

    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""

        markov_dict = {}
        source_list = corpus.split(" ")
        source_list.pop()

        for i in range(len(source_list)-1):
            if (source_list[i], source_list[i+1]) not in markov_dict:
                markov_dict[(source_list[i], source_list[i+1])] = [] 

            if i <= len(source_list)-3:
                    markov_dict[(source_list[i], source_list[i+1])].append(source_list[i+2])

        print markov_dict
        return markov_dict

    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        # your code here


if __name__ == "__main__":

    #Instantiating the class
    m=SimpleMarkovGenerator()
    source_string = m.read_files(sys.argv[1:])
    m.make_chains(source_string)

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x