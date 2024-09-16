def build_questions(project_text, data):
    base_info = f"This is the project: \"{project_text}\". These are the grant requirements: \"{data}\"."
    
    questions = [
        f"{base_info} How does this project align with these grant requirements? Explain your decision.",
        f"{base_info} With what aspects of the grant requirements does this project align?",
        f"{base_info} With what aspects of the grant requirements does this project not align?",
        f"{base_info} How good is the overall alignment of this project with the grant requirements?",
        f"{base_info} What percentage does this project align with these grant requirements?",
        f"{base_info} What should be added to this project description to maximize alignment with the grant requirements without making major changes? Provide the updated project description.",
        f"{base_info} What is the percentage of alignment of the updated project description with the grant requirements?",
        f"{base_info} Is it worth spending time to prepare the grant application for this grant for both the original and updated project descriptions, or is it better to skip this grant?"
    ]
    
    return questions