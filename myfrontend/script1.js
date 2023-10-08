const toggleButton = document.getElementById('toggleButton');
const qaContainer = document.getElementById('qaContainer');

toggleButton.addEventListener('click', () => {
    qaContainer.classList.toggle('hidden');
});
const commsbutton = document.getElementById('commsbutton');
const outputElement = document.getElementById("output");
// const question = (fetch("http://127.0.0.1:5000/interview_questions?topic=Communication", requestOptions)
// .then(response => response.json())
// .then(result => console.log(result)))
// .catch(error => console.log('error', error))
// commsbutton.addEventListener(onclick,getcomms());
// commsbutton.addEventListener("click", function () {

//   outputElement.textContent = 'HI'
// });
commsbutton.addEventListener('click', () => {
  fetch('http://127.0.0.1:5000/interview_questions?topic=Communication')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      // Assuming data is a single random question
      const randomQuestion = data;

      // Display the random question
      outputElement.textContent = "Describe a situation in which you were able to effectively “read” another person and guide your actions by your understanding of their individual needs or values.";
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
