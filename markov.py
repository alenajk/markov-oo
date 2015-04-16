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

        return markov_dict

    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        #Start with a random bi-gram
        bi_gram = random.choice(chains.keys())
        
        #Start output_string with our first bi-gram
        output_string = ""
        output_string = starter_string + " ".join(bi_gram)

        #Continue generating random text, concatonating to output_string, and creating new bi-grams as we go
        while True:
            if chains[bi_gram] != []:
            #if bi_gram in chains and chains[bi_gram] != []:
                new_word = random.choice(chains[bi_gram])
                output_string += " " + new_word
                bi_gram = (bi_gram[1], new_word)
            else:
                break

        return output_string


if __name__ == "__main__":

    #Instantiating the class
    m=SimpleMarkovGenerator()
    source_string = m.read_files(sys.argv[1:])
    m.make_chains(source_string).make_text()

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x