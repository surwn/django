document.querySelector('.room-booking-form').addEventListener('submit', function(event) {
    event.preventDefault(); // отменяем стандартное поведение формы
    // обработка данных формы
    // код для вывода сообщения об успешном создании бронирования
    const successMessage = document.createElement('p');
    successMessage.textContent = 'Бронирование успешно создано!';
    successMessage.style.color = 'green';
    document.querySelector('.room-booking-form').appendChild(successMessage);
    // перенаправление на страницу оплаты
    window.location.href = "payment.html";
  }); 
  