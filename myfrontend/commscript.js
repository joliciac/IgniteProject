var myHeaders = new Headers();
myHeaders.append("Authorization", "Basic ZXhhbXBsZV91c2VybmFtZTpleGFtcGxlX3Bhc3N3b3Jk");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("http://127.0.0.1:5000/interview_questions?topic=Communication", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));

/*
 1. make a function to fetch the q
 2. get button by id ==> document.getElementBy..
 3. button.addEvevent (onclikc, func)
*/
// function getcomms() {
//   fetch("http://127.0.0.1:5000/interview_questions?topic=Communication", requestOptions)
//   .then(response => response.json())
//   .then(result => console.log(result))
//   .catch(error => console.log('error', error));
// }

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
