/*
Template Name: Konrix - Responsive Tailwind Admin Dashboard
Author: CoderThemes
Website: https://coderthemes.com/
Contact: support@coderthemes.com
File: Quilljs init js
*/

// Snow theme
var quill = new Quill("#snow-editor", {
  theme: "snow",
  modules: {
    toolbar: [
      [{ font: [] },{ header: ["false", 1, 2, 3, 4, 5, 6] }],
      ["bold", "italic", "underline", "strike"],
      [{ color: [] }, { background: [] }],
      [{ script: "super" }, { script: "sub" }],
      ["blockquote", "code-block"],
      [
        { list: "ordered" },
        { list: "bullet" },
        { indent: "-1" },
        { indent: "+1" },
      ],
      ["direction", { align: [] }],
      ["link", "image", "video"],
      ["clean"],
    ],
  },
});

// Bubble theme
var quill = new Quill("#bubble-editor", {
  theme: "bubble",
});
