
import streamlit as st

import g4f

from g4f.Provider import (
    GptGo
)

st.title("🎮 Gaming Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Welcome to the Gaming Chatbot!"}]

    st.write(
        'Ask me about video games! I can also recommend games to you. Try asking me "Mario Wonder Reviews" or "What is the best game?"'
    )

    st.write(
        '- Write `help` to see a list of commands'
    )

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt == 'help':
        st.write(
            """
            - Recommend me a game!
            - What is the best game?
            - Tell me more about [specific game title].
            - What are the top-rated RPG games?
            - Find me a game for Nintendo Switch.
            - I like action-adventure games, what do you recommend?
            - Show me user reviews for [game title].
            - What's the latest news in the gaming industry?
            - How can I start a career in game development?
            - I'm having trouble running [game title], can you help?
            """
        )
    else:
        st.chat_message("user").write(prompt)

        lastMessages = st.session_state.messages[-2:]

        if len(lastMessages) == 0:
            lastMessages = [{"role": "user", "content": " "}]

        # Set with provider
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=g4f.Provider.GptGo,
            messages=[
                {'role': 'system', 'content': 'You are a gamer.'},
                {'role': 'system', 'content': 'Your job is to chat to people about video games. You can also recommend games to people.'},
            ] + lastMessages + [{"role": "user", "content": prompt}]
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": response})

        st.chat_message("assistant").write(response)
