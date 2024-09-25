from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def create_blog_prompt() -> ChatPromptTemplate:
    # TODO: 토론 결과를 블로그 글로 변환하기 위한 ChatPromptTemplate 작성
    # 힌트: 토론 주제, 참가자, 주요 논점, 결론 등을 입력으로 받도록 설계
    pass

def debate_to_blog(debate_result: dict, llm: ChatOpenAI) -> str:
    # TODO: create_blog_prompt()를 사용하여 프롬프트 템플릿 가져오기
    # TODO: 프롬프트 템플릿, llm, StrOutputParser를 사용하여 체인 구성
    # TODO: 체인 실행 및 결과 반환
    # 힌트: debate_result에서 필요한 정보를 추출하여 프롬프트에 전달
    pass

# 사용 예:
# llm = ChatOpenAI()
# debate_result = {
#     "topic": "인공지능의 윤리",
#     "participants": ["Alan Turing", "Elon Musk"],
#     "key_points": ["AI의 책임성", "인간의 일자리 대체", "AI 발전의 통제"],
#     "conclusion": "AI 발전은 엄격한 윤리적 가이드라인 하에 진행되어야 한다."
# }
# blog_post = debate_to_blog(debate_result, llm)
# print(blog_post)