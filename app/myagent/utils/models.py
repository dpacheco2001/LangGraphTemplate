#make sure you have your api keys in the .env file.
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
load_dotenv()

class Models:
    @classmethod
    def get_model(self,model_name,temperature=0,max_tokens=None,timeout=None,max_retries=None):
        deepseek_v3= ChatDeepSeek(
            model="deepseek-chat",
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
            max_retries=max_retries
        )
        deepseek_r1 = ChatDeepSeek(
            model="deepseek-reasoner",
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
            max_retries=max_retries
        )

        gpt4omini = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
            max_retries=max_retries
        )

        gpt4o = ChatOpenAI(
            model="gpt-4o",
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
            max_retries=max_retries
        )

        available_models = {
            "deepseek-chat": deepseek_v3,
            "deepseek-reasoner": deepseek_r1,
            "gpt-4o-mini": gpt4omini,
            "gpt-4o": gpt4o,
        }

        return available_models[model_name]







