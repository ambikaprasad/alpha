document.querySelector('#amb').addEventListener('click', function(e) {

    e.preventDefault();
    this.classList.toggle('opened');
    window.location.href = document.referrer;
});
