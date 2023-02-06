from graphics import graphics


window = graphics(300,200, "Example")

window.line(10,10, 150,10, "black", 1)
window.line(10,20, 150,70, "red", 5)
window.rectangle(0,80, 100,20, "green")

print("before mainloop")
window.mainloop()
print("after mainloop")