import subprocess
import json
import requests

# Get ingredients from user
user_ingredients = input("Enter ingredients (separated by commas): ")

# Get recipe recommendation using Ollama model
def generate_recipe(ingredients):
    # Generate prompt
    prompt = f"[{ingredients}]"
    # Call Ollama model (using command line interface)
    # Modify the path and command according to your actual environment
    command = ['ollama', 'generate', 'custom_llama2', '--prompt', prompt]
    result = subprocess.run(command, capture_output=True, text=True)
    response = result.stdout.strip()
    return response

model_response = generate_recipe(user_ingredients)

# Extract recipe name from model's response
def extract_recipe_name(response):
    # Simply extract recipe name from the first sentence (modify based on response format)
    recipe_name = response.split(' ')[0]
    return recipe_name

recipe_name = extract_recipe_name(model_response)

# Search for cooking video on YouTube
def search_youtube(recipe_name):
    api_key = 'YOUR_YOUTUBE_API_KEY'  # Replace with your own YouTube API key
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': recipe_name + ' recipe',
        'type': 'video',
        'key': api_key,
        'maxResults': 1
    }
    response = requests.get(search_url, params=params)
    data = response.json()
    if 'items' in data and len(data['items']) > 0:
        video_id = data['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    else:
        return None

video_url = search_youtube(recipe_name)

# Combine model's response and YouTube video URL
if video_url:
    final_response = f"{model_response}\nCheck here for detailed recipe: {video_url}"
else:
    final_response = f"{model_response}\nSorry, we couldn't find a video for this recipe."

# Print final response
print(final_response)