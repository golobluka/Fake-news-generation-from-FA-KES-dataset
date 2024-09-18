#Prompts for fake detector
#_____________________________________________________________________

TOPICS = [{'Name of fact': 'Name of casualty or group', 'Description of fact': ' represents the casualties names or the names of the groups associated with the casualties.', 'Common examples': 'men, solders, children'},
{'Name of fact': 'Gender or age group', 'Description of fact': ' of casualty indicates if the casualties are male or female, or specify their age group .', 'Common examples': 'Male, Female, Child, Adult, Senior'},
{'Name of fact': 'Cause of death', 'Description of fact': ' specifies the weapons used by the aggressor (e.g., shooting, shelling, chemical weapons, etc.)', 'Common examples': 'Shooting, Shelling, Chemical weapons'},
{'Name of fact': 'Type', 'Description of fact': ' of casualty classifies the casualties as a civilian or non-civilian (e.g., military personnel are non-civilians).', 'Common examples': 'Civilian, Non-civilian'},
{'Name of fact': 'Actor', 'Description of fact': ' identifies the actors responsible for the incident, such as rebel groups, Russian forces, ISIS, the Syrian army, U.S. military, etc.', 'Common examples': 'Rebel groups, Russian forces, ISIS'},
{'Name of fact': 'Place of death', 'Description of fact': ' specifies the locations where the attacks occurred (e.g., Aleppo, Damascus, Homs, Idlib, Raqqa, Daraa, Deir ez-Zor, Qamishli, Palmyra, etc.).', 'Common examples': 'Aleppo, Damascus, Homs'},
{'Name of fact': 'Date of death', 'Description of fact': ' provides the dates when the attacks occurred.', 'Common examples': '2021-01-01, 2022-06-15'}
]

LIST_OF_CHANGES = [
    ["Name of casualty or group", "Name of casualty or group is the name of the casualties or the name of the group associated with the casualties. It may also include the number of casualities.", """Name of casualty or group is the name of the casualties or the name of the group associated with the casualties. It may also include the number of casualities. Is the "Name of casualty or group" in the article approximately coherent with this description: {}? If the description comes from the article, output "The answer is true" and otherwise output "The answer is false". In addition to "The answer is true" or "The answer is false" label provide short explanation."""],
    ["Gender or age group", "Gender or age group indicates if the casualty is male or female, or specifies their age group.", """Gender or age group indicates if the casualty is male or female, or specifies their age group. Is the "Gender or age group" of the casualty in the article approximately coherent with this description: {}? If the description comes from the article, output "The answer is true" and otherwise output "The answer is false". In addition to "The answer is true" or "The answer is false" label provide short explanation."""],
    ["Cause of death", "Cause of death is the weapon used in the attack (e.g., shooting, shelling, chemical weapons, etc.).", """Cause of death is the weapon used in the attack (e.g., shooting, shelling, chemical weapons, etc.). Is the "Cause of death" in the article approximately coherent with this description: {}? If the description comes from the article, output "The answer is true" and otherwise output "The answer is false". In addition to "The answer is true" or "The answer is false" label provide short explanation."""],
    ["Type", "Type is the information if the casualty is civilian or non-civilian.", """Type is the information if the casualty is civilian or non-civilian. Is the "Type" (civilian or non-civilian) in the article approximately coherent with this description: {}? If the description comes from the article, output "The answer is true" and otherwise output "The answer is false". In addition to "The answer is true" or "The answer is false" label provide short explanation."""],
    ["Actor", "The actor is the person or group responsible for the attack.", """The actor is the person or group responsible for the attack. Is the "Actor" (group responsible for the attack) in the article approximately coherent with this description: {}? If the description comes from the article, output "The answer is true" and otherwise output "The answer is false". In addition to "The answer is true" or "The answer is false" label provide short explanation."""],
    ["Place of death", "Place of death refers to the cities or areas where the attacks happened.", """Place of death refers to the cities or areas where the attacks happened. Is the "Place of death" in the article approximately coherent with this description: {}? If the description comes from the article, output "The answer is true" and otherwise output "The answer is false". In addition to "The answer is true" or "The answer is false" label provide short explanation."""],
    ["Date of death", "The date of death refers to theme where the attack happened in the article.", """The date of death refers to when the attack happened in the article. Is the "Date of death" in the article approximately coherent with this description: {}? If the description comes from the article, output "The answer is true" and otherwise output "The answer is false". In addition to "The answer is true" or "The answer is false" label provide short explanation."""]
]

