# File: input_layer.py

def get_file_content(file_path):
    """
    Reads the input file and returns the letter soup and the words to search for.
    
    Description:
    This function reads the input file that contains a letter soup and a list of words to search for. The file is structured with the letter soup first, followed by a separator (`---`), and then the words to search.
    
    :param file_path: Path to the input file.
        - Type: str
        - Description: The file path where the letter soup and words are stored.
    
    :return: A tuple (letter_soup, words).
        - Type: tuple
        - letter_soup: A list of lists representing the matrix of letters in uppercase.
        - words: A list of words to search for in the letter soup.
    """
    with open(file_path, 'r') as file:
        content = file.readlines()  # Read all lines from the file
    
    # Separate the letter soup and the words to search for
    letter_soup = []
    words = []
    parsing_soup = True  # Variable to track whether we are reading the letter soup or the words

    for line in content:
        stripped_line = line.strip()  # Remove leading and trailing spaces

        # If we find the separator "---", switch to reading the words
        if stripped_line == "---":
            parsing_soup = False
        elif parsing_soup:
            # If we are in the letter soup part, add the line to the letter matrix
            valid_line = True
            is_valid = True  # Flag to track if the line is valid
            for c in stripped_line:
                if not (c.isalpha() or c.isspace()):
                    is_valid = False
            if is_valid:
                letter_soup.append(list(stripped_line.replace(" ", "").upper()))  # Convert to uppercase and remove spaces
        else:
            # If we are in the word search part, add each word to the list of words
            if stripped_line.isalpha():
                words.append(stripped_line)

    return letter_soup, words  # Return the letter soup and the words to search for
