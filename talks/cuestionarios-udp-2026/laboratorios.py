"""Los ocho laboratorios interactivos (HTML + JS vanilla, sin dependencias)."""
W = {}

# Utilidades compartidas (se inyectan una vez, en la portada)
W["utils"] = r"""
<script>
window.LAB = {
  randn: function(){ let u=0,v=0; while(!u)u=Math.random(); while(!v)v=Math.random();
    return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v); },
  svg: function(tag, attrs){ const e=document.createElementNS('http://www.w3.org/2000/svg',tag);
    for(const k in attrs) e.setAttribute(k, attrs[k]); return e; },
  fmt: function(x,d){ return x.toFixed(d===undefined?1:d).replace('.',','); },
  // evita que las flechas del teclado en un slider cambien de slide
  guard: function(root){ root.querySelectorAll('input').forEach(function(i){
    i.addEventListener('keydown', function(e){ e.stopPropagation(); }); }); }
};
</script>
"""

# ---------------------------------------------------------------------------
# 1. Tiro al blanco
# ---------------------------------------------------------------------------
W["tiro"] = r"""
<div class="lab" id="lab-tiro">
  <svg viewBox="0 0 420 420" id="tiro-svg">
    <circle cx="210" cy="210" r="195" fill="#17243C" stroke="#3E5578" stroke-width="2"/>
    <circle cx="210" cy="210" r="135" fill="#1F3152"/>
    <circle cx="210" cy="210" r="78" fill="#2B4268"/>
    <circle cx="210" cy="210" r="22" fill="#D9BC66"/>
    <g id="tiro-shots"></g>
    <g id="tiro-mean"></g>
  </svg>
  <div class="panel">
    <label>Sesgo (error sistemático): <b id="tiro-bv"></b></label>
    <input type="range" id="tiro-b" min="0" max="140" value="0">
    <label>Dispersión (error aleatorio): <b id="tiro-sv"></b></label>
    <input type="range" id="tiro-s" min="4" max="90" value="20">
    <div>
      <button class="btn" id="tiro-1">Disparar 1</button>
      <button class="btn" id="tiro-10">Disparar 10</button>
      <button class="btn sec" id="tiro-0">Limpiar</button>
    </div>
    <div class="presets">
      <button class="btn sec chico" data-p="0,10">Ideal</button>
      <button class="btn sec chico" data-p="0,70">Aleatorio</button>
      <button class="btn sec chico" data-p="95,10">Sistemático</button>
      <button class="btn sec chico" data-p="90,65">Ambos</button>
    </div>
    <div class="lectura">
      <div><span class="k">Disparos</span><span class="v" id="tiro-n">0</span></div>
      <div><span class="k">Distancia del promedio al centro</span><span class="v" id="tiro-d">–</span></div>
    </div>
    <p class="glosa">La <span class="hl">cruz</span> marca el promedio de los disparos. Con más disparos, el error aleatorio se compensa; el sesgo, no.</p>
  </div>
</div>
<script>
(function(){
  const $=id=>document.getElementById(id), L=window.LAB;
  const shots=[], g=$('tiro-shots'), gm=$('tiro-mean');
  function upd(){ $('tiro-bv').textContent=$('tiro-b').value; $('tiro-sv').textContent=$('tiro-s').value; }
  function draw(){
    g.innerHTML=''; gm.innerHTML='';
    shots.forEach(s=>g.appendChild(L.svg('circle',{cx:s[0],cy:s[1],r:7,fill:'#E8E3D9',stroke:'#0F1A2E','stroke-width':2})));
    $('tiro-n').textContent=shots.length;
    if(!shots.length){ $('tiro-d').textContent='–'; return; }
    const mx=shots.reduce((a,s)=>a+s[0],0)/shots.length, my=shots.reduce((a,s)=>a+s[1],0)/shots.length;
    const st={stroke:'#7FB0DC','stroke-width':5,'stroke-linecap':'round'};
    gm.appendChild(L.svg('line',Object.assign({x1:mx-16,y1:my-16,x2:mx+16,y2:my+16},st)));
    gm.appendChild(L.svg('line',Object.assign({x1:mx-16,y1:my+16,x2:mx+16,y2:my-16},st)));
    $('tiro-d').textContent=Math.round(Math.hypot(mx-210,my-210));
  }
  function shoot(n){
    const b=+$('tiro-b').value, s=+$('tiro-s').value;
    for(let i=0;i<n;i++){
      shots.push([210+b*0.71+L.randn()*s, 210-b*0.71+L.randn()*s]);
    }
    draw();
  }
  $('tiro-1').onclick=()=>shoot(1); $('tiro-10').onclick=()=>shoot(10);
  $('tiro-0').onclick=()=>{shots.length=0; draw();};
  ['tiro-b','tiro-s'].forEach(id=>$(id).oninput=upd);
  document.querySelectorAll('#lab-tiro .presets button').forEach(bt=>bt.onclick=()=>{
    const p=bt.dataset.p.split(','); $('tiro-b').value=p[0]; $('tiro-s').value=p[1]; upd();
    shots.length=0; shoot(10);
  });
  L.guard($('lab-tiro')); upd(); shoot(10);
})();
</script>
"""

