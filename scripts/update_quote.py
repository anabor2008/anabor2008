import json
import random

# Load quotes
with open("quotes.json", "r") as file:
    quotes = json.load(file)

# Pick random quote
quote = random.choice(quotes)

new_quote = f'> "{quote["quote"]}"\n>\n> — {quote["author"]}'

# Update README
with open("README.md", "r") as file:
    readme = file.read()

start = "<!-- QUOTE_START -->"
end = "<!-- QUOTE_END -->"

before = readme.split(start)[0]
after = readme.split(end)[1]

updated = (
    before
    + start
    + "\n"
    + new_quote
    + "\n"
    + end
    + after
)

with open("README.md", "w") as file:
    file.write(updated)
