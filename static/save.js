function saveToFile() {
    var content = document.getElementById('myInput').innerHTML;

    var form = document.createElement('form');
    form.action = '/save_to_file';
    form.method = 'POST';

    var hiddenField = document.createElement('input');
    hiddenField.type = 'hidden';
    hiddenField.name = 'content';
    hiddenField.value = content;

    form.appendChild(hiddenField);
    document.body.appendChild(form);

    form.submit();
}


function hidesave() {
    var content = document.getElementById('myInput').innerText;

    var form = document.createElement('form');
    form.action = '/input';
    form.method = 'POST';

    var hiddenField = document.createElement('input');
    hiddenField.type = 'hidden';
    hiddenField.name = 'content';
    hiddenField.value = content;

    form.appendChild(hiddenField);
    document.body.appendChild(form);

    form.submit();
}