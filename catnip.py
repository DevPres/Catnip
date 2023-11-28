from cat.mad_hatter.decorators import tool, hook, plugin
from datetime import datetime, date
from .feeder import get_news


@tool
def get_latest_news(tool_input, cat):
    """"use this tool to respond to requests like 'give me good news'. Input is always none """
    try:
        n = get_news()
        return str(n)
    except Exception as e:
        print(e)
        return "Oops, nothing good today!"  


@hook(priority=1)
def before_cat_sends_message(final_output, cat):
    
    prompt =f'This is the news list: {final_output["content"]}. Filter from the list all message that are extremely POSITIVE, and format as bullet pointed list'
    final_output["content"] = cat.llm(prompt);     
    
    return final_output

