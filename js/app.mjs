import { login } from "./login.mjs";

document.addEventListener('DOMContentLoaded', (e) =>{
    const loginForm = document.querySelector('#login_form')
    const data ={}

    loginForm.addEventListener('submit', (e) => {
        e.preventDefault()
        const inputs = document.querySelectorAll('input');
        inputs.forEach(input => {
            data[input.id] = input.value
        });
        login(data);
    })
})