# ---------------------------------------------------------------------------
# 2. ¿Por cuánto? Muestreo e intervalos (MEPCO)
# ---------------------------------------------------------------------------
W["muestreo"] = r"""
<div class="lab lab-ancho" id="lab-mu">
  <svg viewBox="0 0 900 430" id="mu-svg">
    <g id="mu-eje"></g>
    <g id="mu-int"></g>
  </svg>
  <div class="panel">
    <label>Tamaño de muestra: <b id="mu-nv"></b> personas</label>
    <input type="range" id="mu-n" min="100" max="3000" step="100" value="700">
    <label>Sesgo de no respuesta: <b id="mu-bv"></b> puntos</label>
    <input type="range" id="mu-b" min="0" max="8" step="1" value="0">
    <div>
      <button class="btn" id="mu-1">Hacer 1 encuesta</button>
      <button class="btn" id="mu-20">Hacer 20</button>
      <button class="btn sec" id="mu-0">Limpiar</button>
    </div>
    <div class="lectura">
      <div><span class="k">Margen de error (95%)</span><span class="v" id="mu-me">–</span></div>
      <div><span class="k">Intervalos que contienen el 48%</span><span class="v" id="mu-cov">–</span></div>
    </div>
    <p class="glosa">Cada línea es una encuesta distinta. <span class="hld">Verde</span>: el intervalo contiene el valor verdadero. <span class="hlx">Rojo</span>: no lo contiene.</p>
  </div>
</div>
<script>
(function(){
  const $=id=>document.getElementById(id), L=window.LAB;
  const P=0.48, X0=60, X1=870, lo=0.30, hi=0.66, maxRows=24, top=40, rowH=14.5;
  const sx=p=>X0+(p-lo)/(hi-lo)*(X1-X0);
  const surveys=[];
  // eje
  const ej=$('mu-eje');
  ej.appendChild(L.svg('line',{x1:X0,y1:395,x2:X1,y2:395,stroke:'#9BA9BF','stroke-width':2}));
  for(let p=0.30;p<=0.661;p+=0.06){
    ej.appendChild(L.svg('line',{x1:sx(p),y1:395,x2:sx(p),y2:403,stroke:'#9BA9BF','stroke-width':2}));
    const t=L.svg('text',{x:sx(p),y:425,'text-anchor':'middle','font-size':20,fill:'#9BA9BF'}); t.textContent=Math.round(p*100)+'%'; ej.appendChild(t);
  }
  ej.appendChild(L.svg('line',{x1:sx(P),y1:18,x2:sx(P),y2:395,stroke:'#D9BC66','stroke-width':3,'stroke-dasharray':'8 6'}));
  const tv=L.svg('text',{x:sx(P)+8,y:24,'font-size':19,fill:'#F0D588','font-weight':600}); tv.textContent='valor verdadero: 48%'; ej.appendChild(tv);
  function upd(){ $('mu-nv').textContent=$('mu-n').value; $('mu-bv').textContent=$('mu-b').value;
    const n=+$('mu-n').value; $('mu-me').textContent='± '+L.fmt(196*Math.sqrt(P*(1-P)/n),1)+' pts'; }
  function draw(){
    const g=$('mu-int'); g.innerHTML='';
    const vis=surveys.slice(-maxRows);
    vis.forEach((s,i)=>{
      const y=top+i*rowH, ok=(s.l<=P && s.h>=P), c=ok?'#A3BE86':'#E08C81';
      g.appendChild(L.svg('line',{x1:sx(Math.max(lo,s.l)),y1:y,x2:sx(Math.min(hi,s.h)),y2:y,stroke:c,'stroke-width':4,'stroke-linecap':'round'}));
      g.appendChild(L.svg('circle',{cx:sx(s.p),cy:y,r:5,fill:c}));
    });
    if(surveys.length){ const k=surveys.filter(s=>s.l<=P&&s.h>=P).length;
      $('mu-cov').textContent=Math.round(100*k/surveys.length)+'% ('+k+'/'+surveys.length+')'; }
    else $('mu-cov').textContent='–';
  }
  function encuestar(m){
    const n=+$('mu-n').value, b=+$('mu-b').value/100;
    for(let i=0;i<m;i++){
      const pt=P+b; const ph=Math.min(0.99,Math.max(0.01,pt+L.randn()*Math.sqrt(pt*(1-pt)/n)));
      const me=1.96*Math.sqrt(ph*(1-ph)/n); surveys.push({p:ph,l:ph-me,h:ph+me});
    }
    draw();
  }
  $('mu-1').onclick=()=>encuestar(1); $('mu-20').onclick=()=>encuestar(20);
  $('mu-0').onclick=()=>{surveys.length=0; draw();};
  $('mu-n').oninput=upd; $('mu-b').oninput=upd;
  L.guard($('lab-mu')); upd(); encuestar(12);
})();
</script>
"""

