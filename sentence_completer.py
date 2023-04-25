#IMPORTS
import openai
import streamlit as st

# set OpenAI API key
openai.api_key = "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"

# function to generate text
def generate_text(prompt):
    model_engine = "text-davinci-003"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=15,
        n=1,
        stop=None,
        temperature=1,
    )
    completed_sentence = response.choices[0].text.strip()
    return completed_sentence

# main function
def main():
    # set app title
    st.title("OpenAI Text Generator")

    # get user input
    st.write("Enter an incomplete sentence and the AI will finish it for you:")
    prompt = st.text_input("Enter a prompt")

    # generate text when user submits prompt
    if st.button("Generate"):
        if prompt:
            completed_sentence = generate_text(prompt)
            st.write(prompt + completed_sentence)
# run app
if __name__ == "__main__":
    main()
