# README.txt

## Project Setup and Execution Guide

This README file is designed to guide anyone, including those with no prior knowledge of the project, to successfully set up and run the entire project. Follow the detailed steps and procedures below to ensure a smooth experience.

---

### Hardware and Software Requirements:

- **Hardware:**
  - GPU memory (VRAM) of 10 GB or more
  - Memory is at least 16 GB

- **Software:**
  - Mac OS (M2 more) or Ubuntu 22.04
  - Python == 3.11
  - Ollama - https://ollama.com/
  - OpenWebUI == 0.3.35, Python Library

---

### Contributors:

This project was a collaborative effort, and each team member played a crucial role:

- [Student Name 1]: Taejoon Lee
  1. Project Planning
    - Establishing project goals and plans
    - Investigating suitable LLM models for the project
  2. Dataset Preparation
    - Researching and selecting datasets
    - Preprocessing datasets
  3. System Setup and Model Training
    - Configuring the project environment
    - Fine-tuning the LLM model
    - Post-processing model responses
    - Optimizing the code
  4. Documentation and Presentation
    - Preparing the project report and presentation materials

- [Student Name 2]: Khalid Juhi
  1. Project Planning
    - Establishing project goals and plans
    - Conducting research on related studies
    - Investigating suitable LLM models for the project
  2. Dataset Preparation
    - Researching and selecting datasets
  3. Model Evaluation
    - Quantitative evaluation of the LLM model (BLEU, ROUGE)
    - Qualitative evaluation of the LLM model (Survey Monkey)
  4. Documentation and Presentation
    - Preparing the project report and presentation materials
---

### Project Overview:

Provide a concise description of the project to help users understand its purpose and functionality:

Our project created a recipe recommendation service that utilizes a fine-tuned large-scale language model (LLM). 
Users can input the ingredients they have, and the system will suggest recipes based on those ingredients. 
The model provides the recipes and includes URLs for users to check search results on Google and YouTube. 
The system is built on the Open Web UI framework and supports streaming responses, ensuring users do not experience long wait times.

---

### Instructions for Setup and Execution:

1. Install Python 3.11

2. Install Ollama
 - Web: https://ollama.com/download
 - Linux command: ```curl -fsSL https://ollama.com/install.sh | sh ```

3. Install Open Web UI
 - If you install a version other than 0.3.35, our project code will not work.
 - ```pip3 install open-webui==0.3.35```

4. Copy ```./json_parsing_code/main.py ``` to Your Python ```{Your Python Folder}/site-packages/open_webui/apps/ollama/main.py```
 - If you can't find the Python folder, run ./json_parsing_code/replace.py in Python and it will copy the main.py file for you.

5. type ```ollama serve``` in the terminal to run Ollama.

6. type ```ollama pull taejoonlee/v7``` at your terminal to download the recipe generator model.

7. Run the Open Web UI by typing ```open-webui serve``` in the terminal.

8. type ```localhost:8080``` in your web browser to see the login screen.
 - After signing up and successfully logging in, you can use the service.

---
