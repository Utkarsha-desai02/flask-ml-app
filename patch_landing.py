"""
Run this script in the same folder as your app.py.
It will replace the old LANDING_HTML (with SVG India map) 
with the new one (goa.png background, no SVG map).

Usage:  python patch_landing.py
"""
import re, shutil, os

src = "app.py"
backup = "app_backup.py"

if not os.path.exists(src):
    print("ERROR: app.py not found in current directory")
    exit(1)

shutil.copy(src, backup)
print(f"Backup saved to {backup}")

with open(src, "r", encoding="utf-8") as f:
    content = f.read()

NEW_LANDING = r'''LANDING_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Machine Learning Based Environmental Vulnerability Assessment for Goa</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --teal:#0d9488;--teal2:#14b8a6;--emerald:#059669;
  --ink:#0a1410;--mid:#3d5450;--soft:#7a8f8c;
  --paper:#f7faf9;--border:rgba(13,148,136,0.15);
}
html{scroll-behavior:smooth;font-size:16px}
body{font-family:'DM Sans',sans-serif;background:var(--paper);color:var(--ink);overflow-x:hidden;}
nav{position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:20px 56px;transition:all 0.4s ease;}
nav.scrolled{padding:14px 56px;background:rgba(247,250,249,0.96);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);box-shadow:0 4px 24px rgba(10,20,16,0.06);}
.nav-logo{display:flex;align-items:center;gap:12px;text-decoration:none;}
.nav-logo-mark{width:38px;height:38px;background:linear-gradient(135deg,var(--teal),var(--emerald));border-radius:10px;display:flex;align-items:center;justify-content:center;}
.nav-logo-mark img{width:30px;height:30px;object-fit:contain;border-radius:6px;}
.nav-brand-text{font-family:'DM Serif Display',serif;font-size:14px;color:var(--ink);max-width:240px;line-height:1.3;}
.nav-brand-text span{color:var(--teal);}
.nav-links{display:flex;align-items:center;gap:32px;}
.nav-links a{color:var(--mid);text-decoration:none;font-size:13px;font-weight:500;transition:color 0.2s;}
.nav-links a:hover{color:var(--teal);}
.nav-auth{display:flex;align-items:center;gap:10px;}
.nav-btn-outline{padding:9px 18px;border:1.5px solid var(--border);border-radius:50px;font-size:13px;font-weight:500;color:var(--mid);text-decoration:none;transition:all 0.25s;}
.nav-btn-outline:hover{border-color:var(--teal);color:var(--teal);}
.nav-btn-solid{padding:9px 20px;background:var(--ink);border-radius:50px;font-size:13px;font-weight:500;color:#fff;text-decoration:none;transition:all 0.25s;}
.nav-btn-solid:hover{background:var(--teal);}

/* ─── HERO ─── */
#hero{
  position:relative;
  width:100vw;
  min-height:100vh;
  display:flex;
  align-items:center;
  overflow:hidden;
}
.hero-bg{
  position:absolute;
  inset:0;
  background-image:url('/static/images/goa.png');
  background-size:cover;
  background-position:right center;
  background-repeat:no-repeat;
  z-index:0;
}
.hero-overlay{
  position:absolute;
  inset:0;
  background:linear-gradient(100deg,
    rgba(237,250,247,1.0) 0%,
    rgba(237,250,247,0.96) 30%,
    rgba(237,250,247,0.75) 55%,
    rgba(237,250,247,0.15) 80%,
    transparent 100%
  );
  z-index:1;
}
.hero-content{
  position:relative;
  z-index:2;
  padding:130px 80px 80px;
  max-width:700px;
}
.hero-badge{display:inline-flex;align-items:center;gap:8px;padding:7px 18px;background:rgba(13,148,136,0.1);border:1px solid rgba(13,148,136,0.2);border-radius:50px;margin-bottom:24px;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--teal);text-transform:uppercase;}
.hero-badge-dot{width:5px;height:5px;border-radius:50%;background:var(--teal);animation:blink 1.8s ease infinite;}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}
.hero-title{font-family:'DM Serif Display',serif;font-size:clamp(36px,4.5vw,62px);line-height:1.08;letter-spacing:-1.5px;color:var(--ink);margin-bottom:20px;}
.hero-title em{font-style:italic;color:var(--teal);}
.hero-sub{font-size:16px;line-height:1.85;color:var(--mid);max-width:500px;margin-bottom:36px;}
.hero-btns{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:32px;}
.btn-primary{display:inline-flex;align-items:center;gap:8px;padding:14px 28px;background:linear-gradient(135deg,var(--teal),var(--emerald));color:#fff;border-radius:50px;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.3s;box-shadow:0 8px 24px rgba(13,148,136,0.3);}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 12px 32px rgba(13,148,136,0.4);}
.btn-dark{display:inline-flex;align-items:center;gap:8px;padding:13px 24px;background:#1e3a5f;color:#fff;border-radius:50px;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.3s;box-shadow:0 8px 22px rgba(30,58,95,0.2);}
.btn-dark:hover{transform:translateY(-2px);background:#162d4a;}
.btn-ghost{display:inline-flex;align-items:center;gap:8px;padding:13px 22px;color:var(--mid);border:1.5px solid rgba(61,84,80,0.2);border-radius:50px;font-size:14px;font-weight:500;text-decoration:none;transition:all 0.3s;background:rgba(255,255,255,0.7);backdrop-filter:blur(8px);}
.btn-ghost:hover{border-color:var(--teal);color:var(--teal);}

/* Role access cards */
.access-cards{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:40px;}
.ac{padding:14px 18px;border-radius:16px;background:rgba(255,255,255,0.85);border:1.5px solid var(--border);text-decoration:none;transition:all 0.3s;backdrop-filter:blur(10px);display:flex;align-items:center;gap:10px;min-width:160px;}
.ac:hover{transform:translateY(-3px);box-shadow:0 10px 32px rgba(13,148,136,0.12);}
.ac.ac-auth{border-color:rgba(30,58,95,0.18);background:rgba(240,244,255,0.85);}
.ac.ac-auth:hover{box-shadow:0 10px 32px rgba(30,58,95,0.12);}
.ac-icon{font-size:20px;flex-shrink:0;}
.ac-text{}
.ac-title{font-size:13px;font-weight:600;color:var(--ink);display:block;}
.ac-sub{font-family:'Space Mono',monospace;font-size:8px;letter-spacing:1.5px;text-transform:uppercase;color:var(--teal);}
.ac.ac-auth .ac-sub{color:#1e3a5f;}

.hero-stats{display:flex;gap:32px;padding-top:28px;border-top:1px solid var(--border);}
.hstat-num{font-family:'DM Serif Display',serif;font-size:32px;color:var(--ink);letter-spacing:-1px;display:block;}
.hstat-num span{color:var(--teal);}
.hstat-label{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:var(--soft);}

/* ─── TICKER ─── */
.ticker-wrap{overflow:hidden;padding:13px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border);background:var(--paper);}
.ticker{display:flex;gap:18px;animation:tickScroll 22s linear infinite;white-space:nowrap;}
@keyframes tickScroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.tick-chip{display:inline-flex;align-items:center;gap:7px;padding:6px 16px;border:1px solid var(--border);border-radius:50px;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--mid);text-transform:uppercase;background:rgba(255,255,255,0.6);flex-shrink:0;}
.tick-chip::before{content:'';width:4px;height:4px;border-radius:50%;background:var(--teal);flex-shrink:0;}

/* ─── STATS ROW ─── */
.stats-row{display:flex;border-top:1.5px solid var(--border);border-bottom:1.5px solid var(--border);}
.stat-cell{flex:1;padding:44px 36px;border-right:1.5px solid var(--border);text-align:center;opacity:0;transform:translateY(18px);transition:opacity 0.6s ease,transform 0.6s ease;}
.stat-cell:last-child{border-right:none;}
.stat-cell.visible{opacity:1;transform:translateY(0);}
.stat-num-big{font-family:'DM Serif Display',serif;font-size:52px;color:var(--ink);letter-spacing:-2px;display:block;margin-bottom:6px;}
.stat-num-big span{color:var(--teal);}
.stat-label{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--soft);text-transform:uppercase;}

/* ─── SECTIONS ─── */
.section{padding:100px 80px;}
.section-tinted{background:linear-gradient(135deg,#edfaf7,#f5fffe);}
.section-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;}
.section-inner.rev{direction:rtl;}
.section-inner.rev > *{direction:ltr;}
.section-tag{display:inline-block;padding:5px 14px;background:rgba(13,148,136,0.1);border:1px solid rgba(13,148,136,0.2);border-radius:50px;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--teal);text-transform:uppercase;margin-bottom:18px;}
.section-num{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:3px;color:var(--soft);text-transform:uppercase;margin-bottom:12px;}
.section-title{font-family:'DM Serif Display',serif;font-size:clamp(30px,3.5vw,48px);line-height:1.1;letter-spacing:-1.5px;color:var(--ink);margin-bottom:16px;}
.section-title em{font-style:italic;color:var(--teal);}
.section-body{font-size:16px;line-height:1.85;color:var(--mid);}
.data-card{background:rgba(255,255,255,0.92);border:1.5px solid var(--border);border-radius:22px;padding:28px;box-shadow:0 16px 48px rgba(13,148,136,0.08);position:relative;overflow:hidden;}
.data-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--teal),var(--emerald));}
.data-card-label{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2.5px;color:var(--soft);text-transform:uppercase;margin-bottom:18px;}
.factor-rows{display:flex;flex-direction:column;gap:11px;}
.frow{display:flex;align-items:center;gap:10px;}
.frow-label{font-family:'Space Mono',monospace;font-size:9px;color:var(--mid);width:110px;flex-shrink:0;text-transform:uppercase;letter-spacing:1px;}
.frow-bar{flex:1;height:3px;background:rgba(13,148,136,0.1);border-radius:2px;overflow:hidden;}
.frow-fill{height:100%;border-radius:2px;background:linear-gradient(90deg,var(--teal),var(--emerald));width:0%;transition:width 1.2s cubic-bezier(0.16,1,0.3,1);}
.frow-val{font-family:'Space Mono',monospace;font-size:9px;color:var(--teal);width:34px;text-align:right;}
.mli{display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--border);}
.mli:last-child{border-bottom:none;}
.mli-l{display:flex;align-items:center;gap:11px;}
.mli-name{font-size:13px;font-weight:600;color:var(--ink);}
.mli-full{font-family:'Space Mono',monospace;font-size:9px;color:var(--soft);letter-spacing:1px;}
.mli-status{font-family:'Space Mono',monospace;font-size:9px;color:var(--teal);letter-spacing:1.5px;}
.cov-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
.cov-item{display:flex;align-items:center;gap:8px;padding:9px 11px;background:rgba(13,148,136,0.04);border:1px solid var(--border);border-radius:9px;}
.cov-dot{width:5px;height:5px;border-radius:50%;background:var(--teal);flex-shrink:0;}
.cov-name{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:1.5px;color:var(--mid);text-transform:uppercase;}
.feat-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;max-width:1200px;margin:0 auto;padding:0 80px 90px;}
.feat{padding:30px;border-radius:20px;background:rgba(255,255,255,0.85);border:1.5px solid var(--border);transition:all 0.35s;opacity:0;transform:translateY(20px);}
.feat.visible{opacity:1;transform:translateY(0);}
.feat:hover{transform:translateY(-5px);box-shadow:0 16px 48px rgba(13,148,136,0.12);}
.feat-icon{width:48px;height:48px;border-radius:13px;background:rgba(13,148,136,0.1);display:flex;align-items:center;justify-content:center;font-size:21px;margin-bottom:16px;}
.feat-title{font-family:'DM Serif Display',serif;font-size:20px;color:var(--ink);margin-bottom:8px;}
.feat-body{font-size:14px;line-height:1.75;color:var(--mid);}

/* ─── CTA ─── */
.cta-section{padding:90px 80px;text-align:center;background:linear-gradient(135deg,#edfaf7,var(--paper));border-top:1.5px solid var(--border);}
.cta-title{font-family:'DM Serif Display',serif;font-size:clamp(34px,5vw,60px);color:var(--ink);letter-spacing:-2px;margin-bottom:16px;line-height:1.05;}
.cta-title em{font-style:italic;color:var(--teal);}
.cta-sub{font-size:16px;color:var(--mid);line-height:1.8;max-width:460px;margin:0 auto 40px;}
.cta-roles{display:flex;align-items:stretch;justify-content:center;gap:18px;flex-wrap:wrap;}
.cta-card{display:flex;flex-direction:column;align-items:center;gap:9px;padding:26px 22px;border-radius:20px;text-decoration:none;transition:all 0.3s;min-width:180px;position:relative;overflow:hidden;}
.cta-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;}
.cta-res{background:rgba(13,148,136,0.07);border:1.5px solid rgba(13,148,136,0.22);}
.cta-res::before{background:linear-gradient(90deg,var(--teal),var(--emerald));}
.cta-res:hover{transform:translateY(-5px);box-shadow:0 14px 36px rgba(13,148,136,0.15);}
.cta-auth{background:rgba(30,58,95,0.06);border:1.5px solid rgba(30,58,95,0.18);}
.cta-auth::before{background:linear-gradient(90deg,#1e3a5f,#2563eb);}
.cta-auth:hover{transform:translateY(-5px);box-shadow:0 14px 36px rgba(30,58,95,0.12);}
.cta-icon{font-size:30px;}
.cta-card-title{font-family:'DM Serif Display',serif;font-size:17px;color:var(--ink);}
.cta-card-desc{font-family:'Space Mono',monospace;font-size:8px;letter-spacing:1.5px;text-transform:uppercase;color:var(--soft);text-align:center;}
.cta-btn{margin-top:4px;padding:7px 18px;border-radius:50px;font-size:12px;font-weight:600;color:white;}
.cta-btn-res{background:linear-gradient(135deg,var(--teal),var(--emerald));}
.cta-btn-auth{background:linear-gradient(135deg,#1e3a5f,#2563eb);}

footer{padding:28px 80px;display:flex;align-items:center;justify-content:space-between;border-top:1px solid var(--border);font-family:'Space Mono',monospace;font-size:9px;letter-spacing:1.5px;color:var(--soft);text-transform:uppercase;}

@media(max-width:900px){
  .hero-content{padding:100px 24px 60px;max-width:100%;}
  .access-cards{flex-wrap:wrap;}
  .section-inner{grid-template-columns:1fr;gap:36px;padding:0;}
  .section{padding:60px 24px;}
  .feat-grid{grid-template-columns:1fr;padding:0 24px 60px;}
  .stats-row{flex-direction:column;}
  .stat-cell{border-right:none;border-bottom:1.5px solid var(--border);}
  nav{padding:14px 20px;}
  footer{flex-direction:column;gap:8px;text-align:center;padding:20px;}
  .cta-section{padding:60px 24px;}
}
</style>
</head>
<body>

<nav id="nav">
  <a class="nav-logo" href="/">
    <div class="nav-logo-mark">
      <img src="/static/images/logo.jpg" alt="EVA" onerror="this.parentElement.innerHTML='🌿'">
    </div>
    <div class="nav-brand-text">ML-Based Environmental<br><span>Vulnerability Assessment · Goa</span></div>
  </a>
  <div class="nav-links">
    <a href="#how">How It Works</a>
    <a href="#coverage">Areas</a>
    <a href="#models">Models</a>
  </div>
  <div class="nav-auth">
    <a href="{{ url_for('login') }}" class="nav-btn-outline">Researcher Login</a>
    <a href="{{ url_for('authority_login') }}" class="nav-btn-solid">Authority Login</a>
  </div>
</nav>

<!-- ═══ HERO — goa.png full background, NO SVG MAP ═══ -->
<section id="hero">
  <div class="hero-bg"></div>
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <div class="hero-badge"><div class="hero-badge-dot"></div>Final Year Research Project</div>
    <h1 class="hero-title">
      Machine Learning Based<br>
      <em>Environmental Vulnerability</em><br>
      Assessment for Goa
    </h1>
    <p class="hero-sub">Landslide risk mapped across all 12 talukas of Goa using five computer models trained on satellite images — helping researchers and authorities understand where the land is most at risk.</p>

    <div class="hero-btns">
      <a href="{{ url_for('register') }}" class="btn-primary">👤 Researcher Sign Up</a>
      <a href="{{ url_for('authority_register') }}" class="btn-dark">🏛️ Authority Register</a>
      <a href="{{ url_for('login') }}" class="btn-ghost">Sign In</a>
    </div>

    <div class="access-cards">
      <a href="{{ url_for('login') }}" class="ac">
        <span class="ac-icon">👤</span>
        <div class="ac-text"><span class="ac-title">Researcher</span><span class="ac-sub">Login →</span></div>
      </a>
      <a href="{{ url_for('register') }}" class="ac">
        <span class="ac-icon">📝</span>
        <div class="ac-text"><span class="ac-title">Register</span><span class="ac-sub">New Account →</span></div>
      </a>
      <a href="{{ url_for('authority_login') }}" class="ac ac-auth">
        <span class="ac-icon">🏛️</span>
        <div class="ac-text"><span class="ac-title">Authority</span><span class="ac-sub">Login →</span></div>
      </a>
      <a href="{{ url_for('authority_register') }}" class="ac ac-auth">
        <span class="ac-icon">🔐</span>
        <div class="ac-text"><span class="ac-title">Auth. Register</span><span class="ac-sub">Apply →</span></div>
      </a>
    </div>

    <div class="hero-stats">
      <div><span class="hstat-num">12</span><span class="hstat-label">Talukas</span></div>
      <div><span class="hstat-num">5</span><span class="hstat-label">Models</span></div>
      <div><span class="hstat-num">60<span>+</span></span><span class="hstat-label">Risk Maps</span></div>
    </div>
  </div>
</section>

<!-- TICKER -->
<div class="ticker-wrap">
  <div class="ticker">
    {% for t in taluks %}<div class="tick-chip">{{ t }}</div>{% endfor %}
    {% for t in taluks %}<div class="tick-chip">{{ t }}</div>{% endfor %}
    {% for t in taluks %}<div class="tick-chip">{{ t }}</div>{% endfor %}
  </div>
</div>

<!-- STATS -->
<div class="stats-row">
  <div class="stat-cell" data-delay="0"><span class="stat-num-big" id="cnt1">0</span><div class="stat-label">Areas fully mapped</div></div>
  <div class="stat-cell" data-delay="100"><span class="stat-num-big" id="cnt2">0</span><div class="stat-label">Models deployed</div></div>
  <div class="stat-cell" data-delay="200"><span class="stat-num-big"><span id="cnt3">0</span><span style="color:var(--teal)">+</span></span><div class="stat-label">Risk maps available</div></div>
  <div class="stat-cell" data-delay="300"><span class="stat-num-big" style="font-size:38px">Goa</span><div class="stat-label">Complete state coverage</div></div>
</div>

<!-- HOW IT WORKS -->
<section class="section" id="how">
  <div class="section-inner">
    <div data-reveal>
      <div class="section-num">01 / 04</div>
      <div class="section-tag">How It Works</div>
      <h2 class="section-title">Goa's landslide risk,<br>mapped <em>area by area</em></h2>
      <p class="section-body">Satellite images of Goa were used to train models to recognise high-risk terrain. Key factors include vegetation, water presence, soil moisture, land use, and historical landslide data.</p>
    </div>
    <div data-reveal>
      <div class="data-card">
        <div class="data-card-label">Risk Factors Studied</div>
        <div class="factor-rows">
          <div class="frow"><span class="frow-label">Vegetation</span><div class="frow-bar"><div class="frow-fill" data-w="82"></div></div><span class="frow-val">82%</span></div>
          <div class="frow"><span class="frow-label">Water Cover</span><div class="frow-bar"><div class="frow-fill" data-w="70"></div></div><span class="frow-val">70%</span></div>
          <div class="frow"><span class="frow-label">Soil Moisture</span><div class="frow-bar"><div class="frow-fill" data-w="65"></div></div><span class="frow-val">65%</span></div>
          <div class="frow"><span class="frow-label">Land Use</span><div class="frow-bar"><div class="frow-fill" data-w="75"></div></div><span class="frow-val">75%</span></div>
          <div class="frow"><span class="frow-label">Slide History</span><div class="frow-bar"><div class="frow-fill" data-w="88"></div></div><span class="frow-val">88%</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- MODELS -->
<section class="section section-tinted" id="models">
  <div class="section-inner rev">
    <div data-reveal>
      <div class="section-num">02 / 04</div>
      <div class="section-tag">Models</div>
      <h2 class="section-title">Five models,<br><em>one clear answer</em></h2>
      <p class="section-body">CNN, Random Forest, SVM, K-Nearest Neighbours, and Logistic Regression each analyse the same satellite data differently. Agreement across models means high confidence.</p>
    </div>
    <div data-reveal>
      <div class="data-card">
        <div class="data-card-label">Available Models</div>
        {% for m, name in model_names.items() %}
        <div class="mli">
          <div class="mli-l">
            <span style="font-size:17px">{{ icons[m] }}</span>
            <div>
              <div class="mli-name">{{ m }}</div>
              <div class="mli-full">{{ name.split('—')[1].strip() if '—' in name else name }}</div>
            </div>
          </div>
          <div class="mli-status">● Active</div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<!-- COVERAGE -->
<section class="section" id="coverage">
  <div class="section-inner">
    <div data-reveal>
      <div class="section-num">03 / 04</div>
      <div class="section-tag">Coverage</div>
      <h2 class="section-title">All 12 talukas,<br><em>fully covered</em></h2>
      <p class="section-body">From Pernem in the north to Canacona in the south — every area of Goa has a complete risk assessment based on actual satellite data.</p>
    </div>
    <div data-reveal>
      <div class="data-card">
        <div class="data-card-label">Talukas — Goa State</div>
        <div class="cov-grid">
          {% for t in taluks %}
          <div class="cov-item">
            <div class="cov-dot"></div>
            <span class="cov-name">{{ t }}</span>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FEATURES -->
<section style="padding:60px 0 0" id="platform">
  <div style="text-align:center;padding:0 80px 44px;max-width:580px;margin:0 auto">
    <div class="section-tag">04 / 04 — Platform</div>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(30px,4vw,48px);color:var(--ink);letter-spacing:-1.5px;margin-top:16px;line-height:1.1">Built for <em style="font-style:italic;color:var(--teal)">researchers</em></h2>
  </div>
  <div class="feat-grid">
    <div class="feat" data-reveal><div class="feat-icon">🗺️</div><div class="feat-title">Visual Risk Maps</div><p class="feat-body">Colour maps from deep green (safe) to dark red (very high risk) for every part of Goa.</p></div>
    <div class="feat" data-reveal><div class="feat-icon">🔬</div><div class="feat-title">5 Trained Models</div><p class="feat-body">Compare results across five models. When they agree, the risk reading is solid.</p></div>
    <div class="feat" data-reveal><div class="feat-icon">📊</div><div class="feat-title">Risk Breakdown</div><p class="feat-body">See percentages for Low, Moderate, High, and Very High risk per taluka.</p></div>
    <div class="feat" data-reveal><div class="feat-icon">🔐</div><div class="feat-title">Secure Access</div><p class="feat-body">Separate portals for researchers and authorities with full activity tracking.</p></div>
  </div>
</section>

<!-- CTA -->
<div class="cta-section">
  <div class="cta-title">Ready to explore<br><em>Goa's risk?</em></div>
  <p class="cta-sub">Create a free researcher account or register authority credentials to access the admin panel.</p>
  <div class="cta-roles">
    <a href="{{ url_for('register') }}" class="cta-card cta-res">
      <div class="cta-icon">👤</div>
      <div class="cta-card-title">Researcher</div>
      <div class="cta-card-desc">Students &amp; academics</div>
      <div class="cta-btn cta-btn-res">Sign Up Free</div>
    </a>
    <a href="{{ url_for('login') }}" class="cta-card cta-res">
      <div class="cta-icon">🔑</div>
      <div class="cta-card-title">Researcher Login</div>
      <div class="cta-card-desc">Have an account?</div>
      <div class="cta-btn cta-btn-res">Sign In</div>
    </a>
    <a href="{{ url_for('authority_register') }}" class="cta-card cta-auth">
      <div class="cta-icon">🏛️</div>
      <div class="cta-card-title">Authority</div>
      <div class="cta-card-desc">Government bodies</div>
      <div class="cta-btn cta-btn-auth">Register</div>
    </a>
    <a href="{{ url_for('authority_login') }}" class="cta-card cta-auth">
      <div class="cta-icon">🔐</div>
      <div class="cta-card-title">Authority Login</div>
      <div class="cta-card-desc">Existing authority</div>
      <div class="cta-btn cta-btn-auth">Sign In</div>
    </a>
  </div>
</div>

<footer>
  <span>© 2024 — ML-Based Environmental Vulnerability Assessment for Goa</span>
  <span>Final Year Research Project</span>
</footer>

<script>
const nav=document.getElementById('nav');
window.addEventListener('scroll',()=>nav.classList.toggle('scrolled',window.scrollY>60));
const ro=new IntersectionObserver(e=>{e.forEach(x=>{if(x.isIntersecting){x.target.classList.add('visible');x.target.querySelectorAll('.frow-fill').forEach(b=>setTimeout(()=>b.style.width=b.dataset.w+'%',200));}});},{threshold:0.15});
document.querySelectorAll('[data-reveal],.feat,.stat-cell').forEach(el=>ro.observe(el));
const so=new IntersectionObserver(e=>{e.forEach(x=>{if(x.isIntersecting){x.target.classList.add('visible');const d=parseInt(x.target.dataset.delay||0);setTimeout(()=>{const id=x.target.querySelector('[id^="cnt"]');if(!id)return;const tg={cnt1:12,cnt2:5,cnt3:60}[id.id];let s=null;(function step(ts){if(!s)s=ts;const p=Math.min((ts-s)/1400,1);id.textContent=Math.round(p*tg);if(p<1)requestAnimationFrame(step);})(performance.now());},d);so.unobserve(x.target);}});},{threshold:0.3});
document.querySelectorAll('.stat-cell').forEach(el=>so.observe(el));
</script>
</body>
</html>"""
'''

# Find LANDING_HTML = """ ... """ and replace it
pattern = r'LANDING_HTML\s*=\s*""".*?"""'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("ERROR: Could not find LANDING_HTML in app.py")
    print("Make sure you're running this from the same folder as app.py")
    exit(1)

new_content = content[:match.start()] + NEW_LANDING.strip() + content[match.end():]

with open(src, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✓ LANDING_HTML replaced successfully!")
print("✓ SVG India map removed")
print("✓ goa.png background added")
print("")
print("Now:")
print("  1. Make sure goa.png is in  static/images/goa.png")
print("  2. Restart Flask:  python app.py")
print("  3. Hard refresh browser: Ctrl+Shift+R")
