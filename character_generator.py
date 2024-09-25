from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def create_character_prompt() -> ChatPromptTemplate:
    # TODO: 캐릭터 프로필 생성을 위한 ChatPromptTemplate 작성
    pass

def generate_character_profile(name: str, llm: ChatOpenAI) -> dict:
    # TODO: create_character_prompt()를 사용하여 프롬프트 템플릿 가져오기
    # TODO: 프롬프트 템플릿, llm, StrOutputParser를 사용하여 체인 구성
    # TODO: 체인 실행 및 결과 반환
    pass

# 사용 예:
# llm = ChatOpenAI()
# profile = generate_character_profile("Sherlock Holmes", llm)
# print(profile)