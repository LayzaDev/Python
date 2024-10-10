import sys
import spacy
from collections import defaultdict

nlp = spacy.load('pt_core_news_lg')

base_path = sys.argv[1]
query_path = sys.argv[2]

with open(base_path, 'r') as file:
    file_paths = file.readlines()

    file_paths = [path.strip() for path in file_paths]

    for file_path in file_paths:
        with open(file_path, 'r') as txt_file:
            text = txt_file.read()
            doc = nlp(text.lower())
            tokens = list(doc)
            lemmas = [(tokens.text, tokens.lemma_) for tokens in doc if not(tokens.is_stop) and not(tokens.is_punct) and tokens.is_alpha]
            for lemma in lemmas: 
                l = lemma
                print(l)
        
