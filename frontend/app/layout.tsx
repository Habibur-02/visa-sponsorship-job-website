import type { Metadata } from 'next';
import { Fraunces, JetBrains_Mono } from 'next/font/google';
import './globals.css';
import Link from 'next/link';

const fraunces = Fraunces({
  subsets: ['latin'],
  variable: '--font-fraunces',
  display: 'swap',
});

const geist = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-geist',
  display: 'swap',
});

export const metadata: Metadata = {
  title: 'Visa Sponsorship Atlas',
  description: 'Curated visa-sponsored job sites for 20+ countries. Government portals, entry-level friendly, free for candidates.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${fraunces.variable} ${geist.variable}`}>
      <body className="font-sans relative">
        <div className="relative z-10">
          <Navbar />
          <main className="min-h-screen">{children}</main>
          <Footer />
        </div>
      </body>
    </html>
  );
}

function Navbar() {
  return (
    <nav className="border-b border-ink/10">
      <div className="max-w-6xl mx-auto px-6 py-5 flex items-center justify-between">
        <Link href="/" className="font-serif text-xl tracking-tight">
          Visa<span className="text-clay">·</span>Atlas
        </Link>
        <div className="flex gap-8 text-sm">
          <Link href="/countries" className="link-underline">Countries</Link>
          <Link href="/ai-match" className="link-underline">AI Match</Link>
        </div>
      </div>
    </nav>
  );
}

function Footer() {
  return (
    <footer className="border-t border-ink/10 mt-24">
      <div className="max-w-6xl mx-auto px-6 py-8 text-xs text-ink/60 flex justify-between">
        <span>Built with FastAPI · Next.js · SQLite</span>
        <span>{new Date().getFullYear()}</span>
      </div>
    </footer>
  );
}
