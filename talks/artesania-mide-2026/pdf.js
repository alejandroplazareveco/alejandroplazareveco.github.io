const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args:['--no-sandbox'] });
  const p = await b.newPage();
  await p.goto('file:///home/claude/quarto-poc/artesania.html?print-pdf', { waitUntil: 'networkidle' });
  await p.waitForTimeout(3500);
  await p.pdf({ path: 'artesania-respaldo.pdf', width: '1600px', height: '900px',
                printBackground: true, margin: {top:0,right:0,bottom:0,left:0}, pageRanges: '1-' });
  await b.close(); console.log('pdf ok');
})();
