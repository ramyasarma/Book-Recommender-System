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

from genrebasedrecommendation import *
from authorbasedrecommendation import *
#from ratingbasedrecommendations import *

def hybrid(user_id, ratingweight, authorweight, genreweight, numberofrecos):
	recommendations = pd.DataFrame()
	# normalizing weights
	sumofweights = ratingweight + authorweight + genreweight
	ratingweight = float(ratingweight)/sumofweights
	authorweight = float(authorweight)/sumofweights
	genreweight = float(genreweight)/sumofweights
	recommendations = pd.concat([recommendations,ratingbasedrecommendations.getBooksLikedByRating(user_id).head(int(ratingweight*numberofrecos))])
	recommendations = pd.concat([recommendations,getBooksLikedByGenre(user_id).head(int(genreweight*numberofrecos))])
	recommendations = pd.concat([recommendations,getBooksLikedByAuthor(user_id).head(int(authorweight*numberofrecos))])
	return recommendations
	
if __name__ == "__main__":
	user_id = int(sys.argv[1])
	ratingweight =  int(sys.argv[2])
	authorweight = int(sys.argv[3])
	genreweight = int(sys.argv[4])
	numberofrecos = 10
	print(hybrid(user_id, ratingweight, authorweight, genreweight, numberofrecos))
