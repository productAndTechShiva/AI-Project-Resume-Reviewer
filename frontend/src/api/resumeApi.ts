import axios from "axios";

const API_BASE_URL =
  "http://localhost:8000";

export const uploadResume =
  async (file: File) => {

    const formData =
      new FormData();

    formData.append(
      "resume",
      file
    );

    const response =
      await axios.post(
        `${API_BASE_URL}/api/resume/upload`,
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

    return response.data;
};