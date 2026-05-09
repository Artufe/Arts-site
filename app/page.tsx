import type { Metadata } from 'next';
import { Hero } from '@/components/hero';
import { AboutSnippet } from '@/components/about-snippet';
import { FeaturedWork } from '@/components/featured-work';
import { BuildingTeaser } from '@/components/building-teaser';
import { Snapshot } from '@/components/snapshot';
import { CtaSection } from '@/components/cta-section';
import { site } from '@/content/site';

export const metadata: Metadata = {
  description:
    'Freelance AI & ML infrastructure engineer. Python, Rust, PyO3, model serving, Triton Inference Server, MLOps. Available for consulting — remote, EU-time.',
  openGraph: {
    title: site.name,
    description:
      'Freelance AI & ML infrastructure engineer. Python, Rust, model serving, pipeline integration. Available for consulting — remote, EU-time.',
    url: site.url,
  },
};

export default function Home() {
  return (
    <>
      <Hero />
      <AboutSnippet />
      <FeaturedWork />
      <BuildingTeaser />
      <Snapshot />
      <CtaSection />
    </>
  );
}
