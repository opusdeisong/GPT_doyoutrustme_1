from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from debate_prompts import create_debate_prompt

def create_debate_chain(llm: ChatOpenAI):
    # TODO: create_debate_prompt()를 사용하여 프롬프트 템플릿 가져오기
    # TODO: 프롬프트 템플릿, llm, StrOutputParser를 사용하여 체인 구성
    # TODO: 구성된 체인 반환
    pass

# 사용 예:
# llm = ChatOpenAI()
# debate_chain = create_debate_chain(llm)
# result = debate_chain.invoke({"character": "Sherlock Holmes", "topic": "AI ethics", "previous_turns": []})
# print(result)