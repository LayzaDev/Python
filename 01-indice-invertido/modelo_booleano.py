import sys
import spacy
from collections import defaultdict

nlp = spacy.load('pt_core_news_lg')

base_path = sys.argv[1]
query_path = sys.argv[2]

inverted_index = defaultdict(lambda: defaultdict(int))
doc_names = []

def tokenize_and_lemmatize(doc_id, text):
    doc = nlp(text.lower())
    lemmas = [token.lemma_ for token in doc if not(token.is_stop) and not(token.is_punct) and token.is_alpha]
    for lemma in lemmas:
        inverted_index[lemma][doc_id] += 1
    return inverted_index

def write_term_occurrences_to_index(inverted_index):
    for term in sorted(inverted_index.keys()):
        occurrences = ", ".join([f"{doc_id}, {freq}" for doc_id, freq in inverted_index[term].items()])
        index_entry = f"({term}: {occurrences})\n"
        index_file.write(index_entry)

with open(base_path, 'r') as file:
    file_paths = file.readlines()
    file_paths = [path.strip() for path in file_paths]
    
for doc_id, file_path in enumerate(file_paths, start=1):

    doc_names.append(file_path)
    
    with open(file_path, 'r') as txt_file:
        text = txt_file.read()
        inverted_index = tokenize_and_lemmatize(doc_id, text)

with open('indice.txt', 'w') as index_file:
    write_term_occurrences_to_index(inverted_index)

print("Índice invertido criado e salvo em 'indice.txt'")

def consult_files(query):
    terms = query.split()
    all_docs = set(range(len(doc_names)))
    results = set()
    current_operation = None

    for term in terms:
        if term in ('&', '|'):
            current_operation = term
        elif term[0] == '!':
            negated_docs = set(inverted_index.get(term[1:], {}).keys())
            results = (all_docs - negated_docs) if not results else results - negated_docs
        else:
            term_docs = set(inverted_index.get(term, {}).keys())
            results = term_docs if not results else (results & term_docs if current_operation == '&' else results | term_docs)
    
    return results

with open(query_path, 'r') as query_file:
    query = query_file.read().strip()
    result_docs = consult_files(query)

with open('resposta.txt', 'w') as response_file:
    response_file.write(f"{len(result_docs)}\n")
    
    for doc_id in sorted(result_docs):
        response_file.write(f"{doc_names[doc_id - 1]}\n")
        
print("Arquivo de resposta as consultas criado e salvo em 'resposta.txt'")