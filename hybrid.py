## input is user id, new weights for author, rating, and genre.
## normalize the weights so that they sum to 100
## check which one is larger -> include more of those books
## step 1 -> generate new recommendations based on author.
## step 2 -> generate new recommendations based on rating.
## step 3 -> generate new recommendations based on genre

# Python File to generate book recommendation based on genre of the User ID's
# Input is the user ID
# Returns a list of books - Book name, Book image, Book ID
# Command to run this file - "python genrebasedrecommendation.py <user_id>"

import numpy as np 
import pandas as pd 
import sys

#from genrebasedrecommendation import *
#from authorbasedrecommendation import *
#from ratingbasedrecommendations import *

def getBooksLikedByGenre1(user_id):
	#print('inside likes by genre')
	ratings=pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/ratings.csv')
	books=pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/books.csv')
	tags=pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/book_tags.csv')
	dtag = pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/tags.csv')
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
	tags_dict = dict(zip(dtag['tag_id'], dtag['tag_name']))
	# f = open('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/tags.csv')
	# tags_dict = {}
	# print(type(f))
	# for line in f:
	# 	# to skip the first row which has the column headers
		
	# 	if(count==0):
	# 		count = count+1
	# 	else:
	# 		data_line = line.rstrip().split(',')
	# 		#print(data_line)
			#tags_dict[int(data_line[0])]= (data_line[1])
	# matching the tag ids of the mostliked genres to tag/genre_name name
	for key,value in sorted(mostlikedgenres.items(), key=lambda kv: (kv[1], kv[0])):
		# get the tag name
		genreids.append(int(key))
		genrenames.append(tags_dict[int(key)])
	top5genres = genreids[:5]
	genre_based_recommendations = pd.DataFrame()
	#print(bookgenres.columns)
	genre_based_bookids = list(tags.loc[tags['tag_id'].isin(top5genres)]['goodreads_book_id'])
	top10recommendations = genre_based_bookids[:11]
	genre_based_recommendations = books.loc[books['goodreads_book_id'].isin(top10recommendations)]
	
	return genre_based_recommendations

def getBooksLikedByAuthor1(user_id):
	#print("inside likes by author")
	ratings=pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/ratings.csv')
	books=pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/books.csv')
	tags=pd.read_csv('/Users/aditya16.narula/Sites/BookReco/goodbooks-10k/book_tags.csv')
	# get the books liked by this user id
	userBooks = ratings.loc[ratings['user_id'] == user_id]
	# join tables based on book_ids to get book 
	userbookdetails = pd.merge(userBooks, books, left_on = 'book_id', right_on = 'goodreads_book_id')
	# get the most frequently occuring author
	mostlikedauthors = userbookdetails['authors'].value_counts().to_dict()
	# get a dictionary with key=tag_id, value = [list of books with this tag]
	authorbookrecommendations = pd.DataFrame()
	for key, value in mostlikedauthors.items():
		authorname = key
		otherbooksbythisauthor = books.loc[books['authors'] == authorname]
		authorbookrecommendations = pd.concat([otherbooksbythisauthor.head(5),authorbookrecommendations])
	return authorbookrecommendations

def hybrid(user_id, ratingweight, authorweight, genreweight, numberofrecos):
	recommendations = pd.DataFrame()
	# normalizing weights
	sumofweights = ratingweight + authorweight + genreweight
	ratingweight = float(ratingweight)/sumofweights
	authorweight = float(authorweight)/sumofweights
	genreweight = float(genreweight)/sumofweights
	#recommendations = pd.concat([recommendations,getBooksLikedByRating1(user_id).head(int(ratingweight*numberofrecos))]).copy()
	recommendations = pd.concat([recommendations,getBooksLikedByGenre1(user_id)]).tail(int(numberofrecos*genreweight)).copy()
	recommendations = pd.concat([recommendations,getBooksLikedByAuthor1(user_id)]).tail(int(numberofrecos*authorweight)).copy()
	#recommendations.append(getBooksLikedByGenre1(user_id))
	#print("HII")
	#print(recommendations)
	return recommendations.to_json(orient = 'records')

	#return recommendations.to_json()
	
if __name__ == "__main__":
	user_id = int(sys.argv[1])
	ratingweight =  int(sys.argv[2])
	authorweight = int(sys.argv[3])
	genreweight = int(sys.argv[4])
	numberofrecos = 10
	print(hybrid(user_id, ratingweight, authorweight, genreweight, numberofrecos))
