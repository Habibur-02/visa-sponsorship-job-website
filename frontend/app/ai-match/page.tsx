'use client';
import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { aiMatch } from '@/lib/api';
import type { MatchResult } from '@/lib/types';

export default function AIMatchPage() {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<MatchResult | null>(null);
  const [error, setError] = useState('');

  async function onSubmit() {
    if (text.trim().length < 20) {
      setError('Tell us at least a sentence or two about your skills.');
      return;
    }
    setError('');
    setLoading(true);
    setResult(null);
    try {
      const r = await aiMatch(text);
      setResult(r);
    } catch (e: any) {
      setError(e.message || 'Something went wrong.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-3xl mx-auto px-6 py-16">
      <p className="font-mono text-xs uppercase tracking-widest text-clay mb-4">
        ↳ AI Match
      </p>
      <h1 className="font-serif text-5xl tracking-tight">
        Tell us about you, <em className="text-clay not-italic">we&apos;ll suggest countries.</em>
      </h1>

      <p className="mt-6 text-ink/70 leading-relaxed">
        Paste a paragraph from your CV, or describe your skills, experience, and what you&apos;re looking for.
        We&apos;ll match you to entry-friendly countries.
      </p>

      <div className="mt-10">
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="e.g. Python backend developer with 2 years experience at a SaaS startup. Comfortable with FastAPI, PostgreSQL, AWS. Looking for a tech-friendly country in Europe with low cost of living and English-speaking work environment."
          className="w-full h-44 p-5 bg-cream border border-ink/20 focus:border-ink outline-none font-sans text-base leading-relaxed resize-none"
        />
        <div className="mt-4 flex items-center justify-between">
          <span className="font-mono text-xs text-ink/50">{text.length} chars</span>
          <button
            onClick={onSubmit}
            disabled={loading}
            className="px-6 py-3 bg-ink text-cream hover:bg-clay transition-colors disabled:opacity-50"
          >
            {loading ? 'Matching...' : 'Match me →'}
          </button>
        </div>
        {error && <p className="mt-4 text-sm text-clay">{error}</p>}
      </div>

      <AnimatePresence>
        {result && (
          <motion.div
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="mt-16"
          >
            <div className="p-6 bg-clay/10 border-l-2 border-clay mb-10">
              <p className="font-mono text-xs uppercase tracking-widest text-clay mb-2">
                {result.used_llm ? 'AI advice' : 'Keyword match (fallback)'}
              </p>
              <p className="text-sm leading-relaxed">{result.advice}</p>
            </div>

            <h2 className="font-serif text-3xl mb-6">Your top {result.recommended_countries.length} matches</h2>
            <div className="space-y-px bg-ink/10 border border-ink/10">
              {result.recommended_countries.map((c, i) => (
                <motion.a
                  key={c.id}
                  href={`/countries/${c.slug}`}
                  initial={{ opacity: 0, x: -8 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.1 * i, duration: 0.4 }}
                  className="block p-6 bg-cream hover:bg-ink hover:text-cream transition-colors group"
                >
                  <div className="flex items-start gap-5">
                    <span className="text-4xl">{c.flag_emoji}</span>
                    <div className="flex-1">
                      <h3 className="font-serif text-2xl">{c.name}</h3>
                      <p className="text-sm opacity-70 mt-2 italic">&ldquo;{c.reason}&rdquo;</p>
                    </div>
                    <span className="text-2xl opacity-30 group-hover:opacity-100 group-hover:translate-x-1 transition-transform">→</span>
                  </div>
                </motion.a>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
