import pandas as pd
import string

def word_count(input_csv, output_csv):
    word_freq = {}
    df = pd.read_csv(input_csv)

    for column in df.columns:
        for text in df[column]:
            if isinstance(text, str):  # Check if the cell contains text
                words = text.lower().split()
                for word in words:
                    # Remove punctuation from the word (optional)
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    word_freq[word] = word_freq.get(word, 0) + 1

    # Convert the word frequency dictionary to a DataFrame
    word_count_df = pd.DataFrame(list(word_freq.items()), columns=['Word', 'Frequency'])

    # Sort the DataFrame by word frequency in descending order
    word_count_df = word_count_df.sort_values(by='Frequency', ascending=False)

    # Save the word count DataFrame to a new CSV file
    word_count_df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    input_csv_file = "/home/hadoop/negativedata.csv"
    output_csv_file = "/home/hadoop/negcount.csv"
    word_count(input_csv_file, output_csv_file)
