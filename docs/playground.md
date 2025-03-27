# Code Editor Example

<textarea id="editor">// Write your JavaScript code here...</textarea>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
      mode: "javascript",
      lineNumbers: true,
      theme: "default"
    });
  });
</script>