# ---------------------------------------------------------------------------
# 3. ¿Qué nivel de medición? (tarjetas)
# ---------------------------------------------------------------------------
_niveles = [
    ("Edad en años cumplidos", "Continua", "Un año más es siempre un año más: tiene sentido promediar."),
    ("Edad en tramos: 18–29, 30–44, 45–64, 65+", "Ordinal", "Hay orden, pero los tramos no tienen el mismo ancho."),
    ("Comuna de residencia", "Nominal", "Categorías distintas, sin ningún orden."),
    ("Satisfacción con la vida, de 1 a 10", "Ordinal", "…aunque en la práctica muchas veces se trata como continua."),
    ("Número de amigos cercanos", "Continua", "Es un conteo: numérica (discreta), con distancias iguales."),
    ("Candidato por el que votó", "Nominal", "Ningún candidato es «más» que otro."),
]
_cards = "".join(
    f'<div class="tarjeta" onclick="this.classList.toggle(\'abierta\')"><span class="num">{i}</span>'
    f'<div class="q">{q}</div><div class="resp"><b>{a}</b><span>{e}</span></div></div>'
    for i, (q, a, e) in enumerate(_niveles, 1)
)
W["niveles"] = f'<div class="tarjetas">{_cards}</div>'

# ---------------------------------------------------------------------------
# 4. ¿Por qué varias preguntas? (correlación con el valor verdadero)
# ---------------------------------------------------------------------------
W["items"] = r"""
<div class="lab" id="lab-it">
  <svg viewBox="0 0 520 470" id="it-svg">
    <g id="it-ejes"></g><g id="it-pts"></g>
  </svg>
  <div class="panel">
    <label>Número de preguntas en la escala: <b id="it-kv"></b></label>
    <input type="range" id="it-k" min="1" max="12" value="1">
    <div><button class="btn sec" id="it-new">Nuevas personas</button></div>
    <div class="lectura">
      <div><span class="k">Correlación entre puntaje y valor verdadero</span><span class="v" id="it-r">–</span></div>
      <div><span class="k">Confiabilidad aproximada (r²)</span><span class="v" id="it-r2">–</span></div>
    </div>
    <p class="glosa">Cada punto es una persona. Eje horizontal: su <span class="hlr">valor verdadero</span> (que en la realidad nunca vemos). Eje vertical: el <span class="hl">promedio de sus respuestas</span>. Cada pregunta trae su propio error; al promediar varias, los errores se compensan.</p>
  </div>
</div>
<script>
(function(){
  const $=id=>document.getElementById(id), L=window.LAB, N=220, K=12, SD=1.4;
  let V=[], E=[];
  const sx=v=>60+(v+3)/6*440, sy=v=>420-(v+3)/6*400;
  const ej=$('it-ejes');
  ej.appendChild(L.svg('line',{x1:60,y1:420,x2:500,y2:420,stroke:'#9BA9BF','stroke-width':2}));
  ej.appendChild(L.svg('line',{x1:60,y1:20,x2:60,y2:420,stroke:'#9BA9BF','stroke-width':2}));
  ej.appendChild(L.svg('line',{x1:sx(-3),y1:sy(-3),x2:sx(3),y2:sy(3),stroke:'#D9BC66','stroke-width':2,'stroke-dasharray':'6 6'}));
  let t=L.svg('text',{x:280,y:458,'text-anchor':'middle','font-size':19,fill:'#9BA9BF'}); t.textContent='valor verdadero'; ej.appendChild(t);
  t=L.svg('text',{x:22,y:220,'text-anchor':'middle','font-size':19,fill:'#9BA9BF',transform:'rotate(-90 22 220)'}); t.textContent='puntaje en la escala'; ej.appendChild(t);
  function gen(){ V=[];E=[]; for(let i=0;i<N;i++){ V.push(L.randn()); const e=[]; for(let k=0;k<K;k++) e.push(L.randn()*SD); E.push(e);} }
  function draw(){
    const k=+$('it-k').value; $('it-kv').textContent=k;
    const S=V.map((v,i)=>v+E[i].slice(0,k).reduce((a,b)=>a+b,0)/k);
    const g=$('it-pts'); g.innerHTML='';
    S.forEach((s,i)=>g.appendChild(L.svg('circle',{cx:sx(V[i]),cy:sy(Math.max(-3,Math.min(3,s))),r:4.5,fill:'#7FB0DC','fill-opacity':.75})));
    const mv=V.reduce((a,b)=>a+b)/N, ms=S.reduce((a,b)=>a+b)/N;
    let c=0,a=0,b=0; for(let i=0;i<N;i++){c+=(V[i]-mv)*(S[i]-ms);a+=(V[i]-mv)**2;b+=(S[i]-ms)**2;}
    const r=c/Math.sqrt(a*b); $('it-r').textContent=L.fmt(r,2); $('it-r2').textContent=L.fmt(r*r,2);
  }
  $('it-k').oninput=draw; $('it-new').onclick=()=>{gen();draw();};
  L.guard($('lab-it')); gen(); draw();
})();
</script>
"""

