from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from debate_prompts import create_debate_prompt

from dotenv import load_dotenv
import os

load_dotenv()

def create_debate_chain(llm: ChatOpenAI):
    # TODO: create_debate_prompt()를 사용하여 프롬프트 템플릿 가져오기
    # TODO: 프롬프트 템플릿, llm, StrOutputParser를 사용하여 체인 구성
    # TODO: 구성된 체인 반환

    debate_prompt = create_debate_prompt()
    llm = ChatOpenAI(model_name="gpt-4o-mini")
    debate_chain = debate_prompt | llm | StrOutputParser()

    # 실행 예시
    # result = debate_chain.invoke({"character": "노는 걸 제일 좋아하는 뽀로로", "topic": "어린이들의 놀이를 전면 금지 해야 한다.",
    #                               "prev_turns": "어린이들은 곧 시험을 봐야 하므로, 놀이를 금지해야 합니다."})
    
    # print(result)


    return debate_chain

    # pass

# 사용 예:
# llm = ChatOpenAI()
# debate_chain = create_debate_chain(llm)
# result = debate_chain.invoke({"character": "Sherlock Holmes", "topic": "AI ethics", "previous_turns": []})
# result = debate_chain.invoke({"character": "노는 걸 제일 좋아하는 뽀로로", "topic": "어린이들의 놀이를 전면 금지 해야 한다.",
#                                  "prev_turns": "어린이들은 곧 시험을 봐야 하므로, 놀이를 금지해야 합니다."})
# print(result)