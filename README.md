# Endianness-Converter
While conducting a chip-off acquisition of an OnStar Gen 9 telematics control module. It came to my attention Berla iVe was unable to correctly import and process the resulting binary image. This was because the chip-off imaging process did not account for converting the endianess of the file. This script forensically converts a binary image from one endianness to another.

The converted binary file can then be directly imported into Berla iVe successfully or manually parsed for artifacts.

While this was developed for a specific use case it can also be utilized to convert any binary file from one endianness to another.

### Technical Overview

The Endianness Converter is a Python script and executable application that provides a graphical user interface for reversing the byte order of 16-bit words (2-byte pairs) in a binary file. This can be useful for converting the endianness of data files. Additionally, the application computes the SHA-256 hash of the processed file and records the process start and end times. The output file and the hash information are saved in the same directory as the input file.

### Features

- Reverse the byte order of 16-bit words in a binary file.
- Automatically generate the output file name by appending "_converted" to the original file name.
- Compute the SHA-256 hash of the output file.
- Record the process start and end times.
- Save the hash information, including the file name and full path, to a text file.

### Requirements

- Python 3.x
- Tkinter (usually included with Python)
- hashlib (included with Python)
- PyInstaller (for creating the executable)

### Usage

1. **Running the Script:**

   To run the script directly using Python, navigate to the directory containing the script and execute the following command:

   ```bash
   python endianness_converter_gui.py
   ```

2. **Using the GUI:**

   - Launch the application.
   - Click the "Browse..." button to select the input file (binary image).
   - Click the "Process" button to reverse the byte order and generate the output file.
   - A message box will display the success message along with the SHA-256 hash and the location of the hash file.

3. **Output Files:**

   - The output file with reversed byte order is saved in the same directory as the input file with "_converted" appended to the original file name.
   - The SHA-256 hash and process times are saved in a text file with "_hash.txt" appended to the original file name.

### Script Explanation

Here's a breakdown of the script:

- **Imports and Setup:**
  - The script uses Tkinter for the GUI, hashlib for computing the SHA-256 hash, and datetime for recording process times.

- **Functions:**
  - `reverse_two_byte_pairs(input_file)`: Reads the input file, reverses the byte order of 16-bit words, writes the output file, computes the SHA-256 hash, and records the process times.
  - `generate_output_file_path(input_file, suffix)`: Generates the output file path based on the input file path and a suffix.
  - `compute_sha256_hash(file_path)`: Computes the SHA-256 hash of a file.
  - `write_hash_to_file(file_path, sha256_hash, start_time, end_time, output_file)`: Writes the hash, file name, full path, and process times to a text file.
  - `select_input_file()`: Opens a file dialog to select the input file.
  - `process_files()`: Validates the input file and calls `reverse_two_byte_pairs`.

- **GUI Setup:**
  - Creates the main Tkinter window, sets the title, and loads the icon.
  - Creates input file selection widgets and a process button.
  - Starts the Tkinter main loop.

### Acknowledgement

This application was created by Shanon Burgess for use within the digital forensics and security research communities.
