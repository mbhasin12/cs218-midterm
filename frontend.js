document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();

    var formData = new FormData();
    formData.append('file', document.querySelector('input[type=file]').files[0]);
   
    fetch('http://127.0.0.1:5005/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('uploadStatus').innerHTML = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
