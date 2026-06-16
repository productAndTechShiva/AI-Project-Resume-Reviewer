import { useState } from "react";

import { uploadResume } from "../api/resumeApi";

import type {
  ResumeApiResponse,
} from "../types/resume";

import "../styles/FileUpload.css";

interface FileUploadProps {
  onReviewReceived: (
    data: ResumeApiResponse
  ) => void;
}

export default function FileUpload({
  onReviewReceived,
}: FileUploadProps) {
  // ----------------------------------
  // Selected file
  // ----------------------------------

  const [file, setFile] =
    useState<File | null>(null);

  // ----------------------------------
  // Loading state
  // ----------------------------------

  const [loading, setLoading] =
    useState(false);

  // ----------------------------------
  // Error state
  // ----------------------------------

  const [error, setError] =
    useState("");

  // ----------------------------------
  // Handle file selection
  // ----------------------------------

  const handleFileChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const selectedFile =
      event.target.files?.[0];

    if (!selectedFile) {
      return;
    }

    setFile(selectedFile);

    setError("");
  };

  // ----------------------------------
  // Handle upload
  // ----------------------------------

  const handleUpload =
    async () => {

      if (!file) {
        setError(
          "Please select a resume."
        );
        return;
      }

      try {
        setLoading(true);

        setError("");

        const response =
          await uploadResume(
            file
          );

        onReviewReceived(
          response
        );
      } catch (err) {

        console.error(err);

        setError(
          "Failed to upload resume."
        );
      } finally {

        setLoading(false);
      }
    };

  return (
    <div className="upload-card">

      <h2>
        Upload Resume
      </h2>

      {/* File Picker */}

      <input
        type="file"
        accept=".pdf,.docx"
        onChange={
          handleFileChange
        }
      />

      {/* Selected File */}

      {file && (
        <p>
          Selected:
          {" "}
          {file.name}
        </p>
      )}

      {/* Upload Button */}

      <button className="upload-button" 
        onClick={
          handleUpload
        }
        disabled={
          loading
        }
      >
        {loading
          ? "Analyzing..."
          : "Analyze Resume"}
      </button>

      {/* Error */}

      {error && (
        <p>
          {error}
        </p>
      )}

    </div>
  );
}