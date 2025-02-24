from collections import Counter

def count_letters(text):
    text = text.lower()
    letter_counts = Counter(c for c in text if c.isalpha())
    return letter_counts

# 測試範例
text = "Hello welcome to Cathay 60th year anniversary"
letter_counts = count_letters(text)
print("字母出現次數:", letter_counts)
