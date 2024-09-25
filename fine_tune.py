import subprocess

# Set up information needed for fine-tuning
new_model_name = 'custom_model'
base_model_name = 'llama2'
dataset_file = 'dataset.jsonl'

# Compose ollama fine-tuning command
command = [
    'ollama',
    'create',
    new_model_name,
    '--base',
    base_model_name,
    '--finetune',
    dataset_file
]

# Execute command and handle the result
try:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    print(f"Model '{new_model_name}' has been successfully fine-tuned.")
except subprocess.CalledProcessError as e:
    print("An error occurred during fine-tuning:")
    print(e.stderr)