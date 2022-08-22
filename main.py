# import spacy
# from PyPDF2 import PdfReader


# nlp = spacy.blank("en")

# # text = "warner@yahoo.com this is the begining of a new claceey@gmail.com  dawn twenty."
# # doc = npl(text)
# email = []





# def getTextFromFile (file_name):
#     texts = []
#     reader = PdfReader(file_name)
#     number_of_pages = len(reader.pages)

#     for page in range(number_of_pages):
#         # text = page.extract_text()
#         text = reader.pages[page].extract_text()
#         texts.append(text)
    
#     texts = " ".join(texts)
#     return texts

# text = getTextFromFile("sample_file2.docx")
# doc = nlp(text)

# for token in doc:
#     if token.like_num:
#         email.append(token.text)
    
# print(email)

# .pdf
# .docx
# .doc
# .txt

with open ('sample_file.txt', 'r') as file:
    print(file.read())