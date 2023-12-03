import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text, output_file='output.mp3', language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    return output_file

def main(pdf_path):
    text_content = pdf_to_text(pdf_path)
    if text_content:
        output_file = text_to_speech(text_content)
        print(f"Speech generated and saved as {output_file}")
        os.system(f'start {output_file}')  # Open the generated speech file (Windows)
    else:
        print("Failed to extract text from the PDF.")

if __name__ == "__main__":
    pdf_file_path = "lorem-ipsum.pdf"  
    main(pdf_file_path)
