# coding=utf8

from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    
    PER,
    NamesExtractor,

    Doc
)

from utils import text_to_string

class Natasha_Parser:
    '''Initialization and Analysis Methods'''
    def __init__(self, filename): # here we give the text filename, not the text itself
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        self.emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(self.emb)
        self.syntax_parser = NewsSyntaxParser(self.emb)
        self.ner_tagger = NewsNERTagger(self.emb)
        self.names_extractor = NamesExtractor(self.morph_vocab)
        self.doc = Doc(text_to_string(filename)) # preconvertion to string, then instancing

    def segmentation(self):
        '''Split text into tokens and sentencies'''
        self.doc.segment(self.segmenter)

    def morphology(self):
        '''For every token extract rich morphology tags'''
        self.doc.tag_morph(self.morph_tagger)

    def lemmatization(self):
        '''Lemmatize every token'''
        for token in self.doc.tokens:
            token.lemmatize(self.morph_vocab)

    def syntax(self):
        '''For every sentence run syntax analyzer'''
        self.doc.parse_syntax(self.syntax_parser)

    def NER(self):
        '''Extract standart named entities: names, locations, organizations'''
        self.doc.tag_ner(self.ner_tagger)

    def NEN(self):
        '''For every NER span apply normalization procedure'''
        for span in self.doc.spans:
            span.normalize(self.morph_vocab)

    def NEP(self):
        '''Parse PER named entities into firstname, surname and patronymic'''
        for span in self.doc.spans:
            if span.type == PER:
                span.extract_fact(self.names_extractor)
