const socket = io()

document.addEventListener("mousemove", (e) => {
    socket.emit("mousemove", {
        x: e.clientX,
        y: e.clientY
    })
})

socket.on("updatecursors", (data) => {
    document.body.innerHTML = ""

    for (let i in data) {
        if (i != socket.id) {
            const cursor = document.createElement("img")

            cursor.style.left = data[i].x + "px"
            cursor.style.top = data[i].y + "px"
            cursor.classList.add("cursor")
            cursor.src = "static/cursor.png"

            document.body.appendChild(cursor)
        }
    }
})