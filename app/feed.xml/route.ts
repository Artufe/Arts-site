import { site } from '@/content/site';
import { getNotesIndex } from '@/lib/notes';

export const dynamic = 'force-static';

function escapeXml(s: string) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

function toRfc822(iso: string) {
  return new Date(iso).toUTCString();
}

export async function GET() {
  const base = site.url.replace(/\/$/, '');
  const notes = await getNotesIndex();
  const feedUrl = `${base}/feed.xml`;
  const lastBuildDate = notes.length
    ? toRfc822(notes[0].meta.datePublished)
    : new Date().toUTCString();

  const items = notes
    .map(({ slug, meta }) => {
      const link = `${base}/notes/${slug}/`;
      return [
        '    <item>',
        `      <title>${escapeXml(meta.title)}</title>`,
        `      <link>${escapeXml(link)}</link>`,
        `      <guid isPermaLink="true">${escapeXml(link)}</guid>`,
        `      <pubDate>${toRfc822(meta.datePublished)}</pubDate>`,
        `      <description>${escapeXml(meta.description)}</description>`,
        `      <author>${escapeXml(`${site.email} (${site.name})`)}</author>`,
        '    </item>',
      ].join('\n');
    })
    .join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${escapeXml(`${site.name} · Notes`)}</title>
    <link>${escapeXml(`${base}/notes/`)}</link>
    <atom:link href="${escapeXml(feedUrl)}" rel="self" type="application/rss+xml" />
    <description>${escapeXml('AI in production, not in pitches. Short, opinionated notes from the senior-engineer side of AI/ML.')}</description>
    <language>en</language>
    <lastBuildDate>${lastBuildDate}</lastBuildDate>
${items}
  </channel>
</rss>
`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  });
}
