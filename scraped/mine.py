import pickle

tweets_data = []
file_to_load = {'companies.pkl', 'neg.pkl', 'neutral.pkl', 'pos.pkl'}
info = {}


def main():

	print("-----------------start--------------")
	print()

	for i in range(15):
		load = "challenge{}.pkl".format(i)
		with open(load, "rb") as f:
			tweets_data.append(pickle.load(f))


	if len(tweets_data) != 15:
		print("we don't have all the challenges")
		return 1

	# for challenge in tweets_data:
	# 	for idx, tweet in enumerate(challenge.tweets): #4687 tweets altogether
	# 		print(tweet.tweet)


	for filename in file_to_load:
		with open(filename, 'rb') as f:
			info[filename] = pickle.load(f)

	# for item in info: #the data in pos and neg are really small
 # 		print(item)	
 # 		print()

	# for key, val in info.items():
	# 	print (key, val)	
	# 	print()

	companies = info['companies.pkl'] #list of companies

	# list of words
	neg_words = info['neg.pkl'] 
	neutral_words = info['neutral.pkl']
	pos_words = info['pos.pkl']

	

	for compname in companies:
		print(compname.name)

	




if __name__ == "__main__":
	main()


