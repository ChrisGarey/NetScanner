# Cosmo's NetScanner

![Your Animated GIF Here](https://github.com/ChrisGarey/NetScanner/blob/main/scanner.gif)

Cosmo's NetScanner is a simple Python script that combines Figlet, Lolcat, and Nmap to create a colorful and interactive network scanner.

## Features

- Generates colorful ASCII art using Figlet and Lolcat.
- Scans a target IP address with Nmap.
- Allows customization of Nmap scan options.
- Displays scan progress with blinking dots.
- Reports open ports and known services found during the scan.

## Getting Started

### Prerequisites

To run this program, you need to have the following prerequisites installed:

- [Lolcat](https://github.com/busyloop/lolcat)
- [Nmap](https://nmap.org/)
- [Python](https://www.python.org/)
- [pip](https://pypi.org/project/pip/) (for installing Python packages)

### Installation

1. Clone this repository to your local machine.

   ```
   git clone https://github.com/your-username/NetScanner.git
   ```
2. Change to the project directory.

    ```
    cd NetScanner
    ```
3. Install the Python dependencies.

    ```
    pip install -r requirements.txt
    ```
4. Run the program.

    ```
    python3 scanner.py
    ```

### Usage

1.  Run the program.

2.  Follow the on-screen instructions to enter the target IP address and Nmap switches.

3.  The program will display colorful ASCII art and start the scan.

4.  You'll see a progress bar with blinking dots while the scan is in progress.

5.  The program will report open ports and known services found during the scan.

6.  At the end, the program will display a summary of the results.

### License

This project is licensed under the MIT License - see the LICENSE file for details.