export type Country = {
  id: number;
  name: string;
  slug: string;
  iso_code: string;
  flag_emoji?: string;
  continent?: string;
  summary?: string;
  visa_difficulty: number;
  entry_friendly: boolean;
  job_site_count?: number;
  avg_salary_usd?: number;
  currency?: string;
  notes?: string;
  job_sites?: JobSite[];
};

export type JobSite = {
  id: number;
  name: string;
  url: string;
  description?: string;
  site_type?: string;
  is_government: boolean;
  hires_entry_level: boolean;
  is_free: boolean;
  pay_after_hire: boolean;
  rank: number;
  notes?: string;
};

export type MatchResult = {
  recommended_countries: (Country & { reason: string })[];
  advice: string;
  used_llm: boolean;
};
