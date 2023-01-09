
function download_mp3(token, itag=undefined, furl=undefined){
    console.log('Requst: Download');
    let fileUrl = furl==undefined? get_fileUrl() : furl
    let fileItag = itag==undefined? 0 : itag
    let data = {"itag" : fileItag, "url" : fileUrl, 'isSimpleDownload' : furl==undefined? 'true' : 'false'};
    let url = "download/download_yt_mp3";
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'blob';

    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            var blob = xhr.response;
            var a = document.createElement('a');
            a.href = window.URL.createObjectURL(blob);
            filename = xhr.getResponseHeader('Filename');
            a.download = filename
            a.dispatchEvent(new MouseEvent('click'));

            delete_mp3(token, filename);
        }
    }
    xhr.open("POST", url, true);
    xhr.setRequestHeader('Content-type', 'application/force-download');
    xhr.setRequestHeader("X-CSRFToken", token);
    xhr.send(JSON.stringify(data))
}


function delete_mp3(token, filename){
    console.log('Requst: Delete');
    let data = { "filename":filename };
    let url = "download/download_yt_mp3";
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", url, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader("X-CSRFToken", token);
    xhr.send(JSON.stringify(data))
}

function get_fileUrl(){
    return document.getElementById('url_file').value
}