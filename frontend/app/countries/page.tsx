import { getCountries } from '@/lib/api';
import { CountryCard } from '@/components/CountryCard';

export default async function CountriesPage() {
  let countries: any[] = [];
  try {
    countries = await getCountries();
  } catch {}

  return (
    <div className="max-w-6xl mx-auto px-6 py-16">
      <p className="font-mono text-xs uppercase tracking-widest text-clay mb-4">
        ↳ Browse all
      </p>
      <h1 className="font-serif text-5xl tracking-tight mb-12">
        {countries.length} countries
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-px bg-ink/10 border border-ink/10">
        {countries.map((c, i) => (
          <CountryCard key={c.id} country={c} index={i} />
        ))}
      </div>
    </div>
  );
}