# ---------------------------------------------------------------------------
# 5. Mapa del error total, clickeable
# ---------------------------------------------------------------------------
_tse_info = {
    "validez": ("Validez", "La pregunta no captura el concepto que queremos medir.",
                "Medir «participación política» solo con el voto deja fuera protestas, organizaciones y redes."),
    "medicion": ("Error de medición", "La respuesta se aleja del valor verdadero por la pregunta, el encuestador o la situación.",
                 "«¿Ha consumido drogas?» preguntado cara a cara, con la familia en la sala."),
    "proc": ("Error de procesamiento", "Errores al digitar, codificar o limpiar los datos.",
             "Una escala codificada 1, 2, 3, 4, <b>6</b>: todos los promedios quedan inflados. O codificar «trabaja en el retail»: ¿cajero o gerente?"),
    "cobertura": ("Error de cobertura", "El marco muestral no incluye a toda la población objetivo.",
                  "Una encuesta por teléfono fijo deja fuera a los hogares sin línea. En 1936, el <i>Literary Digest</i> encuestó a 2,4 millones de personas y predijo la derrota de Roosevelt."),
    "muestral": ("Error muestral", "La diferencia por haber estudiado una muestra y no a toda la población.",
                 "El «margen de error ± 3 puntos». Es el único con fórmula, y el único que publica la prensa."),
    "norespuesta": ("Error de no respuesta", "Quienes no responden son sistemáticamente distintos de quienes sí.",
                    "Personas con jornadas largas nunca están en casa; quienes votan aceptan más responder encuestas políticas."),
    "ajuste": ("Error de ajuste", "Los ponderadores corrigen mal (o no corrigen) los errores anteriores.",
               "Ponderar solo por sexo y edad cuando el sesgo es educacional."),
}

