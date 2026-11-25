import { useDropzone } from "react-dropzone";

export default function AvatarUpload() {

    const {
        getRootProps,
        getInputProps
    } = useDropzone({
        accept: {
            "image/*": []
        },
        multiple: false,
        onDrop: (acceptedFiles) => {
            console.log(acceptedFiles);
        }
    });

    return (
        <div
            {...getRootProps()}
            style={{
                border: "2px dashed gray",
                padding: 20,
                textAlign: "center",
                cursor: "pointer"
            }}
        >
            <input {...getInputProps()} />

            <p>Drag and drop an image here, or click to select one.</p>
        </div>
    );
}