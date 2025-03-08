import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Animación GIF")
root.configure(bg="#b1ff96")  # Color de fondo

# Cargar el GIF
gif = Image.open("imagenes/bienvenida_git.gif")

# Obtener todos los frames correctamente
frames = []
for i in range(gif.n_frames):
    gif.seek(i)  # Moverse al frame i
    frame = gif.copy()  # Hacer una copia del frame actual
    frames.append(ImageTk.PhotoImage(frame))  # Convertir a formato Tkinter

# Crear un frame contenedor con fondo
frame_container = tk.Frame(root, bg="#b1ff96")
frame_container.pack()

# Etiqueta con el mensaje
message_label = tk.Label(frame_container, text="Gracias por descargarme :)",
                         font=("Arial", 14, "bold"), bg="#b1ff96")
message_label.pack()

# Etiqueta para la animación del GIF
gif_label = tk.Label(frame_container, bg="#b1ff96")
gif_label.pack()

# Función para actualizar la animación


def update(ind):
    frame = frames[ind]
    gif_label.configure(image=frame)
    root.after(100, update, (ind+1) % len(frames))  # 100 ms por frame


# Iniciar la animación
update(0)

root.mainloop()
