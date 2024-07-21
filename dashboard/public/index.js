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
    let key = event.key;
    let pyautoguiKey = keyMap[event.code] || key;
    fetch("{ip}/press?key=Test123@&type=down&content="+pyautoguiKey)
})

document.addEventListener('keyup', (event) => {
    let key = event.key;
    let pyautoguiKey = keyMap[event.code] || key;
    fetch("{ip}/press?key=Test123@&type=up&content="+pyautoguiKey)
})

document.addEventListener('mousedown', (event) => {
    fetch("{ip}/mouse_mode?key=Test123@&type=down")
});

document.addEventListener('mouseup', (event) => {
    fetch("{ip}/mouse_mode?key=Test123@&type=up")
});