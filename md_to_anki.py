import re
import argparse

def convert_md_to_anki(md_content):
    # Convert bold text from **text** to <b>text</b>
    anki_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', md_content)
    
    # Convert inline math from $formula$ to \[formula\]
    anki_content = re.sub(r'\$(.*?)\$', r'\\(\1\\)', anki_content)
    
    # Convert block math from $$formula$$ to \[formula\]
    anki_content = re.sub(r'\$\$(.*?)\$\$', r'\\[\1\\]', anki_content, flags=re.DOTALL)
    
    return anki_content

def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_txt_file(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def convert_md_file_to_anki(md_file_path, txt_file_path):
    md_content = read_md_file(md_file_path)
    anki_content = convert_md_to_anki(md_content)
    write_txt_file(anki_content, txt_file_path)

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown file to Anki format')
    parser.add_argument('input', help='Path to the input Markdown file')
    parser.add_argument('output', help='Path to the output text file')

    args = parser.parse_args()

    convert_md_file_to_anki(args.input, args.output)

if __name__ == '__main__':
    main()
