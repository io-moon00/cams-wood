function closeImg(){
    document.getElementById('image-container').classList.add('d-none');
    document.getElementById('body').classList.remove('noscroll');
}

function openImg(imgUrl){
    document.getElementById('image-container').classList.remove('d-none');
    document.getElementById('body').classList.add('noscroll');
    document.getElementById('detail-image').src = imgUrl;
}