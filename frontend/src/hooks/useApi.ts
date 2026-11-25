import { useState } from "react";

export default function useApi() {

    const [loading,setLoading]=useState(false);

    async function execute(request:any){

        try{

            setLoading(true);

            return await request();

        }

        finally{

            setLoading(false);

        }

    }

    return{

        loading,

        execute

    };

}