import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat

from librarian.agents.librarian_io import LibrarianInput, LibrarianOutput
from librarian.agents.librarian_prompts import DESCRIPTION, INSTRUCTIONS


load_dotenv(override=True)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

librarian = Agent(
    name='Librarian',
    role='Librarian',

    # model=Ollama(id='gemma4:e2b', options={'temperature': 0.0}, format='json', keep_alive='15s'),
    model=OpenAIChat(id='gpt-4o-mini', api_key=OPENAI_API_KEY, temperature=0.0),

    # parser_model=Ollama(id='qwen2.5-coder:0.5b'),
    # parser_model=OpenAIChat(id='gpt-4o-mini', api_key=OPENAI_API_KEY),

    description=DESCRIPTION,
    instructions=INSTRUCTIONS,
    # parser_model_prompt=INSTRUCTIONS_PARSE_MODEL,

    input_schema=LibrarianInput,
    output_schema=LibrarianOutput,
    
    debug_mode=True
)