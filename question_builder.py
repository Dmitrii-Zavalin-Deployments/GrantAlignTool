def build_question(project_text, data):
    question = (
        f"How does this project: \"{project_text}\" align with these grant requirements: \"{data}\"? "
        "Explain your decision. With what it aligns, with what not aligns, and how good is the alignment? "
        "1. What percentage does this project align with these grant requirements? "
        "2. What should be added to this project description to maximize alignment with the grant requirements without making major changes? Provide the updated project description. "
        "3. What is the percentage of alignment of the updated project description with the grant requirements? "
        "4. Is it worth spending time to prepare the grant application for this grant for both the original and updated project descriptions, or is it better to skip this grant?"
    )
    return question