def _tse_svg():
    from svgkit import Diagram
    d = Diagram(1700, 400, "Error total de encuesta, interactivo")
    d.text(10, 28, "MEDICIÓN · ¿qué medimos y qué tan bien?", 22, "lbl azul", "start", "700")
    top = [("c1", "Constructo", "obs"), ("validez", "Validez", "err"), ("c2", "Pregunta", "obs"),
           ("medicion", "Error de\nmedición", "err"), ("c3", "Respuesta", "obs"),
           ("proc", "Error de\nprocesamiento", "err"), ("c4", "Respuesta\neditada", "obs")]
    for i, (k, t, kind) in enumerate(top):
        d.node(k, 85 + i * 182, 95, 158, 80, t, kind, 20, cls="clic" if kind == "err" else "")
    for i in range(len(top) - 1):
        d.arrow(top[i][0], top[i + 1][0])
    d.text(10, 205, "REPRESENTACIÓN · ¿a quiénes medimos?", 22, "lbl verde", "start", "700")
    bot = [("r1", "Población\nobjetivo", "obs"), ("cobertura", "Error de\ncobertura", "err"), ("r2", "Marco\nmuestral", "obs"),
           ("muestral", "Error\nmuestral", "err"), ("r3", "Muestra", "obs"), ("norespuesta", "Error de no\nrespuesta", "err"),
           ("r4", "Respon-\ndentes", "obs"), ("ajuste", "Error de\najuste", "err")]
    for i, (k, t, kind) in enumerate(bot):
        d.node(k, 85 + i * 182, 272, 158, 80, t, kind, 20, cls="clic" if kind == "err" else "")
    for i in range(len(bot) - 1):
        d.arrow(bot[i][0], bot[i + 1][0])
    d.node("est", 1610, 185, 170, 110, "Estadístico\nde la\nencuesta", "lat", 20)
    d.path("M1170,95 L1610,95 L1610,124", "g")
    d.path("M1442,272 L1610,272 L1610,246", "g")
    return d.svg()

import json
W["tse"] = (
    '<div id="lab-tse">' + _tse_svg() +
    '<div id="tse-panel" class="tse-panel"><span class="t">Hagan clic en un recuadro dorado</span>'
    '<span class="def">Cada uno es un lugar donde podemos perder la verdad.</span></div></div>'
    "<script>(function(){const I=" + json.dumps(_tse_info, ensure_ascii=False) + r""";
  const root=document.getElementById('lab-tse'), p=document.getElementById('tse-panel');
  root.querySelectorAll('.clic').forEach(function(g){
    g.addEventListener('click',function(){
      root.querySelectorAll('.clic').forEach(x=>x.classList.remove('activo')); g.classList.add('activo');
      const k=I[g.dataset.k]; p.innerHTML='<span class="t">'+k[0]+'</span><span class="def">'+k[1]+'</span><span class="ej"><b>Ejemplo.</b> '+k[2]+'</span>';
    });
  });
})();</script>"""
)

