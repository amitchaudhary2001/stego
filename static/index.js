
function copyToClipboard(element) {
  var copyText = document.getElementById("myInput").innerHTML;
  navigator.clipboard.writeText(copyText);
}

function myFunction() {
  const paragraph = document.getElementById("myInput");
  const edit_button = document.getElementById("edit-button");
  const end_button = document.getElementById("end-editing");
  edit_button.addEventListener("click", function () {
paragraph.className="container"
    paragraph.contentEditable = true;
    paragraph.style.backgroundColor = "#dddbdb";
  });

  end_button.addEventListener("click", function () {
    paragraph.contentEditable = false;
    paragraph.style.backgroundColor = "#829be8";
  })
}


function setImage() {
  var imageContainer = document.getElementById('imageContainer');
  var image1 = new Image();
  var image2 = new Image();

  image1.src = 'image1.jpg';
  image2.src = 'image2.jpg';
  
  image1.onload = function() {
      imageContainer.innerHTML = '<img src="' + image1.src + '"height="300" alt="Image 1">';
  };

  image1.onerror = function() {
      imageContainer.innerHTML = '<img src="' + image2.src + '" height="300"alt="Image 2">';
  };
}


function getRandomImage() {
  var imageUrls = [
      'static\images\image1\image1.jpg',
      'static\images\image1\image2.jpg',
      'static\images\image1\image3.jpg',
      'static\images\image1\image4.jpg'
      // Add more image URLs as needed
  ];

  var randomIndex = Math.floor(Math.random() * imageUrls.length);
  var randomImage = imageUrls[randomIndex];

  var imageContainer = document.getElementById('imageContainer');
  imageContainer.innerHTML = '<img src="' + randomImage + '" alt="Random Image">';
}
