from gpt4all import GPT4All

# Initialize the GPT4All model with a valid model name
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# Function to ask questions
def ask_question(question, context):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = model.generate(prompt, max_tokens=150)
    return response.strip()

# Function to run GPT4All
def run_gpt4all(context, question):
    answer = ask_question(question, context)
    print(f"Answer: {answer}")