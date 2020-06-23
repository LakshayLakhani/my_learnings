from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import  cosine_similarity

text = ["London Paris London", "Paris Paris London"]

cv = CountVectorizer()
cv_fit=cv.fit_transform(text)

count_matrix = cv_fit.toarray()

similarity_scores = cosine_similarity(count_matrix)

# print(similarity_scores)

l = [100, 123, 4546, 21]
k = list(enumerate(l))
print(k)
