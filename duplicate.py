import csv

class DoubleCSVSize:
    def double_size(self, input_file, output_file):
        # Read input CSV file
        with open(input_file, 'r') as infile:
            reader = csv.reader(infile)
            data = [row for row in reader]

        # Double the size by duplicating each record
        doubled_data = data + data

        # Write the doubled data to a new CSV file
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(doubled_data)

if __name__ == '__main__':
    input_csv_file = '/home/hadoop/negativedata.csv'  # Replace with your input CSV file path
    output_csv_file = '/home/hadoop/dupnegative.csv'  # Replace with your desired output CSV file path

    # Instantiate the DoubleCSVSize class and call the double_size method
    csv_doubler = DoubleCSVSize()
    csv_doubler.double_size(input_csv_file, output_csv_file)
