function showTableStyle2() {
    document.getElementById('table-style-1').classList.add('hidden');
    document.getElementById('table-style-2').classList.remove('hidden');
    document.getElementById('style2-button').classList.add('active-button');
    document.getElementById('style1-button').classList.remove('active-button');
    document.getElementById('style2-button').classList.remove('inactive-button');
    document.getElementById('style1-button').classList.add('inactive-button');
    document.querySelector('#style2-button svg').classList.add('fill-[#40454D]');
    document.querySelector('#style1-button svg').classList.add('fill-[#FCFEFF]');
}

document.getElementById('style1-button').addEventListener('click', function() {
    document.getElementById('table-style-1').classList.remove('hidden');
    document.getElementById('table-style-2').classList.add('hidden');
    document.getElementById('style1-button').classList.add('active-button');
    document.getElementById('style2-button').classList.remove('active-button');
    document.getElementById('style1-button').classList.remove('inactive-button');
    document.getElementById('style2-button').classList.add('inactive-button');
    document.querySelector('#style1-button svg').classList.add('fill-[#40454D]');
    document.querySelector('#style2-button svg').classList.add('fill-[#FCFEFF]');
});

document.getElementById('style2-button').addEventListener('click', function() {
    document.getElementById('table-style-1').classList.add('hidden');
    document.getElementById('table-style-2').classList.remove('hidden');
    document.getElementById('style2-button').classList.add('active-button');
    document.getElementById('style1-button').classList.remove('active-button');
    document.getElementById('style2-button').classList.remove('inactive-button');
    document.getElementById('style1-button').classList.add('inactive-button');
    document.querySelector('#style2-button svg').classList.add('fill-[#40454D]');
    document.querySelector('#style1-button svg').classList.add('fill-[#FCFEFF]');
});


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

                    // Обновляем таблицу и отображаем table-style-2
                    location.reload();
                    showTableStyle2();
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




document.addEventListener('DOMContentLoaded', function() {
            const deleteButtons = document.querySelectorAll('.delete-btn');
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            deleteButtons.forEach(button => {
                button.addEventListener('click', function() {
                    const meetId = this.getAttribute('data-meet-id');
                    if (confirm('Вы уверены, что хотите удалить эту встречу?')) {
                        deleteMeet(meetId, this);
                    }
                });
            });

            function deleteMeet(meetId, buttonElement) {
                fetch(`delete-meet/${meetId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/json'
                    },
                })
                .then(response => {
                    if (response.ok) {
                        // Удаляем строку из DOM только после успешного удаления на сервере
                        buttonElement.closest('tr').remove();
                    } else {
                        throw new Error('Ошибка при удалении встречи');
                    }
                })
                .catch(error => {
                    console.error('Ошибка:', error);
                    alert('Произошла ошибка при удалении встречи');
                });
            }
        });
