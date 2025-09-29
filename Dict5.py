reportCard = {
    "Physics":93,
    "Chemistry":96,
    "Math":97,
    "English":79,
    "French":84
}

print("All grades above 90 ?", any(g > 75 for g in reportCard.values()))