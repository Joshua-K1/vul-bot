import json

def read_prompts(prompt_type):
    with open('system_prompts/prompts.json', 'r', encoding='utf-8') as prompt_file:
        prompts = json.load(prompt_file)

        return prompts[prompt_type]
