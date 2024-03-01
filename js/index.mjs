import {getToken} from "./getToken.mjs";

const url = "/";
const token = await getToken(url);

console.log(token);