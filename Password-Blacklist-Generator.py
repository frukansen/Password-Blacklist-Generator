import os
import itertools

def get_user_data():
    print("Enter details to generate the wordlist:")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    birth_year = input("Year of Birth: ").strip()
    pet_name = input("Pet's Name: ").strip()
    # Updated prompt for custom words with commas
    custom_word = input("Custom Word(s) (optional, separate with commas): ").strip().split(',')
    return [first_name, last_name, birth_year, pet_name] + custom_word

def generate_case_variations(word):
    """Generates all case variations for a given word."""
    if not word:
        return [""]
    variations = set(itertools.product(*((char.lower(), char.upper()) for char in word)))
    return ["".join(variation) for variation in variations]

def generate_combinations(data):
    """Generate combinations from case variations."""
    data = [item for sublist in data for item in sublist if item]
    combinations = set()
    for r in range(1, len(data) + 1):
        for combo in itertools.permutations(data, r):
            combinations.add("".join(combo))
    return sorted(combinations)

def save_wordlist_in_chunks(wordlist, filename="output/wordlist.txt", chunk_size=10000):
    """Save the generated combinations to a file in chunks."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        for i, word in enumerate(wordlist):
            f.write(word + "\n")
            if (i + 1) % chunk_size == 0:
                print(f"Processed {i + 1} combinations...")
    print(f"Wordlist saved to {filename}")

if __name__ == "__main__":
    user_data = get_user_data()
    case_variations = [generate_case_variations(item) for item in user_data]
    wordlist = generate_combinations(case_variations)
    save_wordlist_in_chunks(wordlist)
