import subprocess
import json
import requests

user_ingredients = input("Enter ingredients (separated by commas): ")

def generate_recipe(ingredients):
    prompt = f"[{ingredients}]"
    command = ['ollama', 'generate', 'custom_llama2', '--prompt', prompt]
    result = subprocess.run(command, capture_output=True, text=True)
    response = result.stdout.strip()
    return response

model_response = generate_recipe(user_ingredients)

def extract_recipe_name(response):
    recipe_name = response.split(' ')[0]
    return recipe_name

recipe_name = extract_recipe_name(model_response)

def search_youtube(recipe_name):
    api_key = 'YOUR_YOUTUBE_API_KEY'
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

if video_url:
    final_response = f"{model_response}\nCheck here for detailed recipe: {video_url}"
else:
    final_response = f"{model_response}\nSorry, we couldn't find a video for this recipe."

print(final_response)
