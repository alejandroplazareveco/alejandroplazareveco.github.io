const { chromium } = require('playwright');
(async () => {
  const want = process.argv.slice(2).map(Number);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args:['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1440, height: 810 } });
  await p.goto('file:///home/claude/quarto-poc/artesania.html?print-pdf', { waitUntil: 'networkidle', timeout: 90000 });
  await p.waitForTimeout(5000);
  const pages = await p.$$('.reveal .slides .pdf-page');
  console.log('paginas:', pages.length);
  for (const n of want) if (pages[n-1]) await pages[n-1].screenshot({ path: `p${String(n).padStart(2,'0')}.png` });
  await b.close();
})();
