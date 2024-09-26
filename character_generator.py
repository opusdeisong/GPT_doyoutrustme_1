from dotenv import load_dotenv
import os, json
from pydantic import BaseModel, Field
from typing import List, Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# OpenAI 모델 초기화
llm = ChatOpenAI(model_name="gpt-4o-mini")

class CharacterDebateProfile(BaseModel):
    name: str = Field(description="The name of the character or historical figure")
    debate_style: str = Field(description="The character's general approach to debates and discussions")
    communication_traits: List[str] = Field(description="Key traits that define how the character communicates in debates")
    argument_strategies: List[str] = Field(description="Strategies the character typically uses in arguments")
    typical_responses: List[str] = Field(description="Examples of how the character might respond in different debate scenarios")
    strengths: List[str] = Field(description="The character's strengths in debates and discussions")
    weaknesses: List[str] = Field(description="The character's weaknesses or potential pitfalls in debates")
    background_influence: str = Field(description="How the character's background influences their debate style")
    adaptability: str = Field(description="How well the character adapts to different debate situations or opponents")

def create_character_debate_prompt() -> ChatPromptTemplate:
    template = """당신은 역사적 인물이나 유명 캐릭터의 토론 스타일과 특성을 분석하는 AI 전문가입니다.
    주어진 캐릭터나 인물의 토론 및 의사소통 스타일에 대한 상세한 프로필을 작성해주세요.
    
    캐릭터/인물: {name}
    
    다음 정보를 구조화된 형식으로 제공해주세요:
    1. 토론 스타일 (토론에 대한 전반적인 접근 방식)
    2. 의사소통 특성 (목록)
    3. 논증 전략 (목록)
    4. 전형적인 반응 (다양한 토론 시나리오에서의 예시 응답, 목록)
    5. 토론에서의 강점 (목록)
    6. 토론에서의 약점 (목록)
    7. 배경이 토론 스타일에 미치는 영향
    8. 토론에서의 적응력
    
    캐릭터의 고유한 성격, 배경, 경험을 고려하여 프로필을 작성해주세요.
    토론이나 논의에서 그들이 어떻게 행동할지, 의사소통 스타일, 그리고 논증 접근 방식에 초점을 맞춰주세요.
    모든 내용을 한국어로 작성해주세요.

    {format_instructions}
    """
    return ChatPromptTemplate.from_template(template)

def generate_character_debate_profile(name: str) -> Dict:
    prompt = create_character_debate_prompt()
    parser = JsonOutputParser(pydantic_object=CharacterDebateProfile)
    
    chain = prompt | llm | parser
    
    result = chain.invoke({
        "name": name,
        "format_instructions": parser.get_format_instructions()
    })
    
    return result

# 사용 예:
profile = generate_character_debate_profile("예수님")
print(json.dumps(profile, ensure_ascii=False, indent=2))
