import streamlit as st
from typing import List
from nltk.tokenize import sent_tokenize
from app.mcq_generation import MCQGenerator
from app.models.question import Question

def main():
    st.title("MCQ Generation Tool")

    context = st.text_area("Enter the context:")
    desired_count = st.number_input("Enter the number of questions to generate:", min_value=1, step=1, value=1)

    if st.button("Generate MCQs"):
        mcq_generator = MCQGenerator()
        questions = mcq_generator.generate_mcq_questions(context, desired_count)
        
        st.write(f"Generated {len(questions)} MCQ(s):")
        for i, question in enumerate(questions, start=1):
            show_question(f"Question {i}", question)


def show_question(title: str, question: Question):
    st.subheader(title)
    st.write(question.questionText)
    st.write("Options:")
    for option in question.distractors:
        st.write(option)


if __name__ == "__main__":
    main()
