from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat

from librarian.agents.librarian_io import LibrarianInput, LibrarianOutput
from librarian.agents.librarian_prompts import DESCRIPTION, INSTRUCTIONS

from librarian.core.settings import openai_api_key


librarian = Agent(
    name='Librarian',
    role='Librarian',

    # model=Ollama(id='gemma4:e2b', options={'temperature': 0.0}, format='json', keep_alive='15s'),
    model=OpenAIChat(id='gpt-5.4-mini', api_key=openai_api_key, temperature=0.0),

    description=DESCRIPTION,
    instructions=INSTRUCTIONS,

    input_schema=LibrarianInput,
    output_schema=LibrarianOutput,
    
    debug_mode=True
)