# ---------------------------------------------------------------------------
# 6. Preguntas mal hechas
# ---------------------------------------------------------------------------
_malas = [
    ("¿Está de acuerdo con que el gobierno aumente el sueldo mínimo y reduzca la jornada laboral?",
     "Pregunta doble", "Separar en dos preguntas: ¿y si apoyo el sueldo pero no la jornada?"),
    ("¿No está usted en contra de que no se prohíba fumar en los parques?",
     "Doble negación", "«¿Está de acuerdo con que se prohíba fumar en los parques?»"),
    ("¿Con qué frecuencia lee el diario? (Nunca / A veces / Frecuentemente)",
     "Términos vagos", "«En la última semana, ¿cuántos días leyó el diario?» (0 a 7)"),
    ("¿Cuánto se ha visto perjudicado por la delincuencia desatada que vive el país?",
     "Sesgada y con presupuesto", "«En los últimos 12 meses, ¿usted o alguien de su hogar fue víctima de un delito?»"),
    ("¿Cuál es su ingreso? (Menos de $500 mil / $500 mil a $1 millón / $1 a $2 millones)",
     "Categorías no exhaustivas ni excluyentes", "Agregar «Más de $2 millones» y límites que no se toquen: $500.001 a $1.000.000…"),
    ("¿Cuántas veces fue al médico el año pasado?",
     "Periodo ambiguo", "«En los últimos 12 meses, ¿cuántas veces consultó a un médico?»"),
]
_mcards = "".join(
    f'<div class="tarjeta larga" onclick="this.classList.toggle(\'abierta\')"><span class="num">{i}</span>'
    f'<div class="q">{q}</div><div class="resp"><b>{p}</b><span>{f}</span></div></div>'
    for i, (q, p, f) in enumerate(_malas, 1)
)
W["malas"] = f'<div class="tarjetas">{_mcards}</div>'

