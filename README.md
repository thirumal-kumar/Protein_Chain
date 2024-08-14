Here's a README file tailored for the provided Python script:

---

# Protein PDB Chain Selection and ATOM Line Extraction Script

### Developed by Dr. Thirumal Kumar D, Ph.D from India

## Overview

This Python script is designed to help users extract specific chain information from Protein Data Bank (PDB) files, focusing only on the ATOM lines. The script reads a PDB file, filters out the ATOM lines for user-specified chains, and writes the filtered information to a new PDB file. This is particularly useful for researchers working with protein structures who need to isolate specific chains for further analysis or visualization.

## Features

- **Chain Selection**: Specify one or more chains from a PDB file to extract the corresponding ATOM lines.
- **Clean Output**: The script generates a clean PDB file containing only the selected chains' ATOM information.
- **User-Friendly Prompts**: The script guides you through the process with prompts for input and output file names, as well as chain selection.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed on your system.
- The `colorama` library for colored terminal output.

You can install the `colorama` library using pip:

```bash
pip install colorama
```

## Usage Instructions

1. **Download the Script**: Save the script as `Protein_NoANISOU_Chain_Selection.py` in your working directory.

2. **Prepare Your PDB File**: Ensure your PDB file is in the same directory as the script.

3. **Run the Script**: Execute the script from the command line or terminal:

   ```bash
   python Protein_NoANISOU_Chain_Selection.py
   ```

4. **Input Details**:
   - **Input PDB File**: When prompted, enter the name of your input PDB file (without the `.pdb` extension).
   - **Output PDB File**: Enter the desired name for the output PDB file (without the `.pdb` extension).
   - **Chain Selection**: Enter the chain identifiers (e.g., A, B) separated by commas. The script will extract and save the ATOM lines corresponding to these chains.

5. **Output**: The script will generate a new PDB file containing only the selected chains' ATOM lines.

## Example

Here’s an example of how the script might be used:

```bash
The code was written by Dr. Thirumal Kumar D, Ph.D from India.
This code helps you to create clean protein (only the ATOM information) from the overall protein file retrieved from the Protein Data Bank in PDB format. You can also select the Chains of your interest.

Enter the name of the input .pdb file (without extension): 1abc
Enter the name of the output .pdb file (without extension): 1abc_chain_A
Enter the chain characters you want to extract (separated by commas): A
```

After running the script, `1abc_chain_A.pdb` will contain the ATOM lines for chain A from the original `1abc.pdb` file.

## Error Handling

- **File Not Found**: If the input PDB file is not found, the script will display an error message.
- **General Errors**: Any other issues will be caught, and an appropriate error message will be displayed.

## Important Notes

- The script is designed to work with files in the PDB format and assumes standard formatting for ATOM lines.
- Make sure the PDB file and script are in the same directory for easy file access.

## License

This script is provided without any warranties. You are free to modify and use the script as needed for your research purposes.
