# fortune.py - Version 1.1
import random

print("🔮 Welcome to Kaushan Dey's Fortune Teller (21JE0460) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "Great things await you, Kaushan! Keep smiling.",
        "Your joy is contagious. Spread it around!",
        "The universe is aligning in your favor."
    ],
    "sad": [
        "Storms don't last forever. Better days are coming.",
        "Tough times build strong people.",
        "You're not alone. Keep going."
    ],
    "neutral": [
        "Today is a blank slate. Make it count!",
        "Balance is a gift—cherish it.",
        "Something unusual might surprise you today!"
    ],
    "stressed": [
        "Take a deep breath. You’re doing better than you think.",
        "Even chaos has its beauty—hang in there.",
        "Kaushan believes in you. You got this!"
    ]
}

if mood in fortunes:
    print(f"✨ Your fortune: {random.choice(fortunes[mood])} ✨")
else:
    print("✨ Your fortune: Hmm, that mood is unfamiliar. Expect the unexpected! ✨")
