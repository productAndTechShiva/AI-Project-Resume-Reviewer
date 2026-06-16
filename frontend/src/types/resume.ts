export interface ResumeReview {
  score: number;

  strengths: string[];

  weaknesses: string[];

  suggestions: string[];

  improved_summary: string;
}

export interface ResumeApiResponse {
  success: boolean;

  filename: string;

  review: ResumeReview;
}