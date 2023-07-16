// Previewing the title and caption
var titleInput = document.getElementById("title-input"),
    captionInput = document.getElementById("caption-input");

var previewTitle = document.getElementById("preview-title"),
    previewCaption = document.getElementById("preview-caption");

titleInput.addEventListener("input",function(){
    previewTitle.innerText = titleInput.value;
});

captionInput.addEventListener("input",function(){
    previewCaption.innerText = captionInput.value;
});



// Previewing the image
var imageInput = document.getElementById("image-input");
var previewImage = document.getElementById("preview-image");

imageInput.addEventListener("change", function(event){
     if (event.target.files.length == 0){
        return;
     }
     var tempUrl = URL.createObjectURL(event.target.files[0]);
     previewImage.setAttribute("src",tempUrl);
});



