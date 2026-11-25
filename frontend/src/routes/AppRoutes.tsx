import { lazy, Suspense } from "react";
import { Routes, Route, Navigate } from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";
import ProtectedRoute from "../components/ProtectedRoute";
import Loading from "../components/common/Loading";

const Login = lazy(() => import("../pages/Login"));
const Register = lazy(() => import("../pages/Register"));
const Dashboard = lazy(() => import("../pages/Dashboard"));
const Routers = lazy(() => import("../pages/Routers"));
const Networks = lazy(() => import("../pages/Networks"));
const Devices = lazy(() => import("../pages/Devices"));
const Monitoring = lazy(() => import("../pages/Monitoring"));
const Reports = lazy(() => import("../pages/Reports"));
const Notifications = lazy(() => import("../pages/Notifications"));
const Security = lazy(() => import("../pages/Security"));
const Settings = lazy(() => import("../pages/Settings"));
const Users = lazy(() => import("../pages/Users"));

export default function AppRoutes() {

    return (

        <Suspense fallback={<Loading />}>
        <Routes>

            <Route

                path="/login"

                element={<Login />}

            />

            <Route
                path="/register"
                element={<Register />}
            />

            <Route
                element={
                    <ProtectedRoute>
                        <DashboardLayout />
                    </ProtectedRoute>
                }
            >
                <Route path="/" element={<Navigate to="/dashboard" replace />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/routers" element={<Routers/>} />
                <Route path="/networks" element={<Networks/>} />
                <Route path="/devices" element={<Devices/>} />
                <Route path="/monitoring" element={<Monitoring/>} />
                <Route path="/reports" element={<Reports/>} />
                <Route path="/notifications" element={<Notifications/>} />
                <Route path="/security" element={<Security/>} />
                <Route path="/settings" element={<Settings/>} />
                <Route path="/users" element={<Users/>} />

            </Route>

            <Route

                path="*"

                element={<Navigate to="/dashboard" />}

            />
        </Routes>
        </Suspense>

    );

}