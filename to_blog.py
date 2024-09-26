from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def create_blog_prompt() -> ChatPromptTemplate:
    template = """
    당신은 AI 토론을 블로그 포스트로 변환하는 전문 작가입니다. 
    다음 정보를 바탕으로 흥미롭고 정보가 풍부한 블로그 포스트를 작성해주세요.

    토론 주제: {topic}
    참가자: {participants}
    주요 논점:
    {key_points}

    토론 내용:
    {debate_content}

    결론: {conclusion}

    블로그 포스트 작성 지침:
    1. 흥미로운 제목으로 시작하세요.
    2. 토론 주제와 참가자를 소개하는 간단한 서론을 작성하세요.
    3. 주요 논점을 중심으로 토론 내용을 요약하세요. 각 참가자의 주장과 근거를 균형있게 다루세요.
    4. 토론 중 가장 흥미로웠거나 논쟁적이었던 부분을 강조하세요.
    5. 결론을 요약하고, 토론이 어떤 의미를 가지는지 설명하세요.
    6. 독자들이 더 생각해볼 만한 질문으로 글을 마무리하세요.

    모든 내용을 한국어로 작성해주세요.
    """
    return ChatPromptTemplate.from_template(template)

def debate_to_blog(debate_result: dict, llm: ChatOpenAI) -> str:
    # 프롬프트 템플릿 가져오기
    blog_prompt = create_blog_prompt()
    
    # 체인 구성
    chain = blog_prompt | llm | StrOutputParser()
    
    # debate_result에서 필요한 정보 추출
    topic = debate_result["topic"]
    participants = ", ".join(debate_result["participants"])
    key_points = "\n".join([f"- {point}" for point in debate_result["key_points"]])
    debate_content = debate_result.get("debate_content", "상세한 토론 내용이 제공되지 않았습니다.")
    conclusion = debate_result["conclusion"]
    
    # 체인 실행 및 결과 반환
    blog_post = chain.invoke({
        "topic": topic,
        "participants": participants,
        "key_points": key_points,
        "debate_content": debate_content,
        "conclusion": conclusion
    })
    
    return blog_post

# 사용 예:
# llm = ChatOpenAI(temperature=0.7)
# debate_result = {
#     "topic": "인공지능의 윤리",
#     "participants": ["Alan Turing", "Elon Musk"],
#     "key_points": ["AI의 책임성", "인간의 일자리 대체", "AI 발전의 통제"],
#     "debate_content": "Alan Turing: AI의 발전은 불가피하지만, 엄격한 윤리적 기준이 필요합니다...\nElon Musk: AI는 인류의 발전을 위한 도구이며, 과도한 규제는 혁신을 저해할 수 있습니다...",
#     "conclusion": "AI 발전은 엄격한 윤리적 가이드라인 하에 진행되어야 한다."
# }
# blog_post = debate_to_blog(debate_result, llm)
# print(blog_post)
