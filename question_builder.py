import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def build_questions(project_text, data):
    sentences = sent_tokenize(data)
    questions = []

    for sentence in sentences:
        questions.extend([
            f"How does the project \"{project_text}\" meet the grant requirements \"{sentence}\"? Explain your decision.",
            f"What aspects of the project \"{project_text}\" fulfill the grant requirements \"{sentence}\"?",
            f"What aspects of the project \"{project_text}\" fail to meet the grant requirements \"{sentence}\"?",
            f"How well does the project \"{project_text}\" match the grant requirements \"{sentence}\" overall?",
            f"What percentage does the project \"{project_text}\" meet the grant requirements \"{sentence}\"?",
            f"What should be added to the project \"{project_text}\" to maximize its match with the grant requirements \"{sentence}\" without making major changes? Provide the updated project description.",
            f"What is the percentage of match of the updated project description with the grant requirements \"{sentence}\"?",
            f"What are the risky points in these grant requirements: \"{sentence}\"?"
        ])
    
    return questions