import sys, random


class SimpleMarkovGenerator(object):
    character_limit = False

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""
        
        source_string = ""

        for myfile in filenames:
            source_text = open(myfile)
            for line in source_text:
                source_line = line.rstrip()
                source_string += source_line + " "    

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

        markov_dict[(source_list[-2], source_list[-1])] = []

        self.chain = markov_dict
        return markov_dict


    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        #Start with a random bi-gram
        bi_gram = random.choice(self.chain.keys())

        #Start output_string with our first bi-gram
        starter_string = ""
        output_string = starter_string + " ".join(bi_gram)

        #Continue generating random text, concatonating to output_string, and creating new bi-grams as we go

        while True:
            if self.chain[bi_gram] != []:
            #if bi_gram in chains and chains[bi_gram] != []:
                new_word = random.choice(self.chain[bi_gram])
                output_string += " " + new_word
                bi_gram = (bi_gram[1], new_word)
            else:
                break

        if self.character_limit == True:
            output_string = output_string[:139]
        
        return output_string

class TweetableMarkovGenerator(SimpleMarkovGenerator):

    character_limit = True

    def make_text(self):
        text_from_super = super(TweetableMarkovGenerator,self).make_text()
        return text_from_super[:139]

if __name__ == "__main__":

    #Instantiating the class
    m=TweetableMarkovGenerator()
    
    source_string = m.read_files(sys.argv[1:])
    m.make_chains(source_string)
    print m.make_text()

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x