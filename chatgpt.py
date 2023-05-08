import openai
openai.api_key = 'xxkey'

def ask(prompt):
    model="gpt-3.5-turbo"
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    result = response.choices[0].message["content"]
    return result

from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)

@magics_class
class ChatGPTMagics(Magics):
 
    @line_magic
    def chat(self, line):
        return ask(line)
 
    @cell_magic
    def gpt(self, line, cell):
        result = ask(cell)
        print(result)
 
    @line_cell_magic
    def chatgpt(self, line, cell=None):
        "Magic that works both as %chatgpt and as %%chatgpt"
        if cell is None:
            return ask(line)
        else:
            print(ask(cell))


# In order to actually use these magics, you must register them with a
# running IPython.
def load_ipython_extension(ipython):
    """
    Any module file that define a function named `load_ipython_extension`
    can be loaded via `%load_ext module.path` or be configured to be
    autoloaded by IPython at startup time.
    """
    ipython.register_magics(ChatGPTMagics)
