from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_debate_prompt() -> ChatPromptTemplate:
    # TODO: 토론 참가자의 발언을 생성하기 위한 ChatPromptTemplate 작성
    # 힌트: MessagesPlaceholder를 사용하여 이전 대화 기록을 포함할 수 있음
    pass

def create_moderator_prompt() -> ChatPromptTemplate:
    # TODO: 진행자의 발언을 생성하기 위한 ChatPromptTemplate 작성
    pass

def create_evaluation_prompt() -> ChatPromptTemplate:
    # TODO: 토론 평가를 위한 ChatPromptTemplate 작성
    pass

# 사용 예:
# debate_prompt = create_debate_prompt()
# moderator_prompt = create_moderator_prompt()
# evaluation_prompt = create_evaluation_prompt()