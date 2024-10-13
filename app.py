import tkinter as tk

# Functia realizeaza computatia masinii si afiseaza starile prin care trece, iar la final daca este cazul
# decizia acesteia cu privire la input.
def update_turing(i, curr_state, state_list, name, init, accept, instructions):
    global is_running
    global paused

    if paused == False:
        # Afisare stare
        clear_canvas_turing()
        start = i - 15
        stop = i + 15
        j = start
        for id in turing_ids:
            txt = ""
            if j < 0 or j >= len(state_list) or state_list[j] == "_":
                txt = ""
            else:
                txt = str(state_list[j])
            j += 1
            canvas_turing.itemconfig(id, text = txt)
        # Sfarsit afisare
        
        # Se calculeaza urmatoarea stare si se modifica secventa.
        key = str(curr_state) + ',' + str(state_list[i])
        if key not in instructions:
            canvas_output.itemconfig(output_id, text="Rejected!")
            run_calcel_button.config(text = "Run")
            is_running = not is_running
            return
        next_instruction = instructions[key]
        comp = next_instruction.split(",")
        state_list[i] = comp[1]
        if comp[2] == ">":
            i += 1
        if comp[2] == "<":
            i -= 1
        if i > len(state_list) - 1:
            state_list.append("_")
        if i < 0:
            state_list.insert(0, "_")
            i = 0
        curr_state = comp[0]
        if curr_state == accept:
            canvas_output.itemconfig(output_id, text="Accepted!")
            run_calcel_button.config(text = "Run")
            pause_button.config(text = "Pause")
            is_running = not is_running
            return

    # Daca se apasa cancel.
    if is_running == False:
        i = 15
        clear_canvas_turing()
        paused = False
        pause_button.config(text = "Pause")
        for char in load_list:
            canvas_turing.itemconfig(turing_ids[i], text=char)
            i += 1
            if i > 30:
                break
        return
    else:
        # Se apeleaza cu intrerupere recursiv functia de update.
        canvas_turing.after(speed_time, update_turing, i, curr_state, state_list, name, init, accept, instructions)


# Functia porneste computatia si extrage toate infromatiile necesare acesteia.
def compute_display():
    global turing_ids
    global canvas_turing
    state_list = []
    for x in load_list:
        state_list.append(x)
    name = compiled_code[0]
    init = compiled_code[1]
    accept = compiled_code[2]
    instructions = compiled_code[3]
    i = 0
    curr_state = init
    update_turing(i, curr_state, state_list, name, init, accept, instructions)


# Functia schimba starea de run sau pause a masinii.
def change_pause():
    global paused
    global is_running
    if is_running == False:
        return
    if paused == True:
        pause_button.config(text = "Pause")
    else:
        pause_button.config(text = "Continue")
        canvas_output.itemconfig(output_id, text="Paused")
    paused = not paused
        
    
# Functia schimba starea de canceled in stare de running si invers.
def play():
    global is_running
    if len(load_list) == 0:
        return
    is_running = not is_running
    if is_running is False:
        canvas_output.itemconfig(output_id, text="Canceled!")
        run_calcel_button.config(text = "Run")
    else:
        canvas_output.itemconfig(output_id, text="Running!")
        run_calcel_button.config(text = "Cancel")
        compute_display()


# Citeste viteaza de computatie de la user.
def get_speed():
    global speed_time
    speed = speed_slider.get()
    speed_time = 1000 - speed * 10 + 10
    speed_slider.after(100, get_speed)

# Elemente grafice initializate ce se modifica in mod dinamic in timpul rularii programului.
root = tk.Tk()
canvas_output = tk.Canvas(root, width=1000, height=100, bg="black", highlightthickness=0)
canvas_name = tk.Canvas(root, width=1000, height=100, bg="black", highlightthickness=0)
canvas_turing = tk.Canvas(root, width=1550, height=50, bg="blue")
input_box = tk.Entry(root, bg="grey", fg="black", font=("Helvetica", 18))
frame = tk.Frame(root, width=500, height=300, bg="lightblue")
text_box = tk.Text(frame, bg="#333441", fg="black", font=("Helvetica", 16), wrap=tk.WORD)
run_calcel_button = tk.Button(root, text="Run", command=play)
pause_button = tk.Button(root, text="Pause", command=change_pause)

# Glider pentru speed.
speed_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300, bg="black", label="Speed", fg="white")

# Liste si variabile ce contin informoatii despre starea si datele programului.
load_list = []
compiled_code = []
turing_ids = []
is_running = False
paused = False
output_id = None
name_id = None
speed_time = 1000


