function handleClick() {
    alert("Вы нажали на кнопку");
}

window.onload = function() {
    console.log('Страница загрузилась');
    document.getElementById('button').addEventListener('click', handleClick);
}