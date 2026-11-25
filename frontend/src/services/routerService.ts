import api from "../api/api";

const BASE="/routers";

export const RouterService={

    async getAll(){

        const res=await api.get(BASE);

        return res.data;

    },

    async create(data:any){

        const res=await api.post(BASE,data);

        return res.data;

    },

    async update(id:number,data:any){

        const res=await api.put(

            `${BASE}/${id}`,

            data

        );

        return res.data;

    },

    async remove(id:number){

        await api.delete(

            `${BASE}/${id}`

        );

    }

};