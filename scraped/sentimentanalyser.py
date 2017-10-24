"""Analyse tweets"""
import webhandler
import math
from collections import defaultdict
import pickle

challenges = defaultdict(list)

class SentimentAnalyser(object):
    def __init__(self):
        self.negative_words = webhandler.get_negative_words() 
        self.neutral_words = webhandler.get_neutral_words()
        self.positive_words = webhandler.get_positive_words() # These are lists
        self.companies = webhandler.get_company_info()
        self.dict = {}
        self.challenges = defaultdict(list)

        with open("neg.pkl", "wb") as f:
            pickle.dump(self.negative_words, f)

        with open("neutral.pkl", "wb") as f:
            pickle.dump(self.neutral_words, f)

        with open("pos.pkl", "wb") as f:
            pickle.dump(self.positive_words, f)

        with open("companies.pkl", "wb") as f:
            pickle.dump(self.companies, f)

        exit()

    def save(self):
        challenges['neg words'].append(self.negative_words)
        challenges['pos words'].append(self.positive_words)
        challenges['companies'].append(self.companies_words)
        challenges['neutral words'].append(self.neutral_words)

        return challenges







    def given_algorithm(self, sentiment,tweet):
        words = {}

        for word in tweet.split(" "):
            if word in self.positive_words:
                sentiment = sentiment + 1
            if word in self.negative_words:
                sentiment = sentiment - 1
            
            return sentiment


    def populate_dict_with_words(self):
        """document count, generate words into dict """

        # fill words into dict
        # and unknown column

        for word in self.positive_words:
            self.dict[word] = 0

        for word in self.negative_words:
            self.dict[word] = 0

# term frequency [x]
# proportions []

    # def term_frequency(self, tweet):
    #     for word in tweet.split(" "):
    #         if word in self.positive_words:
    #             self.dict[word] += 1
    #         if word in self.negative_words:
    #             self.dict[word] += 1


    def term_frequency(term, tokenized_document):
        return tokenized_document.count(term)

    def sublinear_term_frequency(self, term, tokenized_document):
        return 1 + math.log(tokenized_document.count(term))

    def augmented_term_frequency(self, term, tokenized_document):
        max_count = max([term_frequency(t, tokenized_document) for t in tokenized_document])
        return (0.5 + ((0.5 * term_frequency(term, tokenized_document))/max_count))

    def inverse_document_frequencies(self, tokenized_documents):
        idf_values = {}
        all_tokens_set = set(tokenized_documents)
        print(all_tokens_set)
        for tkn in all_tokens_set:
            contains_token = map(lambda doc: tkn in doc, tokenized_documents)
            idf_values[tkn] = 1 + math.log(len(tokenized_documents)/(sum(contains_token)))
        return idf_values

    def analyse_tweet(self, tweet):
        """Analyse a tweet, extracting the subject and sentiment"""
        sentiment_score = 0

        self.given_algorithm(sentiment_score, tweet)
        dict = self.populate_dict_with_words()

        tokenized_doc = tweet.split(" ")
        print(tokenized_doc)

        #IDF
        print(self.inverse_document_frequencies(tokenized_doc))

        return [(self.companies[0].name, sentiment_score)] 

   

# frequency count


    # def sublinear_term_frequency(term, tokenized_document):
    # return 1 + math.log(tokenized_document.count(term))