SHAPE_OF_QUESTION =  """{description_of_fact} ({common_examples}). 

Is the \"{name_of_fact}\" in the article approximately coherent with this description: {{{{}}}} ? If the description comes from the article, output "The answer is true" and otherwise output "The answer is false". In addition to "The answer is true" or "The answer is false" label provide short explanation."""

prompt = """You will be given an event in Syrian war dated from 2013 to 2017. Please read and understand the event that is stored in JSON format:

{events}

You must check that the event presented in the article is from among previously red events. Try to check that all the information matches. That means that "Name of casualty or group" "Gender or age group", "Cause of death", "Type", "Actor", "Place of death" and "Date of death" must match.

{article}

If the article matches some event print 'true', else print 'false'. In addition to 'true' or 'false' provide explanation.
"""

prompt_one_by_one = """Carefully read through the article and try to understand its {topic}. {meaning_of_topic}

{article}

{question}
"""

#Imports
import random
import ollama
import json
import re
import os
import pandas as pd

#Suplementary functions

def find_json(text):
        """Function to find JSON-like content in the text."""
        content = []
        pattern0 = (
            r'.*Name of casualty or group.*:\s*(.*),.*\n'
            r'.*Gender or age group.*:\s*(.*),.*\n'
            r'.*Cause of death.*:\s*(.*),.*\n'
            r'.*Type.*:\s*(.*),.*\n'
            r'.*Actor.*:\s*(.*),.*\n'
            r'.*Place of death.*:\s*(.*),.*\n'
            r'.*Date of death.*:\s*(.*)\s*\n'
        )
        pattern1 = (
            r'\{.*Name of casualty or group.*:\s*(.*),.*'
            r'.*Gender or age group.*:\s*(.*),.*'
            r'.*Cause of death.*:\s*(.*),.*'
            r'.*Type.*:\s*(.*),.*'
            r'.*Actor.*:\s*(.*),.*'
            r'.*Place of death.*:\s*(.*),.*'
            r'.*Date of death.*:\s*(.*)\}.*'
        )
        
        
        pattern2 = r'(?:"Name of casualty or group": \[([^\]]*?)\],?\n\s*"Gender or age group": \[([^\]]*?)\],?\n\s*"Cause of death": \[([^\]]*?)\],?\n\s*"Type": \[([^\]]*?)\],?\n\s*"Actor": \[([^\]]*?)\],?\n\s*"Place of death": \[([^\]]*?)\],?\n\s*"Date of death": \[([^\]]*?)\])'

        matches = re.finditer(pattern2, text)

        for match in matches:
            content_dict = {
                "Name of casualty or group": match.group(1).replace('\"', ''),
                "Gender or age group": match.group(2).replace('\"', ''),
                "Cause of death": match.group(3).replace('\"', ''),
                "Type": match.group(4).replace('\"', ''),
                "Actor": match.group(5).replace('\"', ''),
                "Place of death": match.group(6).replace('\"', ''),
                "Date of death": match.group(7).replace('\"', ''),
            }
            content.append(content_dict)

        
        matches = re.finditer(pattern0, text)

        for match in matches:
            content_dict = {
                "Name of casualty or group": match.group(1).replace('\"', ''),
                "Gender or age group": match.group(2).replace('\"', ''),
                "Cause of death": match.group(3).replace('\"', ''),
                "Type": match.group(4).replace('\"', ''),
                "Actor": match.group(5).replace('\"', ''),
                "Place of death": match.group(6).replace('\"', ''),
                "Date of death": match.group(7).replace('\"', ''),
            }
            content.append(content_dict)

        matches = re.finditer(pattern1, text)

        for match in matches:
            content_dict = {
                "Name of casualty or group": match.group(1).replace('\"', ''),
                "Gender or age group": match.group(2).replace('\"', ''),
                "Cause of death": match.group(3).replace('\"', ''),
                "Type": match.group(4).replace('\"', ''),
                "Actor": match.group(5).replace('\"', ''),
                "Place of death": match.group(6).replace('\"', ''),
                "Date of death": match.group(7).replace('\"', ''),
            }
            content.append(content_dict)

        return content

