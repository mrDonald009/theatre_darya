'use strict';
//меню гамбургер
window.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.nav-menu'),
        menuItem = document.querySelectorAll('.nav-menu__list-item'),
        hamburger = document.querySelector('.hamburger');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('hamburger_active');
        menu.classList.toggle('nav-menu_active');
    });

    menuItem.forEach((item) => {
        item.addEventListener('click', () => {
            hamburger.classList.toggle('hamburger_active');
            menu.classList.toggle('nav-menu_active');
        });
    });
});

//плавный скролл
function addSmoothScroll(anchor) {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth',
        });
    });
}

document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    addSmoothScroll(anchor);
});

//плавный переход с кнопки в первой секции "Записаться в группу"
addSmoothScroll(document.querySelector('.btn-contacts'));
//плавный переход с кнопки в третей секции "Записаться в группу"
addSmoothScroll(document.querySelector('.btn-contacts2'));

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form');
    form.addEventListener('submit', formSend);

    async function formSend(e) {
        e.preventDefault();

        let error = formValidate(form);

        let formData = new FormData(form);

        if (error === 0) {
            let newElement = document.querySelector('.five-section');
            newElement.classList.add('_sending');
            let response = await fetch('sendmail.php', {
                method: 'POST',
                body: formData,
            });
            if (response.ok) {
                let result = await response.json();
                alert(result.message);
                formPreview.innerHTML = '';
                form.reset();
                newElement.classList.remove('_sending');
            } else {
                alert('Ошибка');
                newElement.classList.remove('_sending');
            }
        } else {
            alert('Заполните обязательные поля');
        }
    }

    function formValidate(form) {
        let error = 0;
        let formReq = document.querySelectorAll('._req');

        for (let index = 0; index < formReq.length; index++) {
            const input = formReq[index];
            formRemoveError(input);

            if (input.classList.contains('_email')) {
                if (emailTest(input)) {
                    formAddError(input);
                    error++;
                }
            } else if (
                input.getAttribute('type') === 'checkbox' &&
                input.checked === false
            ) {
                formAddError(input);
                error++;
            } else {
                if (input.value === '') {
                    formAddError(input);
                    error++;
                }
            }
        }
        return error;
    }

    function formAddError(input) {
        input.parentElement.classList.add('_error');
        input.classList.add('_error');
    }
    function formRemoveError(input) {
        input.parentElement.classList.remove('_error');
        input.classList.remove('_error');
    }
    //ф-я теста проверки почты
    function emailTest(input) {
        return !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,8})+$/.test(
            input.value
        );
    }
});
