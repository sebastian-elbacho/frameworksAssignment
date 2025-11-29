// frontend script

// Real-time password validation on registration form
document.addEventListener("DOMContentLoaded", function () {
  const passwordInput = document.getElementById("id_password");
  const passwordHelp = document.getElementById("passwordHelp");

  if (passwordInput && passwordHelp) {
    passwordInput.addEventListener("input", function () {
      const value = passwordInput.value;
      let message = "";
      let isStrong = true;

      if (value.length < 8) {
        message = "Password should be at least 8 characters long.";
        isStrong = false;
      } else if (!/[0-9]/.test(value)) {
        message = "Password should contain at least one digit.";
        isStrong = false;
      } else if (!/[A-Z]/.test(value)) {
        message = "Password should contain at least one uppercase letter.";
        isStrong = false;
      } else {
        message = "Good password 👍";
      }

      passwordHelp.textContent = message;
      passwordHelp.style.color = isStrong ? "green" : "red";

      if (!isStrong) {
        passwordInput.classList.add("is-invalid");
        passwordInput.classList.remove("is-valid");
      } else {
        passwordInput.classList.remove("is-invalid");
        passwordInput.classList.add("is-valid");
      }
    });
  }

  
  const toastElList = [].slice.call(document.querySelectorAll(".toast"));
  toastElList.forEach(function (toastEl) {
    const toast = new bootstrap.Toast(toastEl);
    toast.show();
  });
});
