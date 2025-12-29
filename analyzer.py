# analyzer.py
import re

AMBIGUOUS_WORDS = [
    "fast", "efficient", "user-friendly", "easy",
    "quick", "secure", "scalable", "optimal"
]

def detect_ambiguity(text):
    found = []
    for word in AMBIGUOUS_WORDS:
        if re.search(rf"\b{word}\b", text.lower()):
            found.append(word)
    return found


def detect_missing_constraints(text):
    keywords = ["within", "seconds", "ms", "users", "limit", "%"]
    found = any(k in text.lower() for k in keywords)
    return not found


def detect_contradictions(text):
    lines = text.split(".")
    contradictions = []

    for line in lines:
        if "must" in line.lower() and "optional" in line.lower():
            contradictions.append(line.strip())

    return contradictions
