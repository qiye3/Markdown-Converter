import re

def convert_md_to_anki(md_content):
    # Convert bold text from **text** to <b>text</b>
    anki_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', md_content)
    
    # Convert block math from $$formula$$ to \[formula\]
    anki_content = re.sub(r'\$\$(.*?)\$\$', r'\\[\1\\]', anki_content, flags=re.DOTALL)
    
    # Convert inline math from $formula$ to \(formula\)
    anki_content = re.sub(r'\$(.*?)\$', r'\\(\1\\)', anki_content)
    
    return anki_content
