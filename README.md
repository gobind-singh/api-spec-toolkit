# API Spec Toolkit

A Python script to extract API endpoint details from **Swagger/OpenAPI YAML** files and convert them into a structured **CSV** format. This tool is perfect for API documentation, analysis, and review workflows.

---

## Features

- Supports **Swagger/OpenAPI 3.0** specifications.
- Extracts and organizes:
  - **Tags**: API categories for grouping endpoints.
  - **Methods**: HTTP methods (GET, POST, PUT, DELETE, etc.).
  - **Paths**: API endpoint paths.
  - **Summary**: Short API descriptions.
  - **Description**: Detailed API documentation.
- Outputs a clean **CSV** file for further processing or review.

---

## Table of Contents

- [API Spec Toolkit](#api-spec-toolkit)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Usage](#usage)
  - [Input Example](#input-example)
  - [Output Table](#output-table)

---

## Installation

### Prerequisites

- **Python 3.x**
- **PyYAML** library (for reading YAML files)

Install the required dependency using `pip`:

```bash
pip3 install pyyaml
```

### Clone the Repository
```bash
git clone https://github.com/gobind-singh/api-spec-toolkit.git
cd api-spec-toolkit
```

### Usage
Run the script with the following command:

```bash
python3 extractor.py <input_swagger.yaml> <output_file.csv>
```

Parameters:
- <input_swagger.yaml>: Path to your Swagger/OpenAPI YAML file.
- <output_file.csv>: Path where the resulting CSV file will be saved.

## Input Example

```yaml
openapi: 3.0.0
info:
  title: Sample API
  version: "1.0"
paths:
  /users:
    get:
      tags:
        - Users
      summary: Get Users
      description: Fetch a list of users.
  /users/{id}:
    get:
      tags:
        - Users
      summary: Get User by ID
      description: Fetch a user by their ID.
  /orders:
    post:
      tags:
        - Orders
      summary: Create Order
      description: Create a new order.
```

## Output Table

| Tag       | Method | Path          | Summary              | Description                  |
|-----------|--------|---------------|----------------------|------------------------------|
| Users     | GET    | /users        | Get Users            | Fetch a list of users.       |
| Users     | GET    | /users/{id}   | Get User by ID       | Fetch a user by their ID.    |
| Orders    | POST   | /orders       | Create Order         | Create a new order.          |
