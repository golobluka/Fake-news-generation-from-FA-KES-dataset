# Facts for fake article generation
#_________________________________________________________________
CHANGES3 = [
        #['actor', 'The actor is the person or group responsible for the attack. You need to choose different facts for the value "Actor". Changed facts must bear different meaning. Common actors of Syrian war are: rebel groups, Russian forces, ISIS, the Syrian army, USA army, etc.'],
        ['cause of death', 'Cause of death is the weapon used in the attack. You need to choose different facts for the value "Cause of death". Changed facts must bear different meaning. Examples are shooting, shelling, chemical weapons, explosions, etc.'],
        ['date of death', 'The date of death refers to time where the attack happened in the article. You need to choose different dates for the value "Date of death". Changed facts must bear different meaning.'],
        ['Place of death', 'Place of death refers to the cities or areas where the attacks happened. You need to choose different facts for the value "Place of death". Changed facts must bear different meaning. Common places are Aleppo, Damascus, Homs, Idlib, Hasaka, Deir ez-Zor, Daraa, Qamishli or Tartus.'],
        ['name of casualty or group', 'Name of casualty or group is the name of the casualty or the name of the group associated with the casualty. You need to choose different facts for the value "Name of casualty or group". Changed facts must bear different meaning. Common examples are: Civilians (General category encompassing men, women, and children), Syrian Army (SAA), Free Syrian Army (FSA), National Liberation Front (NLF), Hay\'at Tahrir al-Sham (HTS), People\'s Protection Units (YPG), Syrian Democratic Forces (SDF), Islamic State (ISIS), Hezbollah, Russian Forces, The White Helmets (Syrian Civil Defence), Kurdish Female Fighters (YPJ), Foreign Fighters (joining various factions), Al-Nusra Front Commanders, Civilians in Refugee Camps.'],
    ]
CHANGES_AGGRESSIVE = [
        ['Actor', 'The actor is the person or group responsible for the attack. You need to choose totally different facts for the values of "Actor". Changed values must bear different meaning. Common actors of Syrian war are: rebel groups, Russian forces, ISIS, the Syrian army, USA army, etc.'],
        ['Cause of death', 'Cause of death is the weapon used in the attack. You need to choose totally different facts for the values of "Cause of death". Changed values must bear different meaning. Examples are shooting, shelling, chemical weapons, explosions, etc.'],
        ['Date of death', 'The date of death refers to time where the attack happened in the article. You need to choose totally different dates for the values of "Date of death". Changed values must bear different meaning. Use date that precedes the date for up to 1 year.'],
        ['Place of death', 'Place of death refers to the cities or areas where the attacks happened. You need to choose totally different facts for the values of "Place of death". Changed values must bear different meaning. Common places are Aleppo, Damascus, Homs, Idlib, Hasaka, Deir ez-Zor, Daraa, Qamishli or Tartus.'],
        ['Name of casualty or group', 'Name of casualty or group is the name of the casualty or the name of the group associated with the casualty. You need to choose totally different facts for the values of "Name of casualty or group". Changed values must bear different meaning. Common examples are: Civilians (General category encompassing men, women, and children), Syrian Army (SAA), Free Syrian Army (FSA), National Liberation Front (NLF), Hay\'at Tahrir al-Sham (HTS), People\'s Protection Units (YPG), Syrian Democratic Forces (SDF), Islamic State (ISIS), Hezbollah, Russian Forces, The White Helmets (Syrian Civil Defence), Kurdish Female Fighters (YPJ), Foreign Fighters (joining various factions), Al-Nusra Front Commanders, Civilians in Refugee Camps.'],
    ]

TOPICS = [["Name of casualty or group", " represents the casualties names or the names of the groups associated with the casualties."],
                ["Gender or age group", " of casualty indicates if the casualties are male or female, or specify their age group (e.g., child, adult, senior)."],
                ["Cause of death", " specifies the weapons used by the aggressor (e.g., shooting, shelling, chemical weapons, etc.)"],
                ["Type", " of casualty classifies the casualties as a civilian or non-civilian (e.g., military personnel are non-civilians)."],
                ["Actor", " identifies the actors responsible for the incident, such as rebel groups, Russian forces, ISIS, the Syrian army, U.S. military, etc."],
                ["Place of death", " specifies the locations where the attacks occurred (e.g., Aleppo, Damascus, Homs, Idlib, Raqqa, Daraa, Deir ez-Zor, Qamishli, Palmyra, etc.)."],
                ["Date of death", " provides the dates when the attacks occurred."]]

prompt_for_one_by_one_fact_extraction_concise_version = """You are a journalist tasked with analyzing an article that reports on casualties related to the war in Syria. Your goal is to extract specific information regarding attacks and casualties mentioned in the article.

    BEGINNING OF THE ARTICLE
    {article}
    END OF THE ARTICLE

    Please extract the facts about the {topic} from the article. {topic}{topic_content}. Be as detailed as possible and do not output information that does not relate to {topic}, and if information is not present in the article, output "No information". Output should not exceed 25 words and should be written in the following format:
    BEGINNING OF FACTS
    <Display the extracted facts>
    END OF FACTS
    """

