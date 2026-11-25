import {
    createContext,
    useContext,
    useState,
    useEffect
} from "react";

import api from "../api/api";

interface User {
    id: number;
    username: string;
    email: string;
    role: string;
}

interface AuthContextType {
    user: User | null;
    token: string | null;
    login: (email: string, password: string, role: string) => Promise<boolean>;
    logout: () => void;
    loading: boolean;
}

const AuthContext = createContext<AuthContextType>(null!);

export function AuthProvider({
    children
}: {
    children: React.ReactNode;
}) {

    const [user, setUser] = useState<User | null>(null);

    const [token, setToken] = useState(
        localStorage.getItem("token")
    );

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        if (token) {

            loadUser();

        } else {

            setLoading(false);

        }

    }, []);

    async function loadUser() {

        try {

            const res = await api.get("/auth/me");

            const authenticatedUser = res.data.data;

            setUser(authenticatedUser);
            localStorage.setItem("role", authenticatedUser.role);

        } catch {

            logout();

        }

        setLoading(false);

    }

    async function login(
        email: string,
        password: string,
        role: string
    ) {

        try {

            const res = await api.post(
                "/auth/login",
                {
                    email,
                    password,
                    role
                }
            );

            const accessToken = res.data.data.access_token;

            localStorage.setItem("token", accessToken);
            setToken(accessToken);

            await loadUser();

            return true;

        } catch {

            return false;

        }

    }

    function logout() {

        localStorage.removeItem("token");
        localStorage.removeItem("role");

        setUser(null);

        setToken(null);

    }

    return (

        <AuthContext.Provider
            value={{
                user,
                token,
                login,
                logout,
                loading
            }}
        >

            {children}

        </AuthContext.Provider>

    );

}

export function useAuth() {

    return useContext(AuthContext);

}