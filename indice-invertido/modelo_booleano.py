import sys
import spacy
from collections import defaultdict

nlp = spacy.load('pt_core_news_lg')

base_path = sys.argv[1]
query_path = sys.argv[2]

inverted_index = defaultdict(lambda: defaultdict(int))

with open(base_path, 'r') as file:
    file_paths = file.readlines()
    file_paths = [path.strip() for path in file_paths]

    for doc_id, file_path in enumerate(file_paths):
        with open(file_path, 'r') as txt_file:
            text = txt_file.read()
            doc = nlp(text.lower())
        
            lemmas = [token.lemma_ for token in doc if not(token.is_stop) and not(token.is_punct) and token.is_alpha]
            
            for lemma in lemmas: 
                inverted_index[lemma][doc_id] += 1

with open('indice.txt', 'w') as index_file:
    for lemma in sorted(inverted_index.keys()):
        occurrences = ", ".join([f"{doc_id}, {freq}" for doc_id, freq in inverted_index[lemma].items()])
        index_entry = f"({lemma}: {occurrences})\n"
        index_file.write(index_entry)

print("Índice invertido criado e salvo em 'indice.txt'")