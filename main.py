file_contents=None

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
num_of_words=len(file_contents.split())
lowed=file_contents.lower()
letter_dict={}
for i in lowed:
    if i not in letter_dict:
        letter_dict[i]=1
    else:
        letter_dict[i] += 1
report = list(letter_dict.items())
sorted_report=sorted(report, key=lambda x:x[1])
sorted_report.reverse()
for i in sorted_report:
    if i[0].isalpha():
        print(f"The '{i[0]}' character was found {i[1]} times")
