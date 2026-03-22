
import re, shutil, os, sys

PROJECT = r"C:\Users\Utkarsha\Music\simple_model"
APP_PY  = os.path.join(PROJECT, "app.py")
GOA_PNG = os.path.join(PROJECT, "static", "images", "goa.png")

print("=" * 60)
print("FIXING app.py — Removing SVG, Adding goa.png background")
print("=" * 60)

# Check goa.png exists
if os.path.exists(GOA_PNG):
    print(f"✓ goa.png found at: {GOA_PNG}")
else:
    print(f"✗ goa.png MISSING at: {GOA_PNG}")
    print("  Copy your goa.png to that location first!")
    sys.exit(1)

# Check app.py exists
if not os.path.exists(APP_PY):
    print(f"✗ app.py not found at: {APP_PY}")
    sys.exit(1)

print(f"✓ app.py found")

# Read
with open(APP_PY, "r", encoding="utf-8") as f:
    code = f.read()

# Backup
backup = APP_PY.replace("app.py", "app_backup.py")
shutil.copy(APP_PY, backup)
print(f"✓ Backup saved: {backup}")

print("\nApplying fixes...")

# ── FIX 1: Replace the ENTIRE LANDING_HTML variable ─────────────────────────
NEW_LANDING = '''LANDING_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ML-Based Environmental Vulnerability Assessment for Goa</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --teal:#0d9488;--emerald:#059669;
  --ink:#0a1410;--mid:#3d5450;--soft:#7a8f8c;
  --paper:#f7faf9;--border:rgba(13,148,136,0.15);
}
html{scroll-behavior:smooth}
body{font-family:'DM Sans',sans-serif;background:var(--paper);color:var(--ink);overflow-x:hidden;}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:18px 56px;transition:all 0.4s;}
nav.scrolled{padding:12px 56px;background:rgba(247,250,249,0.97);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);box-shadow:0 4px 20px rgba(10,20,16,0.06);}
.nav-logo{display:flex;align-items:center;gap:11px;text-decoration:none;}
.nav-logo-mark{width:36px;height:36px;background:linear-gradient(135deg,var(--teal),var(--emerald));border-radius:9px;display:flex;align-items:center;justify-content:center;}
.nav-logo-mark img{width:28px;height:28px;object-fit:contain;border-radius:5px;}
.nav-brand{font-family:'DM Serif Display',serif;font-size:13px;color:var(--ink);max-width:230px;line-height:1.3;}
.nav-brand span{color:var(--teal);}
.nav-links{display:flex;gap:28px;}
.nav-links a{color:var(--mid);text-decoration:none;font-size:13px;font-weight:500;transition:color 0.2s;}
.nav-links a:hover{color:var(--teal);}
.nav-auth{display:flex;gap:10px;}
.nb1{padding:8px 17px;border:1.5px solid var(--border);border-radius:50px;font-size:13px;color:var(--mid);text-decoration:none;transition:all 0.2s;}
.nb1:hover{border-color:var(--teal);color:var(--teal);}
.nb2{padding:8px 18px;background:var(--ink);border-radius:50px;font-size:13px;color:#fff;text-decoration:none;transition:all 0.2s;}
.nb2:hover{background:var(--teal);}

/* ══ HERO — goa.png FULL BACKGROUND ══ */
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
  background:linear-gradient(105deg,
    rgba(237,250,247,1.0)  0%,
    rgba(237,250,247,0.97) 25%,
    rgba(237,250,247,0.80) 50%,
    rgba(237,250,247,0.20) 75%,
    transparent            100%
  );
  z-index:1;
}
.hero-body{
  position:relative;
  z-index:2;
  padding:140px 80px 80px;
  max-width:680px;
}
.badge{display:inline-flex;align-items:center;gap:8px;padding:6px 16px;background:rgba(13,148,136,0.10);border:1px solid rgba(13,148,136,0.22);border-radius:50px;margin-bottom:24px;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--teal);text-transform:uppercase;}
.badge-dot{width:5px;height:5px;border-radius:50%;background:var(--teal);animation:blink 1.8s infinite;}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}
h1.hero-title{font-family:'DM Serif Display',serif;font-size:clamp(34px,4.2vw,60px);line-height:1.08;letter-spacing:-1.5px;color:var(--ink);margin-bottom:20px;}
h1.hero-title em{font-style:italic;color:var(--teal);}
.hero-sub{font-size:16px;line-height:1.85;color:var(--mid);max-width:500px;margin-bottom:36px;}

/* Buttons */
.hero-btns{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:28px;}
.btn-a{display:inline-flex;align-items:center;gap:8px;padding:13px 26px;background:linear-gradient(135deg,var(--teal),var(--emerald));color:#fff;border-radius:50px;font-size:14px;font-weight:600;text-decoration:none;box-shadow:0 8px 22px rgba(13,148,136,0.28);transition:all 0.3s;}
.btn-a:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(13,148,136,0.38);}
.btn-b{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;background:#1e3a5f;color:#fff;border-radius:50px;font-size:14px;font-weight:600;text-decoration:none;box-shadow:0 8px 20px rgba(30,58,95,0.2);transition:all 0.3s;}
.btn-b:hover{transform:translateY(-2px);background:#152f50;}
.btn-c{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;color:var(--mid);border:1.5px solid rgba(61,84,80,0.2);border-radius:50px;font-size:14px;font-weight:500;text-decoration:none;background:rgba(255,255,255,0.75);backdrop-filter:blur(6px);transition:all 0.3s;}
.btn-c:hover{border-color:var(--teal);color:var(--teal);}

/* Access role cards */
.role-row{display:flex;gap:11px;flex-wrap:wrap;margin-bottom:36px;}
.rc{display:flex;align-items:center;gap:10px;padding:13px 16px;border-radius:15px;background:rgba(255,255,255,0.88);border:1.5px solid var(--border);text-decoration:none;min-width:150px;transition:all 0.3s;backdrop-filter:blur(10px);}
.rc:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(13,148,136,0.12);border-color:rgba(13,148,136,0.28);}
.rc.rc-admin{border-color:rgba(30,58,95,0.16);background:rgba(240,244,255,0.88);}
.rc.rc-admin:hover{box-shadow:0 10px 28px rgba(30,58,95,0.10);border-color:rgba(30,58,95,0.3);}
.rc-icon{font-size:19px;}
.rc-title{font-size:13px;font-weight:600;color:var(--ink);display:block;}
.rc-sub{font-family:'Space Mono',monospace;font-size:8px;letter-spacing:1.5px;text-transform:uppercase;color:var(--teal);}
.rc-admin .rc-sub{color:#1e3a5f;}

/* Stats */
.hero-stats{display:flex;gap:28px;padding-top:24px;border-top:1px solid var(--border);}
.hs-num{font-family:'DM Serif Display',serif;font-size:30px;color:var(--ink);letter-spacing:-1px;display:block;}
.hs-num span{color:var(--teal);}
.hs-lbl{font-family:'Space Mono',monospace;font-size:8px;letter-spacing:1.5px;text-transform:uppercase;color:var(--soft);}

/* TICKER */
.ticker-wrap{overflow:hidden;padding:12px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border);}
.ticker{display:flex;gap:16px;animation:tick 24s linear infinite;white-space:nowrap;}
@keyframes tick{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.tc{display:inline-flex;align-items:center;gap:6px;padding:6px 15px;border:1px solid var(--border);border-radius:50px;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--mid);text-transform:uppercase;background:rgba(255,255,255,0.6);flex-shrink:0;}
.tc::before{content:'';width:4px;height:4px;border-radius:50%;background:var(--teal);}

/* STATS ROW */
.stats-row{display:flex;border-top:1.5px solid var(--border);border-bottom:1.5px solid var(--border);}
.sc{flex:1;padding:40px 32px;border-right:1.5px solid var(--border);text-align:center;opacity:0;transform:translateY(16px);transition:opacity 0.6s,transform 0.6s;}
.sc:last-child{border-right:none;}
.sc.vis{opacity:1;transform:translateY(0);}
.sc-num{font-family:'DM Serif Display',serif;font-size:48px;color:var(--ink);letter-spacing:-2px;display:block;margin-bottom:5px;}
.sc-num span{color:var(--teal);}
.sc-lbl{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--soft);text-transform:uppercase;}

/* SECTIONS */
.section{padding:90px 80px;}
.section-tinted{background:linear-gradient(135deg,#edfaf7,#f5fffe);}
.si{max-width:1180px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;}
.si.rev{direction:rtl;}
.si.rev>*{direction:ltr;}
.stag{display:inline-block;padding:5px 13px;background:rgba(13,148,136,0.1);border:1px solid rgba(13,148,136,0.2);border-radius:50px;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--teal);text-transform:uppercase;margin-bottom:16px;}
.snum{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:3px;color:var(--soft);text-transform:uppercase;margin-bottom:12px;}
.stitle{font-family:'DM Serif Display',serif;font-size:clamp(28px,3.2vw,46px);line-height:1.1;letter-spacing:-1.5px;color:var(--ink);margin-bottom:14px;}
.stitle em{font-style:italic;color:var(--teal);}
.sbody{font-size:15px;line-height:1.85;color:var(--mid);}

.card{background:rgba(255,255,255,0.92);border:1.5px solid var(--border);border-radius:20px;padding:26px;box-shadow:0 14px 44px rgba(13,148,136,0.08);position:relative;overflow:hidden;}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--teal),var(--emerald));}
.card-lbl{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--soft);text-transform:uppercase;margin-bottom:16px;}
.frow{display:flex;align-items:center;gap:10px;margin-bottom:11px;}
.fl{font-family:'Space Mono',monospace;font-size:9px;color:var(--mid);width:100px;flex-shrink:0;text-transform:uppercase;}
.fb{flex:1;height:3px;background:rgba(13,148,136,0.1);border-radius:2px;overflow:hidden;}
.ff{height:100%;background:linear-gradient(90deg,var(--teal),var(--emerald));width:0;transition:width 1.2s cubic-bezier(0.16,1,0.3,1);}
.fv{font-family:'Space Mono',monospace;font-size:9px;color:var(--teal);width:32px;text-align:right;}
.mrow{display:flex;align-items:center;justify-content:space-between;padding:11px 0;border-bottom:1px solid var(--border);}
.mrow:last-child{border-bottom:none;}
.ml{display:flex;align-items:center;gap:10px;}
.mn{font-size:13px;font-weight:600;color:var(--ink);}
.mf{font-family:'Space Mono',monospace;font-size:9px;color:var(--soft);}
.ms{font-family:'Space Mono',monospace;font-size:9px;color:var(--teal);}
.cgrid{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
.ci{display:flex;align-items:center;gap:7px;padding:9px 11px;background:rgba(13,148,136,0.04);border:1px solid var(--border);border-radius:9px;}
.cd{width:5px;height:5px;border-radius:50%;background:var(--teal);}
.cn{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:1.5px;color:var(--mid);text-transform:uppercase;}

/* FEATURES */
.fg{display:grid;grid-template-columns:1fr 1fr;gap:18px;max-width:1180px;margin:0 auto;padding:0 80px 80px;}
.fi{padding:28px;border-radius:18px;background:rgba(255,255,255,0.85);border:1.5px solid var(--border);transition:all 0.3s;opacity:0;transform:translateY(18px);}
.fi.vis{opacity:1;transform:translateY(0);}
.fi:hover{transform:translateY(-4px);box-shadow:0 14px 44px rgba(13,148,136,0.11);}
.fi-icon{width:46px;height:46px;border-radius:12px;background:rgba(13,148,136,0.1);display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:14px;}
.fi-title{font-family:'DM Serif Display',serif;font-size:19px;color:var(--ink);margin-bottom:8px;}
.fi-body{font-size:14px;line-height:1.75;color:var(--mid);}

/* CTA */
.cta{padding:80px;text-align:center;background:linear-gradient(135deg,#edfaf7,var(--paper));border-top:1.5px solid var(--border);}
.cta-title{font-family:'DM Serif Display',serif;font-size:clamp(32px,4.5vw,58px);color:var(--ink);letter-spacing:-2px;margin-bottom:14px;line-height:1.06;}
.cta-title em{font-style:italic;color:var(--teal);}
.cta-sub{font-size:16px;color:var(--mid);line-height:1.8;max-width:440px;margin:0 auto 36px;}
.cta-cards{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;}
.cc{display:flex;flex-direction:column;align-items:center;gap:8px;padding:24px 20px;border-radius:18px;text-decoration:none;min-width:170px;position:relative;overflow:hidden;transition:all 0.3s;}
.cc::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;}
.cc-r{background:rgba(13,148,136,0.07);border:1.5px solid rgba(13,148,136,0.22);}
.cc-r::before{background:linear-gradient(90deg,var(--teal),var(--emerald));}
.cc-r:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(13,148,136,0.14);}
.cc-a{background:rgba(30,58,95,0.06);border:1.5px solid rgba(30,58,95,0.18);}
.cc-a::before{background:linear-gradient(90deg,#1e3a5f,#2563eb);}
.cc-a:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(30,58,95,0.11);}
.cc-icon{font-size:28px;}
.cc-title{font-family:'DM Serif Display',serif;font-size:16px;color:var(--ink);}
.cc-desc{font-family:'Space Mono',monospace;font-size:8px;letter-spacing:1.5px;text-transform:uppercase;color:var(--soft);text-align:center;}
.cc-btn{padding:6px 16px;border-radius:50px;font-size:11px;font-weight:600;color:#fff;margin-top:3px;}
.cb-r{background:linear-gradient(135deg,var(--teal),var(--emerald));}
.cb-a{background:linear-gradient(135deg,#1e3a5f,#2563eb);}

footer{padding:24px 80px;display:flex;align-items:center;justify-content:space-between;border-top:1px solid var(--border);font-family:'Space Mono',monospace;font-size:9px;letter-spacing:1.5px;color:var(--soft);text-transform:uppercase;}

@media(max-width:900px){
  .hero-body{padding:100px 24px 60px;max-width:100%;}
  .si{grid-template-columns:1fr;gap:32px;padding:0;}
  .section{padding:55px 24px;}
  .fg{grid-template-columns:1fr;padding:0 24px 55px;}
  .stats-row,.cta-cards{flex-direction:column;}
  .sc{border-right:none;border-bottom:1.5px solid var(--border);}
  nav{padding:13px 20px;}
  footer{flex-direction:column;gap:8px;text-align:center;padding:18px;}
  .cta{padding:55px 24px;}
}
</style>
</head>
<body>

<nav id="nav">
  <a class="nav-logo" href="/">
    <div class="nav-logo-mark">
      <img src="/static/images/logo.jpg" alt="EVA" onerror="this.parentElement.innerHTML='🌿'">
    </div>
    <div class="nav-brand">ML-Based Environmental<br><span>Vulnerability Assessment · Goa</span></div>
  </a>
  <div class="nav-links">
    <a href="#how">How It Works</a>
    <a href="#coverage">Areas</a>
    <a href="#models">Models</a>
  </div>
  <div class="nav-auth">
    <a href="{{ url_for('login') }}" class="nb1">Researcher Login</a>
    <a href="{{ url_for('authority_login') }}" class="nb2">Authority Login</a>
  </div>
</nav>

<!-- ═══════════ HERO — GOA.PNG FULL BACKGROUND, NO SVG ═══════════ -->
<section id="hero">
  <div class="hero-bg"></div>
  <div class="hero-overlay"></div>
  <div class="hero-body">
    <div class="badge"><div class="badge-dot"></div>Final Year Research Project</div>
    <h1 class="hero-title">
      Machine Learning Based<br>
      <em>Environmental Vulnerability</em><br>
      Assessment for Goa
    </h1>
    <p class="hero-sub">Landslide risk mapped across all 12 talukas of Goa using five computer models trained on satellite images — helping researchers and authorities understand where the land is most at risk.</p>

    <div class="hero-btns">
      <a href="{{ url_for('register') }}" class="btn-a">👤 Researcher Sign Up</a>
      <a href="{{ url_for('authority_register') }}" class="btn-b">🏛️ Authority Register</a>
      <a href="{{ url_for('login') }}" class="btn-c">Sign In</a>
    </div>

    <div class="role-row">
      <a href="{{ url_for('login') }}" class="rc">
        <span class="rc-icon">👤</span>
        <div><span class="rc-title">Researcher</span><span class="rc-sub">Login →</span></div>
      </a>
      <a href="{{ url_for('register') }}" class="rc">
        <span class="rc-icon">📝</span>
        <div><span class="rc-title">Register</span><span class="rc-sub">New Account →</span></div>
      </a>
      <a href="{{ url_for('authority_login') }}" class="rc rc-admin">
        <span class="rc-icon">🏛️</span>
        <div><span class="rc-title">Authority</span><span class="rc-sub">Login →</span></div>
      </a>
      <a href="{{ url_for('authority_register') }}" class="rc rc-admin">
        <span class="rc-icon">🔐</span>
        <div><span class="rc-title">Auth. Register</span><span class="rc-sub">Apply →</span></div>
      </a>
    </div>

    <div class="hero-stats">
      <div><span class="hs-num">12</span><span class="hs-lbl">Talukas</span></div>
      <div><span class="hs-num">5</span><span class="hs-lbl">Models</span></div>
      <div><span class="hs-num">60<span>+</span></span><span class="hs-lbl">Risk Maps</span></div>
    </div>
  </div>
</section>
<!-- ═══════════════════════════════════════════════════════════════ -->

<div class="ticker-wrap">
  <div class="ticker">
    {% for t in taluks %}<div class="tc">{{ t }}</div>{% endfor %}
    {% for t in taluks %}<div class="tc">{{ t }}</div>{% endfor %}
    {% for t in taluks %}<div class="tc">{{ t }}</div>{% endfor %}
  </div>
</div>

<div class="stats-row">
  <div class="sc" data-delay="0"><span class="sc-num" id="cnt1">0</span><div class="sc-lbl">Areas fully mapped</div></div>
  <div class="sc" data-delay="100"><span class="sc-num" id="cnt2">0</span><div class="sc-lbl">Models deployed</div></div>
  <div class="sc" data-delay="200"><span class="sc-num"><span id="cnt3">0</span><span style="color:var(--teal)">+</span></span><div class="sc-lbl">Risk maps available</div></div>
  <div class="sc" data-delay="300"><span class="sc-num" style="font-size:36px">Goa</span><div class="sc-lbl">Complete state coverage</div></div>
</div>

<section class="section" id="how">
  <div class="si">
    <div data-reveal>
      <div class="snum">01 / 04</div>
      <div class="stag">How It Works</div>
      <h2 class="stitle">Goa's landslide risk,<br>mapped <em>area by area</em></h2>
      <p class="sbody">Satellite images of Goa were used to train models to recognise high-risk terrain. Key factors include vegetation, water presence, soil moisture, land use, and historical landslide data.</p>
    </div>
    <div data-reveal>
      <div class="card">
        <div class="card-lbl">Risk Factors Studied</div>
        <div class="frow"><span class="fl">Vegetation</span><div class="fb"><div class="ff" data-w="82"></div></div><span class="fv">82%</span></div>
        <div class="frow"><span class="fl">Water Cover</span><div class="fb"><div class="ff" data-w="70"></div></div><span class="fv">70%</span></div>
        <div class="frow"><span class="fl">Soil Moisture</span><div class="fb"><div class="ff" data-w="65"></div></div><span class="fv">65%</span></div>
        <div class="frow"><span class="fl">Land Use</span><div class="fb"><div class="ff" data-w="75"></div></div><span class="fv">75%</span></div>
        <div class="frow"><span class="fl">Slide History</span><div class="fb"><div class="ff" data-w="88"></div></div><span class="fv">88%</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section-tinted" id="models">
  <div class="si rev">
    <div data-reveal>
      <div class="snum">02 / 04</div>
      <div class="stag">Models</div>
      <h2 class="stitle">Five models,<br><em>one clear answer</em></h2>
      <p class="sbody">CNN, Random Forest, SVM, K-Nearest Neighbours, and Logistic Regression each analyse the same satellite data differently. Agreement across models means high confidence.</p>
    </div>
    <div data-reveal>
      <div class="card">
        <div class="card-lbl">Available Models</div>
        {% for m, name in model_names.items() %}
        <div class="mrow">
          <div class="ml">
            <span style="font-size:16px">{{ icons[m] }}</span>
            <div><div class="mn">{{ m }}</div><div class="mf">{{ name.split('—')[1].strip() if '—' in name else name }}</div></div>
          </div>
          <span class="ms">● Active</span>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="section" id="coverage">
  <div class="si">
    <div data-reveal>
      <div class="snum">03 / 04</div>
      <div class="stag">Coverage</div>
      <h2 class="stitle">All 12 talukas,<br><em>fully covered</em></h2>
      <p class="sbody">From Pernem in the north to Canacona in the south — every area of Goa has a complete risk assessment based on actual satellite data.</p>
    </div>
    <div data-reveal>
      <div class="card">
        <div class="card-lbl">Talukas — Goa State</div>
        <div class="cgrid">
          {% for t in taluks %}
          <div class="ci"><div class="cd"></div><span class="cn">{{ t }}</span></div>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</section>

<section style="padding:55px 0 0">
  <div style="text-align:center;padding:0 80px 40px;max-width:560px;margin:0 auto">
    <div class="stag">04 / 04 — Platform</div>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(28px,3.8vw,46px);color:var(--ink);letter-spacing:-1.5px;margin-top:14px;line-height:1.1">Built for <em style="color:var(--teal);font-style:italic">researchers</em></h2>
  </div>
  <div class="fg">
    <div class="fi" data-reveal><div class="fi-icon">🗺️</div><div class="fi-title">Visual Risk Maps</div><p class="fi-body">Colour maps from deep green (safe) to dark red (very high risk) for every part of Goa.</p></div>
    <div class="fi" data-reveal><div class="fi-icon">🔬</div><div class="fi-title">5 Trained Models</div><p class="fi-body">Compare results across five models — agreement means high confidence in the risk reading.</p></div>
    <div class="fi" data-reveal><div class="fi-icon">📊</div><div class="fi-title">Risk Breakdown</div><p class="fi-body">See percentages for Low, Moderate, High, and Very High risk zones per taluka.</p></div>
    <div class="fi" data-reveal><div class="fi-icon">🔐</div><div class="fi-title">Secure Access</div><p class="fi-body">Separate portals for researchers and authorities with full activity tracking.</p></div>
  </div>
</section>

<div class="cta">
  <div class="cta-title">Ready to explore<br><em>Goa's risk?</em></div>
  <p class="cta-sub">Create a free researcher account or register authority credentials to access the admin panel.</p>
  <div class="cta-cards">
    <a href="{{ url_for('register') }}" class="cc cc-r">
      <div class="cc-icon">👤</div><div class="cc-title">Researcher</div>
      <div class="cc-desc">Students &amp; academics</div>
      <div class="cc-btn cb-r">Sign Up Free</div>
    </a>
    <a href="{{ url_for('login') }}" class="cc cc-r">
      <div class="cc-icon">🔑</div><div class="cc-title">Researcher Login</div>
      <div class="cc-desc">Have an account?</div>
      <div class="cc-btn cb-r">Sign In</div>
    </a>
    <a href="{{ url_for('authority_register') }}" class="cc cc-a">
      <div class="cc-icon">🏛️</div><div class="cc-title">Authority</div>
      <div class="cc-desc">Government bodies</div>
      <div class="cc-btn cb-a">Register</div>
    </a>
    <a href="{{ url_for('authority_login') }}" class="cc cc-a">
      <div class="cc-icon">🔐</div><div class="cc-title">Authority Login</div>
      <div class="cc-desc">Existing authority</div>
      <div class="cc-btn cb-a">Sign In</div>
    </a>
  </div>
</div>

<footer>
  <span>© 2024 — ML-Based Environmental Vulnerability Assessment for Goa</span>
  <span>Final Year Research Project</span>
</footer>

<script>
const nav=document.getElementById('nav');
window.addEventListener('scroll',()=>nav.classList.toggle('scrolled',window.scrollY>50));
const ro=new IntersectionObserver(e=>{e.forEach(x=>{if(x.isIntersecting){x.target.classList.add('vis');x.target.querySelectorAll('.ff').forEach(b=>setTimeout(()=>b.style.width=b.dataset.w+'%',180));}});},{threshold:0.14});
document.querySelectorAll('[data-reveal],.fi,.sc').forEach(el=>ro.observe(el));
const so=new IntersectionObserver(e=>{e.forEach(x=>{if(x.isIntersecting){x.target.classList.add('vis');const d=+(x.target.dataset.delay||0);setTimeout(()=>{const el=x.target.querySelector('[id^=cnt]');if(!el)return;const t={cnt1:12,cnt2:5,cnt3:60}[el.id];let s=null;(function r(ts){if(!s)s=ts;const p=Math.min((ts-s)/1300,1);el.textContent=Math.round(p*t);if(p<1)requestAnimationFrame(r);})(performance.now());},d);so.unobserve(x.target);}});},{threshold:0.3});
document.querySelectorAll('.sc').forEach(el=>so.observe(el));
</script>
</body>
</html>"""
'''

