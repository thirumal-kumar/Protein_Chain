import os
import colorama
from colorama import Fore, Style

# Initialize colorama to work on Windows as well
colorama.init()

def retrieve_atom_lines(input_file, output_file, selected_chains):
    selected_chains = [chain.upper() for chain in selected_chains.split(',')]
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Error: File '{input_file}' not found.")

        with open(input_file, 'r') as pdb_file:
            lines = pdb_file.readlines()

        atom_lines = [line for line in lines if line.startswith('ATOM') and line[21] in selected_chains]

        with open(output_file, 'w') as clean_pdb_file:
            clean_pdb_file.writelines(atom_lines)

        print(f"{Fore.GREEN}{introduction}{Style.RESET_ALL}")
        print(f"ATOM lines corresponding to chains '{', '.join(selected_chains)}' successfully retrieved and written to '{output_file}'.")
        
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

# Introduction
introduction = "The code was written by Dr. Thirumal Kumar D, Ph.D from India.\n" \
               "This code helps you to create clean protein (only the ATOM information) from the overall protein file retrieved from the Protein Data Bank in PDB format. You can also select the Chains of your interest.\n" \
               f"{Fore.RED}Keep the input protein in .pdb format and this python script in the same folder before execution{Style.RESET_ALL}."

# Center the introduction within 80 characters (adjust the width as needed)
centered_intro = introduction.center(80)

# Print the centered introduction in green color
print(f"{Fore.GREEN}{centered_intro}{Style.RESET_ALL}")

# Ask for user input for the input and output file names
input_pdb_file = input("Enter the name of the input .pdb file (without extension): ").strip()
output_pdb_file = input("Enter the name of the output .pdb file (without extension): ").strip()

# Add the .pdb extension if not provided by the user
input_pdb_file = input_pdb_file + '.pdb' if not input_pdb_file.endswith('.pdb') else input_pdb_file
output_pdb_file = output_pdb_file + '.pdb' if not output_pdb_file.endswith('.pdb') else output_pdb_file

# Ask for user input for the chain characters
selected_chains = input("Enter the chain characters you want to extract (separated by commas): ")

# Call the function to retrieve and extract the atom lines
retrieve_atom_lines(input_pdb_file, output_pdb_file, selected_chains)

# Final step: Successful message
print("Code written by Dr. Thirumal Kumar D, Ph.D - India")

# Pause execution to prevent immediate termination
input("Press Enter to close the terminal...")
