import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import { QueryClient } from "@tanstack/react-query";
import { QueryClientProvider } from "@tanstack/react-query";
import { AuthProvider } from "./contexts/AuthContext";
import { Toaster } from "react-hot-toast";

import App from "./App";

import "./styles/global.css";

const queryClient = new QueryClient();

ReactDOM.createRoot(
    document.getElementById("root")!
).render(

    <React.StrictMode>

        <QueryClientProvider client={queryClient}>

            <BrowserRouter>
            <AuthProvider>

                <App />
                <Toaster position="top-right"/>

            </AuthProvider>

            </BrowserRouter>

        </QueryClientProvider>

    </React.StrictMode>

);