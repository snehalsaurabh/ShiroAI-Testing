import PyPDF2

reader = PyPDF2.PdfReader("national income.pdf")
text = "\n".join(page.extract_text() for page in reader.pages)

lines = text.splitlines()
output = []
for line in lines:
    line = line.strip()
    if line.startswith("Question"):
        output.append(line)  # keep question
    elif line.startswith("Option"):
        output.append(line)  # keep options
# write to a new text file
with open("questions_only.txt", "w") as f:
    f.write("\n".join(output))



