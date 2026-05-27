/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        serif: ['var(--font-fraunces)', 'Georgia', 'serif'],
        sans: ['var(--font-geist)', 'system-ui', 'sans-serif'],
      },
      colors: {
        ink: '#1a1a1a',
        cream: '#f5f1e8',
        clay: '#c9622a',
        moss: '#5c6b3e',
      },
    },
  },
  plugins: [],
};
