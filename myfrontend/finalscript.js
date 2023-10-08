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



const commsbutton = document.getElementById('commsbutton');
const outputElement = document.getElementById("output");

commsbutton.addEventListener('click', () => {
  fetch('http://127.0.0.1:5000/interview_questions?topic=Communication')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
    
      const randomQuestion = data;

      outputElement.textContent = `${randomQuestion.question}`;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
