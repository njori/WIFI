import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { AuthApi } from "../api/authApi";

export default function Register() {
    const navigate = useNavigate();
    const [form, setForm] = useState({
        username: "",
        email: "",
        password: "",
        first_name: "",
        last_name: ""
    });
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    function updateField(field: keyof typeof form, value: string) {
        setForm((current) => ({ ...current, [field]: value }));
    }

    async function submit(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();
        setError("");
        setLoading(true);

        try {
            await AuthApi.register({
                ...form,
                username: form.username.trim(),
                email: form.email.trim(),
                first_name: form.first_name.trim(),
                last_name: form.last_name.trim()
            });
            navigate("/login", {
                replace: true,
                state: { message: "Registration successful. Please log in." }
            });
        } catch (error: unknown) {
            if (axios.isAxiosError(error)) {
                const responseMessage = error.response?.data?.message;
                const validationErrors = error.response?.data?.errors;

                if (typeof responseMessage === "string") {
                    setError(responseMessage);
                } else if (validationErrors && typeof validationErrors === "object") {
                    setError(
                        Object.entries(validationErrors)
                            .map(([field, messages]) => `${field}: ${String(messages)}`)
                            .join(" ")
                    );
                } else if (error.code === "ERR_NETWORK") {
                    setError("Cannot connect to the backend. Make sure it is running on port 5000.");
                } else {
                    setError("Registration failed. Check your details and try again.");
                }
            } else {
                setError("Registration failed. Check your details and try again.");
            }
        } finally {
            setLoading(false);
        }
    }

    return (
        <main style={{ width: 350, margin: "60px auto" }}>
            <h1>Create account</h1>

            <form onSubmit={submit}>
                <input
                    required
                    placeholder="Username"
                    value={form.username}
                    onChange={(event) => updateField("username", event.target.value)}
                />
                <br /><br />
                <input
                    required
                    type="email"
                    placeholder="Email"
                    value={form.email}
                    onChange={(event) => updateField("email", event.target.value)}
                />
                <br /><br />
                <input
                    required
                    placeholder="First name"
                    value={form.first_name}
                    onChange={(event) => updateField("first_name", event.target.value)}
                />
                <br /><br />
                <input
                    required
                    placeholder="Last name"
                    value={form.last_name}
                    onChange={(event) => updateField("last_name", event.target.value)}
                />
                <br /><br />
                <input
                    required
                    minLength={8}
                    type="password"
                    placeholder="Password (at least 8 characters)"
                    value={form.password}
                    onChange={(event) => updateField("password", event.target.value)}
                />
                <br /><br />
                <button type="submit" disabled={loading}>
                    {loading ? "Creating account..." : "Register"}
                </button>
            </form>

            {error && <p role="alert">{error}</p>}
            <p>
                Already registered? <Link to="/login">Log in</Link>
            </p>
        </main>
    );
}
