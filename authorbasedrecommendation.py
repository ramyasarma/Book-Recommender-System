# Python File to generate book recommendation based on authors previously liked by the User ID's
# Input is the user ID
# Returns a list of books - Book name, Book image, Book ID
# Command to run this file - "python authorbasedrecommendation.py <user_id>"

import numpy as np 
import pandas as pd 
import sys

def getBooksLikedByAuthor(user_id):
	ratings=pd.read_csv('/var/www/html/bookreco/Data/goodbooks-10k/ratings.csv')
	books=pd.read_csv('/var/www/html/bookreco/Data/goodbooks-10k/books.csv')
	tags=pd.read_csv('/var/www/html/bookreco/Data/goodbooks-10k/book_tags.csv')
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
if __name__ == "__main__":
	user_id = int(sys.argv[1])
	print(getBooksLikedByAuthor(user_id))
