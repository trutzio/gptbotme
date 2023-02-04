import os

import openai


class OpenAIService():

    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def answer(self, prompt: str) -> str:
        # see also https://platform.openai.com/docs/api-reference/completions
        text_completion = openai.Completion.create(
            model="text-davinci-003", prompt=prompt, temperature=0.6, max_tokens=self.max_tokens(prompt))
        answer = text_completion.get('choices')[0].get('text').strip()
        return answer

    def max_tokens(self, prompt: str) -> int:
        # count words in string
        word_count = len(prompt.split())
        # text-davinci-003 has maximal 4*1024 tokens, 1024 are set aside as reserves
        # see also https://platform.openai.com/tokenizer
        max_tokens = 3*1024 - word_count * 2
        return max_tokens
