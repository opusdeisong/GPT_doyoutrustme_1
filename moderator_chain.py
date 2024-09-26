from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from debate_prompts import create_moderator_prompt

def create_moderator_chain(llm: ChatOpenAI):
    # 프롬프트 템플릿 가져오기
    moderator_prompt = create_moderator_prompt()
    
    # 체인 구성
    chain = (
        moderator_prompt
        | llm
        | StrOutputParser()
    )
    
    return chain

# 사용 예:
# llm = ChatOpenAI(temperature=0.3)
# moderator_chain = create_moderator_chain(llm)
# result = moderator_chain.invoke({
#     "topic": "AI 윤리",
#     "participant1_name": "셜록 홈즈",
#     "participant1_stance": "AI 개발에 대한 엄격한 규제 필요성",
#     "participant2_name": "아이언맨",
#     "participant2_stance": "AI 개발의 자유로운 혁신 필요성",
#     "history": [
#         "셜록 홈즈: AI의 윤리적 사용을 위해서는 엄격한 규제가 필요합니다...",
#         "아이언맨: AI 기술의 발전을 위해서는 자유로운 혁신 환경이 중요합니다...",
#         # ... 더 많은 대화 기록
#     ],
#     "input": "다음 토론 주제나 질문을 제시해주세요."
# })
# print(result)
