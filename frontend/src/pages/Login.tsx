import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

const roles = [
    { value: "admin", label: "Admin" },
    { value: "manager", label: "Manager" },
    { value: "technician", label: "Technician" },
    { value: "viewer", label: "Viewer" }
];

export default function Login(){

    const { login } = useAuth();

    const navigate = useNavigate();

    const[email,setEmail]=useState("");

    const[password,setPassword]=useState("");
    const[role,setRole]=useState("admin");

    const[error,setError]=useState("");

    async function submit(e:React.FormEvent){

        e.preventDefault();

        const ok = await login(email.trim(), password, role);

        if(ok){

            navigate("/dashboard");

        }else{

            setError("Invalid credentials");

        }

    }

    return(

        <div
            style={{
                width:350,
                margin:"100px auto"
            }}
        >

            <h1>WiFi Management</h1>

            <form onSubmit={submit}>

                <input

                    placeholder="Email"

                    value={email}

                    onChange={e=>setEmail(e.target.value)}

                />

                <br/><br/>

                <input

                    type="password"

                    placeholder="Password"

                    value={password}

                    onChange={e=>setPassword(e.target.value)}

                />

                <br/><br/>

                <select
                    required
                    value={role}
                    onChange={e=>setRole(e.target.value)}
                >
                    <option value="" disabled>Select role</option>
                    {roles.map((item) => (
                        <option key={item.value} value={item.value}>
                            {item.label}
                        </option>
                    ))}
                </select>

                <br/><br/>

                <button>

                    Login

                </button>

            </form>

            <p>{error}</p>
            <p>
                Need an account? <Link to="/register">Register</Link>
            </p>

        </div>

    );

}