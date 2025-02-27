import { Link, useNavigate } from "react-router-dom";
import React, { useState } from "react";
import styled from "styled-components";
import { Navigate } from "react-router-dom";

const Wrapper = styled.div`
    display: flex;
    flex-direction: column;
    height: 100vh; 
    width: 100%;
    margin: 0;
    padding: 0;
`;

const Title = styled.h1`
    margin: 0;
    color: rgb(0, 0, 0);
    font-size: 1.8rem;
    text-align: center;
    margin-bottom: 1.5rem;

`;

const Main = styled.main`
    display: flex;
    justify-content: center;
    align-items: center;
    flex: 1;
    padding: 1rem;
    background-image: url("src/img/fondo(1).svg");
    background-size: cover;
    background-position: center;

    @media (max-width: 768px) {
        padding: 0.5rem;
    }
`;

const LoginContainer = styled.div`
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 0 20px 5px rgba(0, 0, 0, 0.25);
    padding: 1.5rem;
    width: 100%;
    max-width: 400px;
    border: 1px solid grey;

    @media (max-width: 480px) {
        padding: 1rem;
        max-width: 90%;
    }
`;

const FormLogin = styled.form`
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
`;

const Input = styled.input`
    width: 100%;
    padding: 0.5rem;
    border: 1px solid gray-light;
    border-radius: 6px;
    background-color: rgb(243, 243, 242);
    color: #4e342e;
    font-size: 0.9rem;
    transition: border-color 0.3s;

    &:focus {
        outline: none;
        border-color: gray-light;
    }
`;

const Button = styled.button`
    background-color: gray-light;
    border: none;
    padding: 0.6rem;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.3s;
    width: 100%;
    margin-top: 0.5rem;

    &:hover {
        background-color: gray;
    }

    &:disabled {
        background-color: #ddd;
        cursor: not-allowed;
    }
`;

const StyledLink = styled(Link)`
    text-decoration: none;
    color: rgb(0, 0, 0);
    text-align: center;
    font-size: 0.7rem;
    margin-top: 0.5rem;

    &:hover {
        color: #f79d60;
    }
`;

const ErrorMessage = styled.p`
    color: red;
    font-size: 0.8rem;
    margin-bottom: 0.5rem;
    text-align: center;
`;

function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);


    const handleLogin = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        setError("");

        try {
            const response = await fetch("http://127.0.0.1:8000/users/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username,
                    password,
                }),
            });

            const data = await response.json();

            if (response.ok) {
                if (!data.accessToken || !data.refreshToken) {
                    throw new Error("Tokens no recibidos correctamente.");
                }
                
                // Guardar información de autenticación
                localStorage.setItem("id", data.id)
                sessionStorage.setItem("username", data.username);
                localStorage.setItem("token", data.accessToken);
                localStorage.setItem("refreshToken", data.refreshToken);

            } else {
                setError(data.message || "Error al iniciar sesión");
            }
        } catch (err) {
            setError(err.message || "Error de conexión. Por favor, intente nuevamente.");
            console.error("Error durante el inicio de sesión:", err);
        } finally {
            setIsLoading(false);
        }
    };

  return (
    <Wrapper>
            
            

            <Main>
                <LoginContainer>
                 <Title>Iniciar Sesion</Title>

                    <FormLogin onSubmit={handleLogin}>
                        <Input
                            type="text"
                            placeholder="Usuario"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                        />

                        <Input
                            type="password"
                            placeholder="Contraseña"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />

                        {error && <ErrorMessage>{error}</ErrorMessage>}

                        <Button type="submit" disabled={isLoading}>
                            {isLoading ? "Cargando..." : "Iniciar Sesión"}
                        </Button>
                        
                    </FormLogin>
                </LoginContainer>
            </Main>

            
        </Wrapper>
    );
};

export default Login;