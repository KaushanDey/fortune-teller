# fortune.py - Version 1.0

print("🔮 Welcome to Kaushan Dey's Fortune Teller (21JE0460) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Kaushan! Keep smiling. ✨")
elif mood == "sad":
    print("✨ Your fortune: Storms don't last forever. Better days are coming. ✨")
elif mood == "neutral":
    print("✨ Your fortune: Today is a blank slate. Make it count! ✨")
else:
    print("✨ Your fortune: Hmm, that mood is unfamiliar. Expect the unexpected! ✨")