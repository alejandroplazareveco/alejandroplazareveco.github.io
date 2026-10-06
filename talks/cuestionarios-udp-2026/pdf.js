const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args:['--no-sandbox'] });
  const p = await b.newPage();
  await p.goto('file://'+process.cwd()+'/clase_cuestionarios.html?print-pdf', { waitUntil: 'networkidle' });
  await p.waitForTimeout(4000);
  await p.pdf({ path: 'clase_cuestionarios-respaldo.pdf', width: '1600px', height: '900px',
                printBackground: true, margin: {top:0,right:0,bottom:0,left:0} });
  await b.close(); console.log('pdf ok');
})();
