# Fake-news-generation-from-FA-KES-dataset
This is the work I did while working as a student in IJS (Inštitut Jožeta Štefana). The intent is to use LLMs to generate false synthetic news articles, by using language understanding of LLMs.

There are some privacy issues related to publicizing my project's source code. Because of this, **two Python files that provide prompts and basic source code were removed** (the files `generating_new_article.py` and `fake_datector.py`) , and only the results are present. This might change in the future, but for now, everybody who wants the main source code needs to contact me.

The articles are generated from FA-KES, a fake news dataset about the Syrian war. 

The three basic steps in this code are:

1) Article generation from which we save the data into the folder `changed_articles`. Here there are the original and transformed articles and their facts tables for data, generated in different ways.
2) Detection (which uses the method called fact verification) that saves the results in `saved_results`.
3) Analysis of results from detection. This is done in `analysis.ipynb`.


In the folder `saved_prints` I saved some of the printed output, that gives the outputs of LLMs. I used these prints to understand how the code works. It is hard to understand if you do not have the source code
