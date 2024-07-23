var resolution=[0,0]
async function fetchAndReplaceImage(i) {
        try {
            var response = await fetch(ip.Value()+"?key="+password.Value()+"&q="+String(i));
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            var blob = await response.blob();
            var imageUrl = URL.createObjectURL(blob);
            var imgElement = document.getElementById("screen");
            var tempImg = new Image();
            tempImg.src = imageUrl;
            tempImg.onload = function() {
                resolution=[tempImg.width, tempImg.height]
            };
            imgElement.src = imageUrl;
        } catch (error) {
            throw error
        }
}

(async ()=>{
    var i=0
    while (true) {
        i+=1
        try {
            await fetchAndReplaceImage(i)
        } catch {
            break
        }
    }
})()
var lastMouse=true
document.getElementById("screen").addEventListener("mousemove", ()=>{
    if (!controlsActive.Value()) {
        return
    }
    if (document.getElementById("screen").src!="https://placehold.co/600x400" && lastMouse) {
        var rect = document.getElementById("screen").getBoundingClientRect();
        var x = event.clientX - rect.left;
        var y = event.clientY - rect.top;
        var widthRatio = resolution[0] / rect.width;
        var heightRatio = resolution[1] / rect.height;
        var originalX = Math.round(x * widthRatio);
        var originalY = Math.round(y * heightRatio);
        lastMouse=false
        fetch(ip.Value()+"/mouse?key="+password.Value()+"&x="+String(originalX)+"&y="+String(originalY)).then(async ()=>{
            lastMouse=true
        })
    }
})

var keyMap = {
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
    if (controlsActive.Value()) {
        if (event.code === 'Space') {
            event.preventDefault()
        }
        let key = event.key;
        let pyautoguiKey = keyMap[event.code] || key;
        fetch(ip.Value()+"/press?key="+password.Value()+"&type=down&content="+pyautoguiKey)
    }
})

document.addEventListener('keyup', (event) => {
    if (controlsActive.Value()) {
        if (event.code === 'Space') {
            event.preventDefault()
        }
        let key = event.key;
        let pyautoguiKey = keyMap[event.code] || key;
        fetch(ip.Value()+"/press?key="+password.Value()+"&type=up&content="+pyautoguiKey)
    }
})

function onScreen(event) {
    var toReturn=false
    try {
        var rect = document.getElementById("screen").getBoundingClientRect();
        var x = event.clientX - rect.left;
        var y = event.clientY - rect.top;
        var widthRatio = resolution[0] / rect.width;
        var heightRatio = resolution[1] / rect.height;
        var originalX = Math.round(x * widthRatio);
        var originalY = Math.round(y * heightRatio);
        return originalX>=0 && originalY>=0
    } catch {
        toReturn=true
    }
    if (toReturn) {
        return false
    }
}

document.addEventListener('mousedown', (event) => {
    if (onScreen(event) && controlsActive.Value()) {
        fetch(ip.Value()+"/mouse_mode?key="+password.Value()+"&type=down")
    }
})

document.addEventListener('mouseup', (event) => {
    if (onScreen(event) && controlsActive.Value()) {
        fetch(ip.Value()+"/mouse_mode?key="+password.Value()+"&type=up")
    }
})

document.getElementById("screen").addEventListener("contextmenu", (event)=>{
    event.preventDefault()
    if (controlsActive.Value()) {
        fetch(ip.Value()+"/right_click?key="+password.Value())
    }
})