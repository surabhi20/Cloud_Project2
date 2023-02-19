import os
import re
from collections import Counter
import subprocess
import socket

# Define the file paths
data_dir = "/home/data"
result_file = "/home/output/result.txt"

# List the names of all the text files in the directory
file_names = os.listdir(data_dir)
text_files = [f for f in file_names if f.endswith('.txt')]

# Read the two text files and count the total number of words in each file
total_words = 0
if_words = ""
if_word_counts = Counter()
limerick_words = ""
limerick_word_counts = Counter()
for file in text_files:
    file_path = os.path.join(data_dir, file)
    with open(file_path, "r") as f:
        text = f.read()
        words = re.findall(r'\b\w+\b', text)
        word_count = len(words)
        total_words += word_count
        if file == "IF.txt":
            if_words = text
            if_word_counts = Counter(words)
        elif file == "Limerick.txt":
            limerick_words = text
            limerick_word_counts = Counter(words)

# Add all the number of words to find the grand total
grand_total = total_words

# List the top 3 words with maximum number of counts in IF.txt and include the word counts
if_top_words = if_word_counts.most_common(3)

# Find the IP address of the machine
ip_address = socket.gethostbyname(socket.gethostname())
#subprocess.check_output(['hostname','-I']).decode('utf-8').strip()

# Write all the output to the result file
with open(result_file, "w") as f:
    f.write("List of all text files in /home/data:\n")
    for file in text_files:
        f.write(f"- {file}\n")
    f.write("\n")
    f.write(f"Number of words in IF.txt: {len(if_words.split())}\n")
    f.write(f"Number of words in Limerick.txt: {len(limerick_words.split())}\n")
    f.write(f"Grand total number of words: {grand_total}\n")
    f.write("\n")
    f.write("Top 3 words with maximum number of counts in IF.txt:\n")
    for word, count in if_top_words:
        f.write(f"- {word}: {count}\n")
    f.write("\n")
    f.write(f"IP address of the machine: {ip_address}\n")

# Print the contents of the result file to the console
with open(result_file, "r") as f:
    print(f.read())

