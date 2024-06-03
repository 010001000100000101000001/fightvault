document.addEventListener('DOMContentLoaded', (event) => {
    const stars = document.querySelectorAll('.star-rating input');

    stars.forEach(star => {
        star.addEventListener('change', (e) => {
            const rating = e.target.value;
            submitRating(rating);
        });
    });

 // Menu toggle functionality
    const menuToggle = document.getElementById('menuToggle');
    const closeMenu = document.getElementById('closeMenu');
    const sideMenu = document.getElementById('sideMenu');

    menuToggle.addEventListener('click', () => {
        openNav();
    });

    closeMenu.addEventListener('click', () => {
        closeNav();
    });

    function openNav() {
        sideMenu.style.width = "100%";
        document.body.classList.add('open-sidebar');
    }

    function closeNav() {
        sideMenu.style.width = "0";
        document.body.classList.remove('open-sidebar');
    }
});

function submitRating(rating) {
    const form = document.getElementById('rating-form');
    const csrfToken = getCookie('csrftoken');

    const formData = new FormData(form);
    formData.append('rating', rating);

    fetch(form.action, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.average_rating) {
            document.querySelector('.average-rating').innerText = `Average Rating: ${data.average_rating} out of 5`;
        }
    })
    .catch(error => console.error('Error:', error));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
