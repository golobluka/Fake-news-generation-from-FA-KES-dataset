# Fake-news-generation-from-FAK-ES-dataset
This is the repository of the work I did while working as a student in IJS (Inštitut Jožeta Štefana). The intent is to use LLMs to generate false synthetic news articles, by using language understanding of LLMs.


The articles are generated from FA-KES, a fake news dataset about the Syrian war. Here synthetic data is made public, and so are the extended comments in the file `Report_final`.

There are some privacy issues related to publicizing my project's source code. Because of this, Python files that provide prompts and basic source code are *not available*, and only the results are present. This might change in the future, but for now, everybody who wants the main source code needs to contact me.

The articles are generated from FA-KES, a fake news dataset about the Syrian war.

The three basic steps in this code are:

    Article generation from which we save the data into the folder changed_articles. Here there are the original and transformed articles and their facts tables for data, generated in different ways.
    Detection (which uses the method called fact verification) that saves the results in saved_results.
    Analysis of results from detection. This is done in analysis.ipynb.


