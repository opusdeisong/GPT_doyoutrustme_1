from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from debate_prompts import create_debate_prompt

def create_debate_chain(llm: ChatOpenAI):
    # 프롬프트 템플릿 가져오기
    debate_prompt = create_debate_prompt()
    
    # 체인 구성
    chain = (
        debate_prompt
        | llm
        | StrOutputParser()
    )
    
    return chain

# 사용 예:
# llm = ChatOpenAI(temperature=0.7)
# debate_chain = create_debate_chain(llm)
# result = debate_chain.invoke({
#     "name": "셜록 홈즈",
#     "character_profile": "논리적이고 관찰력이 뛰어난 탐정",
#     "topic": "AI 윤리",
#     "stance": "AI 개발에 대한 엄격한 규제 필요성",
#     "history": [],
#     "input": "AI 윤리에 대한 당신의 견해를 말씀해 주세요."
# })
# print(result)
