import type { ResumeApiResponse } from "../types/resume";

import "../styles/ReviewResult.css";

interface Props {
  data: ResumeApiResponse;
}

export default function ReviewResult({ data }: Props) {
  const review = data.review;

  return (
    <div className="review-card">
      <h2>Analysis Result</h2>

      {/* <h3>
        Score:
        {" "}
        {review.score}/100
      </h3> */}
      <div className="score-card">
        <h2>Resume Score</h2>
        <div className="score-value">{review.score}</div>
      </div>
      <div className="section">
        <h3>Strengths</h3>

        <ul>
          {review.strengths.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>

        <h3>Weaknesses</h3>

        <ul>
          {review.weaknesses.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>

        <h3>Suggestions</h3>

        <ul>
          {review.suggestions.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>

      <h3>Improved Summary</h3>

      <div className="summary-box">{review.improved_summary}</div>
    </div>
  );
}
