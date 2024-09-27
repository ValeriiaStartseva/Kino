//
// function imageUploadInput() {
//     document.getElementById('imageUploadInput').click();
// }
//
// function add_img(inputId, previewId) {
//     const imgInput = document.getElementById(inputId);
//     const imgPreview = document.getElementById(previewId);
//
//     const file = imgInput.files[0];
//     if (file) {
//         const reader = new FileReader();
//         reader.onload = function(e) {
//             imgPreview.src = e.target.result;
//         };
//         reader.readAsDataURL(file);
//     }
// }
//
//     function updateFileName() {
//         const input = document.getElementById('imageInput');
//         const fileNameSpan = document.getElementById('fileName');
//         if (input.files.length > 0) {
//             fileNameSpan.textContent = input.files[0].name;
//         } else {
//             fileNameSpan.textContent = 'Файл не обраний';
//         }
//     }
//
//
//
//
// // функція для отримання CSRF токену
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Відділяємо ім'я і значення куки
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// custom-scripts.js

function showImageOptions() {
    $.ajax({
        url: '/get_gallery_images/',
        method: 'GET',
        success: function(data) {
            const select = $('#imageSelect');
            select.empty();
            data.gallery_images.forEach(function(image) {
                select.append(`<option value="${image.id}" data-image-url="${image.image_url}">${image.alt_text}</option>`);
            });
        },
        error: function() {
            alert('Не вдалося завантажити зображення.');
        }
    });
}
