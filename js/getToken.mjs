export async function getToken(url) {
    try {
        const respuesta = await fetch(url);
        const token = await respuesta.json(); 
        if (respuesta.ok) {
            return token; 
        } else {
            throw new Error('Error al obtener el token');
        }
    } catch (error) {
        console.error("Error durante la obtención del token:", error);
        throw error;
    }
}
