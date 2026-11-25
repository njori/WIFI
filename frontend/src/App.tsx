import AppRoutes from "./routes/AppRoutes";
import AppProvider from "./providers/AppProvider";

export default function App() {

    return (
        <AppProvider>
            <AppRoutes />
        </AppProvider>
    );

}