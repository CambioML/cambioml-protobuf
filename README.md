# CambioML Protobuf Python Setup Guide

This guide provides detailed steps for setting up and using the CambioML Protobuf Python environment. Follow these steps to ensure a correct setup.

## Prerequisites

Before you begin, ensure you have Python and pip installed on your system. You will also need the Protocol Buffers Compiler (`protoc`) installed to generate Python classes from `.proto` files.

## Setup Instructions

### Step 1: Navigate to the Python Directory

First, you need to navigate to the `cambioml-protobuf/python` directory where the Python-related protobuf files and configurations are located. Open a terminal and run the following command:

```bash
cd cambioml-protobuf/python
```

This command changes the current directory to cambioml-protobuf/python, ensuring that all subsequent commands are run in the correct context.

### Step 2: Install Poetry
Poetry is a tool for dependency management and packaging in Python. To install Poetry, run the following command:

```bash
pip3 install poetry
```

This command uses pip3 to install the Poetry package globally. Poetry helps manage project dependencies in an isolated environment, making your project more reproducible and less prone to conflicts.

### Step 3: Install Dependencies with Poetry
Once Poetry is installed, you can install the project dependencies without installing the project package itself (referred to as the "root" package). Run the following command:

```bash
poetry install --no-root
```

The --no-root option tells Poetry to skip installing the root package (typically your project package) and only install its dependencies. This is useful when you're setting up an environment for development or testing purposes.

### Step 4: Generate Python Classes from Protobuf Definitions
Finally, you need to generate Python classes from your .proto files. This step requires the Protocol Buffers Compiler (protoc). Run the following command:

```bash
cd ..
protoc -I=./proto --python_out=./python/cambioml_protobuf ./proto/documents.proto
```

Here's what this command does:

- -I=./proto: Specifies the directory where your .proto files are located.
- --python_out=./python/cambioml_protobuf: Tells protoc to generate Python classes in the specified directory.
- ./proto/documents.proto: The path to the .proto file you want to compile.
This command generates Python classes from the documents.proto file, allowing you to work with Protobuf messages in Python.

Conclusion
Following these steps will set up your Python environment for working with CambioML Protobuf definitions. You can now proceed with development or testing tasks as needed.