light_paraphrase_prompt = """
    Below is an article about an event during the Syrian war from 2015 to 2017:

    {article}

    Here is the related data extracted from the article in JSON format:

    {extracted_data}

    Please lightly paraphrase the article while changing either one or two facts from the extracted data:

    {change}

    Use iformation from JSON format except for the changed indoemation to create lightly paraphrased article. Make sure that all the information in the article is included. Ensure that the generated article is coherent. Print the updated JSON data as well, using double quotes and not single quotes. Do not provide any additional information except for the changed article and the changed JSON dataset.

    The paraphrased article should begin and end with an asterisk sign '*'.
    """


change_one_information = {"fact_transformation_abdul": """ You have a text as follows:  
BEGINNING OF THE ARTICLE
    {article}
END OF THE ARTICLE

The following facts have already been extracted from this article: {facts}. 

1. Please replace the fact {change_topic_1} in this article with a different value. 
2. Provide me with the same JSON file, but ensure that the value of {change_topic_1} is updated to the new value you used.
3. Please give me the news article with replaced value and include the phrases "BEGINNING OF THE ARTICLE" and "END OF THE ARTICLE" at the beginning and end of the paraphrased version, respectively."""

, "paraphrase_abdul": """You have a text as follows:  
BEGINNING OF THE ARTICLE
    {article}
END OF THE ARTICLE

The following facts have already been extracted from this article: {facts}. 

1. Please replace the fact {change_topic_1} in this article with a different value. 
2. Provide me with the same JSON file, but ensure that the value of {change_topic_1} is updated to the new value you used.
3. After making the replacement, please paraphrase the news article and include the phrases "BEGINNING OF THE ARTICLE" and "END OF THE ARTICLE" at the beginning and end of the paraphrased version, respectively."""

, "summarize_abdul": """You have a text as follows:  
BEGINNING OF THE ARTICLE
    {article}
END OF THE ARTICLE

The following facts have already been extracted from this article: {facts}. 

1. Please replace the fact {change_topic_1} in this article with a different value. 
2. Provide me with the same JSON file, but ensure that the value of {change_topic_1} is updated to the new value you used.
3. After making the replacement, please summarize the news article and include the phrases "BEGINNING OF THE ARTICLE" and "END OF THE ARTICLE" at the beginning and end of the paraphrased version, respectively."""
, "paraphrase": """You are a scientist analyzing articles from the well known scientific dataset FA-KES. Here is an article:

    BEGINNING OF THE ARTICLE
    {article}
    END OF THE ARTICLE

    Here is the related data extracted from the article in JSON format:

    {facts}

    Please, follow the instructions:
    Point 1: {change_data_1}
    Point 2: Create a new JSON file, which is the same as the old one, with the exception of {change_topic_1}, which is given new information given in Point 1. JSON file should be displayed in standard notation, with use of double and not single quotes, and should contain all the key values as the original one.
    Point 3: Paraphrase a new article in which you will change the information for {change_topic_1} according to decision made in Point 1. Ensure that all occurrences of {change_topic_1} are changed. You must preserve all other information from article. This article should begin with the phrase "BEGINNING OF THE ARTICLE" and end with "END OF THE ARTICLE". Make sure you include those phrases.
    """
, "paraphrase_aggressive": """You are a scientist analyzing articles from the well known scientific dataset FA-KES which is a historical document about Syrian war from 2013 to 2017. Here is an article:

    BEGINNING OF THE ARTICLE
    {article}
    END OF THE ARTICLE

    Here is the related data extracted from the article in JSON format:

    {facts}

    Please, follow the instructions:
    Point 1: {change_data_1}
    Point 2: Create a new JSON file, which is the same as the old one, with the exception of {change_topic_1}, which is given new information given in Point 1. JSON file should be displayed in standard notation, with use of double and not single quotes, and should contain all the key values as the original one.
    Point 3: Paraphrase a new article in which you will change the information for {change_topic_1} according to decision made in Point 1. Ensure that all occurrences of {change_topic_1} are changed and included in new article. You must preserve all other information from article. This article should begin with the phrase "BEGINNING OF THE ARTICLE" and end with "END OF THE ARTICLE". Make sure you include those phrases.
    Point 4: Check again the newly created article. All occurrences of {change_topic_1} must be changed, and details from original article must be preserved in a consistent way. If you spot any problem paraphrase article once more.
    """ ,
    "summarize_aggressive": """You are a scientist analyzing articles from the well known scientific dataset FA-KES which is a historical document about Syrian war from 2013 to 2017. Here is an article:

    BEGINNING OF THE ARTICLE
    {article}
    END OF THE ARTICLE

    Here is the related facts extracted from the article in JSON format:

    {facts}

    Please, follow the instructions:
    Point 1: {change_data_1}
    Point 2: Create a new JSON file, which is the same as the old one, with the exception of {change_topic_1}, which is given new information given in Point 1. JSON file should be displayed in standard notation, with use of double and not single quotes, and should contain all the key values as the original one.
    Point 3: Summarize the new article in which you will change the information for {change_topic_1} according to decision made in Point 1. Ensure that all occurrences of {change_topic_1} are changed and included in new summarization. You must preserve all other facts mentioned in the list of facts. This summarization should begin with the phrase "BEGINNING OF THE ARTICLE" and end with "END OF THE ARTICLE". Make sure you include those phrases.
    Point 4: Check again the newly created summarization. All occurrences of {change_topic_1} must be changed, and content from original article must be preserved in a consistent way. If you spot any problem summarize the article once more.
    """
}

