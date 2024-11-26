# **Wordlist Generator for Social Engineering Protection**

By generating wordlists based on personal information, it simulates potential password vulnerabilities that attackers might exploit. This tool is ideal for penetration testing, vulnerability assessment, and improving password security. The script is optimized for memory usage, ensuring efficient performance even with large wordlists.

## **Features**

- **Personalized Wordlist Generation**: Collects data such as first name, last name, birth year, pet's name, and optional custom words to generate a list of common passwords.
- **Case Variation Support**: Automatically generates all possible case variations (lowercase, uppercase, capitalized) for each word.
- **Combinations and Permutations**: Creates all possible permutations and combinations of the user-provided data, ensuring a comprehensive wordlist for testing.
- **Blacklist Creation**: The wordlist can be used to generate a blacklist of weak, common, or easily guessable passwords to secure your systems against brute-force or dictionary attacks.
- **Memory Optimization**: Designed to minimize memory usage during wordlist generation by processing data efficiently in chunks. This ensures that even large wordlists can be handled without excessive memory consumption.
- **Chunked File Saving**: Saves the generated wordlist to a file in manageable chunks, making it easier to handle large wordlists.

## **Use Case**

This tool is perfect for:
- **Penetration Testing**: Test the strength of passwords in your systems by simulating social engineering-based attacks.
- **Security Audits**: Identify and block easily guessable passwords based on common user data.
- **Password Strengthening**: Understand the weaknesses in your current password policies and create strong password guidelines.

## **Example**

If you input the following details:

* **First Name**: Furkan  
* **Last Name**: Sen
* **Year of Birth**: 2003
* **Pet's Name**: Golge
* **Custom Words**: ohio, wyoming

The tool will generate a wordlist that includes combinations such as:

* furkansen2003wyoming
* furkansenGOLGE
* GolgeOhio2003

And many more, with all possible case variations and permutations.

## **Why Use This Tool?**

* **Identify Weak Passwords**: Test your systems against real-world social engineering techniques and identify weak passwords based on common personal information.
* **Improve Security**: Use the generated wordlist to strengthen your password policies and avoid easily guessable passwords.
* **Penetration Testing Tool**: Simulate attacks based on social engineering to identify potential vulnerabilities in your security systems.
* **Memory Optimized**: Efficient memory usage ensures that even with large datasets, the tool runs smoothly without consuming excessive resources.

## **Contributing**

Contributions are welcome! Feel free to fork this repository, make improvements, or submit pull requests.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
