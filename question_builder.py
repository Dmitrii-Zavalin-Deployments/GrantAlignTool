def build_questions(project_text, data):
    questions = [
        f"How does the project \"{project_text}\" meet the grant requirements \"{data}\"? Explain your decision.",
        f"What aspects of the project \"{project_text}\" fulfill the grant requirements \"{data}\"?",
        f"What aspects of the project \"{project_text}\" fail to meet the grant requirements \"{data}\"?",
        f"How well does the project \"{project_text}\" match the grant requirements \"{data}\" overall?",
        f"What percentage does the project \"{project_text}\" meet the grant requirements \"{data}\"?",
        f"What should be added to the project \"{project_text}\" to maximize its match with the grant requirements \"{data}\" without making major changes? Provide the updated project description.",
        f"What is the percentage of match of the updated project description with the grant requirements \"{data}\"?",
        f"Is it worth spending time to prepare the grant application for the project \"{project_text}\" for both the original and updated descriptions, or is it better to skip this grant?"
    ]
    
    return questions