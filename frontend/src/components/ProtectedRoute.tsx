import { Navigate } from "react-router-dom";

import { useAuth } from "../contexts/AuthContext";

export default function ProtectedRoute({

    children

}:{

    children: React.ReactNode

}){

    const {

        token,

        loading

    } = useAuth();

    if(loading){

        return <h2>Loading...</h2>;

    }

    if(!token){

        return <Navigate to="/login"/>;

    }

    return children;

}