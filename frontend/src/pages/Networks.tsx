import { useEffect,useState } from "react";

import {
    Paper,
    Button
} from "@mui/material";

import {
    DataGrid,
} from "@mui/x-data-grid";
import type {
    GridColDef
} from "@mui/x-data-grid";

import { NetworkService } from "../services/networkService";

import NetworkDialog from "../components/NetworkDialog";

export default function Networks(){

    const[data,setData]=useState([]);

    const[open,setOpen]=useState(false);

    const[selected,setSelected]=useState<any>(null);

    async function load(){

        const result=await NetworkService.getAll();

        setData(result);

    }

    useEffect(()=>{

        load();

    },[]);

    const columns:GridColDef[]=[

        {field:"name",headerName:"Name",flex:1},

        {field:"cidr",headerName:"CIDR",flex:1},

        {field:"gateway",headerName:"Gateway",flex:1},

        {field:"vlan",headerName:"VLAN",flex:1},

        {field:"router_name",headerName:"Router",flex:1},

        {

            field:"actions",

            headerName:"Actions",

            flex:1,

            renderCell:(params)=>(

                <Button

                    onClick={()=>{

                        setSelected(params.row);

                        setOpen(true);

                    }}

                >

                    Edit

                </Button>

            )

        }

    ];

    return(

        <Paper sx={{height:700,p:2}}>

            <Button

                variant="contained"

                onClick={()=>{

                    setSelected(null);

                    setOpen(true);

                }}

            >

                Add Network

            </Button>

            <DataGrid

                rows={data}

                columns={columns}

                pageSizeOptions={[10]}

            />

            <NetworkDialog

                open={open}

                network={selected}

                onClose={()=>setOpen(false)}

                onSave={async(form:any)=>{

                    if(selected){

                        await NetworkService.update(

                            selected.id,

                            form

                        );

                    }else{

                        await NetworkService.create(

                            form

                        );

                    }

                    setOpen(false);

                    load();

                }}

            />

        </Paper>

    );

}