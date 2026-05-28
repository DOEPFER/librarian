from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat

from librarian.agents.summarizer_io import SummarizerInput, SummarizerOutput
from librarian.agents.summarizer_prompts import DESCRIPTION, INSTRUCTIONS

from librarian.core.settings import openai_api_key


summarizer = Agent(
    name='Summarizer',
    role='Summarizer',

    # model=Ollama(id='gemma4:e2b', options={'temperature': 0.75}, format='json', keep_alive='15s'),
    model=OpenAIChat(id='gpt-5.4-mini', api_key=openai_api_key, temperature=0.75),

    description=DESCRIPTION,
    instructions=INSTRUCTIONS,

    input_schema=SummarizerInput,
    output_schema=SummarizerOutput,
    
    debug_mode=True
)