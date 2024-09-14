from questgen import main

# Initialize the QGen instance
qg = main.BoolQGen()

# Sample text
context = """
When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously.
“I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to,”
said Thrun, in an interview with Recode earlier this week.
"""

# Define a function to ask questions
def ask_question(question, context):
    payload = {
        "input_text": context,
        "question": question
    }
    response = qg.predict_shortq(payload)
    return response['Answer']

# Ask a question
question = "Who started working on self-driving cars at Google in 2007?"
answer = ask_question(question, context)
print(f"Answer: {answer}")