from pypdf import PdfReader
import os

folder = "documents"

for file in os.listdir(folder):
    if file.endswith(".pdf"):
        path = os.path.join(folder, file)

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

        print("\n" + "="*50)
        print(file)
        print("="*50)

        print(text[:1000])