def initial_setup():
    # Id-ul casutei text pentru output.
    global output_id
    global name_id
    # Configurari ale ferestrei.
    root.title("Turing Machine")
    root.configure(bg="black")
    root.geometry("1550x800")

    get_speed()

    # Titlul.
    canvas_title = tk.Canvas(root, width=1000, height=100, bg="black", highlightthickness=0)
    canvas_title.place(x=250, y=25)
    text_id = canvas_title.create_text(500, 50, text="Turing Machine Simulator", fill="white", font=("Helvetica", 35))

    # Configurarea casutei text pentru output.
    canvas_output.place(x=700, y=100)
    output_id = canvas_output.create_text(500, 50, text="", fill="green", font=("Helvetica", 25))
    
    # Configurarea casutei text in care se afiseaza numele masinii.
    canvas_name.place(x=0, y=100)
    name_id = canvas_name.create_text(0, 50, text="Name:", fill="green", font=("Helvetica", 20), anchor="w")


    # Configurarea benzii masinii turing.
    canvas_turing.place(x=0, y=200)
    x0, y0 = 2, 2
    x1, y1 = 50, 50
    for i in range(0, 31):
        canvas_turing.create_rectangle(x0, y0, x1, y1, outline="black", fill="red", width=2)
        text_id = canvas_turing.create_text(x0 + 25, y0 + 25, text="", fill="white", font=("Helvetica", 30))
        turing_ids.append(text_id)
        x0 += 50
        x1 += 50

    # Configurarea si crearea cursorului.
    x0, y0 = 25, 0
    x1, y1 = 0, 50
    x2, y2 = 50, 50
    canvas_triangle = tk.Canvas(root, width=50, height=50, bg="black", highlightthickness=0)
    canvas_triangle.place(x=750, y=270)
    canvas_triangle.create_polygon(x0, y0, x1, y1, x2, y2, outline="black", fill="blue", width=2)

    # Configurarea glider-ului pentru viteza computatiei.
    speed_slider.place(x=1000, y=300)


    # Configurarea text_box-ului pentru descrierea masinii.
    frame.place(x=975, y=450)
    text_box.place(x=0, y=0, width=500, height=300)
    scrollbar = tk.Scrollbar(frame, command=text_box.yview)
    scrollbar.place(x=485, y=0, height=300)
    text_box.config(yscrollcommand=scrollbar.set)

    # Crearea si configurarea butonului compile.
    compile_button = tk.Button(root, text="Compile", command=compile_instructions)
    compile_button.place(x=975, y=750)

    # Configurarea casetei de input.
    input_box.place(x=100, y=400, width=200, height=35)

    # Crearea si configurarea butonului load.
    load_button = tk.Button(root, text="Load", command=load_input)
    load_button.place(x=302, y=402)

    # Configurarea butonului run/calcel.
    run_calcel_button.place(x=749, y=330)
    pause_button.place(x=749, y=370)


# Functia este folsita pentru a curata banda masinii turing atunci cand este nevoie(de obicei pentru a afisa urmatoarea stare).
def clear_canvas_turing():
    global canvas_turing
    for i in range(0, 31):
        canvas_turing.itemconfig(turing_ids[i], text="")


# Functia se apeleaza atunci cand se apasa butonul load, afiseaza secventa de input pe banda si salveaza in "load_list"
# secventa de input.
def load_input():
    # Banda masinii.
    global canvas_turing
    # Lista in care se salveaza input-ul.
    global load_list
    global is_running
    if is_running == True:
        return
    input = input_box.get()
    load_list = list(input)
    clear_canvas_turing()
    i = 15
    for char in load_list:
        canvas_turing.itemconfig(turing_ids[i], text=char)
        i += 1
        if i > 30:
            break
    if len(load_list) != 0:
        canvas_output.itemconfig(output_id, text="Loaded")
    else:
        canvas_output.itemconfig(output_id, text="Input is missing")


# Functia se apeleaza atunci cand se apasa butonul compile si extrage in lista "compile_code" toate informatiile necesare
# din descrierea masinii.
def compile_instructions():
    # Lista unde se salveaza informatia.
    global compiled_code
    global is_running
    if is_running == True:
        return
    try:
        # Se parseaza descrierea eliminandu-se comentariile si spatiile si newline-urile.
        compiled_code = []
        description = text_box.get("1.0", tk.END)
        filtered_description = [line for line in description.splitlines() if not line.strip().startswith("//")]
        description = "\n".join(filtered_description)

        instruction_list_first = description.split("\n")
        instruction_list = [elem for elem in instruction_list_first if elem != "" and elem != " "]
        name = instruction_list[0].split(" ")[1]
        init = instruction_list[1].split(" ")[1]
        accept = instruction_list[2].split(" ")[1]

        compiled_code.append(name)
        compiled_code.append(init)
        compiled_code.append(accept)
        instructions = {}
        i = 3
        while (i < len(instruction_list)):
            instructions[instruction_list[i]] = instruction_list[i + 1]
            i += 2
        compiled_code.append(instructions)
        canvas_output.itemconfig(output_id, text="Compiled")
        canvas_name.itemconfig(name_id, text = "Name: " + name, anchor="w")
    except Exception as e:
        canvas_output.itemconfig(output_id, text="Compile error!")


# Main-ul programului.
if __name__ == '__main__':
    # Se construiesc elementele grafice folosite in reprezentare.
    initial_setup()
    # Se porneste fereastra ce ruleaza in continuu.
    root.mainloop() 
