const { chromium } = require('playwright');
(async () => {
  const want = process.argv.slice(2).map(Number);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args:['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1440, height: 810 } });
  const errs=[]; p.on('pageerror', e=>errs.push(e.message)); p.on('console', m=>{ if(m.type()==='error') errs.push(m.text()); });
  await p.goto('file://'+process.cwd()+'/clase_cuestionarios.html?print-pdf', { waitUntil: 'networkidle', timeout: 90000 });
  await p.waitForTimeout(5000);
  const pages = await p.$$('.reveal .slides .pdf-page');
  console.log('paginas:', pages.length, 'errores:', JSON.stringify(errs));
  const list = want.length ? want : pages.map((_,i)=>i+1);
  for (const n of list) if (pages[n-1]) await pages[n-1].screenshot({ path: `shots/p${String(n).padStart(2,'0')}.png` });
  await b.close();
})();
