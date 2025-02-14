import os

# Define the file paths
INPUT_FILE = os.path.join("files", "alice_in_wonderland.txt")
OUTPUT_FILE = os.path.join("files", "first_10_lines.txt")

def read_file(filepath):
    """Reads the entire file and returns the content as a string."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return ""

def count_lines(filepath):
    """Counts and returns the number of lines in the file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return 0

def most_common_words(filepath, top_n=10):
    """Finds and returns the top N most common words in the file using a dictionary."""
    content = read_file(filepath)
    if not content:
        return []
    
    words = content.lower().split()
    words = [word.strip('.,!?()[]";:') for word in words]  # Remove punctuation

    word_counts = {}  # Dictionary to store word frequencies
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]

def print_n_lines(filepath, n=5):
    """Prints the first N lines of the file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if i >= n:
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")

def search_word(filepath, word):
    """Searches for a word in the file and returns the count of occurrences."""
    content = read_file(filepath)
    if not content:
        return 0

    words = content.lower().split()
    words = [w.strip('.,!?()[]";:') for w in words]
    return words.count(word.lower())

def write_first_n_lines(input_filepath, output_filepath, n=10):
    """Writes the first N lines of the input file to the output file."""
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile, \
             open(output_filepath, 'w', encoding='utf-8') as outfile:
            
            for i, line in enumerate(infile):
                if i >= n:
                    break
                outfile.write(line)
        
        print(f"First {n} lines written to {output_filepath}")
    except FileNotFoundError:
        print(f"Error: File {input_filepath} not found.")

def main():
    """Main function to call other functions and display results."""

    total_lines = count_lines(INPUT_FILE)
    print(f"Total number of lines: {total_lines}\n")

    print("First 5 lines of the file:")
    print_n_lines(INPUT_FILE, 5)
    print("\n")

    common_words = most_common_words(INPUT_FILE, 10)
    print("Top 10 most common words:")
    for word, count in common_words:
        print(f"{word}: {count}")
    print("\n")

    search_term = "alice"
    word_count = search_word(INPUT_FILE, search_term)
    print(f"The word '{search_term}' appears {word_count} times in the file.\n")

    write_first_n_lines(INPUT_FILE, OUTPUT_FILE, 10)

if __name__ == "__main__":
    main()
