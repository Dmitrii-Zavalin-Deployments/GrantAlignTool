from gpt4all import GPT4All

# Initialize the GPT4All model with a valid model name
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# Function to chunk text
def chunk_text(text, max_tokens):
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
    # Estimate the number of tokens used by the question
    question_tokens = len(question.split())
    # Reserve 500 tokens for the model's response
    reserved_tokens = 500
    # Calculate the maximum tokens available for each chunk
    max_tokens_per_chunk = (2048 - question_tokens - reserved_tokens) // 2

    # Debugging: Print lengths and max_tokens_per_chunk
    print(f"Length of project_text: {len(project_text.split())} tokens")
    print(f"Length of data: {len(data.split())} tokens")
    print(f"Max tokens per chunk: {max_tokens_per_chunk}")
    log_file.write(f"Length of project_text: {len(project_text.split())} tokens\n")
    log_file.write(f"Length of data: {len(data.split())} tokens\n")
    log_file.write(f"Max tokens per chunk: {max_tokens_per_chunk}\n")

    project_chunks = chunk_text(project_text, max_tokens=max_tokens_per_chunk)
    data_chunks = chunk_text(data, max_tokens=max_tokens_per_chunk)
    
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