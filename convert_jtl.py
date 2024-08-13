import pandas as pd
import sys
import os

def convert_jtl_to_csv(jtl_file, csv_file):
    # Read JTL file (assuming XML format) into a DataFrame
    try:
        df = pd.read_xml(jtl_file)
    except Exception as e:
        print(f"Error reading XML file: {e}")
        return
    
    # Save DataFrame to CSV
    try:
        df.to_csv(csv_file, index=False)
        print(f"Successfully converted {jtl_file} to {csv_file}")
    except Exception as e:
        print(f"Error saving CSV file: {e}")

def convert_jtl_to_json(jtl_file, json_file):
    # Read JTL file (assuming XML format) into a DataFrame
    try:
        df = pd.read_xml(jtl_file)
    except Exception as e:
        print(f"Error reading XML file: {e}")
        return
    
    # Save DataFrame to JSON
    try:
        df.to_json(json_file, orient='records', lines=True)
        print(f"Successfully converted {jtl_file} to {json_file}")
    except Exception as e:
        print(f"Error saving JSON file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python convert_jtl.py <input_jtl_file> <output_file> <output_format>")
        print("output_format: 'csv' or 'json'")
        sys.exit(1)

    input_jtl_file = sys.argv[1]
    output_file = sys.argv[2]
    output_format = sys.argv[3].lower()

    if not os.path.isfile(input_jtl_file):
        print(f"Input file {input_jtl_file} does not exist.")
        sys.exit(1)

    if output_format == 'csv':
        convert_jtl_to_csv(input_jtl_file, output_file)
    elif output_format == 'json':
        convert_jtl_to_json(input_jtl_file, output_file)
    else:
        print("Invalid output format specified. Use 'csv' or 'json'.")
        sys.exit(1)