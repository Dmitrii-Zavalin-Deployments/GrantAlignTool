from transformers import GPT2Tokenizer
from gpt4all import GPT4All

# Initialize the GPT-4All model with a valid model name
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# Initialize the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Function to calculate the number of tokens
def calculate_tokens(text):
    tokens = tokenizer.encode(text)
    return len(tokens)

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
    # Calculate the number of tokens in the question without project_text and data
    question_without_context = question.replace("{project_text}", "").replace("{data}", "")
    question_tokens = calculate_tokens(question_without_context)
    
    # Fixed chunk size
    max_tokens_per_chunk = 750

    # Debugging: Print lengths and max_tokens_per_chunk
    project_text_tokens = calculate_tokens(project_text)
    data_tokens = calculate_tokens(data)
    print(f"Length of project_text: {project_text_tokens} tokens")
    print(f"Length of data: {data_tokens} tokens")
    print(f"Max tokens per chunk: {max_tokens_per_chunk}")
    log_file.write(f"Length of project_text: {project_text_tokens} tokens\n")
    log_file.write(f"Length of data: {data_tokens} tokens\n")
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
            context_tokens = calculate_tokens(context)
            total_tokens = context_tokens + question_tokens + 500  # Including the response tokens
            
            # Debugging: Print the total tokens for the current prompt
            print(f"Total tokens for project chunk {i} and data chunk {j}: {total_tokens}")
            log_file.write(f"Total tokens for project chunk {i} and data chunk {j}: {total_tokens}\n")
            
            if total_tokens > 2048:
                print(f"Skipping project chunk {i} and data chunk {j} due to token limit.")
                log_file.write(f"Skipping project chunk {i} and data chunk {j} due to token limit.\n")
                continue
            
            answer = ask_question(question, context, log_file)
            answers.append(answer)
            
            # Log the current chunk being processed
            print(f"Processing project chunk {i} and data chunk {j}.")
            log_file.write(f"Processing project chunk {i} and data chunk {j}.\n")
    
    return ' '.join(answers)