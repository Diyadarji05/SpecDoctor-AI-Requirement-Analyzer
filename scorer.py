# scorer.py

def calculate_score(ambiguity, missing_constraints, contradictions):
    score = 100

    score -= len(ambiguity) * 10
    if missing_constraints:
        score -= 20
    score -= len(contradictions) * 15

    return max(score, 0)
