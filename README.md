# Cryptanalysis Tool

## Introduction

This Python script is a cryptanalysis tool designed to aid in breaking simple XOR-based encryption. It consists of two main functions: finding the probable key length and determining the encryption key. The script assumes that the text is encrypted using a repeating-key XOR cipher.

## Usage

### Dependencies

Before using the tool, ensure you have Python installed on your machine.

### Running the Script

1. Copy and paste the script into a Python environment or save it as a `.py` file.
2. Replace the `ciphertext` variable with the encrypted text you want to analyze.
3. Run the script.

### Output

The script outputs the probable key length and attempts to determine the encryption key. If successful, it displays the secret key used for encryption.

## Functions

### 1. `findKeyLength(ciphertext)`

This function takes the encrypted text as input and iterates through possible key lengths to find the most probable one. It uses the Index of Coincidence (IC) to measure the likelihood of a correct key length.

### 2. `findKey(ciphertext, key_length)`

Given the probable key length, this function divides the encrypted text into blocks and attempts to find the most likely letter for each position in the key. It uses a frequency analysis approach.

### 3. `shift_decrypt(ciphertext)`

For each potential key, this function attempts to decrypt the text and calculates a correlation score. The key with the highest correlation score is considered the most likely encryption key.

## Example

To demonstrate the usage of the script, a sample encrypted text (`ciphertext`) is provided within the script. The script is then executed to find the probable key length and determine the encryption key.

Feel free to replace the provided `ciphertext` with your own encrypted text for analysis.

**Note:** The accuracy of the tool depends on the length and nature of the encrypted text. It may not work well for short or highly repetitive texts.
