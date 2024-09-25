from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from debate_prompts import create_moderator_prompt

def create_moderator_chain(llm: ChatOpenAI):
    # TODO: create_moderator_prompt()를 사용하여 프롬프트 템플릿 가져오기
    # TODO: 프롬프트 템플릿, llm, StrOutputParser를 사용하여 체인 구성
    # TODO: 구성된 체인 반환
    pass

# 사용 예:
# llm = ChatOpenAI()
# moderator_chain = create_moderator_chain(llm)
# result = moderator_chain.invoke({"topic": "AI ethics", "debate_history": []})
# print(result)