prompt_fact_extraction = """You are a journalist tasked with analyzing an article that reports on casualties related to the war in Syria. Your goal is to extract specific information regarding casualties mentioned in the article.

    Please extract the following details of casualties in the news in JSON format.
    {{
        "Name of casualty or group": The individual's names or the names of the groups associated with the casualties.,
        "Gender or age group": Indicates if the persons is male or female, or specify their age groups (e.g., child, adult, senior).,
        "Cause of death": (e.g., shooting, shelling, chemical weapons, etc.),
        "Type": Classify the casualties as a civilian or non-civilian (e.g., military personnel are civilian).,
        "Actor": Identify the actors involved in the incidents, such as rebel groups, Russian forces, ISIS, the Syrian army, U.S. military, etc.,
        "Place of death": Specify the locations of the attack (e.g., Aleppo, Damascus, Homs, Idlib, Raqqa, Daraa, Deir ez-Zor, Qamishli, Palmyra, etc.).,
        "Date of death": Provide the dates when the attacks occurred.
    }}

    EXAMPLE of an output:
    {{
        "Name of casualty or group": Not specifically named; referred to casualties at the airbase,
        "Gender or age group": Not specified in the article.,
        "Cause of death": explosion,
        "Type": Non-civilian (military personnel at the airbase).,
        "Actor": U.S. military (responsible for the missile strike). Syrian Arab Army (the airbase was providing support for army operations).,
        "Place of death": Near Homs, Syria (specific airbase mentioned).,
        "Date of death": April 7, 2017
    }}

    BEGINNING OF THE ARTICLE
    {article}
    END OF THE ARTICLE

    Ensure that the extracted information is as accurate and detailed as possible. Take context into account, and if certain data points are not available or mentioned in the article, output "Not available". Try to incorporate all casualties in one file.
    """

prompt_fact_extraction_abdul = """You are a journalist assigned to analyze a war-related article that reports on casualties. Your task is to identify specific events, facts, or information regarding casualties mentioned in the article.

Please extract the following details about the casualties mentioned in the news article, ensuring that the information is as accurate and detailed as possible. If certain details are missing or not provided in the article, write "Not available". Finally, compile the extracted information into one JSON file, which contains informtion about all casualties in the article.

Details to extract:
{{
    "Name of casualty or group": The names of the individuals or groups involved with casualties.
    "Gender or age group": Specifie if the persons is male or female, or mention their age group (e.g., child, adult, senior).
    "Cause of death": (e.g., shooting, shelling, chemical weapons, etc.)
    "Type": Determine whether the casualties are civilians or non-civilians (e.g., military personnel).
    "Actor": Identify the parties involved in the incident, such as rebel groups, Russian forces, ISIS, the Syrian army, U.S. military, etc.
    "Place of death": Indicate the locations where the casualties occurred (e.g., Aleppo, Damascus, Homs, Idlib, Raqqa, Daraa, Deir ez-Zor, Qamishli, Palmyra, etc.).
    "Date of death": Provide the date when the attacks accured.
}}
Example JSON output:
{{
    "Name of casualty or group": "Abu Abdelrahman Salqeen, Ahrar al-Sham members, Hassan Abboud, Islamic State leaders, Maher Meshaal (Abu Hajar al-Hadrami), Hizbollah fighters",
    "Gender or age group": "males",
    "Cause of death": "suicide bombing, bombing, airstrikes, combat",
    "Type": "non-civilian",
    "Actor": "Ahrar al-Sham, U.S. military, Syrian Army, Hizbollah",
    "Place of death": "Idlib, Hasakeh, Zabadani",
    "Date of death": "07/14/2015, 09/2014, 07/2015"
}}

{article}
"""



# imports 
import fake_detector
import random
import ollama
import json
import re
import pandas as pd

# Function used for article generation

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

def extract_last_article(text):
    """Function to extract the last article."""
    pattern = r"BEGINNING OF THE ARTICLE(.*?)END OF THE ARTICLE"
    matches = list(re.finditer(pattern, text, re.DOTALL))
    if matches:
        last_match = matches[-1]
        return last_match.group(1).strip()
    return None

