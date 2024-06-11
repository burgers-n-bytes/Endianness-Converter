import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import os
import hashlib
from datetime import datetime

def reverse_two_byte_pairs(input_file):
    try:
        start_time = datetime.now()
        
        with open(input_file, 'rb') as infile:
            data = infile.read()
            
            # Ensure the data length is even for proper 2-byte pairing
            if len(data) % 2 != 0:
                messagebox.showerror("Error", "Data length is not even.")
                return
            
            # Reverse every 2-byte pair (changing endianness of 16-bit words)
            reversed_data = bytearray()
            for i in range(0, len(data), 2):
                reversed_data.extend(data[i:i+2][::-1])
                
        output_file = generate_output_file_path(input_file, "_converted")
        with open(output_file, 'wb') as outfile:
            outfile.write(reversed_data)
        
        end_time = datetime.now()
        sha256_hash = compute_sha256_hash(output_file)
        hash_file = generate_output_file_path(input_file, "_hash.txt")
        write_hash_to_file(hash_file, sha256_hash, start_time, end_time, output_file)
        
        messagebox.showinfo("Success", f"Successfully converted endianness and saved to '{output_file}'\nSHA-256 Hash: {sha256_hash}\nHash saved to: '{hash_file}'")
        
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{input_file}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def generate_output_file_path(input_file, suffix):
    dir_name, base_name = os.path.split(input_file)
    name, ext = os.path.splitext(base_name)
    if ext and suffix.endswith(".txt"):
        return os.path.join(dir_name, f"{name}{suffix}")
    else:
        return os.path.join(dir_name, f"{name}{suffix}{ext}")

def compute_sha256_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def write_hash_to_file(file_path, sha256_hash, start_time, end_time, output_file):
    with open(file_path, 'w') as f:
        f.write(f"File Name: {os.path.basename(output_file)}\n")
        f.write(f"Full Path: {output_file}\n\n")
        f.write(f"SHA-256 Hash: {sha256_hash}\n\n")
        f.write(f"Process Start Time: {start_time}\n")
        f.write(f"Process End Time: {end_time}\n")

def select_input_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        input_file_path.set(file_path)

def process_files():
    input_file = input_file_path.get()
    
    if not input_file:
        messagebox.showerror("Error", "Please select an input file.")
        return
    
    reverse_two_byte_pairs(input_file)

# Create the main window
root = tk.Tk()
root.title("Endianness Converter Version 1.7")

# Set the window icon
logo_path = "C:/Users/ShanonBurgess/AppData/Local/Programs/Python/Python39/Brand Mark - White.png"
try:
    logo = PhotoImage(file=logo_path)
    root.iconphoto(False, logo)
except Exception as e:
    print(f"Error loading icon: {e}")

# Create StringVar variable to hold the file path
input_file_path = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Select the Input File (binary image):").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_file_path, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=select_input_file).grid(row=1, column=2, padx=10, pady=10)
tk.Button(root, text="Process", command=process_files).grid(row=2, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
