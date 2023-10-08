var myHeaders = new Headers();
myHeaders.append("Authorization", "Basic ZXhhbXBsZV91c2VybmFtZTpleGFtcGxlX3Bhc3N3b3Jk");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("http://127.0.0.1:5000/interview_questions?topic=Caution", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));



const cautionbutton = document.getElementById('cautionbutton');
const cautionele = document.getElementById("cautionele");

cautionbutton.addEventListener('click', () => {
  fetch('http://127.0.0.1:5000/interview_questions?topic=Caution')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
    
      const randomQuestion3 = data;

      cautionele.textContent = `${randomQuestion3.question}`;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