# Find and replace LANDING_HTML
match = re.search(r'LANDING_HTML\s*=\s*""".*?"""', code, re.DOTALL)
if match:
    code = code[:match.start()] + NEW_LANDING.strip() + '\n' + code[match.end():]
    print("  ✓ LANDING_HTML completely replaced")
else:
    print("  ✗ Could not find LANDING_HTML — trying alternate replacement...")
    # Try with single quotes or different formatting
    match2 = re.search(r"LANDING_HTML\s*=\s*'''.*?'''", code, re.DOTALL)
    if match2:
        code = code[:match2.start()] + NEW_LANDING.strip() + '\n' + code[match2.end():]
        print("  ✓ LANDING_HTML replaced (single quote variant)")
    else:
        print("  ✗ STILL could not find LANDING_HTML")
        print("    Your app.py may be structured differently.")
        sys.exit(1)

# Write
with open(APP_PY, "w", encoding="utf-8") as f:
    f.write(code)

print("\n" + "=" * 60)
print("  SUCCESS! goa.png background is now live.")
print("=" * 60)
print(f"\n  goa.png path : {GOA_PNG}")
print(f"  File exists  : {os.path.exists(GOA_PNG)}")
print("\nNow:")
print("  1.  Ctrl+C  to stop Flask")
print("  2.  python app.py")
print("  3.  Ctrl+Shift+R in browser")