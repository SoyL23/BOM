import {getToken} from "./getToken.mjs";



export async function login(){
    const url = "/api/auth/login";
    const token = await getToken(url);    
    console.log(token);
}