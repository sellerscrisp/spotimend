'use strict';

// function getToggleLikeAPI(msgId) {
//     return `/api/messages/${msgId}/toggle_like`
// }

// async function toggleLike(evt) {
//     let icon = $(evt.target);
//     let msgId = icon.data('msg-id');
//     const API = getToggleLikeAPI(msgId);
//     let resp = await axios.post(API)

//     if (resp.data.message === 'Bad like' || resp.status === 401) {
//         return;
//     }

//     icon.toggleClass('far');
//     icon.toggleClass('fas');
// }

$('#heart').on('click', function () {
    $('#heart i')
        .addClass('far-heart')
});
// $('#messages').on('click', '.fa-heart', toggleLike);

// let songModal = document.getElementById('song_modal')
// let songInput = document.getElementById('song_input')

// myModal.addEventListener('shown.bs.modal', function () {
//     songInput.focus();
// })

// $('#song_modal').on('show.bs.modal', function (event) {
//     var button = $(event.relatedTarget) // Button that triggered the modal
//     var recipient = button.data('whatever') // Extract info from data-* attributes
//     // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
//     // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
//     var modal = $(this)
//     modal.find('.modal-title').text('New message to ' + recipient)
//     modal.find('.modal-body input').val(recipient)
// })


$(document).ready(function () {
    $("#myModal").modal();
});

let popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
let popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
})

let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})