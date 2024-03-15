def word_count(text):
    """
    Function to count the number of words in a given text.
    """
    # Split the text into words using whitespace as delimiter
    words = text.split()
    # Return the count of words
    return len(words)

def main():
    """
    Main function to handle user input, call word_count function, and display output.
    """
    print("Welcome to Word Counter!")
    
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")
    
    # Check if the user input is empty
    if not user_input:
        print("Error: Empty input! Please enter some text.")
    else:
        # Call word_count function and display the word count
        count = word_count(user_input)
        print(f"Word count: {count}")

if __name__ == "__main__":
    main()
