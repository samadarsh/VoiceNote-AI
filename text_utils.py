import json
from typing import Any


def extract_json(content: str) -> dict[str, Any]:
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        start = content.find("{")
        end = content.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise
        return json.loads(content[start : end + 1])


def contains_indic_text(text: str) -> bool:
    return any(
        "\u0900" <= char <= "\u097f"
        or "\u0980" <= char <= "\u09ff"
        or "\u0a00" <= char <= "\u0a7f"
        or "\u0a80" <= char <= "\u0aff"
        or "\u0b00" <= char <= "\u0b7f"
        or "\u0b80" <= char <= "\u0bff"
        or "\u0c00" <= char <= "\u0c7f"
        or "\u0c80" <= char <= "\u0cff"
        or "\u0d00" <= char <= "\u0d7f"
        for char in text
    )


def normalize_tanglish(transcript: str) -> str:
    replacements = {
        "நீரஸ்தா": "nearby",
        "நியர்ஸ்தா": "nearby",
        "நியராச்சியாக": "near-ah",
        "நியர்": "near",
        "பஜ்செட்": "budget",
        "பட்ஜெட்": "budget",
        "ஃபிரிண்ட் லியர்": "friendly",
        "ஃபிரெண்ட்லி": "friendly",
        "பிரெண்ட்லி": "friendly",
        "ஐஸ்க்ரிம் சாப்பிட்டு": "ice cream shop",
        "ஐஸ்க்ரிம் ஷாப்": "ice cream shop",
        "ஐஸ்கிரீம் ஷாப்": "ice cream shop",
        "ஐஸ்க்ரீம் ஷாப்": "ice cream shop",
    }

    normalized = transcript
    for source, target in replacements.items():
        normalized = normalized.replace(source, target)
    normalized = normalized.replace("budget friendly", "budget-friendly")
    normalized = normalized.replace("budget-friendly", "budget-friendly")
    return normalized
