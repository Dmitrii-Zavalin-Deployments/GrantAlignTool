def run_gpt4all(project_text, data, question, log_file):
    # Calculate the number of tokens in the question without project_text and data
    question_without_context = question.replace("{project_text}", "").replace("{data}", "")
    question_tokens = calculate_tokens(question_without_context)
    
    # Reduced chunk size
    max_tokens_per_chunk = 500

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