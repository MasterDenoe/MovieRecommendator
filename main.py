"""
Started on 04/07/2024 by Dean Price
"""
import numpy as np


print("*********************")
print("Hello, Master Denoe!!")
print("*********************")
print("")

# mission critical data
viewerRating = 0
criticRating = 0
viewer_ratings = np.array([])   # n dimensional array using numpy library (more efficient and single data type)
critics_ratings = []    # list dynamic array (less efficient multiple data types allowed [stores pointers to objects in memory elsewhere])

new_ratings = np.array([4.5, 3.8, 5.0])
viewer_ratings = np.concatenate((viewer_ratings, new_ratings))
for rating in [4.2, 3.9, 4.8]:
    critics_ratings.append(rating)


avgViewerRating = 0
avgCriticRating = 0
yearMade = 2000
genre = { "action", "adventure", "comedy", "crime", "documentry", "drama", "family", "thriller" }
budget = 1000000
language = { "english", "norwegian" }
region = { "US", "United States" }

# misc data (not critical but may be a factor)
runtime = 120




# Example of basic syntax
def myFunc():
    count = 0
    for x in range(1000):
        if x == 0:
            print(x)
            print("")
        if (x % 100) == 0:
            count += 1
            print(count) # minimum print value = 1
 

myFunc()
    

print("")
print("*********************")
print("Program Finished!!!!!")
print("*********************")
