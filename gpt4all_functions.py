from gpt4all import GPT4All

# Initialize the GPT4All model with a valid model name
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# Function to chunk text
def chunk_text(text, max_tokens=750):
    words = text.split()
    chunks = [' '.join(words[i:i + max_tokens]) for i in range(0, len(words), max_tokens)]
    return chunks

# Function to ask questions
def ask_question(question, context, log_file):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = model.generate(prompt, max_tokens=500)  # Set max_tokens to 500
    token_count = len(response.split())
    log_file.write(f"Processed tokens: {token_count}\n")  # Log the number of tokens to the file
    print(f"Processed tokens: {token_count}")  # Print the number of tokens to the console
    return response.strip()

# Function to run GPT-4
def run_gpt4all(project_text, data, question, log_file):
    project_chunks = chunk_text(project_text, max_tokens=750)
    data_chunks = chunk_text(data, max_tokens=750)
    
    # Log the number of chunks
    print(f"Project text split into {len(project_chunks)} chunks.")
    print(f"Data split into {len(data_chunks)} chunks.")
    log_file.write(f"Project text split into {len(project_chunks)} chunks.\n")
    log_file.write(f"Data split into {len(data_chunks)} chunks.\n")
    
    answers = []
    for i, project_chunk in enumerate(project_chunks, 1):
        for j, data_chunk in enumerate(data_chunks, 1):
            context = f"Project: {project_chunk}\n\nGrant Requirements: {data_chunk}"
            answer = ask_question(question, context, log_file)
            answers.append(answer)
            
            # Log the current chunk being processed
            print(f"Processing project chunk {i} and data chunk {j}.")
            log_file.write(f"Processing project chunk {i} and data chunk {j}.\n")
    
    return ' '.join(answers)