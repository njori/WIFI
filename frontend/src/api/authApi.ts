import api from "./axios";

export const AuthApi = {

    login(data:any){

        return api.post("/auth/login",data);

    },

    register(data:any){

        return api.post("/auth/register",data);

    },

    profile(){

        return api.get("/auth/profile");

    },

    logout(){

        return api.post("/auth/logout");

    }

};