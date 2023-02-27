# -*- coding: utf-8 -*-
"""NLP_Exercise2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xRYQjwOVBiy9ItDNv4k-Ed5aTfyucePw
"""

#Packs and modules to run this code
!python -m spacy download es_core_news_sm
import spacy
from spacy import displacy
import seaborn as sns
import sklearn.metrics 
from sklearn.metrics import confusion_matrix
nlp = spacy.load('es_core_news_sm')
nlp = spacy.load('en_core_web_sm')

#SAMPLE ENGLISH #https://github.com/UniversalDependencies/UD_English-LinES/blob/master/en_lines-ud-dev.conllu
en1 = nlp('The administrator of the SQL Server can also add additional security by changing the default SA account password.')
en2 = nlp('This makes it difficult to allow other users to gain access to the Access project.')
#SAMPLE SPANISH #https://github.com/UniversalDependencies/UD_Spanish-AnCora/blob/master/es_ancora-ud-dev.conllu
es1 = nlp('Desde entonces entró en silencio absoluto.')
es2 = nlp('Nadie sabe cuál es la nueva fecha que propone para las votaciones, ni si las quiere juntas o separadas, ni cuando va a reanudar la campaña.')

#Dependency parsing
for d in (en1, en2, es1, es2):
  for t in d:
    print(t.i, t.text, t.pos_, t.dep_, t.head.i)
  print('')
for d in(en1,en2, es1, es2):
  options = {'compact': True, 'distance':150, 'bg':'#f5ede9', 'color':'440FD1'}
  displacy.render(d, style='dep', jupyter=True, options=options)
#estimated tags as returned by the parser
dep_pred_en1 = ['DET','NOUN','ADP','DET','PROPN','PROPN','AUX','ADV','VERB','ADJ','NOUN','ADP','VERB','DET','NOUN','PROPN','NOUN','NOUN','PUNCT']
dep_pred_en2 = ['PRON','VERB','PRON','ADJ','PART','VERB','ADJ','NOUN','PART','VERB','NOUN','ADP','DET','PROPN','NOUN','PUNCT']
dep_pred_es1 = ['ADP','ADV','VERB','ADP','NOUN','ADJ','PUNCT']
dep_pred_es2 = ['PRON','VERB','PRON','AUX','DET','ADJ','NOUN','PRON','VERB','ADP','DET','NOUN','PUNCT','CCONJ','SCONJ','PRON','VERB','ADJ','CCONJ','ADJ','PUNCT','CCONJ','SCONJ','AUX','ADP','VERB','DET','NOUN','PUNCT']
#assigning ground truth (correct) target values 
dep_true_en1 = ['DET','NOUN','ADP','DET','PROPN','NOUN','AUX','ADV','VERB','ADJ','NOUN','ADP','VERB','DET','NOUN','X','NOUN','NOUN','PUNCT']
dep_true_en2 = ['PRON','VERB','PRON','ADJ','PART','VERB','ADJ','NOUN','PART','VERB','NOUN','ADP','DET','PROPN','NOUN','PUNCT']
dep_true_es1 = ['ADP','ADV','VERB','ADP','NOUN','ADJ','PUNCT']
dep_true_es2 = ['PRON','VERB','PRON','AUX','DET','ADJ','NOUN','PRON','VERB','ADP','DET','NOUN','PUNCT','CCONJ','SCONJ','PRON','VERB','ADJ','CCONJ','ADJ','PUNCT','CCONJ','PRON','VERB','ADP','VERB','DET','NOUN','PUNCT']

"""#Matrix evaluation"""

#EN1
confusion_matrix(dep_pred_en1, dep_true_en1)
cf_matrix_en1 = confusion_matrix(dep_pred_en1, dep_true_en1)
sns.heatmap(cf_matrix_en1, annot=True)

#EN2
confusion_matrix(dep_pred_en2, dep_true_en2)
cf_matrix_en2 = confusion_matrix(dep_pred_en2, dep_true_en2)
sns.heatmap(cf_matrix_en2, annot=True)

#ES1
confusion_matrix(dep_pred_es1, dep_true_es1)
cf_matrix_es1 = confusion_matrix(dep_pred_es1, dep_true_es1)
sns.heatmap(cf_matrix_es1, annot=True)

#ES2
confusion_matrix(dep_pred_es2, dep_true_es2)
cf_matrix_es2 = confusion_matrix(dep_pred_es2, dep_true_es2)
sns.heatmap(cf_matrix_es2, annot=True)