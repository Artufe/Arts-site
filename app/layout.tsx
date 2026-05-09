import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import { fraunces, inter, jetBrainsMono } from './fonts';
import { ThemeProvider } from '@/components/theme-provider';
import { Nav } from '@/components/nav';
import { Footer } from '@/components/footer';
import { Gridlines } from '@/components/gridlines';
import { Grain } from '@/components/grain';
import { HeroShader } from '@/components/hero-shader';
import { CommandPaletteLazy } from '@/components/command-palette-lazy';
import { site } from '@/content/site';
import './globals.css';

export const metadata: Metadata = {
  metadataBase: new URL(site.url),
  title: { default: site.name, template: `%s · ${site.name}` },
  description: site.description,
  keywords: [
    'AI developer',
    'ML engineer',
    'freelance AI consultant',
    'machine learning infrastructure',
    'Python',
    'Rust',
    'PyO3',
    'model serving',
    'Triton Inference Server',
    'MLOps',
    'AI pipeline integration',
    'backend engineer',
    'AI consulting',
    'remote AI developer',
    'Kubernetes ML',
  ],
  creator: site.name,
  referrer: 'origin-when-cross-origin',
  alternates: { canonical: '/' },
  robots: { index: true, follow: true },
  openGraph: {
    title: site.name,
    description: site.description,
    url: site.url,
    siteName: site.name,
    type: 'website',
    locale: 'en_US',
  },
  twitter: {
    card: 'summary_large_image',
    title: site.name,
    description: site.description,
    creator: '@arthurbuikis',
  },
};

const personLd = {
  '@context': 'https://schema.org',
  '@type': 'Person',
  '@id': `${site.url}/#person`,
  name: site.name,
  url: site.url,
  email: `mailto:${site.email}`,
  jobTitle: site.bio.jobTitle,
  description: site.bio.summary,
  address: {
    '@type': 'PostalAddress',
    addressLocality: site.bio.location.city,
    addressCountry: site.bio.location.country,
  },
  knowsAbout: site.bio.knowsAbout,
  sameAs: site.socials.map((s) => s.href),
};

const websiteLd = {
  '@context': 'https://schema.org',
  '@type': 'WebSite',
  '@id': `${site.url}/#website`,
  url: site.url,
  name: site.name,
  description: site.description,
  inLanguage: 'en',
  publisher: { '@id': `${site.url}/#person` },
};

const professionalServiceLd = {
  '@context': 'https://schema.org',
  '@type': 'ProfessionalService',
  '@id': `${site.url}/#service`,
  name: `${site.name} — AI & ML infrastructure consulting`,
  description:
    'Freelance AI and ML infrastructure engineering. Python, Rust, model serving, pipeline integration, MLOps. Remote consulting for teams that need AI to ship.',
  url: site.url,
  provider: { '@id': `${site.url}/#person` },
  serviceType: 'AI infrastructure engineering',
  areaServed: {
    '@type': 'AdministrativeArea',
    name: 'Worldwide (remote)',
  },
  availableChannel: {
    '@type': 'ServiceChannel',
    serviceUrl: `${site.url}/contact/`,
    availableLanguage: ['English', 'Latvian'],
  },
  hasOfferCatalog: {
    '@type': 'OfferCatalog',
    name: 'AI & ML engineering services',
    itemListElement: [
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'ML model integration & serving',
          description: 'Integrate ML models into production pipelines with Triton Inference Server, Docker, and Kubernetes.',
        },
      },
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'AI pipeline architecture',
          description: 'Design and build end-to-end AI/ML pipelines — data ingestion, model training orchestration, inference deployment.',
        },
      },
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'Performance optimization for ML systems',
          description: 'Profile and optimize ML inference backends in Python and Rust (PyO3). Cut hot-path latency and scale model serving.',
        },
      },
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'Freelance AI backend development',
          description: 'Solo or embedded. Twelve years of Python backend experience, available for AI infrastructure contracts.',
        },
      },
    ],
  },
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning className={`${fraunces.variable} ${inter.variable} ${jetBrainsMono.variable}`}>
      <body className="min-h-screen">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(personLd) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteLd) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(professionalServiceLd) }}
        />
        <ThemeProvider>
          <HeroShader />
          <Gridlines />
          <Grain />
          <Nav />
          <main className="relative z-10 pt-20">{children}</main>
          <Footer />
          <CommandPaletteLazy />
        </ThemeProvider>
      </body>
    </html>
  );
}
