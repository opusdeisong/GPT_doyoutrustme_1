from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def create_character_prompt() -> ChatPromptTemplate:
    template = """We are going to make Character Profile. The Name of this character is {name}. 
    Please provide the following information in a structured format:
    
    1. Name: {name}
    2. Background: A brief history of the character.
    3. Personality: Key personality traits of the character.
    4. Debate Style: How the character approaches debates and arguments.
    5. Strengths: List exactly 3 strengths of the character.
    6. Weaknesses: List exactly 3 weaknesses of the character.
    
    If this Character doesn't exist as real character or animation character, then creatively make new virtual character.
    the output form "must" be json dictionary as below
    {{
      "name": str,
      "background": str,
      "personality": str,
      "debate_style": str,
      "strengths": List[str],
      "weaknesses": List[str]
    }}
    """
    return ChatPromptTemplate.from_template(template)
    # TODO: 캐릭터 프로필 생성을 위한 ChatPromptTemplate 작성

def generate_character_profile(name: str, llm: ChatOpenAI) -> dict:
    prompt = create_character_prompt()
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"name": name})
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        print("Error: Invalid JSON response")
        return {}
    # TODO: create_character_prompt()를 사용하여 프롬프트 템플릿 가져오기
    # TODO: 프롬프트 템플릿, llm, StrOutputParser를 사용하여 체인 구성
    # TODO: 체인 실행 및 결과 반환

# 사용 예:
# llm = ChatOpenAI()
# profile = generate_character_profile("Sherlock Holmes", llm)
# print(profile)


if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    import json

    load_dotenv()
    llm = ChatOpenAI()
    
    character = input()
    profile = generate_character_profile(character, llm)
    
    if profile:
        print(json.dumps(profile, indent=2))
    else:
        print("Failed to generate a valid character profile.")