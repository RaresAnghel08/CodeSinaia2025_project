import re
from responses import get_custom_response, unknown


RULES = [
    {
        "keywords": ["hello", "hi", "hey", "salut"],
        "response": "Hello! 😊",
        "single_response": True
    },
    {
        "keywords": ["how", "are", "you", "doing"],
        "required": ["how"],
        "response": "I'm doing fine, and you?"
    },
    {
        "keywords": ["what", "is", "your", "name"],
        "required": ["name"],
        "response": "I'm CodePal, your friendly chatbot 🤖"
    },
    {
        "keywords": ["i", "love", "code", "palace"],
        "required": ["code", "palace"],
        "response": "Thank you! ❤️"
    },
    {
        "keywords": ["what", "you", "eat", "like"],
        "required": ["eat"],
        "response": get_custom_response("eat")
    }
]

def message_probability(user_message, keywords, single_response=False, required=[]):
    message_certainty = sum(1 for word in user_message if word in keywords)
    match_ratio = message_certainty / len(keywords)

    if required:
        if not all(word in user_message for word in required):
            return 0

    return int(match_ratio * 100) if match_ratio > 0 else 0 if not single_response else 1

def check_all_messages(message):
    highest_prob = 0
    best_response = None

    for rule in RULES:
        prob = message_probability(
            message,
            rule["keywords"],
            rule.get("single_response", False),
            rule.get("required", [])
        )

        if prob > highest_prob:
            highest_prob = prob
            best_response = rule["response"]

    return best_response if highest_prob > 0 else unknown()

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?.-]\s*', user_input.lower())
    return check_all_messages(split_message)
