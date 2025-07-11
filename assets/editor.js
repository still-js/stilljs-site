document.addEventListener("DOMContentLoaded", function () {
    // Initialize CodeMirror Editor
    let editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
        mode: "javascript",
        lineNumbers: true,
        theme: "dracula", // Theme for better contrast
        tabSize: 2,
        autoCloseBrackets: true
    });

    // Simulated file system
    let files = {
        "main.js": "// Welcome to your file-based editor!\nconsole.log('Hello, World!');"
    };
    let currentFile = "main.js";

    // Function to update the file list
    function updateFileList() {
        let fileList = document.getElementById("file-list");
        fileList.innerHTML = "";
        Object.keys(files).forEach(filename => {
            let li = document.createElement("li");
            li.textContent = filename;
            li.style.cursor = "pointer";
            li.style.padding = "5px";
            li.onclick = () => openFile(filename);
            fileList.appendChild(li);
        });
    }

    // Open file and load content in editor
    function openFile(filename) {
        currentFile = filename;
        editor.setValue(files[filename]);
    }

    // Create a new file
    window.createFile = function () {
        let filename = prompt("Enter new file name (e.g., script.js):");
        if (filename && !files[filename]) {
            files[filename] = "// New file: " + filename + "\n";
            updateFileList();
            openFile(filename);
        }
    };

    // Save editor content on change
    editor.on("change", () => {
        files[currentFile] = editor.getValue();
    });

    updateFileList();
    openFile(currentFile);
});
