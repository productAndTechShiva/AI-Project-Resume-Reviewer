import { useState } from "react";
import "./styles/App.css";

import FileUpload
  from "./components/FileUpload";

import ReviewResult
  from "./components/ReviewResult";

import type {
  ResumeApiResponse,
} from "./types/resume";

function App() {

  const [
    reviewData,
    setReviewData
  ] = useState<
    ResumeApiResponse | null
  >(null);

  const handleReview =
    (
      data: ResumeApiResponse
    ) => {

      console.log(data);

      setReviewData(
        data
      );
    };

  return (

     <div className="app-container">

    <h1 className="page-title">
      AI Resume Reviewer
    </h1>

    <FileUpload
      onReviewReceived={
        handleReview
      }
    />

    {reviewData && (
      <ReviewResult
        data={reviewData}
      />
    )}

  </div>
  
    // <div>

    //   <h1>
    //     AI Resume Reviewer
    //   </h1>

    //   <FileUpload
    //     onReviewReceived={
    //       handleReview
    //     }
    //   />

    //   {reviewData && (
    //     <ReviewResult
    //       data={
    //         reviewData
    //       }
    //     />
    //   )}

    // </div>
  );
}

export default App;