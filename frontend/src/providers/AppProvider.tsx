import { ThemeProvider } from "@mui/material";

import {

lightTheme

} from "../theme/theme";

export default function AppProvider({

children

}:any){

return(

<ThemeProvider theme={lightTheme}>

{children}

</ThemeProvider>

);

}