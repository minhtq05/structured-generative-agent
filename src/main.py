import time
import streamlit as st
from agent import AIAgent

def main():
    st.title("Structured Generative Agent")
    
    # Initialize chat history in session state if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Initialize AI agent
    if "agent" not in st.session_state:
        st.session_state.agent = AIAgent()
    
    # Chat input for user
    if prompt := st.chat_input("What would you like to know?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # TODO: remove timeout placeholder
                time.sleep(1)
                response = st.session_state.agent.generate_response(prompt)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()