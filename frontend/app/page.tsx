import Link from 'next/link';
import { getCountries, getStats } from '@/lib/api';
import { CountryCard } from '@/components/CountryCard';
import { FadeIn } from '@/components/FadeIn';

export default async function HomePage() {
  let countries: any[] = [];
  let stats: any = { countries: 0, job_sites: 0, government_sites: 0 };
  try {
    [countries, stats] = await Promise.all([getCountries(), getStats()]);
  } catch (e) {
    // gateway down during dev
  }

  const featured = countries.filter((c) => c.entry_friendly).slice(0, 6);

  return (
    <div className="max-w-6xl mx-auto px-6">
      {/* Hero */}
      <section className="pt-20 pb-16">
        <FadeIn>
          <p className="font-mono text-xs uppercase tracking-widest text-clay mb-6">
            ↳ A curated atlas
          </p>
        </FadeIn>
        <FadeIn delay={0.1}>
          <h1 className="font-serif text-5xl md:text-7xl leading-[1.05] tracking-tight max-w-3xl">
            Find visa-sponsored jobs,{' '}
            <em className="text-clay not-italic">without the noise.</em>
          </h1>
        </FadeIn>
        <FadeIn delay={0.2}>
          <p className="mt-8 text-lg max-w-xl text-ink/70 leading-relaxed">
            Government job portals + entry-level friendly sites + free recruiters,
            curated across {stats.countries || '20+'} countries. Start with the
            official ones (highest visa success rate).
          </p>
        </FadeIn>
        <FadeIn delay={0.3}>
          <div className="mt-10 flex gap-4 text-sm">
            <Link
              href="/countries"
              className="px-6 py-3 bg-ink text-cream hover:bg-clay transition-colors"
            >
              Browse countries →
            </Link>
            <Link
              href="/ai-match"
              className="px-6 py-3 border border-ink/30 hover:border-ink transition-colors"
            >
              AI match my profile
            </Link>
          </div>
        </FadeIn>
      </section>

      {/* Stats strip */}
      <FadeIn delay={0.4}>
        <section className="border-t border-b border-ink/10 py-6 grid grid-cols-3 gap-4 text-center">
          <Stat n={stats.countries} label="Countries" />
          <Stat n={stats.job_sites} label="Job sites" />
          <Stat n={stats.government_sites} label="Government portals" />
        </section>
      </FadeIn>

      {/* Featured */}
      <section className="py-20">
        <div className="flex items-baseline justify-between mb-10">
          <h2 className="font-serif text-3xl">Entry-level friendly</h2>
          <Link href="/countries" className="text-sm link-underline">
            All countries →
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-px bg-ink/10 border border-ink/10">
          {featured.map((c, i) => (
            <CountryCard key={c.id} country={c} index={i} />
          ))}
        </div>
      </section>
    </div>
  );
}

function Stat({ n, label }: { n: number; label: string }) {
  return (
    <div>
      <div className="font-serif text-4xl">{n}</div>
      <div className="font-mono text-xs uppercase tracking-widest text-ink/50 mt-1">
        {label}
      </div>
    </div>
  );
}
