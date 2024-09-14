from gpt4all import GPT4All

# Initialize the GPT4All model
model = GPT4All("gpt4all-lora-quantized")

# Sample text
context = """
The Northern Lights, also known as the Aurora Borealis, are a natural light display predominantly seen in high-latitude regions around the Arctic. 
They are caused by the collision of energetic charged particles with atoms in the high-altitude atmosphere. 
These particles originate from the magnetosphere and solar wind and are directed by the Earth's magnetic field into the atmosphere.
"""

# Define a function to ask questions
def ask_question(question, context):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = model.generate(prompt, max_tokens=150)
    return response.strip()

# Ask a question
question = "What causes the Northern Lights?"
answer = ask_question(question, context)
print(f"Answer: {answer}")