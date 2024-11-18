# File: output_layer.py
import json

def generate_report(letter_soup, words, output_file="soup_report.json"):
    """
    Generates a report in JSON format with the words found and not found in the letter soup.
    
    Description:
    This function generates a JSON file that reports which words were found and which were not found in the letter soup. It uses the functions defined in the logic layer to perform the search.
    
    :param letter_soup: The matrix of letters to search within.
        - Type: list of lists of str
        - Description: Represents the letter soup, where each sublist is a row in the soup.
    
    :param words: The list of words to search for in the letter soup.
        - Type: list of str
        - Description: The words that we are trying to find in the letter soup.
    
    :param output_file: The name of the output JSON file.
        - Type: str
        - Default: "soup_report.json"
        - Description: The file path where the output report will be stored.
    """
    from logic_layer import find_words  # Import find_words function from the logic layer
    
    # Find words in the letter soup using the find_words function
    report = find_words(letter_soup, words)
    
    # Write the report to the output JSON file
    with open(output_file, 'w') as json_file:
        json.dump(report, json_file, indent=4)  # Save the report in JSON format with an indentation of 4 spaces
    
    # Print the location of the generated file
    print(f"The report has been saved to: {output_file}")

# Usage example
if __name__ == "__main__":
    from input_layer import get_file_content  # Import get_file_content function from the input layer
    
    # Define the input file path (modify this according to the actual location of the input file)
    file_path = "letter_soup.txt"  # Change to the path of the input file
    
    # Get the letter soup and the words to search for from the input file
    letter_soup, words = get_file_content(file_path)
    
    # Generate the report in JSON format
    generate_report(letter_soup, words)
