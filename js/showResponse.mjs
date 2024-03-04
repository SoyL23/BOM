export function showResponse(data) {
    // Importar SweetAlert2 desde la CDN
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/sweetalert2@10';
    document.head.appendChild(script);
    script.onload = () => {
        Swal.fire('¡Hola mundo!');
    };
    console.log(data)
}