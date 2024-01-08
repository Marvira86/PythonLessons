import string

# Given text
original_text = """
homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Task 1: Normalize text from letter cases point of view
normalized_text = original_text.capitalize()

# Task 2: Create one more sentence with last words of each existing sentence
sentences = normalized_text.split('.')
last_words = [sentence.split()[-1] for sentence in sentences if sentence.strip()]
additional_sentence = ' '.join(last_words) + '.'

# Concatenate the normalized text, the original additional sentence, and the new additional sentence
normalized_paragraph = f"""
homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. {additional_sentence}

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

normalized_paragraph = normalized_paragraph.capitalize()

# Fix misspelling "iZ" with correct "is" only when it is a mistake
normalized_paragraph = normalized_paragraph.replace(' iz ', ' is ')

# Calculate the number of whitespace characters in the text
#
whitespace_count = 0
for char in normalized_paragraph:
    if char.isspace():
        whitespace_count += 1


print("Normalized Paragraph:")
print(normalized_paragraph)

print("\nNumber of Whitespaces:", whitespace_count)