# ---------------------------------------------------------------------------
# 7. Aquiescencia: una relación fabricada
# ---------------------------------------------------------------------------
W["aquiescencia"] = r"""
<div class="lab" id="lab-aq">
  <svg viewBox="0 0 520 440" id="aq-svg"><g id="aq-g"></g></svg>
  <div class="panel">
    <label>Fuerza de la aquiescencia: <b id="aq-sv"></b></label>
    <input type="range" id="aq-s" min="0" max="10" value="6">
    <label>Formato de la escala</label>
    <div>
      <button class="btn" id="aq-mismo">4 ítems en la misma dirección</button>
      <button class="btn sec" id="aq-bal">Escala balanceada (2 + 2 invertidos)</button>
    </div>
    <div class="lectura">
      <div><span class="k">Diferencia observada (educación baja − alta)</span><span class="v" id="aq-dif">–</span></div>
      <div><span class="k">Diferencia verdadera</span><span class="v">0,00</span></div>
    </div>
    <p class="glosa">Simulación: 600 personas, con el <b>mismo</b> autoritarismo promedio en ambos grupos. Las personas con menos educación tienden a decir «de acuerdo» un poco más. La línea dorada es el promedio verdadero.</p>
  </div>
</div>
<script>
(function(){
  const $=id=>document.getElementById(id), L=window.LAB, N=600;
  let bal=false; const A=[],Z=[],ED=[],NZ=[];
  for(let i=0;i<N;i++){A.push(L.randn()); Z.push(Math.abs(L.randn())); ED.push(i%2); const nz=[]; for(let j=0;j<4;j++) nz.push(L.randn()*0.6); NZ.push(nz);}
  function puntaje(i,s){
    const q=s*(ED[i]===0?1:0.3)*Z[i]; let tot=0;
    for(let j=0;j<4;j++){
      const inv = bal && j>=2;
      // respuesta en escala 1-5 (continua), "acuerdo" sube con la aquiescencia
      const r = inv ? 3 - 0.8*A[i] + q + NZ[i][j] : 3 + 0.8*A[i] + q + NZ[i][j];
      tot += inv ? 6 - r : r;
    }
    return tot/4;
  }
  function draw(){
    const s=+$('aq-s').value/10*0.9; $('aq-sv').textContent=$('aq-s').value;
    let m=[0,0], n=[0,0]; for(let i=0;i<N;i++){ m[ED[i]]+=puntaje(i,s); n[ED[i]]++; }
    m=[m[0]/n[0], m[1]/n[1]];
    const g=$('aq-g'); g.innerHTML='';
    const y=v=>390-(v-2)/2*330;
    g.appendChild(L.svg('line',{x1:50,y1:390,x2:500,y2:390,stroke:'#9BA9BF','stroke-width':2}));
    [2,2.5,3,3.5,4].forEach(v=>{ const t=L.svg('text',{x:40,y:y(v)+6,'text-anchor':'end','font-size':17,fill:'#9BA9BF'}); t.textContent=L.fmt(v,1); g.appendChild(t);
      g.appendChild(L.svg('line',{x1:50,y1:y(v),x2:500,y2:y(v),stroke:'#2B3D5C','stroke-width':1})); });
    [['Educación baja',m[0],120,'#C9A84C'],['Educación alta',m[1],330,'#4E7FB0']].forEach(b=>{
      g.appendChild(L.svg('rect',{x:b[2],y:y(b[1]),width:120,height:390-y(b[1]),fill:b[3],rx:3}));
      let t=L.svg('text',{x:b[2]+60,y:y(b[1])-10,'text-anchor':'middle','font-size':22,'font-weight':700,fill:'#E8E3D9'}); t.textContent=L.fmt(b[1],2); g.appendChild(t);
      t=L.svg('text',{x:b[2]+60,y:420,'text-anchor':'middle','font-size':19,fill:'#9BA9BF'}); t.textContent=b[0]; g.appendChild(t);
    });
    g.appendChild(L.svg('line',{x1:50,y1:y(3),x2:500,y2:y(3),stroke:'#D9BC66','stroke-width':3,'stroke-dasharray':'9 6'}));
    $('aq-dif').textContent=L.fmt(m[0]-m[1],2);
  }
  $('aq-s').oninput=draw;
  $('aq-mismo').onclick=()=>{bal=false; $('aq-mismo').classList.remove('sec'); $('aq-bal').classList.add('sec'); draw();};
  $('aq-bal').onclick=()=>{bal=true; $('aq-bal').classList.remove('sec'); $('aq-mismo').classList.add('sec'); draw();};
  L.guard($('lab-aq')); draw();
})();
</script>
"""

