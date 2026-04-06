import graphics as gs
import logic as lg
import tools as tls
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_about():
    messagebox.showinfo(
        "About",
        "Author: Dao Anh Tuan\n"
        "Root finder application\n\n"
        "Method: Steffensen\n"
        "Code explanation:\n"
        "0 - Success\n"
        "1 - Convergence errors\n"
        "2 - Zero division errors\n"
        "3 - Errors related to types(TypeError)\n"
        "4 - Errors related to type conversion(ValueError)\n"
        "5 - The root doesn't lie on the current interval\n\n"
        "Supports:\n"
        "- Root finding\n"
        "- Graph plotting\n"
        "- Extrema & inflection points"
    )

def clear_inputs():
    for e in entries:
        e.delete(0, tk.END)

def clear_entry(i):
    entries[i].delete(0, tk.END)

def calculate():
    try:
        func_str = entries[0].get()
        a = float(entries[1].get())
        b = float(entries[2].get())
        h = float(entries[3].get())
        nmax = int(entries[4].get())
        eps = float(entries[5].get())

        f = tls.parse_function(func_str)

        valid, msg = tls.validate_input(a, b, h, eps, nmax, f)
        if not valid:
            messagebox.showerror("Error", msg)
            return None

        roots = lg.find_roots(f, a, b, h, eps, nmax)

        for row in tree.get_children():
            tree.delete(row)
            
        for r in roots:
            tree.insert("", "end", values=(
                r["id"],
                f"[{r['interval'][0]:.3f}; {r['interval'][1]:.3f}]",
                f"{r['root']:.6f}" if r["root"] != None and r["interval"][0] < r["root"] < r["interval"][1] else "-",
                f"{r['fx']:.1e}" if r["fx"] != None else "-",
                r["iters"],
                r["error"]
            ))

        gs.plot_function(f, a, b, roots)

    except ValueError as e:
        messagebox.showerror("Error:", e)

root = tk.Tk()
root.title("Steffensen method")
root.geometry("600x600")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

menubar = tk.Menu(root)
actions = tk.Menu(menubar, tearoff=0)
actions.add_command(label='Clear', command=clear_inputs)
menubar.add_cascade(label="Actions", menu=actions)
about_menu = tk.Menu(menubar, tearoff=0)
about_menu.add_command(label="About program", command=show_about)
menubar.add_cascade(label="About", menu=about_menu)


personal_info = tk.Menu(menubar, tearoff=0)
root.config(menu=menubar)


fonts = ("Arial", 14)

left_frame = tk.Frame(root)
left_frame.grid(row = 0, column=0, sticky='nsew')
left_frame.columnconfigure(0, weight=1)
left_frame.columnconfigure(1, weight=2)
left_frame.columnconfigure(2, weight=1)

for i in range(7):
    left_frame.rowconfigure(i, weight=1)

# Left column
ttk.Label(left_frame, font=fonts, text="Function", anchor="center").grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
ttk.Label(left_frame, font=fonts,text="Initial point", anchor="center").grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
ttk.Label(left_frame, font=fonts, text="Endpoint", anchor="center").grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
ttk.Label(left_frame, font=fonts, text="Division step", anchor="center").grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
ttk.Label(left_frame, font=fonts, text="Max number of iterations", anchor="center").grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
ttk.Label(left_frame, font=fonts, text="Precision", anchor="center").grid(row=5, column=0, sticky="nsew", pady=5, padx=5)
ttk.Button(left_frame, text="Calculate", command=calculate).grid(row=6, column=0, sticky="nsew", pady=5, padx=10)


# Right column
entries = []
for i in range(7):
    e = ttk.Entry(left_frame, width=30, font=fonts)
    e.grid(row=i, column=1, pady=5, padx=5)
    entries.append(e)


entries[0].insert(tk.END, "sin(x) / (x-1) - 1")
entries[1].insert(tk.END, "-4")
entries[2].insert(tk.END, "4")
entries[3].insert(tk.END, "0.12")
entries[4].insert(tk.END, "100")
entries[5].insert(tk.END, "1e-8")

ttk.Button(left_frame, text="Clear input", command=clear_inputs).grid(row=6, column=1, sticky="nsew", pady=5, padx=10)

for i in range(6):
    ttk.Button(
        left_frame,
        text="clear",
        command=lambda i=i: clear_entry(i)
    ).grid(row=i, column=2, padx=5, pady=5)


right_frame = tk.Frame(root)
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(0, weight=1)
right_frame.grid(row=0, column=1, sticky="nsew")

columns = ("Root №", "[x(i); x(i+1)]", "x", "f(x)", "Number of iterations", "Error code")
tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=10)

tree.heading("Root №", text="Root №")
tree.heading("[x(i); x(i+1)]", text="[x(i); x(i+1)]")
tree.heading("x", text="x")
tree.heading("f(x)", text="f(x)")
tree.heading("Number of iterations", text="Number of iterations")
tree.heading("Error code", text="Error code")

tree.grid(row=0, column=0, sticky="nsew")


root.mainloop()
