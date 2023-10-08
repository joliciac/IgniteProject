const toggleButton = document.getElementById('toggleButton');
const qaContainer = document.getElementById('qaContainer');

toggleButton.addEventListener('click', () => {
    qaContainer.classList.toggle('hidden');
});