def find_first_true_or_false(text):
    """Finds the first occurrence of the words 'true' or 'false' in the text and returns it with its position."""
    # Regular expression pattern to match 'true' or 'false'
    pattern = r'\b(The answer is true|The answer is false|The answer is True|The answer is False|The answer is TRUE|The answer is FALSE|the answer is true|the answer is false|the answer is True|the answer is False|the answer is TRUE|the answer is FALSE)\b'

    # Search for the first occurrence
    match = re.search(pattern, text, re.IGNORECASE)  # Using IGNORECASE to match 'True', 'False' etc.

    if match:
        word = match.group(1)  # Get the matched word ('true' or 'false')
        return word.lower()
    else:
        return None # Return None if not found, and -1 for position
    
def generate_one_by_one_prompts(topics):
    questions = []
    for topic in topics:
        question_for_fact = SHAPE_OF_QUESTION.format(name_of_fact = topic["Name of fact"], description_of_fact = topic["Description of fact"], common_examples=topic["Common examples"])
        dictionary = {"Name of fact": topic["Name of fact"], "Description of fact": topic["Description of fact"], "Question for fact": question_for_fact}
        questions.append(dictionary)
    return questions


def model_response(model_name, prompt, prompt_variables):
    formatted_content = prompt.format(**prompt_variables)
    response = ollama.chat(model=model_name, messages=[
        {
            'role': 'user',
            'content': formatted_content,
            'temperature': 0.2,
        }
    ])
    return response['message']['content']

#______________________________________________________________________________________-
#main function

def fake_detect_comparison_true_to_true_and_false_to_true(list_of_changed_articles, model_name = "llama3.1:8b", print_comments = False): 
    """
    Inputs
    list_of_changed_articles: A list containing pairs of true and false articles along with their facts and changes.
    [
    ["Index", "True Article Content", "Facts table", "Fake article content", "Changed topics", Facts", "Changed Topic 1", "Changed Topic 2"]
    ]
    model_name: The name of the model to be used for comparison (default is "llama3.1:8b").
    print_comments: A boolean flag to print intermediate comments (default is False).
    Flow
    Initialize an empty list data to store results.
    Iterate over each article pair in list_of_changed_articles.
    For each true article, generate responses for each topic using the model and count the number of true and false responses.
    Repeat the process for the corresponding false article.
    Append the results to data and return it.
    Outputs
    Returns a list of results containing counts of true and false responses for each article pair.
    [
    [0,7,2,7]
    ]
    first entry: number of false falses (true article is compared to true facts so idealy you wold want the falses to sum up to 0)
    second entry: number of computed outputs. This checks, that all the oututs were processed correctly. This should sum to all cases (in our case to 7).
    third entry: number of true falses (false article is compared to true facts so idealy you wold want the falses to sum up to 2)
    forth entry: number of computed outputs. This checks, that all the oututs were processed correctly. This should sum to all cases (in our case to 7).
    """
    question_list = generate_one_by_one_prompts(TOPICS)
    data = []
    for i, list_of_data in enumerate(list_of_changed_articles):
        num_of_false = 0
        num_of_true = 0
        information = []

        if print_comments:
            print('True article:')
            print("Article: ", list_of_data[3])
            print("Facts: \n", list_of_data[4])

        for  fact in question_list:
            prompt_variables = {
                'article': list_of_data[3],
                'meaning_of_topic': fact["Description of fact"],
                'question': fact["Question for fact"].format(find_json(list_of_data[4])[0][fact["Name of fact"]]),
                'topic': fact["Description of fact"]
            }
            generated = model_response(model_name, prompt_one_by_one, prompt_variables)

            if print_comments == True:
                print("This was generated when comparing topic: ", fact["Description of fact"], " for the true article.")
                print(generated)

            opinion = find_first_true_or_false(generated)
            if opinion == "the answer is true":
                num_of_true += 1
            elif opinion == "the answer is false":
                num_of_false += 1
            else:
                pass
        print('True article:')
        if num_of_false + num_of_true == len(LIST_OF_CHANGES):
            print(num_of_false)
            print(data)
            first_information = [num_of_false, num_of_false + num_of_true]
        else:
            print(num_of_false, "Missing!!!")
            first_information = [num_of_false, num_of_false + num_of_true]

        num_of_false = 0
        num_of_true = 0

        if print_comments:
            print("False article")
            print("Article: ", list_of_data[1])
            print("We changed", list_of_data[5], " and ", list_of_data[6])
            print("Fasts: \n", list_of_data[2])

        for  fact in question_list:
            prompt_variables = {
                'article': list_of_data[3],
                'meaning_of_topic': fact["Description of fact"],
                'question': fact["Question for fact"].format(find_json(list_of_data[4])[0][fact["Name of fact"]]),
                'topic': fact["Description of fact"]
                }
            
            generated = model_response(model_name, prompt_one_by_one, prompt_variables)

            if print_comments == True:
                print("This was generated when comparing topic: ", fact["Description of fact"], ", with the false article.")
                print(generated)
    
            opinion = find_first_true_or_false(generated)
            if opinion == "the answer is true":
                num_of_true += 1
            elif opinion == "the answer is false":
                num_of_false += 1
            else:
                pass
        print('False article:')
        if num_of_false + num_of_true == len(LIST_OF_CHANGES):
            print(num_of_false)
            data.append([first_information[0], first_information[1], num_of_false, num_of_false + num_of_true])
        else:
            print(num_of_false, "Missing!!!")
            data.append([first_information[0], first_information[1], num_of_false, num_of_false + num_of_true])
    
    return data

