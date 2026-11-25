import {
    Dialog,
    DialogTitle,
    DialogContent,
    Stack,
    TextField,
    Button
} from "@mui/material";

import { useEffect, useState } from "react";

export default function DeviceDialog({

    open,
    device,
    onClose,
    onSave

}:any){

    const [form,setForm]=useState({

        hostname:"",
        ip_address:"",
        mac_address:"",
        manufacturer:"",
        operating_system:"",
        device_type:"",
        signal_strength:100,
        router_id:1

    });

    useEffect(()=>{

        if(device){

            setForm(device);

        }

    },[device]);

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

                Device

            </DialogTitle>

            <DialogContent>

                <Stack component="div" spacing={2} sx={{ mt: 2 }}>

                    <TextField
                        label="Hostname"
                        name="hostname"
                        value={form.hostname}
                        onChange={change}
                    />

                    <TextField
                        label="IP Address"
                        name="ip_address"
                        value={form.ip_address}
                        onChange={change}
                    />

                    <TextField
                        label="MAC Address"
                        name="mac_address"
                        value={form.mac_address}
                        onChange={change}
                    />

                    <TextField
                        label="Manufacturer"
                        name="manufacturer"
                        value={form.manufacturer}
                        onChange={change}
                    />

                    <TextField
                        label="Operating System"
                        name="operating_system"
                        value={form.operating_system}
                        onChange={change}
                    />

                    <TextField
                        label="Device Type"
                        name="device_type"
                        value={form.device_type}
                        onChange={change}
                    />

                    <TextField
                        label="Signal Strength"
                        name="signal_strength"
                        type="number"
                        value={form.signal_strength}
                        onChange={change}
                    />

                    <TextField
                        label="Router ID"
                        name="router_id"
                        type="number"
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