import api from "./axios";

export const RouterApi = {

    all(){

        return api.get("/routers");

    },

    create(data:any){

        return api.post("/routers",data);

    },

    update(id:number,data:any){

        return api.put(`/routers/${id}`,data);

    },

    delete(id:number){

        return api.delete(`/routers/${id}`);

    }

};