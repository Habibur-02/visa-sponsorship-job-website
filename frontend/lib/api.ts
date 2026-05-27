import type { Country, MatchResult } from './types';

// Server-side: hit the gateway container directly.
// Client-side: hit the gateway exposed on localhost (or in prod, your domain).
const API_BASE =
  typeof window === 'undefined'
    ? process.env.GATEWAY_URL || 'http://gateway:8000'
    : process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function getCountries(): Promise<Country[]> {
  const r = await fetch(`${API_BASE}/api/countries`, { cache: 'no-store' });
  if (!r.ok) throw new Error('Failed to fetch countries');
  return r.json();
}

export async function getCountry(slug: string): Promise<Country> {
  const r = await fetch(`${API_BASE}/api/countries/${slug}`, { cache: 'no-store' });
  if (!r.ok) throw new Error('Failed to fetch country');
  return r.json();
}

export async function getStats() {
  const r = await fetch(`${API_BASE}/api/stats`, { cache: 'no-store' });
  if (!r.ok) throw new Error('Failed to fetch stats');
  return r.json();
}

export async function aiMatch(skills_text: string): Promise<MatchResult> {
  const r = await fetch(`${API_BASE}/api/ai/match`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ skills_text, entry_level_only: true }),
  });
  if (!r.ok) throw new Error('AI match failed');
  return r.json();
}
