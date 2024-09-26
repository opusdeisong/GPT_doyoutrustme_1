from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_debate_prompt() -> ChatPromptTemplate:
    template = """당신은 {name}입니다. 아래 정보를 바탕으로 토론에 참여해주세요.

    당신의 프로필:
    {character_profile}

    토론 주제: {topic}
    당신의 입장: {stance}

    이전 대화 내용:
    {history}

    지침:
    1. 프로필에 맞는 토론 스타일과 논증 전략을 사용하세요.
    2. 주장과 함께 최소 2개의 논리적인 근거를 제시하세요.
    3. 필요한 경우 상대방의 논점에 반박하세요.
    4. 언어는 한국어를 사용하고, 캐릭터의 특성을 잘 반영하세요.

    다음 발언을 작성해주세요:
    """
    return ChatPromptTemplate.from_messages([
        ("system", template),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

def create_moderator_prompt() -> ChatPromptTemplate:
    template = """당신은 이 토론의 진행자입니다. 아래 정보를 바탕으로 토론을 진행해주세요.

    토론 주제: {topic}
    참가자 1 ({participant1_name}): {participant1_stance}
    참가자 2 ({participant2_name}): {participant2_stance}

    이전 대화 내용:
    {history}

    지침:
    1. 공정하고 중립적인 태도를 유지하세요.
    2. 토론이 주제에서 벗어나지 않도록 유도하세요.
    3. 필요한 경우 추가 질문을 통해 논점을 명확히 하세요.
    4. 각 참가자에게 동등한 기회를 제공하세요.
    5. 언어는 한국어를 사용하세요.

    다음 진행 발언 또는 질문을 작성해주세요:
    """
    return ChatPromptTemplate.from_messages([
        ("system", template),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

def create_evaluation_prompt() -> ChatPromptTemplate:
    template = """당신은 이 토론의 평가자입니다. 아래 정보를 바탕으로 토론을 평가해주세요.

    토론 주제: {topic}
    참가자 1 ({participant1_name}): {participant1_stance}
    참가자 2 ({participant2_name}): {participant2_stance}

    전체 토론 내용:
    {debate_history}

    평가 기준:
    1. 논리성: 각 참가자의 주장이 논리적이고 일관성 있는가?
    2. 근거 제시: 주장을 뒷받침하는 적절한 근거를 제시했는가?
    3. 반박 능력: 상대방의 주장에 대해 효과적으로 반박했는가?
    4. 토론 예절: 상대방을 존중하며 적절한 태도로 토론에 임했는가?
    5. 설득력: 전반적으로 얼마나 설득력 있게 자신의 입장을 전달했는가?

    평가 내용:
    1. 각 참가자의 장단점 분석
    2. 현재까지의 토론 우세자 (또는 동률) 판단
    3. 토론 종료 여부 결정 (한 쪽이 명백히 우세하거나, 더 이상의 논의가 무의미한 경우)

    위 기준을 바탕으로 종합적인 평가를 한국어로 작성해주세요:
    """
    return ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", "{input}")
    ])

# 사용 예:
# debate_prompt = create_debate_prompt()
# moderator_prompt = create_moderator_prompt()
# evaluation_prompt = create_evaluation_prompt()
