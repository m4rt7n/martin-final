# File: logic_layer.py

def find_word(letter_soup, word):
    """
    Searches for a word in the letter soup.
    
    Description:
    This function searches for a specific word within the given letter soup matrix. The search is conducted in all possible directions, including horizontal, vertical, and diagonal.
    
    :param letter_soup: The matrix of letters to search within.
        - Type: list of lists of str
        - Description: Represents the letter soup, where each sublist is a row in the soup.
    
    :param word: The word to search for in the letter soup.
        - Type: str
        - Description: The word that we are trying to find in the letter soup.
    
    :return: True if the word is found, False otherwise.
        - Type: bool
    """
    rows = len(letter_soup)
    cols = len(letter_soup[0]) if rows > 0 else 0
    word = word.upper()  # Convert the word to uppercase to avoid matching issues

    # Define all possible movement directions (8 directions)
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (0, -1), # left
        (-1, 0), # up
        (1, 1),  # diagonal down-right
        (-1, -1),# diagonal up-left
        (1, -1), # diagonal down-left
        (-1, 1)  # diagonal up-right
    ]

    # Function to check if a word exists starting from a given position and direction
    def check_word(x, y, word, direction):
        dx, dy = direction
        is_valid = True  # Flag to track if the word is found in the given direction
        for i in range(len(word)):
            new_x, new_y = x + i * dx, y + i * dy
            # Check if out of bounds or if the letter doesn't match
            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols or letter_soup[new_x][new_y] != word[i]:
                is_valid = False
        return is_valid

    # Search the word in the entire letter soup
    for i in range(rows):
        for j in range(cols):
            # If we find the first letter, start checking all directions
            if letter_soup[i][j] == word[0]:
                for direction in directions:
                    if check_word(i, j, word, direction):
                        return True
    return False

def find_words(letter_soup, words):
    """
    Searches for a list of words in the letter soup.
    
    Description:
    This function takes a letter soup matrix and a list of words and determines which words are present in the matrix.
    
    :param letter_soup: The matrix of letters to search within.
        - Type: list of lists of str
        - Description: Represents the letter soup, where each sublist is a row in the soup.
    
    :param words: The list of words to search for in the letter soup.
        - Type: list of str
        - Description: The words that we are trying to find in the letter soup.
    
    :return: A dictionary with each word as a key and a boolean indicating if it was found as the value.
        - Type: dict
    """
    found_words = {}
    for word in words:
        found_words[word] = find_word(letter_soup, word)  # Call find_word for each word
    return found_words
