export const Validators={

required:(v:string)=>v.length>0,

email:(v:string)=>

/^\S+@\S+\.\S+$/.test(v),

ip:(v:string)=>

 /^(\d{1,3}\.){3}\d{1,3}$/.test(v)

}