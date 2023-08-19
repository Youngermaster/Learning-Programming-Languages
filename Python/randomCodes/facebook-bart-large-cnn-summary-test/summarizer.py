text = """
Justin Timberlake and Jessica Biel, welcome to parenthood. 
The celebrity couple announced the arrival of their son, Silas Randall Timberlake, in 
statements to People."""

from transformers import pipeline

smr_bart = pipeline(task="summarization", model="facebook/bart-large-cnn")
smbart = smr_bart(text, max_length=150)

print(smbart[0]['summary_text'])
