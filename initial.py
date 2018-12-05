# Python File to fetch the User ID's initial likes
# Input is the user ID
# Returns a list of books - Book name, Book image, Book ID
# Command to run this file - "python initial.py <user_id>""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sys

def getBooksLikedByUserID(user_id):
	ratings=pd.read_csv('/var/www/html/bookreco/Data/goodbooks-10k/ratings.csv')
	books=pd.read_csv('/var/www/html/bookreco/Data/goodbooks-10k/books.csv')
	userBooks = ratings.loc[ratings['user_id'] == user_id]
	userbookdetails = pd.merge(userBooks, books, left_on = 'book_id', right_on = 'goodreads_book_id')
	return userbookdetails.to_json()

if __name__ == "__main__":
	user_id = int(sys.argv[1])
	print(getBooksLikedByUserID(user_id))
