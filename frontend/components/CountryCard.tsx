'use client';
import { motion } from 'framer-motion';
import Link from 'next/link';
import type { Country } from '@/lib/types';

export function CountryCard({
  country,
  index = 0,
}: {
  country: Country;
  index?: number;
}) {
  const diff = '●'.repeat(country.visa_difficulty) + '○'.repeat(5 - country.visa_difficulty);

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 0.05 * index, duration: 0.5 }}
    >
      <Link
        href={`/countries/${country.slug}`}
        className="block bg-cream p-6 hover:bg-ink hover:text-cream transition-colors duration-300 group h-full"
      >
        <div className="flex items-start justify-between">
          <span className="text-4xl">{country.flag_emoji}</span>
          <span className="font-mono text-xs opacity-60">{country.iso_code}</span>
        </div>
        <h3 className="font-serif text-2xl mt-4">{country.name}</h3>
        <p className="text-xs font-mono uppercase tracking-wider opacity-60 mt-1">
          {country.continent}
        </p>
        <p className="text-sm mt-4 opacity-80 leading-relaxed line-clamp-3">
          {country.summary}
        </p>
        <div className="mt-6 pt-4 border-t border-current/20 flex items-center justify-between text-xs font-mono">
          <span>{country.job_site_count} sites</span>
          <span title="Visa difficulty">{diff}</span>
        </div>
      </Link>
    </motion.div>
  );
}
