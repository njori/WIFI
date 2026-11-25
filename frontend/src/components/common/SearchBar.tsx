import {TextField} from "@mui/material";

export default function SearchBar({value,change}:any){

return(
<TextField placeholder="Search..."
value={value}
onChange={change}
fullWidth
/>
);
}