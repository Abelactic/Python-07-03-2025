import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Animación GIF")
root.configure(bg="#b1ff96")


gif = Image.open("imagenes/bienvenida_git.gif")


frames = []
for i in range(gif.n_frames):
    gif.seek(i)
    frame = gif.copy()
    frames.append(ImageTk.PhotoImage(frame))


frame_container = tk.Frame(root, bg="#b1ff96")
frame_container.pack()

message_label = tk.Label(frame_container, text="Gracias por descargarme :)",
                         font=("Arial", 20, "bold"), bg="#b1ff96")
message_label.pack()


gif_label = tk.Label(frame_container, bg="#b1ff96")
gif_label.pack()


def update(ind):
    frame = frames[ind]
    gif_label.configure(image=frame)
    root.after(100, update, (ind+1) % len(frames))  # 100 ms por frame


update(0)

root.mainloop()
