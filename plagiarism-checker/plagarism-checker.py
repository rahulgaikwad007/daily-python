#Using the OS module in loading paths
#using TfidfVectorizer to perform word embedding on textual data
#using cosin similarit to compute the plagarism
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#reading all the .txt files in the directory
person_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
person_notes =[open(File).read() for File in  person_files]


#using lambda here to vectorize & compute similarity
#here we are using two lambda functions one to conert text to arrays and other
#to compute the similarity between them
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

#vectorizing the loaded texual data
vectors = vectorize(person_notes)
s_vectors = list(zip(person_files, vectors))

#creating the function to compute the similarity
def check_plagiarism():
    plagiarism_results = set()
    global s_vectors
    for person_a, text_vector_a in s_vectors:
        new_vectors =s_vectors.copy()
        current_index = new_vectors.index((person_a, text_vector_a))
        del new_vectors[current_index]
        for person_b , text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            person_pair = sorted((person_a, person_b))
            score = (person_pair[0], person_pair[1],sim_score)
            plagiarism_results.add(score)
    return plagiarism_results

#printing the plagiarism results
for data in check_plagiarism():
    print(data)
