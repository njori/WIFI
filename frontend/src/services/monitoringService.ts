import api from "../api/api";

const BASE="/monitoring";

export const MonitoringService={

    async getOverview(){

        const res=await api.get(BASE);

        return res.data;

    }

};