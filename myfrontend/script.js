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


