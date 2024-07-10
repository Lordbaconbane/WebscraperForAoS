import pymupdf

order_seraphon_dir = r""

doc = pymupdf.open(order_seraphon_dir)

for page in doc: # iterate the document pages
  text = page.get_text() # get plain text encoded as UTF-8
  
  with open("order_seraphon_output.txt", "a", encoding='utf-8') as output:
    output.write(text)