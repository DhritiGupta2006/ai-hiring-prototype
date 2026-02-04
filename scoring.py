def score_resume(keywords: list[str], rubric: dict[str, int]) -> dict:
    score = 0
    matched = {}
    for skill, weight in rubric.items():
        if skill.lower() in keywords:
            score += weight
            matched[skill] = weight
    return {"total_score": score, "matched": matched}
