from tkinter import *

root = Tk()
root.geometry("500x350")
root.config(bg="lawn green")


def url_slicer(url):
    if not url:  # Check for Empty Input
        pass
    else:
        security = "No Info"
        if "http" in url:
            # If user enters url with http part
            security = url.split(":/")[0]
            sliced_url = url.split("/")[2]
        else:
            # If user enters url without http part
            if url[0] == "/":
                url = url.strip("/")
            sliced_url = url.split("/")[0]

        security_val.set(security)
        slice_url.set(sliced_url)


Label(root, text="Enter URL : ", font=("Bahnschrift Semilight Condensed", 22), bg="lawn green").place(x=70, y=50)
Label(root, text="Security : ", font=("Bahnschrift Semilight Condensed", 22), bg="lawn green").place(x=70, y=120)
Label(root, text="Sliced URL : ", font=("Bahnschrift Semilight Condensed", 22), bg="lawn green").place(x=70, y=190)

url_val = StringVar()
slice_url = StringVar()
security_val = StringVar()

Entry(root, textvariable=url_val, font=("Bahnschrift Semilight Condensed", 18), width=25, bd=4).place(x=200, y=55)
Entry(root, textvariable=security_val, state="readonly", font=("Bahnschrift Semilight Condensed", 18), width=25,
      bd=4).place(x=200, y=125)
Entry(root, textvariable=slice_url, state="readonly", font=("Bahnschrift Semilight Condensed", 18),
      width=25, bd=4).place(x=200, y=195)

Button(root, text="Slice URL", font=("Bahnschrift Semibold Condensed", 20), fg="lawn green", bg="royalblue1",
       command=lambda: url_slicer(url_val.get().strip())).place(x=190, y=260)

root.mainloop()
