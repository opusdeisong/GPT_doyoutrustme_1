import random
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from character_generator import generate_character_profile
from debate_chain import create_debate_chain
from moderator_chain import create_moderator_chain
from evaluation_chain import create_evaluation_chain
from to_blog import debate_to_blog

def simulate_debate(topic: str, character1_name: str, character2_name: str, llm: ChatOpenAI):
    # Generate profiles for both characters
    char1_profile = generate_character_profile(character1_name)
    char2_profile = generate_character_profile(character2_name)
    
    # Create necessary chains
    debate_chain = create_debate_chain(llm)
    moderator_chain = create_moderator_chain(llm)
    evaluation_chain = create_evaluation_chain(llm)
    
    # Randomly assign stances
    stances = random.sample(["for", "against"], 2)
    char1_stance, char2_stance = stances
    
    print(f"\n{character1_name}'s stance: {char1_stance}")
    print(f"{character2_name}'s stance: {char2_stance}\n")
    
    debate_history = []
    round_num = 1
    max_rounds = 10

    while round_num <= max_rounds:
        print(f"\n--- Round {round_num} ---\n")
        
        # Moderator turn
        moderator_input = {
            "topic": topic,
            "participant1_name": character1_name,
            "participant1_stance": char1_stance,
            "participant2_name": character2_name,
            "participant2_stance": char2_stance,
            "history": debate_history,
            "input": "다음 토론 주제나 질문을 제시해주세요."
        }
        moderator_turn = moderator_chain.invoke(moderator_input)
        debate_history.append({"speaker": "Moderator", "content": moderator_turn})
        print(f"Moderator: {moderator_turn}")
        print("\n" + "="*50 + "\n")
        
        # Character 1 turn
        char1_input = {
            "name": character1_name,
            "character_profile": char1_profile,
            "topic": topic,
            "stance": char1_stance,
            "history": debate_history,
            "input": moderator_turn
        }
        char1_turn = debate_chain.invoke(char1_input)
        debate_history.append({"speaker": character1_name, "content": char1_turn})
        print(f"{character1_name}: {char1_turn}")
        print("\n" + "="*50 + "\n")
        
        # Character 2 turn
        char2_input = {
            "name": character2_name,
            "character_profile": char2_profile,
            "topic": topic,
            "stance": char2_stance,
            "history": debate_history,
            "input": moderator_turn
        }
        char2_turn = debate_chain.invoke(char2_input)
        debate_history.append({"speaker": character2_name, "content": char2_turn})
        print(f"{character2_name}: {char2_turn}")
        print("\n" + "="*50 + "\n")
        
        # Evaluate debate
        evaluation_input = {
            "topic": topic,
            "participant1_name": character1_name,
            "participant1_stance": char1_stance,
            "participant2_name": character2_name,
            "participant2_stance": char2_stance,
            "debate_history": debate_history,
            "input": "지금까지의 토론을 평가해주세요."
        }
        evaluation = evaluation_chain.invoke(evaluation_input)
        print("Evaluation:", evaluation)
        print("\n" + "="*50 + "\n")
        
        # Check if debate should be concluded
        if "is_finished" in evaluation and evaluation["is_finished"]:
            break
        
        round_num += 1
    
    # Convert debate to blog post
    blog_post = debate_to_blog(topic, character1_name, character2_name, debate_history, evaluation)
    print("Blog Post:")
    print(blog_post)

# 사용 예:
# llm = ChatOpenAI()
# simulate_debate("인공지능의 윤리", "Alan Turing", "Elon Musk", llm)
