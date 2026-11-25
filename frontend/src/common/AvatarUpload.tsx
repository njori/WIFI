import { useState } from "react";
import { Button, Typography, Stack } from "@mui/material";

interface AvatarUploadProps {
  onChange?: (file: File | null) => void;
}

export default function AvatarUpload({
  onChange,
}: AvatarUploadProps) {
  const [fileName, setFileName] = useState("");

  const handleChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = event.target.files?.[0] || null;

    if (file) {
      setFileName(file.name);
    }

    onChange?.(file);
  };

  return (
    <Stack spacing={1}>
      <Button
        variant="outlined"
        component="label"
      >
        Upload Avatar

        <input
          type="file"
          hidden
          accept="image/*"
          onChange={handleChange}
        />
      </Button>

      {fileName && (
        <Typography variant="body2">
          Selected: {fileName}
        </Typography>
      )}
    </Stack>
  );
}