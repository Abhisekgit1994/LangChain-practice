import os

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import openai
import os
openai.api_key = "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"
chats = ChatOpenAI(temperature=0.0)
print(chat)

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

prompt_template = ChatPromptTemplate.from_template(template_string)
#
# # print(prompt_template.messages[0].prompt)
#
customer_style = """American English \
in a calm and respectful tone
"""

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

customer_messages = prompt_template.format_messages(
    style=customer_style,
    text=customer_email
)

print(type(customer_messages))
print(type(customer_messages[0]))
customer_response = chats(customer_messages)
