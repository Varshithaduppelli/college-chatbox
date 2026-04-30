import random

responses = {
    "fee": "Fee is 50,000 per year",
    "exam": "Exams start from May 10",
    "timing": "College timing is 9 AM to 4 PM",
    "hostel": "Hostel facilities available",
    "placement": "Good placement support with training"
}

fallback = [
    "Try asking about fees, exams, hostel",
    "I didn't understand that",
    "Please ask college-related questions"
]

def chatbot_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return responses[key]

    return random.choice(fallback)