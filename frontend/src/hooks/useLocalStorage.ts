import { useState } from "react";

export default function useLocalStorage(
key:string,
initial:any
){

const[value,setValue]=useState(()=>{

const item=localStorage.getItem(key);

return item?JSON.parse(item):initial;

});

function save(v:any){

setValue(v);

localStorage.setItem(

key,

JSON.stringify(v)

);

}

return[value,save];

}