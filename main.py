import tkinter as tk
from gui.turbojet_gui import TurbojetGUI

def main():
    # Initialize the main application window
    root = tk.Tk()

    # Create and initialize the Turbojet GUI with the main application window instance
    TurbojetGUI(root)

    # Start the main event loop
    root.mainloop()

# Check if the script is executed directly
if __name__ == "__main__":
    # Call the main function
    main()
