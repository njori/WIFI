import {
    Dialog,
    DialogTitle,
    DialogContent,
    Stack,
    TextField,
    Button
} from "@mui/material";

import { useEffect, useState } from "react";

export default function NetworkDialog({

    open,
    network,
    onClose,
    onSave

}:any){

    const [form,setForm]=useState({

        name:"",
        cidr:"",
        gateway:"",
        subnet_mask:"",
        vlan:1,
        dns_server:"",
        description:"",
        router_id:1

    });

    useEffect(()=>{

        if(network){

            setForm(network);

        }

    },[network]);

    function change(e:any){

        setForm({

            ...form,

            [e.target.name]:e.target.value

        });

    }

    return(

        <Dialog
            open={open}
            onClose={onClose}
            fullWidth
        >

            <DialogTitle>

                Network

            </DialogTitle>

            <DialogContent>

                <Stack component="div" spacing={2} sx={{ mt: 2 }}>

                    <TextField
                        label="Network Name"
                        name="name"
                        value={form.name}
                        onChange={change}
                    />

                    <TextField
                        label="CIDR"
                        name="cidr"
                        value={form.cidr}
                        onChange={change}
                    />

                    <TextField
                        label="Gateway"
                        name="gateway"
                        value={form.gateway}
                        onChange={change}
                    />

                    <TextField
                        label="Subnet Mask"
                        name="subnet_mask"
                        value={form.subnet_mask}
                        onChange={change}
                    />

                    <TextField
                        label="VLAN"
                        name="vlan"
                        value={form.vlan}
                        onChange={change}
                    />

                    <TextField
                        label="DNS Server"
                        name="dns_server"
                        value={form.dns_server}
                        onChange={change}
                    />

                    <TextField
                        label="Description"
                        name="description"
                        value={form.description}
                        onChange={change}
                    />

                    <TextField
                        label="Router ID"
                        name="router_id"
                        value={form.router_id}
                        onChange={change}
                    />

                    <Button
                        variant="contained"
                        onClick={()=>onSave(form)}
                    >

                        Save

                    </Button>

                </Stack>

            </DialogContent>

        </Dialog>

    );

}