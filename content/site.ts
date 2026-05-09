export const site = {
  name: 'Arthur Buikis',
  email: 'arthur@buikis.com',
  url: 'https://arthur.buikis.com',
  brand: 'ab.',
  description: 'Freelance AI & ML infrastructure engineer. Python, Rust, model serving, pipeline integration — ships systems that hold up.',
  formspreeEndpoint: 'https://formspree.io/f/xaqadvlz',
  // Newsletter provider form-submit URL. Anything that accepts a POST
  // with form-encoded `email` works — components/subscribe-form.tsx is
  // service-agnostic. Recommended: Buttondown (free <100 subs, no
  // branding, one-click unsubscribe baked in). Drop in one of:
  //   Buttondown:   https://buttondown.email/api/emails/embed-subscribe/<username>
  //   Formspree:    https://formspree.io/f/<form-id>
  //   ConvertKit:   https://app.convertkit.com/forms/<form-id>/subscriptions
  //   MailerLite:   https://assets.mailerlite.com/jsonp/<account>/forms/<id>/subscribe
  // Leave empty to render a "coming soon" CTA instead of a live form.
  // After updating: `node scripts/test-live-subscribe.mjs` against prod
  // confirms a real round-trip.
  subscribeEndpoint: '',
  nav: [
    { label: 'Work', href: '/#work' },
    { label: 'Notes', href: '/notes' },
    { label: 'Building', href: '/building' },
    { label: 'About', href: '/about' },
    { label: 'CV', href: '/cv' },
    { label: 'Contact', href: '/contact' },
  ],
  socials: [
    { label: 'GitHub', href: 'https://github.com/Artufe' },
    { label: 'LinkedIn', href: 'https://www.linkedin.com/in/arthur-buikis-002145151/' },
    { label: 'Upwork', href: 'https://www.upwork.com/freelancers/abuikis' },
  ],
  bio: {
    jobTitle: 'AI & ML infrastructure engineer · freelance / consulting',
    location: { city: 'Riga', country: 'LV', timezone: 'Europe/Riga' },
    summary:
      'AI & ML infrastructure engineer based in Riga. About twelve years in Python with Rust (PyO3) for hot paths. Available for freelance and consulting — integrating ML models into production pipelines, building inference platforms, and shipping performance-critical AI backends.',
    knowsAbout: [
      'Python',
      'Rust',
      'PyO3',
      'Celery',
      'Kubernetes',
      'Postgres',
      'AI infrastructure',
      'ML pipeline integration',
      'Model serving',
      'Triton Inference Server',
      'MLOps',
      'Backend engineering',
      'Platform engineering',
      'Performance engineering',
      'Data infrastructure',
      'AI consulting',
      'Freelance AI developer',
    ],
  },
};
