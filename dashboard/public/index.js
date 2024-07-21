const keyMap = {
    'Backspace': 'backspace',
    'Tab': 'tab',
    'Enter': 'enter',
    'Shift': 'shift',
    'Control': 'ctrl',
    'Alt': 'alt',
    'Pause': 'pause',
    'CapsLock': 'capslock',
    'Escape': 'esc',
    'Space': 'space',
    'PageUp': 'pageup',
    'PageDown': 'pagedown',
    'End': 'end',
    'Home': 'home',
    'ArrowLeft': 'left',
    'ArrowUp': 'up',
    'ArrowRight': 'right',
    'ArrowDown': 'down',
    'PrintScreen': 'printscreen',
    'Insert': 'insert',
    'Delete': 'delete',
    'Meta': 'win',
    'ContextMenu': 'menu'
    // Add more key mappings as needed
};

for (let i = 0; i <= 9; i++) {
    keyMap[`Digit${i}`] = `${i}`;
}

for (let i = 1; i <= 12; i++) {
    keyMap[`F${i}`] = `f${i}`;
}

document.addEventListener('keydown', (event) => {
    if (event.code === 'Space') {
        event.preventDefault()
    }
    let key = event.key;
    let pyautoguiKey = keyMap[event.code] || key;
    fetch("{ip}/press?key=Test123@&type=down&content="+pyautoguiKey)
})

document.addEventListener('keyup', (event) => {
    if (event.code === 'Space') {
        event.preventDefault()
    }
    let key = event.key;
    let pyautoguiKey = keyMap[event.code] || key;
    fetch("{ip}/press?key=Test123@&type=up&content="+pyautoguiKey)
})

function onScreen(event) {
    const rect = document.getElementById("screen").getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    const widthRatio = resolution[0] / rect.width;
    const heightRatio = resolution[1] / rect.height;
    const originalX = Math.round(x * widthRatio);
    const originalY = Math.round(y * heightRatio);
    return originalX>=0 && originalY>=0
}

document.addEventListener('mousedown', (event) => {
    if (onScreen(event)) {
        fetch("{ip}/mouse_mode?key=Test123@&type=down")
    }
})

document.addEventListener('mouseup', (event) => {
    if (onScreen(event)) {
        fetch("{ip}/mouse_mode?key=Test123@&type=up")
    }
})

document.getElementById("screen").addEventListener("contextmenu", (event)=>{
    event.preventDefault()
    fetch("{ip}/right_click?key=Test123@")
})