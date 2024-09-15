from gpt4all import GPT4All

# Initialize the GPT4All model with a valid model name
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# Function to ask questions
def ask_question(question, context, log_file):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = model.generate(prompt, max_tokens=500)  # Set max_tokens to 500
    token_count = len(response.split())
    log_file.write(f"Processed tokens: {token_count}\n")  # Log the number of tokens to the file
    print(f"Processed tokens: {token_count}")  # Print the number of tokens to the console
    return response.strip()

# Function to run GPT4All
def run_gpt4all(context, question, log_file):
    answer = ask_question(question, context, log_file)
    return answer