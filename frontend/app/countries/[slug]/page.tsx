import { getCountry } from '@/lib/api';
import { FadeIn } from '@/components/FadeIn';
import { notFound } from 'next/navigation';
import Link from 'next/link';

export default async function CountryPage({
  params,
}: {
  params: { slug: string };
}) {
  let c: any;
  try {
    c = await getCountry(params.slug);
  } catch {
    notFound();
  }

  const govSites = (c.job_sites || []).filter((s: any) => s.is_government);
  const otherSites = (c.job_sites || []).filter((s: any) => !s.is_government);

  return (
    <div className="max-w-4xl mx-auto px-6 py-16">
      <FadeIn>
        <Link href="/countries" className="text-xs font-mono uppercase tracking-widest text-ink/60 hover:text-clay">
          ← All countries
        </Link>
      </FadeIn>

      <FadeIn delay={0.1}>
        <div className="mt-8 flex items-center gap-6">
          <span className="text-7xl">{c.flag_emoji}</span>
          <div>
            <h1 className="font-serif text-5xl tracking-tight">{c.name}</h1>
            <p className="font-mono text-xs uppercase tracking-widest text-ink/60 mt-2">
              {c.continent} · {c.iso_code}
            </p>
          </div>
        </div>
      </FadeIn>

      <FadeIn delay={0.2}>
        <p className="mt-8 text-lg leading-relaxed text-ink/80">{c.summary}</p>
      </FadeIn>

      <FadeIn delay={0.3}>
        <div className="mt-8 grid grid-cols-3 gap-px bg-ink/10 border border-ink/10">
          <Fact label="Visa difficulty" value={'●'.repeat(c.visa_difficulty) + '○'.repeat(5 - c.visa_difficulty)} />
          <Fact label="Entry friendly" value={c.entry_friendly ? 'Yes' : 'No'} />
          <Fact label="Avg salary" value={c.avg_salary_usd ? `$${(c.avg_salary_usd / 1000).toFixed(0)}k ${c.currency}` : '—'} />
        </div>
      </FadeIn>

      {c.notes && (
        <FadeIn delay={0.4}>
          <div className="mt-8 p-6 bg-clay/10 border-l-2 border-clay">
            <p className="font-mono text-xs uppercase tracking-widest text-clay mb-2">Note</p>
            <p className="text-sm text-ink/80 leading-relaxed">{c.notes}</p>
          </div>
        </FadeIn>
      )}

      {/* Government sites */}
      {govSites.length > 0 && (
        <section className="mt-16">
          <h2 className="font-serif text-3xl mb-2">Official portals</h2>
          <p className="font-mono text-xs uppercase tracking-widest text-ink/60 mb-8">
            🏛️ Government sources · start here
          </p>
          <div className="space-y-0 border border-ink/10">
            {govSites.map((s: any) => (
              <SiteRow key={s.id} site={s} />
            ))}
          </div>
        </section>
      )}

      {/* Other sites */}
      {otherSites.length > 0 && (
        <section className="mt-16">
          <h2 className="font-serif text-3xl mb-2">Job boards & recruiters</h2>
          <p className="font-mono text-xs uppercase tracking-widest text-ink/60 mb-8">
            Private platforms · entry-level friendly
          </p>
          <div className="space-y-0 border border-ink/10">
            {otherSites.map((s: any) => (
              <SiteRow key={s.id} site={s} />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}

function Fact({ label, value }: { label: string; value: string }) {
  return (
    <div className="bg-cream p-4">
      <p className="font-mono text-[10px] uppercase tracking-widest text-ink/50">{label}</p>
      <p className="font-serif text-xl mt-1">{value}</p>
    </div>
  );
}

function SiteRow({ site }: { site: any }) {
  return (
    <a
      href={site.url}
      target="_blank"
      rel="noopener noreferrer"
      className="block p-5 border-b border-ink/10 last:border-b-0 hover:bg-ink hover:text-cream transition-colors group"
    >
      <div className="flex items-start justify-between gap-4">
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-3 flex-wrap">
            <h3 className="font-serif text-xl">{site.name}</h3>
            {site.is_government && (
              <span className="text-[10px] font-mono uppercase tracking-widest bg-moss/20 text-moss group-hover:bg-cream/20 group-hover:text-cream px-2 py-0.5">
                Official
              </span>
            )}
            {site.is_free && !site.is_government && (
              <span className="text-[10px] font-mono uppercase tracking-widest bg-clay/20 text-clay group-hover:bg-cream/20 group-hover:text-cream px-2 py-0.5">
                Free
              </span>
            )}
            {site.pay_after_hire && (
              <span className="text-[10px] font-mono uppercase tracking-widest bg-ink/10 group-hover:bg-cream/20 px-2 py-0.5">
                Pay after hire
              </span>
            )}
          </div>
          <p className="text-sm opacity-70 mt-2 leading-relaxed">{site.description}</p>
          {site.notes && (
            <p className="text-xs font-mono mt-2 opacity-60">{site.notes}</p>
          )}
          <p className="font-mono text-xs mt-3 opacity-50 truncate">{site.url}</p>
        </div>
        <span className="text-2xl opacity-30 group-hover:opacity-100 group-hover:translate-x-1 transition-transform">↗</span>
      </div>
    </a>
  );
}
