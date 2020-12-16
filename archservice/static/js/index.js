const checkBox = document.getElementById("customgrid");
const lenghtblock = document.getElementById("lenghtblock");
const stepblock = document.getElementById("stepblock");
const grid_block = document.getElementById("grid_block");
const lenght = document.getElementById("lenght");
const step = document.getElementById("step");

//Show input error mesage
function showError(input, message) {
  const formElement = input.parentElement;
  formElement.className = "form-element error";
  const small = formElement.querySelector("small");
  small.innerText = message;
}

//In case of success don't show error
function showSuccess(input) {
  const formElement = input.parentElement;
  formElement.className = "form-element";
}

function showGridSelection() {
  // If the checkbox is checked, display
  if (checkBox.checked === true) {
    lenghtblock.style.display = "block";
    stepblock.style.display = "block";
    grid_block.style.display = "none";
  } else {
    lenghtblock.style.display = "none";
    stepblock.style.display = "none";
    grid_block.style.display = "block";
  }
}

// check field
function checkField(input, min, max) {
  if (isEmpty(input)) {
    showError(input, "Поле обов'язкове для заповнення");
    return false;
  }

  if (!checkMinValue(input, min)) {
    showError(input, `Має бути більше ${min}`);
    return false;
  }

  if (!checkMaxValue(input, max)) {
    showError(input, `Має бути менше ${max}`);
    return false;
  }

  showSuccess(input);
  return true;
}

// check if field is empty
function isEmpty(input) {
  if (input.value.trim() == "") {
    return true;
  }
  return false;
}

// Check min length
function checkMinValue(input, min) {
  if (+input.value < min) {
    return false;
  }
  return true;
}

// Check max length
function checkMaxValue(input, max) {
  if (+input.value > max) {
    return false;
  }
  return true;
}

function validateForm() {
  if (checkBox.checked === true) {
    var checkArr = [checkField(lenght, 3, 24), checkField(step, 3, 24)];
    let checker = (arr) => arr.every((v) => v === true);
    return checker(checkArr);
  } else {
    return true;
  }
}
