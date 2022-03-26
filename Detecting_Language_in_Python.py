# We need the alphabet because we convert letters into numerical values to be able to use
# Mathematical operations (note we encrypt the spaces as well)
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# We store the english words in a list (a dictionary would be better though)
ENGLISH_WORDS = []


# Load the english words
def get_data():
    # Let's load all the english words from a .txt file
    dictionary = open("English_Language.txt", "r")

    # Initialize the ENGLISH_WORDS list with the words present in the file
    # Every word is in a distinct line so that why we have to split('\n')
    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)

    dictionary.close()


# Count the number of english words in a given text
def count_words(text):
    # Upper case letters are needed
    text = text.upper()
    # Transform the text into a list of words (split by spaces)
    words = text.split(' ')
    # Matches counts the number of english words in the text
    matches = 0

    # Consider all the words in the text and check whether the given word is english or not
    for word in words:
        if word in ENGLISH_WORDS:
            matches = matches + 1

    return matches


# Decides whether a given text is english or not
def is_text_english(text):
    # Number of english words in a given text
    matches = count_words(text)

    # You can define your own classification algorithm
    # In this case the assumption: if 60% of the words in the text are english words then
    # It is an english text
    if (float(matches) / len(text.split(' '))) * 100 >= 60:
        return True

    # Not an english text
    return False


# Cracking the caesar encryption algorithm with brute-force
def caesar_crack(cipher_text):
    # We try all the possible key values so the size of the ALPHABET
    for key in range(len(ALPHABET)):

        # Reinitialize this to be an empty string
        plain_text = ''

        # We just have to make a simple caesar decryption
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]

        # Print the actual decrypted string with the given key
        if is_text_english(plain_text):
            print("We have managed to crack the Caesar Cipher, the key is : %s" % key) 
            print("The message is : %s" % plain_text)


if __name__ == "__main__":
    get_data()
    encrypted = 'GDWDCHQJLQHHUVCZRUNCLQCDCYDULHWACRICVHWWLQJVCWRCEXLOGCVAVWHPVCWKDWCFROOHFWCPDQDJHCDQGCFRQYHUWCUDZCGDWDCLQWRCXVDEOHCLQIRUPDWLRQCIRUCGDWDCVFLHQWLVWVCDQGCEXVLQHVVCDQDOAVWVCWRCLQWHUSUHW'
    caesar_crack(encrypted)