# Layza Nauane - 12211BSI251

import sys
import math
import spacy
from collections import defaultdict

nlp = spacy.load('pt_core_news_lg')

base_path = sys.argv[1]

inverted_index = defaultdict(lambda: defaultdict(int))
doc_names = []

def tokenize_and_lemmatize(doc_id, text):
    doc = nlp(text.lower())
    lemmas = [token.lemma_ for token in doc if not(token.is_stop) and not(token.is_punct) and token.is_alpha]
    for lemma in lemmas:
        inverted_index[lemma][doc_id] += 1
    return inverted_index

def write_term_occurrences_to_index(inverted_index):
    with open('indice.txt', 'w') as index_file:
        for term in sorted(inverted_index.keys()):
            occurrences = ", ".join([f"{doc_id}, {freq}" for doc_id, freq in inverted_index[term].items()])
            index_entry = f"({term}: {occurrences})\n"
            index_file.write(index_entry)
            
print("Índice invertido criado e salvo em 'indice.txt'")

def calculate_tfidf(N):
    tfidf = defaultdict(lambda: defaultdict(float))
    for term, doc_dict in inverted_index.items():
        doc_freq = len(doc_dict)
        if doc_freq == 0:
            continue
        idf = math.log10(N / doc_freq)
        for doc_id, freq in doc_dict.items():
            if freq > 0:
                tfidf[doc_id][term] = (1 + math.log10(freq)) * idf
    return tfidf

def write_tfidf(tfidf):
    with open('pesos.txt', 'w') as weights_file:
        for doc_id, doc_name in enumerate(doc_names, start=1):
            terms_weights = [(term, weight) for term, weight in tfidf[doc_id].items() if weight > 0]
            if terms_weights: 
                weights_entry = f"{doc_name}: " + " ".join([f"{term},{weight}" for term, weight in terms_weights]) + "\n"
                weights_file.write(weights_entry)

print("Pesos TF-IDF calculados e salvos em 'pesos.txt'")

with open(base_path, 'r') as file:
    file_paths = file.readlines()
    file_paths = [path.strip() for path in file_paths]
    
for doc_id, file_path in enumerate(file_paths, start=1):
    doc_names.append(file_path)
    with open(file_path, 'r') as txt_file:
        text = txt_file.read()
        inverted_index = tokenize_and_lemmatize(doc_id, text)

write_term_occurrences_to_index(inverted_index)

N = len(doc_names)

idf_values = calculate_tfidf(N)

write_tfidf(idf_values)
