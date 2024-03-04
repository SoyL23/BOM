import { showResponse } from "./showResponse.mjs";

export async function login(loginData) {
  const url = "/api/auth/login";
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": String(loginData.token) // Convertir el token a cadena
    },
    body: JSON.stringify({
      'login_name': loginData.login_name,
      'login_password': loginData.login_password
    })
  });

  const responseData = await response.json();
  console.log(responseData);
}
