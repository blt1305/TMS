var counter = 0;
function handleClick() {
    alert("Вы нажали на кнопку");
    counter += 1;
    console.log('Мы нажали кнопку ' + counter + ' раз(а)');
    document.getElementsByTagName('span')[0].textContent = counter
};

window.onload = function() {
    console.log('Страница загрузилась');
    document.getElementById('button').addEventListener('click', handleClick);
};