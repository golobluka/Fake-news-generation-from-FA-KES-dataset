# Fake-news-generation-from-FA-KES-dataset
This is the work done while working as a student in IJS (Inštitut Jožeta Štefana). The intent is to use LLMs to generate false synthetic news articles, by using language understanding of LLMs.



The articles in `Task1` are generated from FA-KES, a fake news dataset about the Syrian war. Then this procedure was extended to arbitrary news articles in `Task2` folder. With the functions in `fact_extraction_and_manipulation` you can make synthetic articles with changed facts. Look at [my paper](https://aile3.ijs.si/dunja/SiKDD2024/Papers/IS2024_-_SIKDD_2024_paper_13.pdf) for more information.

The three basic steps in the `Task1` are:

1) Article generation from which we save the data into the folder `changed_articles`. Here are the original and transformed articles and their facts tables for data, generated in different ways.
2) Detection (which uses the method called fact verification) that saves the results in `saved_results`.
3) Analysis of results from detection. This is done in `analysis.ipynb`.

In `Task2`, we added the process of generating topics of fact from the article. In this way, we can produce synthetic news on arbitrary articles. This is done in the folder `General_generate_topics_of_fact`, which was added to the previous functions. Functions in `Task2` also contain other advancements. For example, you can take the number of changed facts as an argument in the function and, therefore, change its value.   


In the folder `saved_prints` I saved some of the printed output, that gives the outputs of LLMs. I used these prints to understand how the code works. It is hard to understand if you do not have the source code
