def generate_report(scoring_result: dict) -> str:
    explanation = []
    for skill, weight in scoring_result["matched"].items():
        explanation.append(f"Matched skill '{skill}' (+{weight} points)")
    if not explanation:
        explanation.append("No rubric skills matched.")
    return "\n".join(explanation)
