from datetime import date
import inflect


a = date.fromisoformat("2025-01-01")
b = date.fromisoformat("2026-01-01")
print(b - a)
print((b - a).days)
print(((b - a).days * 24) * 60)
p = inflect.engine()
w = p.number_to_words(525600, andword = "") + " minutes"
print(w.capitalize())