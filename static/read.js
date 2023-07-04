
function readTextFile() {
    var fileInput = document.createElement("input");
    fileInput.type = "file";
    
    fileInput.addEventListener("change", function(event) {
      var file = event.target.files[0];
      var reader = new FileReader();
      
      reader.onload = function(event) {
        var contents = event.target.result;
        var resultDiv = document.getElementById("myInput");
        resultDiv.innerHTML = contents;
      };
      
      reader.readAsText(file);
    });
    
    fileInput.click();
  }