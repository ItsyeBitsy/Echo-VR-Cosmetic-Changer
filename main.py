import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class FileSwapper:
    def __init__(self, root):
        self.replace_button = None
        self.file_dropdown = None
        self.file_dropdown_label = None
        self.directory_button = None
        self.label = None
        self.root = root
        self.root.title("Echo Cosmetic Changer")
        self.root.geometry("400x200")
        self.root.configure(bg="#121212")  # color

        # Set the icon
        icon_path = "C:\\Users\\zanzu\\Downloads\\yay testing!\\customcosmetics.ico"  # path of icon file
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        self.selected_directory = None
        self.file_mapping = {}  # To store file name mapping (user-friendly names)

        # Define the files to be shown in the dropdown menu with their names
        self.files_to_show = {
            "458658456206694681": "Pop One Poster (not vibs)",
            "-4324220158131329628": "s5 tag",
            "-4324220153836362332": "s5 final",
            "-4324220149541395036": "s5 champ",
            "-7232698398716931768": "s1 champ",
            "-5624402900360767574": "s3 tag",
            "-5624402896065800278": "s2 tag",
            "-5624402891770832982": "s1 tag",
            "-4840446824099437682": "preseason",
            "-43877368129166514": "lone echo2",
            "-320730475426306063": "flowers",
            "511474952409991066": "s3 final",
            "-660827049241030700": "s2 champ",
            "2073142157391964650": "s3 champ tag",
            "-1366810324886314588": "s2 final tag",
            "-3042205619643299508": "dev tag",
            "-4324212461549935196": "s7 champ",
            "-4324212465844902492": "s7 final tag",
            "-4324212470139869788": "s7 tag",
            "-4324212474434837084": "s6 champ",
            "-4324212478729804380": "s6 final tag",
            "-4324212483024771676": "s6 tag",
            "testing": "testing file"

            # might add more
        }

        self.create_widgets()

    def create_widgets(self):
        # Label and dropdown menu
        self.label = ttk.Label(self.root, text="Select a directory", background="#121212",
                               foreground="purple", font="Roboto")
        self.label.pack(pady=10)

        self.directory_button = ttk.Button(self.root, text="Browse", command=self.browse_directory)
        self.directory_button.pack(pady=5)

        self.file_dropdown_label = ttk.Label(self.root, text="Select a file to replace:", background="#121212",
                                             foreground="white")
        self.file_dropdown_label.pack(pady=10)
        self.file_dropdown = ttk.Combobox(self.root)
        self.file_dropdown.pack(pady=5)

        # Replace button
        self.replace_button = ttk.Button(self.root, text="Replace", command=self.replace_file)
        self.replace_button.pack(pady=5)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.selected_directory = directory
            self.populate_dropdown()

    def populate_dropdown(self):
        # Clear previous items in dropdown menu
        self.file_dropdown['values'] = ()

        if self.selected_directory:
            # Get the files to show from the dictionary
            files = list(self.files_to_show.values())
            # Update dropdown menu with found files
            if files:
                self.file_dropdown['values'] = tuple(files)
                self.file_dropdown.current(0)  # Select the first file by default
            else:
                messagebox.showinfo("Info", "No files found in the selected directory.")

    def replace_file(self):
        selected_file_name = self.file_dropdown.get()
        if selected_file_name:
            # Find the file ID corresponding to the selected file name
            file_id = None
            for key, value in self.files_to_show.items():
                if value == selected_file_name:
                    file_id = key
                    break

            if file_id:
                # Ask user to select a file to replace with
                replacement_file_path = filedialog.askopenfilename()
                if replacement_file_path:
                    # Replace the file
                    try:
                        os.replace(replacement_file_path, os.path.join(self.selected_directory, file_id))
                        messagebox.showinfo("Success", f"File '{selected_file_name}' replaced successfully.")
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred while replacing the file: {str(e)}")
            else:
                messagebox.showerror("Error", "Selected file not found.")
        else:
            messagebox.showerror("Error", "Please select a file.")


def main():
    root = tk.Tk()
    FileSwapper(root)
    root.mainloop()


if __name__ == "__main__":
    main()
