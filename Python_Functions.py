def md_input(path: str):
"""blabla Function to replace markdown links with their names in text
:type
""""
  import re
  with open(path, "r") as mf:
    file = mf.readlines()
  return 

def replace_links_with_names(text):
    # Define the regular expression pattern for a Markdown link
    pattern = r'\[([^]]+)\]\(([^)]+)\)'
    if not re.search(pattern, text):
        return text  # Return the original text if no Markdown links are found
      
    # Use re.sub with a custom replacement function
    def replace_link(match):
        link_text = match.group(1)
        return link_text
    # Use re.sub with the custom replacement function to replace links with their names
    replaced_text = re.sub(pattern, replace_link, text)
    
    return replaced_text

def md_input(path):
  :type
  with open(path, "w") as mf:
    mf.write(new_text)



def decrypt_pdfs(paths,PASSLIST)
  """
  from pypdf import PdfWriter, PdfReader
  PASSLIST = input("enter path: ")
  for file in paths:
    file = PdfReader(file)
    if file.isEncrypted:
      content = PdfWriter()
      for i in file.pages:
        content.addpage(i)
      for i in PASSLIST:       
        pass
        with open(file, "wb") as out_stream: pass

main():
  markdown_text = """"""
# Replace links with their names while preserving the text structure
new_text = replace_links_with_names(markdown_text)
with open("bookmarks_strings.md", "w") as mf:
    mf.write(new_text)
