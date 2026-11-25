import { Navigate } from "react-router-dom";

export default function AdminRoute({ children }: any) {

    const role = localStorage.getItem("role");

    if (role !== "admin") {

        return <Navigate to="/403"/>;
    }

    return children;
}