const form = document.getElementById("contactForm");
const name = document.getElementById("name");
const email = document.getElementById("email");
const tel = document.getElementById("tel");
const category = document.getElementById("category");
const question = document.getElementById("question");

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

// check field
function checkField(input, min, max){
    if (is_empty(input)){
        showError(input, "Поле обов'язкове для заповнення");
        return false;
    }

    if (!check_min_Length(input, min)) {
        showError(input, `Має бути хоча б ${min} символів`);
        return false;
    }

    if (!check_max_Length(input, max)){
        showError(input, `Має бути не більше ${max} символів`);
        return false;
    }

    showSuccess(input);
    return true;
}

// chek tel
function checkTel(input, min, max){
    if (!is_empty(tel)){
        if (!check_min_Length(tel, 9)){
            showError(input, `Має бути хоча б ${min} символів`);
            return false;
        }
        if (!check_max_Length(tel, 18)){
            showError(input, `Має бути не більше ${max} символів`);
            return false;
        }
        showSuccess(input);
    }
    showSuccess(input);
    return true;
}

// Check email is valid
function checkEmail(input) {
    if (is_empty(input)){
        showError(input, "Поле обов'язкове для заповнення");
        return false;
    }

    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (re.test(input.value.trim())) {
      showSuccess(input);
      return true;
    } else {
      showError(input, "E-mail не дійсний");
      return false;
    }
  }


// check if field is empty
function is_empty(input){
    if(input.value.trim() == ''){
        return true;
    }
    return false;
}


// Check min length
function check_min_Length(input, min) {
  if (input.value.length < min) {
    return false;
  }
  return true;
}

// Check max length
function check_max_Length(input, max) {
  if (input.value.length > max) {
    return false;
  } 
  return true;
}


function ContactValidation(){
    var checkArr = [
        checkField(name, 2, 100),
        checkEmail(email),
        checkField(question, 5, 2000),
        checkTel(tel, 9, 18)
    ]

    let checker = arr => arr.every(v => v === true);

    return(checker(checkArr))
}

