from gpt4all import GPT4All

# Initialize the GPT-4All model with a valid model name
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# Function to ask questions
def ask_question(question, context, log_file):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = model.generate(prompt, max_tokens=500)  # Set max_tokens to 500
    token_count = len(response.split())
    log_file.write(f"Processed tokens: {token_count}\n")  # Log the number of tokens to the file
    print(f"Processed tokens: {token_count}")  # Print the number of tokens to the console
    return response.strip()

# Function to split text into paragraphs
def split_into_paragraphs(text):
    paragraphs = text.split('\n\n')
    return [p for p in paragraphs if p.strip()]

# Function to run GPT-4
def run_gpt4all(project_text, data, question, log_file):
    # Split text into paragraphs
    project_paragraphs = split_into_paragraphs(project_text)
    data_paragraphs = split_into_paragraphs(data)
    
    # Log the number of paragraphs
    print(f"Project text split into {len(project_paragraphs)} paragraphs.")
    print(f"Data split into {len(data_paragraphs)} paragraphs.")
    log_file.write(f"Project text split into {len(project_paragraphs)} paragraphs.\n")
    log_file.write(f"Data split into {len(data_paragraphs)} paragraphs.\n")
    
    answers = []
    for i, project_paragraph in enumerate(project_paragraphs, 1):
        for j, data_paragraph in enumerate(data_paragraphs, 1):
            context = f"Project: {project_paragraph}\n\nGrant Requirements: {data_paragraph}"
            answer = ask_question(question, context, log_file)
            answers.append(answer)
            
            # Log the current paragraph being processed
            print(f"Processing project paragraph {i} and data paragraph {j}.")
            log_file.write(f"Processing project paragraph {i} and data paragraph {j}.\n")
    
    return ' '.join(answers)
