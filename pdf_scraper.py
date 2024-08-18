
import pymupdf
import requests

r = requests.get('https://www.warhammer-community.com/wp-content/uploads/2024/07/FcGNwRXuuaZBJLye.pdf')
data = r.content
doc = pymupdf.Document(stream=data)

keywords = ["order", "infantry", "hero", "cavalry", "monster", "warmaster", "unique", "beast"]
filtered_words = []

with open("order_seraphon_output.txt", "w", encoding='utf-8') as output:
  num = 0
  for page in doc:
    num = num +1
    # print(page.number)
    if page.number >5:
      text = page.get_text()
      lines = text.splitlines()
      bottom_lines = lines[-3:]
      for line in bottom_lines:
        line = line.lower()
        print(line)
        for keyword in keywords:
          if keyword in line:
            filtered_words.append(line)
          
  
  for word in filtered_words:
    output.write(word + "\n")    