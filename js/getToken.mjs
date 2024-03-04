export async function getToken() {
    const url = "/api/auth/login";
    const respuesta = await fetch(url);
    const tokenData = await respuesta.json();
    const token = tokenData.token;
    return token;
}