def print_readable_dict(data):
    """Prints a dictionary in a readable JSON-like format."""
    print(json.dumps(data, indent=4, ensure_ascii=False))

def extract_fact_from_text(text):
    pattern1 = r"BEGINNING OF FACTS(.*?)END OF FACTS"
    pattern2 = r"BEGINING OF FACTS(.*?)END OF FACTS" #I don't know why but sometimes BEGINNING is written with one N.
    match = re.search(pattern1, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        match2 = re.search(pattern2, text, re.DOTALL)
        if match2:
            return match2.group(1).strip()
    return None

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

#Generation of text
def generate_facts(article_content, name_of_the_model, print_generated_text = False):
    """
    Summary
    This function generates facts about casualties from a given article using a specified model. It formats the article content into a prompt, sends it to the model, and extracts the relevant facts in JSON format.

    Example Usage
    article_content = "An article about a recent conflict..."
    model_name = "fact_extraction_model"
    facts = generate_facts(article_content, model_name, print_generated_text=True)
    print(facts)
    Copy
    Insert

    Code Analysis
    Inputs
    article_content: The content of the article to analyze.
    name_of_the_model: The name of the model used for fact extraction.
    print_generated_text: A boolean flag to print the generated text (default is False).
    Flow
    The function formats the article content into a prompt using prompt_fact_extraction_abdul.
    It sends the prompt to the specified model using ollama.chat.
    The response from the model is processed to extract JSON-like content using find_json.
    If print_generated_text is True, it prints the generated text.
    The function returns the extracted JSON list or None if no facts are found.
    Outputs
    A list of dictionaries containing the extracted facts in JSON format, or None if no facts are found.
    """    
    prompt_variables = {
        'article': article_content,
    }
    generated = model_response(name_of_the_model, prompt_fact_extraction_abdul, prompt_variables)

    if print_generated_text == True:
        print("Facts generated in normal fact_generator:\n ", generated)

    json_list = find_json(generated)
    if json_list == []:
        json_list  = None
  
    return json_list

def generate_facts_one_by_one(article_content, name_of_the_model, print_generated_text = False):
    """
    Summary
    This function generate_facts_one_by_one extracts specific facts from an article using a predefined list of topics. It uses a model to generate responses for each topic and compiles the extracted facts into a JSON list.

    Example Usage
    article_content = "Sample article content about the Syrian war."
    name_of_the_model = "fact_extraction_model"
    facts = generate_facts_one_by_one(article_content, name_of_the_model, print_generated_text=True)
    print(facts)

    Code Analysis
    Inputs
    article_content: The content of the article from which facts are to be extracted.
    name_of_the_model: The name of the model used for generating responses.
    print_generated_text: A boolean flag to print the generated text for each topic.
    Flow
    Initialize an empty dictionary json_dict.
    Iterate over each topic in the TOPICS list.
    Generate a response using the ollama.chat function with the formatted prompt.
    Optionally print the generated text if print_generated_text is True.
    Extract the fact from the generated text and store it in json_dict.
    Check if any value in json_dict is None and set json_list accordingly.
    Return the json_list.
    Outputs
    json_list: A list containing a dictionary of extracted facts, or None if any fact extraction failed.
    """
    json_dict = {}    
    for topic in TOPICS:
        prompt_variables = {
            'article': article_content,
            'topic': topic[0],
            'topic_content': topic[1],
        }
        generated = model_response(name_of_the_model, prompt_for_one_by_one_fact_extraction_concise_version, prompt_variables)

        if print_generated_text == True:
            print(f"Generated fact on topic {topic[0]}:\n", generated)
        json_dict[topic[0]] = extract_fact_from_text(generated)
        if None in list(json_dict.values()):
            json_list = None
        else: json_list = [json_dict]

    return json_list

def generate(true_articles, name_of_the_model, size_of_sample, type_of_generation = "normal", print_comments=False):
    """
    Summary
    This function generates facts from a sample of articles using a specified model. It can generate facts either in a "normal" mode or "one_by_one" mode and returns the results in a DataFrame.

    Example Usage
    true_articles = pd.DataFrame({'article_content': ["Article 1 content", "Article 2 content"]})
    model_name = "fact_extraction_model"
    sample_size = 1
    results = generate(true_articles, model_name, sample_size, type_of_generation="normal", print_comments=True)
    print(results)

    Inputs
    true_articles: DataFrame containing articles.
    name_of_the_model: The name of the model used for fact extraction.
    size_of_sample: Number of articles to sample.
    type_of_generation: Mode of fact generation ("normal" or "one_by_one").
    print_comments: Boolean flag to print generated text.
    Flow
    Randomly sample indices from the articles.
    For each sampled article, generate facts using the specified mode.
    Append the results to a list.
    Convert the results list to a DataFrame and return it.
    Outputs
    A DataFrame containing the indices, article contents, and extracted facts in JSON format.
    """
    
    
    indices = random.sample(list(range(len(true_articles))), size_of_sample)
    results = []
    for index in indices:
        article_content = list(true_articles['article_content'])[index]

        if type_of_generation == "normal":
            json_list = generate_facts(article_content, name_of_the_model, print_comments)
        elif type_of_generation == "one_by_one":
            json_list = generate_facts_one_by_one(article_content, name_of_the_model, print_comments)
        else:
            raise ValueError("argument 'type of generation' is not a valid string!")

        if json_dict == None:
            print("No JSON found in first step of extracting facts!")
        else:
            for json_dict in json_list:
                results.append(index, article_content, json_dict)
    
    column_names = ["index", "article_content", "json_dict"]
    results = pd.DataFrame(results, columns = column_names)
    return results


#main functions
import random
import ollama
import json
import re
import pandas as pd

def extract_and_change_articles(true_articles, name_of_the_model, size_of_sample=5, type_of_generation = "normal", change_of_article = "paraphrase_abdul", print_comments = False):
    """
    Summary
    This function extracts and modifies articles from a given dataset using a specified model. It samples a subset of articles, generates facts, and changes specific topics within the articles.

    Example Usage
    true_articles = pd.DataFrame({'article_content': ["Article 1 content...", "Article 2 content..."]})
    model_name = "fact_extraction_model"
    results = extract_and_change_articles(true_articles, model_name, size_of_sample=2, type_of_generation="normal", change_of_article="paraphrase_abdul", print_comments=True)
    print(results)

    Inputs
    true_articles: DataFrame containing articles.
    name_of_the_model: Name of the model used for fact extraction and modification.
    size_of_sample: Number of articles to sample (default is 5).
    type_of_generation: Type of fact generation method ("normal" or "one_by_one").
    change_of_article: Type of article change method.
    print_comments: Boolean flag to print intermediate steps (default is False).
    Flow
    Sample a subset of articles.
    Generate facts using the specified model and method.
    Change specific topics within the articles.
    Print intermediate steps if print_comments is True.
    Return a DataFrame with the results.
    Outputs
    DataFrame containing the original and modified articles, along with the topics changed.
    """
   
    indices = random.sample(list(range(len(true_articles))), size_of_sample)
    results = []
    for index in indices:
        article_content = list(true_articles['article_content'])[index]
        if print_comments:
            print("Original article: ", article_content)

            
        if type_of_generation == "normal":
            json_list = generate_facts(article_content, name_of_the_model, print_comments)
        elif type_of_generation == "one_by_one":
            json_list = generate_facts_one_by_one(article_content, name_of_the_model, print_comments)
        else:
            raise ValueError("argument 'type of generation' is not a valid string!")



        if json_list == None:
            print("No JSON found in first step of extracting facts!")
        else:
            for json_dict in json_list:
        
                print("THIS IS DICTIONARY THAT WAS EXTRACTED")
                print_readable_dict(json_dict)
                topic_to_change = random.sample(CHANGES_AGGRESSIVE, 2)
                print("We will change topics:", topic_to_change[0][0], " and ", topic_to_change[1][0])

                # Use model_response function
                prompt_variables = {
                    'article': article_content,
                    'facts': json.dumps(json_dict, indent=4, ensure_ascii=False),
                    'change_topic_1': topic_to_change[0][0],
                    'change_data_1': topic_to_change[0][1]
                }
                generated = model_response(name_of_the_model, change_one_information[change_of_article], prompt_variables)
                
                changed_json = find_json(generated)
                changed_json = changed_json[0] if changed_json else None

                changed_article = extract_last_article(generated)
                if not changed_article or not changed_json:
                    print("We did not get through the first round!")
                    if print_comments == True:
                        print("THIS IS THE FIRST GENERATED TEXT \n\n", generated)
                        print("EXTRACTED ARTICLE: ", changed_article)
                        print("EXTRACTED JSON: ", changed_json)
                    results.append([index, None, None, article_content, json_dict, topic_to_change[0][0], topic_to_change[1][0]])
                else:
                    prompt_variables = {
                        'article': changed_article,
                        'facts': json.dumps(changed_json, indent=4, ensure_ascii=False),
                        'change_topic_1': topic_to_change[1][0],
                        'change_data_1': topic_to_change[1][1],
                    }
                    generated = model_response(name_of_the_model, change_one_information[change_of_article], prompt_variables)
              
                    twice_changed_json = find_json(generated)
                    twice_changed_json = twice_changed_json[0] if twice_changed_json else None

                    twice_changed_article = extract_last_article(generated)
                    if print_comments == True:
                        print("THIS IS THE SECOND GENERATED TEXT \n\n", generated)
                        print("TWICE EXTRACTED ARTICLE: ", twice_changed_article)
                        print("TWICE EXTRACTED JSON: ", twice_changed_json)
                    results.append([index, twice_changed_article, twice_changed_json, article_content, json_dict, topic_to_change[0][0], topic_to_change[1][0]])

    column_names = ["index", "Changed_article", "Changed_json", "Between_article", "Between_json", "first_topic_changed", "second_topic_changed"]
    results = pd.DataFrame(results, columns = column_names)
    return results

def change_articles(articles_with_facts, name_of_the_model, size_of_sample=5, change_of_article = "paraphrase", print_comments = False):
    """
    Summary
    This function change_articles processes a sample of articles by applying two rounds of information changes using a specified language model. It modifies specific topics within the articles and their associated JSON data, then returns the results.

    Example Usage
    import pandas as pd

    # Sample DataFrame
    articles_with_facts = pd.DataFrame({
        'article_content': [
            {"article": "Sample article 1", "facts": {"fact1": "value1"}},
            {"article": "Sample article 2", "facts": {"fact2": "value2"}}
        ]
    })

    # Call the function
    results = change_articles(articles_with_facts, "model_name", size_of_sample=2, change_of_article="paraphrase", print_comments=True)
    print(results)

    Inputs
    articles_with_facts: DataFrame containing articles and their facts.
    name_of_the_model: The name of the language model to use.
    size_of_sample: Number of articles to process (default is 5).
    change_of_article: Type of change to apply (default is "paraphrase").
    print_comments: Boolean to print intermediate comments (default is False).
    Flow
    Randomly sample a subset of articles.
    For each sampled article, extract its content and facts.
    Print the extracted facts in a readable format.
    Randomly select two topics to change.
    Use the language model to generate a modified article and JSON data.
    If the first round of changes is successful, apply a second round of changes.
    Collect and return the results in a DataFrame.
    Outputs
    A DataFrame containing the indices, twice-changed articles, twice-changed JSON, original articles, original JSON, and the topics changed.
    """
    
    indices = random.sample(list(range(len(articles_with_facts))), size_of_sample)
    results = []
    for index in indices:
        article_content = list(articles_with_facts['article_content'])[index]
        json_dict = list(articles_with_facts['article_content'])[index]

        
        print("THIS IS DICTIONARY THAT WAS EXTRACTED")
        print_readable_dict(json_dict)
        topic_to_change = random.sample(CHANGES3, 2)
        print("We will change topics:", topic_to_change[0][0], " and ", topic_to_change[1][0])
        
        prompt_variables = {
            'article': article_content,
            'facts': json.dumps(json_dict, indent=4, ensure_ascii=False),
            'change_topic_1': topic_to_change[0][0],
            'change_data_1': topic_to_change[0][1],
        }
        generated = model_response(name_of_the_model, change_one_information[change_of_article], prompt_variables)

        changed_json = find_json(generated)
        
        changed_json = changed_json[0] if changed_json else None
        changed_article = extract_last_article(generated)
        if not changed_article or not changed_json:
            print("We did not get through the first round!")
            if print_comments == True:
                print("THIS IS THE FIRST GENERATED TEXT \n\n", generated)
                print("EXTRACTED ARTICLE: ", changed_article)
                print("EXTRACTED JSON: ", changed_json)
            results.append((index, None, None, article_content, json_dict, topic_to_change[0][0], topic_to_change[1][0]))
        else:
            prompt_variables = {
                'article': changed_article,
                'facts': json.dumps(changed_json, indent=4, ensure_ascii=False),
                'change_topic_1': topic_to_change[1][0],
                'change_data_1': topic_to_change[1][1],
            }
            generated = model_response(name_of_the_model, change_one_information[change_of_article], prompt_variables)
 
            twice_changed_json = find_json(generated)
            if twice_changed_json:
                twice_changed_json = twice_changed_json[0]
            
            twice_changed_article = extract_last_article(generated)
            if print_comments == True:
                print("THIS IS THE SECOND GENERATED TEXT \n\n", generated)
                print("TWICE EXTRACTED ARTICLE: ", twice_changed_article)
                print("TWICE EXTRACTED JSON: ", twice_changed_json)
            results.append([index, twice_changed_article, twice_changed_json, article_content, json_dict, topic_to_change[0][0], topic_to_change[1][0]])
    
    column_names = ["index", "Changed_article", "Changed_json", "Between_article", "Between_json", "first_topic_changed", "second_topic_changed"]
    results = pd.DataFrame(results, columns = column_names)
    
    return results

    """Applies two rounds of information changes.

    Args:
        articles_with_facts: DataFrame containing the articles and facts.
        name_of_the_model (str): The name of the language model to use.
        size_of_sample (int): Number of articles to process. Default is 60.

    Returns:
        list: A list of results containing the indices, changed articles, changed JSON, original articles, etc.
    """
    
    indices = random.sample(list(range(len(articles_with_facts))), size_of_sample)
    results = []
    for index in indices:
        article_content = list(articles_with_facts['article_content'])[index]
        json_dict = list(articles_with_facts['article_content'])[index]

        
        print("THIS IS DICTIONARY THAT WAS EXTRACTED")
        print_readable_dict(json_dict)
        topic_to_change = random.sample(CHANGES3, 2)
        print("We will change topics:", topic_to_change[0][0], " and ", topic_to_change[1][0])
        response = ollama.chat(model=name_of_the_model, messages=[
            {
                'role': 'user',
                'content': change_one_information[change_of_article].format(
                    article=article_content,
                    facts =json.dumps(json_dict, indent=4, ensure_ascii=False),
                    change_topic_1=topic_to_change[0][0],
                    change_data_1=topic_to_change[0][1]
                ),
                'temperature': 0.2,
            }
        ])
        generated = response['message']['content']
        changed_json = find_json(generated)
        
        changed_json = changed_json[0] if changed_json else None
        changed_article = extract_last_article(generated)
        if not changed_article or not changed_json:
            print("We did not get through the first round!")
            if print_comments == True:
                print("THIS IS THE FIRST GENERATED TEXT \n\n", generated)
                print("EXTRACTED ARTICLE: ", changed_article)
                print("EXTRACTED JSON: ", changed_json)
            results.append((index, None, None, article_content, json_dict, topic_to_change[0][0], topic_to_change[1][0]))
        else:
            response = ollama.chat(model=name_of_the_model, messages=[
                {
                    'role': 'user',
                    'content': change_one_information[change_of_article].format(
                        article=changed_article,
                        facts =json.dumps(changed_json, indent=4, ensure_ascii=False),
                        change_topic_1=topic_to_change[1][0],
                        change_data_1=topic_to_change[1][1]
                    ),
                    'temperature': 0.2,
                }
            ])
            generated = response['message']['content']
            twice_changed_json = find_json(generated)
            if twice_changed_json:
                twice_changed_json = twice_changed_json[0]
            
            twice_changed_article = extract_last_article(generated)
            if print_comments == True:
                print("THIS IS THE SECOND GENERATED TEXT \n\n", generated)
                print("TWICE EXTRACTED ARTICLE: ", twice_changed_article)
                print("TWICE EXTRACTED JSON: ", twice_changed_json)
            results.append([index, twice_changed_article, twice_changed_json, article_content, json_dict, topic_to_change[0][0], topic_to_change[1][0]])
    
    column_names = ["index", "Changed_article", "Changed_json", "Between_article", "Between_json", "first_topic_changed", "second_topic_changed"]
    results = pd.DataFrame(results, columns = column_names)
    
    return results

def extract_and_change_articles_with_labeling_added(true_articles, name_of_the_model, size_of_sample=5, type_of_generation = "normal", change_of_article = "paraphrase_abdul", print_comments = False):
    """
    Summary
    This function extract_and_change_articles_with_labeling_added processes a sample of articles to generate and modify facts using a specified model. It iteratively changes topics within the articles and evaluates the quality of these changes using a fake detector.

    Example Usage
    true_articles = pd.DataFrame({'article_content': ["Article 1 content...", "Article 2 content..."]})
    model_name = "fact_extraction_model"
    results = extract_and_change_articles_with_labeling_added(true_articles, model_name, size_of_sample=2, type_of_generation="normal", change_of_article="paraphrase_abdul", print_comments=True)
    print(results)

    Inputs
    true_articles: DataFrame containing articles to process.
    name_of_the_model: Name of the model used for fact extraction and modification.
    size_of_sample: Number of articles to sample from true_articles (default is 5).
    type_of_generation: Method of fact generation, either "normal" or "one_by_one".
    change_of_article: Type of article modification to apply.
    print_comments: Boolean flag to print intermediate comments (default is False).
    Flow
    Randomly sample articles from true_articles.
    Generate facts from each sampled article using the specified model.
    Modify the article content iteratively by changing specified topics.
    Evaluate the quality of the modified articles using a fake detector.
    Collect and return the results in a DataFrame.
    Outputs
    DataFrame containing the original and modified articles, JSON data, and topics changed.
    """

    indices = random.sample(list(range(len(true_articles))), size_of_sample)
    results = []
    for index in indices:
        article_content = list(true_articles['article_content'])[index]
        if print_comments:
            print("Original article: ", article_content)

            
        if type_of_generation == "normal":
            json_list = generate_facts(article_content, name_of_the_model, print_comments)
        elif type_of_generation == "one_by_one":
            json_list = generate_facts_one_by_one(article_content, name_of_the_model, print_comments)
        else:
            raise ValueError("argument 'type of generation' is not a valid string!")



        if json_list == None:
            print("No JSON found in first step of extracting facts!")
        else:
            print("THIS IS DICTIONARY THAT WAS EXTRACTED")
            print_readable_dict(json_list)
            
            for json_dict in json_list:
                quality_of_generation = False
                number_of_trials = 0
                while quality_of_generation == False and number_of_trials <= 3:
                    number_of_trials += 1

                    topic_to_change = random.sample(CHANGES_AGGRESSIVE, 3)
                    print("We will change topics:", topic_to_change[0][0], ", ", topic_to_change[1][0], " and ", topic_to_change[2][0])

                    prompt_variables = {
                        'article': article_content,
                        'facts': json.dumps(json_dict, indent=4, ensure_ascii=False),
                        'change_topic_1': topic_to_change[0][0],
                        'change_data_1': topic_to_change[0][1],
                    }
                    generated = model_response(name_of_the_model, change_one_information[change_of_article], prompt_variables)
                    

                    changed_json_list = find_json(generated)
                    changed_json = changed_json_list[0] if changed_json_list else None
                    changed_article = extract_last_article(generated)

                    if not changed_article or not changed_json:
                        if print_comments == True:
                            print("THIS IS THE FIRST GENERATED TEXT \n\n", generated)
                            print("EXTRACTED ARTICLE: ", changed_article)
                            print("EXTRACTED JSON: ", changed_json)
                    else: 
                        extracted = {"fake_article": changed_article, "true_json_file": json_dict, "topic": topic_to_change[0][0]} 
                        labeling_result = fake_detector.fake_detect_only_for_one_example(extracted, print_comments=print_comments)
                        if labeling_result[0] == 1 and labeling_result[1] == 1: #False article was labeled in correct way
                            quality_of_generation = True
                            print("Quality of generation was good")
                        else:
                            print("Quality of generation is bad!")
                            if print_comments == True:
                                print("THIS IS THE FIRST GENERATED TEXT \n\n", generated)

                if quality_of_generation == False:
                    print("We did not get through the first round!")
                else:

                    quality_of_generation = False
                    number_of_trials = 0
                    while quality_of_generation == False and number_of_trials <= 3:
                        number_of_trials += 1

                        prompt_variables = {
                            'article': changed_article,
                            'facts': json.dumps(changed_json, indent=4, ensure_ascii=False),
                            'change_topic_1': topic_to_change[1][0],
                            'change_data_1': topic_to_change[1][1],
                        }
                        generated = model_response(name_of_the_model, change_one_information[change_of_article], prompt_variables)
                        
            
                        twice_changed_json = find_json(generated)
                        twice_changed_json = twice_changed_json[0] if twice_changed_json else None
                        twice_changed_article = extract_last_article(generated)

                        if not twice_changed_article or not twice_changed_json:
                            if print_comments == True:
                                print("Failure in detection.")
                        else: 
                            extracted = {"fake_article": twice_changed_article, "true_json_file": changed_json, "topic": topic_to_change[1][0]}
                            labeling_result = fake_detector.fake_detect_only_for_one_example(extracted, print_comments=print_comments)
                        if labeling_result[0] == 1 and labeling_result[1] == 1: #False article was labeled in correct way
                            quality_of_generation = True
                            print("Quality of generation was good")
                        else:
                            print("Quality of generation is bad!")
                            if print_comments == True:
                                print("THIS IS THE FIRST GENERATED TEXT \n\n", generated)
                    
                    if quality_of_generation == False:
                        print("We did not get through the first round")
                    else:
                        quality_of_generation = False
                        number_of_trials = 0
                        while quality_of_generation == False and number_of_trials <= 3:
                            number_of_trials += 1

                            prompt_variables = {
                                'article': twice_changed_article,
                                'facts': json.dumps(twice_changed_json, indent=4, ensure_ascii=False),
                                'change_topic_1': topic_to_change[2][0],
                                'change_data_1': topic_to_change[2][1],
                            }
                            generated = model_response(name_of_the_model, change_one_information[change_of_article], prompt_variables)
                            
                            third_changed_json = find_json(generated)
                            third_changed_json = third_changed_json[0] if third_changed_json else None
                            third_changed_article = extract_last_article(generated)

                            if not third_changed_article or not third_changed_json:
                                if print_comments == True:
                                    print("Failure in detection.")
                            else: 
                                extracted = {"fake_article": third_changed_article, "true_json_file": twice_changed_json, "topic": topic_to_change[2][0]}
                                labeling_result = fake_detector.fake_detect_only_for_one_example(extracted, print_comments=print_comments)
                                if labeling_result[0] == 1 and labeling_result[1] == 1: #False article was labeled in correct way
                                    quality_of_generation = True
                                    print("Quality of generation was good")
                                else:
                                    print("Failure in labeling!")


                        if print_comments == True:
                            print("THIS IS THE THIRD GENERATED TEXT \n\n", generated)
                            print("THIRD EXTRACTED ARTICLE: ", third_changed_article)
                            print("THIRD EXTRACTED JSON: ", third_changed_json)
                        results.append([index, third_changed_article, third_changed_json, twice_changed_article, twice_changed_json, article_content, json_dict, topic_to_change[0][0], topic_to_change[1][0], topic_to_change[2][0]])

    column_names = ["index", "Changed_article", "Changed_json", "Between_article", "Between_json", "Original_article", "Original_json", "first_topic_changed", "second_topic_changed", "third_topic_changed"]
    results = pd.DataFrame(results, columns = column_names)

    return results
