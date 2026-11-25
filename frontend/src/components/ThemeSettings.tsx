import {

Card,
CardContent,
FormControlLabel,
Switch

} from "@mui/material";

export default function ThemeSettings({

form,

change

}:any){

return(

<Card>

<CardContent>

<FormControlLabel

control={

<Switch

checked={form.dark_mode}

onChange={(e)=>change({

target:{

name:"dark_mode",

value:e.target.checked

}

})}

/>

}

label="Dark Mode"

/>

</CardContent>

</Card>

);

}