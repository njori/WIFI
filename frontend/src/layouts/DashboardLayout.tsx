import { Outlet, useLocation } from "react-router-dom";

import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/Navbar";

export default function DashboardLayout() {
    const { pathname } = useLocation();
    const isDashboard = pathname === "/dashboard" || pathname === "/";

    return (

        <div
            style={{
                display: "flex",
                flexDirection: isDashboard ? "row" : "column",
                height: "100vh"
            }}
        >

            <Sidebar horizontal={!isDashboard} />

            <div
                style={{
                    flex: 1,
                    display: "flex",
                    flexDirection: "column",
                    minWidth: 0
                }}
            >

                <Navbar />

                <main
                    style={{
                        flex: 1,
                        padding: 20,
                        background: "#f5f7fb",
                        overflow: "auto"
                    }}
                >

                    <Outlet />

                </main>

            </div>

        </div>

    );

}