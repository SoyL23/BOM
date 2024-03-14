import { login } from "./login.mjs";
import { showResponse } from "./showResponse.mjs";

document.addEventListener('DOMContentLoaded', (e) =>{
    const loginForm = document.querySelector('#login_form')
    const data ={}

    loginForm.addEventListener('submit', async (e) => { // Cambio aquí: async para usar await
        e.preventDefault()
        const inputs = document.querySelectorAll('input');
        inputs.forEach(input => {
            data[input.id] = input.value
        });
        try {
            const { responseData, statusCode } = await login(data); // Cambio aquí: await para esperar la promesa
            console.log(responseData);
            showResponse(responseData, statusCode); // Cambio aquí: pasamos responseData y statusCode directamente
        } catch (error) {
            console.error(error);
        }
    })
})
