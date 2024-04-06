// document.addEventListener("DOMContentLoaded", function () {
//   var form = document.getElementById("contactForm");

//   console.log(form);

//   form.addEventListener("submit", function (event) {
//     var nameInput = document.getElementById("name");
//     var emailInput = document.getElementById("email");
//     var messageInput = document.getElementById("message");

//     // Check if any input field is empty
//     if (!nameInput.value || !emailInput.value || !messageInput.value) {
//       alert("Please fill in all fields.");
//       event.preventDefault(); // Prevent form submission
//     } else {
//       // Additional validation can be added here (e.g., email format)
//       alert("Form submitted successfully!");
//     }
//   });
// });
// static/script.js
// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("contactForm");

//   form.addEventListener("submit", function (event) {
//     event.preventDefault();

//     submitForm();
//     alert("Form submitted successfully!");
//   });

//   function submitForm() {
//     fetch("/contact", {
//       method: "POST",
//       body: new FormData(form),
//     })
//       .then((response) => response.text())
//       .then((data) => {
//         console.log(data);
//       })
//       .catch((error) => console.error("Error:", error));
//   }
// });

function deleteValue(button) {
  var parentDiv = button.parentNode;

  var span = parentDiv.getElementsByTagName("span")[0];
  var value = span.textContent;

  fetch("/delete", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "value=" + encodeURIComponent(value),
  })
    .then((response) => {
      if (response.ok) {
        console.log(response);
        return response.json();
      } else {
        throw new Error("Failed to delete value");
      }
    })
    .then((data) => {
      // Update the page content with the updated data
      // For example, update a table or list with the new data
      console.log("Data after deletion:", data);
    })
    .catch((error) => {
      console.error("Error deleting value:", error);
    });
}