def fake_detect_comparison_true_to_true_and_false_to_true_changed(list_of_changed_articles, model_name = "llama3.1:8b", print_comments = False): 
    """
    Inputs
    list_of_changed_articles: A list containing pairs of true and false articles along with their facts and changes.
    [
    ["Index", "True Article Content", "Facts table", "Fake article content", "Changed topics", Facts", "Changed Topic 1", "Changed Topic 2"]
    ]
    model_name: The name of the model to be used for comparison (default is "llama3.1:8b").
    print_comments: A boolean flag to print intermediate comments (default is False).
    Flow
    Initialize an empty list data to store results.
    Iterate over each article pair in list_of_changed_articles.
    For each true article, generate responses for each topic using the model and count the number of true and false responses.
    Repeat the process for the corresponding false article.
    Append the results to data and return it.
    Outputs
    Returns a list of results containing counts of true and false responses for each article pair.
    [
    [0,7,2,7]
    ]
    first entry: number of false falses (true article is compared to true facts so idealy you wold want the falses to sum up to 0)
    second entry: number of computed outputs. This checks, that all the oututs were processed correctly. This should sum to all cases (in our case to 7).
    third entry: number of true falses (false article is compared to true facts so idealy you wold want the falses to sum up to 2 this proces is slightly different than in the previous case).
    forth entry: number of computed outputs. This checks, that all the oututs were processed correctly. This should sum to all cases (in our case to 7).
    """ 
    question_list = generate_one_by_one_prompts(TOPICS) 
    data = []
    for i, list_of_data in enumerate(list_of_changed_articles):
        num_of_false = 0
        num_of_true = 0
        information = []

        if print_comments:
            print('True article:')
            print("Article: ", list_of_data[3])
            print("Facts: \n", list_of_data[4])

        for  fact in question_list:
            prompt_variables = {
                'article': list_of_data[3],
                'meaning_of_topic': fact["Description of fact"],
                'question': fact["Question for fact"].format(find_json(list_of_data[4])[0][fact["Name of fact"]]),
                'topic': fact["Description of fact"]
            }
            generated = model_response(model_name, prompt_one_by_one, prompt_variables)

            if print_comments == True:
                print("This was generated when comparing topic: ", topic, " for the true article.")
                print(generated)

            opinion = find_first_true_or_false(generated)
            if opinion == "the answer is true":
                num_of_true += 1
            elif opinion == "the answer is false":
                num_of_false += 1
            else:
                pass
        print('True article:')
        if num_of_false + num_of_true == len(LIST_OF_CHANGES):
            print(num_of_false)
            print(data)
            first_information = [num_of_false, num_of_false + num_of_true]
        else:
            print(num_of_false, "Missing!!!")
            first_information = [num_of_false, num_of_false + num_of_true]


        if print_comments:
            print("False article")
            print("Article: ", list_of_data[1])
            print("We changed", list_of_data[5], " and ", list_of_data[6])
            print("Fasts: \n", list_of_data[2])

        num_of_true = 0
        num_of_false = 0
        for  fact in question_list:
            prompt_variables = {
                'article': list_of_data[1],
                'meaning_of_topic': fact["Description of fact"],
                'question': fact["Question for fact"].format(find_json(list_of_data[4])[0][fact["Name of fact"]]),
                'topic': fact["Description of fact"]
            }
            generated = model_response(model_name, prompt_one_by_one, prompt_variables)

            if print_comments == True:
                print("This was generated when comparing topic: ", topic, ", with the false article.")
                print(generated)
    
            opinion = find_first_true_or_false(generated)
            changed_topics = list_of_data[5:]
            if (opinion == "the answer is true" and topic not in changed_topics) or (opinion == "the answer is false" and topic in changed_topics):
                num_of_true += 1
            elif (opinion == "the answer is true" and topic in changed_topics) or (opinion == "the answer is false" and topic not in changed_topics):
                num_of_false += 1
            else:
                pass
        print('False article:')
        if num_of_false + num_of_true == len(LIST_OF_CHANGES):
            print(num_of_false)
            data.append([first_information[0], first_information[1], num_of_false, num_of_false + num_of_true])
        else:
            print(num_of_false, "Missing!!!")
            data.append([first_information[0], first_information[1], num_of_false, num_of_false + num_of_true])
    
    return data

