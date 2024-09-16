def build_question(project_text, data):
    question = (
        f"How does this project: \"{project_text}\" align with these requirements: \"{data}\"? "
        "Explain your decision. With what it aligns, with what not aligns, and how good is the alignment?"
    )
    return question