# ---------------------------------------------------------------------------
# 8. Conjoint en vivo
# ---------------------------------------------------------------------------
W["conjoint"] = r"""
<div class="lab lab-cj" id="lab-cj">
  <div class="cj-pantalla">
    <div class="cj-top"><b>Ronda <span id="cj-r">1</span>.</b> Si tuviera que elegir alcalde/sa, ¿por quién votaría?</div>
    <table class="cj-tabla"><thead><tr><th></th><th>Candidatura A</th><th>Candidatura B</th></tr></thead><tbody id="cj-body"></tbody>
      <tfoot><tr><td>Manos alzadas</td>
        <td><input type="number" id="cj-va" class="cj-voto" min="0" max="200" value="0"></td>
        <td><input type="number" id="cj-vb" class="cj-voto" min="0" max="200" value="0"></td></tr></tfoot></table>
    <div class="cj-botones">
      <button class="btn" id="cj-ok">Registrar ronda y sortear otra</button>
      <button class="btn sec" id="cj-0">Reiniciar</button>
    </div>
    <div class="cj-hist" id="cj-hist"></div>
  </div>
  <div class="panel">
    <div class="cj-res-t">Porcentaje de votos que obtuvo la candidatura con cada característica</div>
    <div id="cj-res" class="cj-res"><p class="glosa">Después de 3 rondas aparecen los resultados.</p></div>
  </div>
</div>
<script>
(function(){
  const $=id=>document.getElementById(id), L=window.LAB;
  const ATR={'Edad':['32 años','47 años','63 años'],'Género':['Mujer','Hombre'],
    'Profesión':['Profesora','Empresario/a','Dirigente vecinal'],'Experiencia':['Ninguna','Concejal/a 8 años'],
    'Prioridad':['Seguridad','Vivienda','Salud']};
  let A,B,ronda=1,total=0; const st={};
  const reset=()=>{ Object.keys(ATR).forEach(k=>ATR[k].forEach(v=>st[k+'|'+v]={g:0,n:0})); };
  const pick=a=>a[Math.floor(Math.random()*a.length)];
  function nuevo(){ A={};B={}; Object.keys(ATR).forEach(k=>{A[k]=pick(ATR[k]); B[k]=pick(ATR[k]);});
    $('cj-body').innerHTML=Object.keys(ATR).map(k=>'<tr><td>'+k+'</td><td>'+A[k]+'</td><td>'+B[k]+'</td></tr>').join('');
    $('cj-r').textContent=ronda; $('cj-va').value=0; $('cj-vb').value=0; }
  function registrar(){
    const va=Math.max(0,parseInt($('cj-va').value)||0), vb=Math.max(0,parseInt($('cj-vb').value)||0), n=va+vb;
    if(!n){ $('cj-va').focus(); return; }
    // cada característica suma los votos de su candidatura sobre los votos totales de la ronda
    Object.keys(ATR).forEach(k=>{ st[k+'|'+A[k]].g+=va; st[k+'|'+A[k]].n+=n; st[k+'|'+B[k]].g+=vb; st[k+'|'+B[k]].n+=n; });
    total+=n; $('cj-hist').textContent='Ronda '+ronda+': A '+va+' · B '+vb+'  —  votos acumulados: '+total;
    ronda++; res(); nuevo();
  }
  function res(){
    if(ronda<=3){ $('cj-res').innerHTML='<p class="glosa">Después de 3 rondas aparecen los resultados.</p>'; return; }
    let h='';
    Object.keys(ATR).forEach(k=>{ h+='<div class="cj-k">'+k+'</div>';
      ATR[k].forEach(v=>{ const s=st[k+'|'+v], p=s.n?s.g/s.n:0;
        h+='<div class="cj-fila"><span class="cj-l">'+v+'</span><span class="cj-barra"><span style="width:'+Math.round(p*100)+'%"></span><i></i></span><span class="cj-p">'+(s.n?Math.round(p*100)+'%':'–')+'</span></div>'; }); });
    $('cj-res').innerHTML=h+'<p class="glosa">La línea marca 50%: lo esperable si la característica no importara. Con pocas rondas, los porcentajes son muy ruidosos (¡error aleatorio!).</p>';
  }
  $('cj-ok').onclick=registrar;
  $('cj-0').onclick=()=>{ reset(); ronda=1; total=0; $('cj-hist').textContent=''; res(); nuevo(); };
  document.querySelectorAll('#lab-cj .cj-voto').forEach(i=>{
    i.addEventListener('keydown',e=>{ e.stopPropagation(); if(e.key==='Enter') registrar(); });
    i.addEventListener('focus',()=>i.select());
  });
  reset(); nuevo();
})();
</script>
"""
