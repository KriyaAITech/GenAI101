import os
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

def get_gemini_model():
    model = OpenAIModel(
                'gemini-2.0-flash',
                provider=OpenAIProvider(
                    base_url='https://generativelanguage.googleapis.com/v1beta/openai/', api_key=os.getenv("GEMINI_API_KEY")
                ),
            )
    return model

def get_openai_model():
    model = OpenAIModel('gpt-4o')
    return model