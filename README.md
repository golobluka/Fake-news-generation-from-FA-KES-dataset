# Fake-news-generation-from-FAK-ES-dataset
This repository contains the work I conducted as a student at IJS (Inštitut Jožeta Štefana). The goal was to utilize large language models (LLMs) to produce synthetic news articles that are falsely constructed, leveraging the language comprehension capabilities of LLMs.

The articles are created from FA-KES, a dataset focused on fake news related to the Syrian war. Both the synthetic data and additional comments can be found in the Report_final file.

Due to privacy concerns regarding the release of my project's source code, the Python files containing prompts and foundational code are currently not available; only the results are accessible. This situation may change in the future, but for the time being, those who require the main source code must reach out to me directly.

The code encompasses three primary steps:

- Article generation, where the data is saved into the changed_articles folder. This folder contains the original articles, their modified versions, and fact tables for the data generated in various ways.
- Detection, which employs a technique known as fact verification, with results being saved in saved_results.
- Result analysis from the detection process, which is performed in analysis.ipynb.