def fake_detect_only_for_one_example(data, model_name = "llama3.1:8b", print_comments = False):
    """Summary
    This function, fake_detect_only_for_one_example, evaluates a given article against predefined topics to determine if the article's content is coherent with the expected descriptions. It uses a language model to generate responses and checks for the presence of "true" or "false" in the output.

    Example Usage
    data = {
        "topic": "Name of casualty or group",
        "fake_article": "The article content here...",
        "true_json_file": {
            "Name of casualty or group": "Expected description here..."
        }
    }
    result = fake_detect_only_for_one_example(data, model_name="llama3.1:8b", print_comments=True)
    print(result)  # Expected output: (0, 1) or (1, 1) or (0, 0)
    Copy
    Insert

    Code Analysis
    Inputs
    data: A dictionary containing the topic, fake article content, and true JSON file with expected descriptions.
    model_name: The name of the language model to use (default is "llama3.1:8b").
    print_comments: A boolean flag to print generated comments (default is False).
    Flow
    Initialize counters for true and false results.
    Iterate through predefined topics and their descriptions.
    For the relevant topic, generate a response using the language model.
    Print comments if print_comments is True.
    Check the generated response for "true" or "false" and return the appropriate result.
    Outputs
    A tuple indicating the detection result: (0, 1) for true, (1, 1) for false, or (0, 0) for missing.
    """
    question_list = generate_one_by_one_prompts(TOPICS)

    num_of_true = 0
    num_of_false = 0
    changed_topics = [data['topic']]
    for fact in question_list:
        if fact["Name of fact"] in changed_topics:
            prompt_variables = {
                'article': data["fake_article"],
                'meaning_of_topic': fact['Description of fact'],
                'question': fact['Question for fact'].format(data["true_json_file"][fact["Name of fact"]]),
                'topic': fact["Name of fact"]
            }
            generated = model_response(model_name, prompt_one_by_one, prompt_variables)

        for  fact in question_list:
            prompt_variables = {
                'article': list_of_data[1],
                'meaning_of_topic': fact["Description of fact"],
                'question': fact["Question for fact"].format(find_json(list_of_data[4])[0][fact["Name of fact"]]),
                'topic': fact["Description of fact"]
            }
            generated = model_response(model_name, prompt_one_by_one, prompt_variables)


            if print_comments == True:
                print("This was generated when comparing topic: ", fact["Name of fact"], ", with the false article.")
                print(generated)

            opinion = find_first_true_or_false(generated)
            print("False article:\n")
            changed_topics = [data['topic']]
            if opinion == "the answer is true":
                
                print("It is labeled true!")
                return (0, 1)
            elif opinion == "the answer is false":
                print("It is labeled false!")
                return (1, 1)
            else:
                print( "Missing!!!")
                return (0, 0)
    return (0,0)
    
    