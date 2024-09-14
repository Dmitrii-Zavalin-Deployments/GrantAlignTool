from haystack.nodes import FARMReader, DensePassageRetriever
from haystack.pipelines import ExtractiveQAPipeline
from haystack.document_stores import InMemoryDocumentStore

# Initialize the document store
document_store = InMemoryDocumentStore()

# Sample text
context = """
When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously.
“I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to,”
said Thrun, in an interview with Recode earlier this week.
"""
document_store.write_documents([{"content": context}])

# Initialize retriever and reader
retriever = DensePassageRetriever(document_store=document_store)
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

# Create the pipeline
pipe = ExtractiveQAPipeline(reader, retriever)

# Ask a question
question = "Who started working on self-driving cars at Google in 2007?"
prediction = pipe.run(query=question, params={"Retriever": {"top_k": 20}, "Reader": {"top_k": 10}})

# Print all answers
if prediction['answers']:
    for answer in prediction['answers']:
        print(f"Answer: {answer.answer} (Score: {answer.score})")
else:
    print("No answer found.")