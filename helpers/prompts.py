import json
from logger.logger import event_logger

def read_prompts(prompt_type):
    event_logger.info("Searching Prompt File")
    try: 
     with open('system_prompts/prompts.json', 'r', encoding='utf-8') as prompt_file:
        prompts = json.load(prompt_file)

        return prompts[prompt_type]

    except(ValueError, FileNotFoundError) as err:
      event_logger.error(err)
      event_logger.error("Prompt file could not be found or is in an invalid format")

      return ""

