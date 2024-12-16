import yaml
import csv
import sys

# Function to read and parse Swagger YAML file
def read_swagger_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            swagger_data = yaml.safe_load(file)
        return swagger_data
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

# Function to extract endpoints and HTTP methods from Swagger YAML
def extract_endpoints(swagger_data):
    endpoints = []

    if 'paths' not in swagger_data:
        print("Invalid Swagger file: Missing 'paths' key.")
        sys.exit(1)

    for path, methods in swagger_data['paths'].items():
        for method, details in methods.items():
            if method.lower() in ['get', 'post', 'put', 'delete', 'patch', 'options', 'head']:
                tags = details.get('tags', ['General'])
                endpoint = {
                    'Tag': ', '.join(tags),
                    'Method': method.upper(),
                    'Path': path,  # Exclude base host from path
                    'Summary': details.get('summary', 'N/A'),
                    'Description': details.get('description', 'N/A')
                }
                endpoints.append(endpoint)
    return endpoints

# Function to write extracted data to a CSV file
def write_to_csv(output_file, endpoints):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Tag', 'Method', 'Path', 'Summary', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for endpoint in endpoints:
            writer.writerow(endpoint)
    print(f"Data successfully written to {output_file}")

# Main function to integrate the process
def main():
    if len(sys.argv) != 3:
        print("Usage: python swagger_to_csv.py <input_swagger.yaml> <output_file.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Parse Swagger YAML
    swagger_data = read_swagger_yaml(input_file)

    # Extract endpoints
    endpoints = extract_endpoints(swagger_data)

    # Write to CSV
    write_to_csv(output_file, endpoints)

if __name__ == "__main__":
    main()
