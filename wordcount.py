def word_count(txt_file):
    """Take a text file and return the word count."""
    script = open(txt_file)
    # create empty dict
    word_count = {}

    def line_stripper(txt_file):
        """Take a test file and strip it by whitespace and space inbetween words."""

        script_list = []
        for line in script:
            new_line = line.strip()
            new_line = new_line.split()
            script_list.extend(new_line)
        return script_list

    for word in line_stripper(script):
        word_count[word] = word_count.get(word, 0) + 1

    for key_word, count in word_count.items():
        print(f"{key_word} {count}")

    script.close()


# def make_letter_counts_dict(phrase):
#     letter_counts = {}
#     for letter in phrase:
#         letter_counts[letter] = letter_counts.get(letter, 0) + 1
#     return letter_counts
