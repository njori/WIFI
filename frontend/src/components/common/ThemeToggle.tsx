import {IconButton} from "@mui/material";

import DarkModeIcon from "@mui/icons-material/DarkMode";
export default function ThemeToggle({toggle}:any){

return(<IconButton
onClick={toggle}
>
<DarkModeIcon/>
</IconButton>

);

}