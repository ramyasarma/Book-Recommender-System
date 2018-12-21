# Python File to generate book recommendation based on genre of the User ID's
# Input is the user ID
# Returns a list of books - Book name, Book image, Book ID
# Command to run this file - "python genrebasedrecommendation.py <user_id>"

import numpy as np 
import pandas as pd 
import sys

def getBooksLikedByGenre(user_id):
	ratings=pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/ratings.csv')
	books=pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/books.csv')
	tags=pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/book_tags.csv')
	# get the books liked by this user id
	userBooks = ratings.loc[ratings['user_id'] == user_id]
	# join tables based on book_ids to get the book genres
	userbookdetails = pd.merge(userBooks, books, left_on = 'book_id', right_on = 'goodreads_book_id')
	bookgenres =  pd.merge(userbookdetails, tags, left_on = 'goodreads_book_id', right_on = 'goodreads_book_id')
	# get the most frequently occuring tag
	mostlikedgenres = bookgenres['tag_id'].value_counts().to_dict()
	# get a dictionary with key=tag_id, value = [list of books with this tag] 
	book_tags = dict(zip(bookgenres['goodreads_book_id'], bookgenres['tag_id']))
	genrenames = []
	genreids = []
	count = 0
	#f = open('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/tags.csv')
	tags_dict = dict(zip(tags.tag_id, tags.tag_name))
	#mydict = dict(zip(df.id, df.value))

	#for line in f:
		# to skip the first row which has the column headers
	#	if(count==0):
	#		count = count+1
	#	else:
	#		data_line = line.rstrip().split(',')
	#		tags_dict[int(data_line[0])]= data_line[1]
	# matching the tag ids of the mostliked genres to tag/genre_name name
	#print("HI")
	#print(mostlikedgenres)
	for key,value in sorted(mostlikedgenres.items(), key=lambda kv: (kv[1], kv[0])):
		# get the tag name
		#print(type(key))
		genreids.append(int(key))
		genrenames.append(tags_dict[int(key)])
	top5genres = genreids[:5]
	genre_based_recommendations = pd.DataFrame()
	#print(bookgenres.columns)
	genre_based_bookids = list(tags.loc[tags['tag_id'].isin(top5genres)]['goodreads_book_id'])
	top10recommendations = genre_based_bookids[:11]
	recommendations = books.loc[books['goodreads_book_id'].isin(top10recommendations)]
	return recommendations

if __name__ == "__main__":
	user_id = int(sys.argv[1])
	print(getBooksLikedByGenre(user_id))
