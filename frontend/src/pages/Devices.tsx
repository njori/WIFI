import { useEffect, useState } from "react";

import {
    Button,
    Chip,
    Paper
} from "@mui/material";

import {

    DataGrid,

    } from "@mui/x-data-grid";
    import type {
        GridColDef
    } from "@mui/x-data-grid";

import DeviceDialog from "../components/DeviceDialog";
import { DeviceService } from "../services/deviceService";

export default function Devices(){

    const[data,setData]=useState([]);

    const[open,setOpen]=useState(false);

    const[selected,setSelected]=useState<any>(null);

    async function load(){

        const devices=await DeviceService.getAll();

        setData(devices);

    }

    useEffect(()=>{

        load();

    },[]);

    const columns:GridColDef[]=[

        {field:"hostname",headerName:"Hostname",flex:1},

        {field:"ip_address",headerName:"IP Address",flex:1},

        {field:"mac_address",headerName:"MAC Address",flex:1},

        {field:"device_type",headerName:"Type",flex:1},

        {field:"router_name",headerName:"Router",flex:1},

        {

            field:"signal_strength",

            headerName:"Signal",

            flex:1,

            renderCell:(params)=>`${params.value}%`

        },

        {

            field:"is_connected",

            headerName:"Status",

            flex:1,

            renderCell:(params)=>(

                <Chip

                    label={params.value ? "Connected" : "Disconnected"}

                    color={params.value ? "success" : "error"}

                />

            )

        },

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

                Add Device

            </Button>

            <DataGrid

                rows={data}

                columns={columns}

                pageSizeOptions={[10]}

            />

            <DeviceDialog

                open={open}

                device={selected}

                onClose={()=>setOpen(false)}

                onSave={async(form:any)=>{

                    if(selected){

                        await DeviceService.update(selected.id,form);

                    }else{

                        await DeviceService.create(form);

                    }

                    setOpen(false);

                    load();

                }}

            />

        </Paper>

    );

}