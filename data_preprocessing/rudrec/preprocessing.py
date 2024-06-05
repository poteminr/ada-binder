import json
from typing import Union, Optional
from collections import defaultdict

import pandas as pd
from corus import load_rudrec, rudrec
import nltk
from nltk.tokenize import NLTKWordTokenizer


nltk.download('punkt')
ru_tokenizer = nltk.data.load("tokenizers/punkt/russian.pickle")
word_tokenizer = NLTKWordTokenizer()


def aggregate_rudrec_data(
    records: list[rudrec.RuDReCRecord],
) -> dict[str, Union[str, list[Union[int, str]]]]:
    data = defaultdict(list)
    
    for record in records:
        entity_types = []
        entity_start_chars = []
        entity_end_chars = []
        offset_mapping = []
        
        for (start, end) in ru_tokenizer.span_tokenize(record.text):
            context = record.text[start : end]
            word_spans = word_tokenizer.span_tokenize(context)
            offset_mapping.extend([(s + start, e + start) for s, e in word_spans])
        
        start_words, end_words = zip(*offset_mapping)

        for entity in record.entities:
            entity_types.append(entity.entity_type)
            entity_start_chars.append(entity.start)
            entity_end_chars.append(entity.end)


        start_words, end_words = zip(*offset_mapping)
        data['text'].append(record.text)
        data['id'].append(record.file_name)
        data['entity_types'].append(entity_types)
        data['entity_start_chars'].append(entity_start_chars)
        data['entity_end_chars'].append(entity_end_chars)
        data['word_start_chars'].append(list(start_words))
        data['word_end_chars'].append(list(end_words))
    return data

def get_binder_format(
    rudrec_path: str,
    path_to_save: Optional[str] = None
) -> pd.DataFrame:
    rudrec_records = list(load_rudrec(rudrec_path))
    preprocessed_dataframe = pd.DataFrame(aggregate_rudrec_data(rudrec_records))
    
    if path_to_save is not None:
        preprocessed_dataframe.to_json(rudrec_path, orient='records', lines=True, force_ascii=False)
    
    return preprocessed_dataframe