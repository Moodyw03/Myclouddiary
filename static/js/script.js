"use strict";

// display the success and error messages for a short time

const success = document.getElementById("success");
const error = document.getElementById("error");

function removeParam(param) {
  const url = window.location.href;
  const urlParams = new URLSearchParams(url);
  urlParams.delete(param);
  window.history.replaceState({}, "", window.location.pathname);
}

if (success) {
  setTimeout(() => {
    success.style.display = "none";

    // remove the success message from the url
    removeParam("success");
  }, 3000);
}

if (error) {
  setTimeout(() => {
    error.style.display = "none";

    // remove the error message from the url
    removeParam("error");
  }, 3000);
}
