import re
# Function to replace markdown links with their names in text
def md_input(path: str):
"""blabla docstring
:type
""""
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
main():
  markdown_text = """"""

# Replace links with their names while preserving the text structure
new_text = replace_links_with_names(markdown_text)
with open("bookmarks_strings.md", "w") as mf:
    mf.write(new_text)
