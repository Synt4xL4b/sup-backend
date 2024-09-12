document.addEventListener('DOMContentLoaded', function () {
    const openModalButton = document.getElementById('open-modal');
    const closeModalButton = document.getElementById('close-modal');
    const modal = document.getElementById('modal');
    const form = document.getElementById('create-meet-form');

    // Открытие модального окна
    if (openModalButton) {
        openModalButton.addEventListener('click', function () {
            modal.classList.remove('hidden');
        });
    }

    // Закрытие модального окна
    if (closeModalButton) {
        closeModalButton.addEventListener('click', function () {
            modal.classList.add('hidden');
        });
    }

    // Обработка отправки формы
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            let formData = new FormData(this);

            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Закрываем модальное окно и обновляем список митов
                    modal.classList.add('hidden');
                    // Здесь можно добавить код для обновления списка митов
                    console.log('Meet успешно создан');
                } else {
                    console.error('Ошибка при создании Meet:', data.error);
                }
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
        });
    }
});
