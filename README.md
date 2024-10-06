# Recipemaker

## Introduction
- This is a project for ELG5121 Multimedia Communications course at University of Ottawa
- Group 8 members:
  - Taejoon Lee
  - Khalid Juhi

## PART 1. Making Recipe Recommendation System
1. Scenario
    - Question
      - Function 1(Ollama called by Python): Recomend Recipe -> str answer
      - Function 2(Ollama called by Python and Python): Classify Question is requesting Recipe or not
        - If recipe, Using Youtube API, search recipe video and recommend -> str link
          - If not found recipe video, return str answer
        - If not recipe, return str answer
    - Result
      - 1. Recommend Recipe + Youtube Link(str answer + str link)
      - 2. Recommend Recipe(str answer)
      - 3. Not Recipe(str answer)
2. Datasets [dataset.md](https://github.com/taejoonlee56/recipemaker/blob/main/datasets.md)
    - There are various datasets on Kaggle.
    - These dataset need to be pre-processing(unify data structure)
4. Models
    - Ollama
5. Fine tuning
6. Evaluation
7. Result
8. Constraints
    - Youtube API has a limit of 10,000 requests per day.
9. Reference


## PART 2. Making Dashboard
1. Scenario



## System prompt

You are an assistant that identifies whether a user is requesting a recipe and extracts the recipe name. User Input: "{user_input}". Please answer in JSON format:{{"is_recipe_request": true or false,"recipe_name": "extracted recipe name or null","user_answer": "answer of model"}}
