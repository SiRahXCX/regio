import tkinter as tk
from tkinter import filedialog
from utils import extract_data_from_xlsx, extract_data_from_csv, fill_and_save_template

csv_path_var_default_text = "No CSV file selected"
pdf_path_var_default_text = "No PDF file selected"
output_path_var_default_text = "No Output directory selected"

def select_csv() -> None:
    csv_filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select CSV",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
    )

    if csv_filename:
        csv_path_display.config(state="normal")
        csv_path_var.set(csv_filename)
        csv_path_display.config(state="readonly")


def select_pdf() -> None:
    pdf_filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select PDF",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
    )

    if pdf_filename:
        pdf_path_display.config(state="normal")
        pdf_path_var.set(pdf_filename)
        pdf_path_display.config(state="readonly")


def select_save_path() -> None:
    new_pdf_file_path = filedialog.askdirectory(
        initialdir="/", title="Select PDF save path", parent=root, mustexist=True
    )

    if new_pdf_file_path:
        output_path_display.config(state="normal")
        output_path_var.set(new_pdf_file_path)
        output_path_display.config(state="readonly")


def validate_paths() -> bool:
    if csv_path_var == csv_path_var_default_text:
        return False
    
    if pdf_path_var == pdf_path_var_default_text:
        return False

    if output_path_var == output_path_var_default_text:
        return False

    return True


def save_pdf() -> None:
    if validate_paths():
        ext = csv_path_var.get().split('.')[-1]
        if ext.lower() == 'xlsx':
            data = extract_data_from_xlsx(csv_path_var.get())
        elif ext.lower() == 'csv':
            data = extract_data_from_csv(csv_path_var.get())
        else:
            print('Error unrecognised data file type')
            return

        fill_and_save_template(data, pdf_path_var.get(), output_path_var.get())
        print('Success files saved successfully')
    else:
        print('Error some paths are missing')
        return


root = tk.Tk()
root.title("Regio")
root.geometry("600x600")

main_label = tk.Label(root, text="Regio", font=("Arial", 24))
main_label.pack(padx=20, pady=20)

main_frame = tk.Frame(root, borderwidth=1, relief="solid")
main_frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor="center")
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=2)

# --- CSV file row ---
csv_con = tk.Frame(main_frame)
csv_con.grid(column=0, row=0, padx=0, pady=5, sticky="ew")
csv_con.columnconfigure(0, weight=1)
csv_con.columnconfigure(1, weight=0)

csv_label = tk.Label(csv_con, text="CSV File", font=("Arial", 10))
csv_label.grid(column=0, row=0, padx=10, pady=0, sticky="w")

csv_path_var = tk.StringVar(value=csv_path_var_default_text)
csv_path_display = tk.Entry(
    csv_con,
    textvariable=csv_path_var,
    borderwidth=1,
    relief="sunken",
    font=("Arial", 10),
    state="readonly",
)
csv_path_display.grid(column=0, row=1, padx=10, pady=0, sticky="ew")

csv_browse_button = tk.Button(
    csv_con, text="Browse", command=select_csv, borderwidth=1, relief="solid",
    font=("Arial", 10), width=10,
)
csv_browse_button.grid(column=1, row=1, padx=15, pady=10)

# --- PDF file row ---
pdf_con = tk.Frame(main_frame)
pdf_con.grid(column=0, row=1, padx=0, pady=5, sticky="ew")
pdf_con.columnconfigure(0, weight=1)
pdf_con.columnconfigure(1, weight=0)

pdf_label = tk.Label(pdf_con, text="PDF File", font=("Arial", 10))
pdf_label.grid(column=0, row=0, padx=10, pady=0, sticky="w")

pdf_path_var = tk.StringVar(value=pdf_path_var_default_text)
pdf_path_display = tk.Entry(
    pdf_con,
    textvariable=pdf_path_var,
    borderwidth=1,
    relief="sunken",
    font=("Arial", 10),
    state="readonly",
)
pdf_path_display.grid(column=0, row=1, padx=10, pady=0, sticky="ew")

pdf_browse_button = tk.Button(
    pdf_con, text="Browse", command=select_pdf, borderwidth=1, relief="solid",
    font=("Arial", 10), width=10,
)
pdf_browse_button.grid(column=1, row=1, padx=15, pady=10)

# --- Output directory row ---
od_con = tk.Frame(main_frame)
od_con.grid(column=0, row=2, padx=0, pady=5, sticky="ew")
od_con.columnconfigure(0, weight=1)
od_con.columnconfigure(1, weight=0)

output_dir_label = tk.Label(od_con, text="Output Directory", font=("Arial", 10))
output_dir_label.grid(column=0, row=0, padx=10, pady=0, sticky="w")

output_path_var = tk.StringVar(value=output_path_var_default_text)
output_path_display = tk.Entry(
    od_con,
    textvariable=output_path_var,
    borderwidth=1,
    relief="sunken",
    font=("Arial", 10),
    state="readonly",
)
output_path_display.grid(column=0, row=1, padx=10, pady=0, sticky="ew")

browse_output_button = tk.Button(
    od_con, text="Browse", command=select_save_path, borderwidth=1, relief="solid",
    font=("Arial", 10), width=10,
)
browse_output_button.grid(column=1, row=1, padx=15, pady=10)

# --- Generate button ---
generate_button = tk.Button(
    main_frame, text="Generate PDF", background="#4c7BD8", foreground="#FFFFFF",
    command=save_pdf, borderwidth=1, relief="solid", font=("Arial", 10), width=14,
)
generate_button.grid(column=0, row=3, padx=10, pady=20, sticky="e")

root.mainloop()
