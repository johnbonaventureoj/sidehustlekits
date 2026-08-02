# -*- coding: utf-8 -*-
"""
SideHustleKits SEO site generator.
Static, Google-indexable HTML for GitHub Pages.
Run:  py build_site.py
Emits: index.html, products/*.html, blog/*.html, sitemap.xml, robots.txt, style.css, assets/*
No external libraries (stdlib only). Reuses cover.png from the product folders.
"""
import os, shutil, html, datetime, re

ROOT = os.path.dirname(os.path.abspath(__file__))
EPROOT = r"C:\Users\johnb\OneDrive\Desktop\E-Products"
DESKTOP = r"C:\Users\johnb\OneDrive\Desktop"
BRAND_LOGO = os.path.join(EPROOT, "_brand", "logo.png")

# Change this ONE line if a custom domain is added later (e.g. https://sidehustlekits.com)
BASE = "https://johnbonaventureoj.github.io/sidehustlekits"
TODAY = "2026-08-02"   # Date.now() is unavailable in some sandboxes; keep explicit for stable sitemap lastmod

BRAND = dict(navy="#17213A", amber="#F5A623", teal="#0E9C86", ink="#1f2733", paper="#FBFAF7")

# ---------------------------------------------------------------- PRODUCTS
# img = absolute path to a cover.png to copy into /assets/products/<slug>.png
PRODUCTS = [
    dict(
        slug="2026-digital-planner",
        name="2026 Digital Planner",
        cat="Planners",
        price="12",
        tagline="A fully hyperlinked, undated digital planner for iPad, GoodNotes & print.",
        keywords=["digital planner 2026","goodnotes planner","hyperlinked planner","ipad planner","undated planner","printable planner"],
        img=os.path.join(EPROOT,"01_Digital_Planner_2026","cover.png"),
        gumroad="https://bonaventure5.gumroad.com/l/wgeonh",
        etsy="https://www.etsy.com/listing/4548076729",
        lede="Take back control of your year with a beautifully simple, fully hyperlinked 2026 digital planner. Tap once to jump anywhere — no endless scrolling. Built for GoodNotes, Notability and Samsung Notes on any tablet, and it prints perfectly too.",
        inside=[
            "Home dashboard that links to everything",
            "2026 year-at-a-glance with tappable months",
            "12 monthly calendars (real dates, Monday-start)",
            "52 undated weekly spreads",
            "Daily planning template",
            "Yearly goals + word of the year",
            "Habit, finance and gratitude trackers",
            "Notes and brain-dump pages",
        ],
        format="Instant download · 1 hyperlinked PDF (75 pages) · works on any tablet or printed",
        faqs=[
            ("Does it work with GoodNotes and Notability?","Yes. Import the PDF into GoodNotes, Notability, Samsung Notes or any notes app that opens PDFs. Every link stays tappable."),
            ("Is it dated or undated?","Undated and reusable — start any month and use it every year. The 2026 monthly calendars use real Monday-start dates."),
            ("Can I print it?","Yes, the pages print cleanly on A4 or Letter."),
        ],
    ),
    dict(
        slug="adhd-life-admin-planner",
        name="ADHD Life-Admin Planner",
        cat="Planners",
        price="15",
        tagline="A forgiving, undated planner that works WITH an ADHD brain — beat overwhelm and actually finish.",
        keywords=["adhd planner","adhd digital planner","neurodivergent planner","brain dump planner","focus planner","executive function planner"],
        img=os.path.join(EPROOT,"02_ADHD_Life_Admin_Planner","cover.png"),
        gumroad="https://bonaventure5.gumroad.com/l/yxamqg",
        etsy="https://www.etsy.com/listing/4548077665",
        lede="A planner that finally works with your ADHD brain, not against it. No broken streaks, no guilt — just simple, forgiving templates to beat overwhelm, start the hard thing, and actually finish. Undated and reusable: print or duplicate any page as often as you like.",
        inside=[
            "\u201cThe ONE Thing\u201d daily page to beat decision paralysis",
            "Brain Dump to empty your loud head onto the page",
            "Task Triage — turn the pile into now / soon / someday / drop",
            "Overwhelmed? A 4-step flow to the next tiny step",
            "Weekly Reset, Routine Anchors and a forgiving Habit Tracker",
            "Dopamine Menu, Focus & body-doubling Log, and a Win List",
            "Monthly Focus and Notes pages",
        ],
        format="Instant download · 1 hyperlinked PDF · use on any tablet in GoodNotes/Notability or print · undated, reuse forever",
        faqs=[
            ("How is this different from a normal planner?","It's designed around executive-function challenges: fewer boxes, no guilt-inducing streaks, a single daily priority, and gentle flows for when you're overwhelmed."),
            ("Is it undated?","Yes — reuse any page as many times as you like."),
            ("Digital or printable?","Both. Use it on a tablet or print the pages you like."),
        ],
    ),
    dict(
        slug="budget-savings-tracker",
        name="Budget & Savings Tracker 2026",
        cat="Finance",
        price="12",
        tagline="One simple spreadsheet that tracks budget, spending, savings, debt & net worth — automatically.",
        keywords=["budget spreadsheet","excel budget template","google sheets budget","savings tracker","debt payoff tracker","net worth tracker"],
        img=os.path.join(EPROOT,"03_Budget_Savings_Tracker","cover.png"),
        gumroad="https://bonaventure5.gumroad.com/l/rpppwy",
        etsy="https://www.etsy.com/listing/4548078279",
        lede="Take control of your money with one simple, powerful spreadsheet. Everything updates automatically — no formulas to build, no accounting knowledge needed. Works in Microsoft Excel, Google Sheets (free), Apple Numbers and LibreOffice.",
        inside=[
            "Dashboard — income, spending, savings rate, net worth and a spending chart, all automatic",
            "Monthly Budget — set a plan; \u201cactual\u201d pulls live from your transactions",
            "Transactions — log spending with a category drop-down",
            "Bills — never miss a payment",
            "Savings Goals — visual progress bars",
            "Debt Payoff — see totals and a plan to clear them",
            "Net Worth — watch it grow month to month",
        ],
        format="Instant download · 1 Excel .xlsx (8 connected tabs) · opens in Excel or Google Sheets",
        faqs=[
            ("Does it work in Google Sheets?","Yes — upload the .xlsx to Google Sheets (File > Import) and the formulas carry over. It also works in Excel, Apple Numbers and LibreOffice."),
            ("Do I need to know spreadsheets?","No. Everything is pre-built — just type in your numbers and the dashboard updates itself."),
        ],
    ),
    dict(
        slug="ai-prompt-vault",
        name="The AI Prompt Vault",
        cat="AI & Productivity",
        price="14",
        tagline="150 copy-paste prompts to get better results from ChatGPT, Claude & Gemini instantly.",
        keywords=["chatgpt prompts","ai prompts pack","prompt library","claude prompts","gemini prompts","productivity prompts"],
        img=os.path.join(EPROOT,"04_AI_Prompt_Vault","cover.png"),
        gumroad="https://bonaventure5.gumroad.com/l/rvpjh",
        etsy="https://www.etsy.com/listing/4548093136",
        lede="Get better results from ChatGPT, Claude and Gemini instantly — no prompt-writing skills needed. Just find what you need, copy, paste, and fill in the blanks.",
        inside=[
            "Getting started — make the AI understand YOU",
            "Email & messages, Money & budgeting, Work & career",
            "Small business & side hustles, Social media & content",
            "Writing & editing, Learning anything faster, Planning & productivity",
            "Home & life admin, Health & fitness, Relationships",
            "Travel, Decisions & problem-solving, Creativity & ideas",
            "Plus the framing tricks that make every other prompt work better",
        ],
        format="Instant download · 1 PDF · 150 prompts across 15 everyday areas · works with any AI chat, free or paid",
        faqs=[
            ("Which AI tools does it work with?","Any chat AI — ChatGPT, Claude, Gemini, Copilot and more, free or paid."),
            ("How many prompts are there?","150 genuinely useful prompts across 15 everyday categories — honestly counted, not padded."),
        ],
    ),
    dict(
        slug="social-media-management-kit",
        name="Client-Ready: Social Media Management Business Kit",
        cat="Business Kits",
        price="49",
        tagline="Everything you need to start and run a paid social-media-management side business.",
        keywords=["social media management business","smm side hustle","freelance social media kit","client onboarding templates","social media proposal template"],
        img=os.path.join(DESKTOP,"SMM Business Kit","cover.png"),
        gumroad="https://bonaventure5.gumroad.com/l/rglfkt",
        etsy="https://www.etsy.com/listing/4547643957",
        lede="Start a paid social-media-management business from zero. A complete, done-for-you toolkit: the playbook to land your first clients, every template and script you'll send them, an AI prompt library to do the work in minutes, and a rate calculator + client tracker.",
        inside=[
            "The Playbook — start → first client → scale",
            "Templates & Scripts — outreach, discovery, proposal, agreement, onboarding, report, invoice, offboarding",
            "AI Prompt Library — 40+ prompts to do client work fast",
            "Rate Calculator & Client Tracker (Excel CRM)",
            "Read-me-first quick start",
        ],
        format="Instant download · ZIP (3 PDFs + Excel tracker) · everything you need to get your first paying client",
        faqs=[
            ("Do I need experience?","No. The playbook takes you from zero to your first client, with every message and document written for you."),
            ("What do I actually sell to clients?","Social media management — content, scheduling and reporting. The kit includes the AI prompts and templates to deliver it efficiently."),
        ],
    ),
    dict(
        slug="shop-social-os",
        name="Shop Social OS — Starter Pack",
        cat="Business Kits",
        price="9",
        tagline="50+ copy-paste AI prompts to run a small shop's social media.",
        keywords=["social media prompts","small business social media","ai prompts for shops","content prompts","instagram caption prompts"],
        img=os.path.join(DESKTOP,"Shop Social OS","cover.png"),
        gumroad="https://bonaventure5.gumroad.com/l/vgwajk",
        etsy="",
        lede="Run your shop's social media in a fraction of the time. 50+ copy-paste AI prompts — set up a \u201cbrand brain\u201d once, then generate content ideas, reels hooks, captions, launches, offers, DMs and more on demand.",
        inside=[
            "Brand-Brain setup prompt (do this once)",
            "Content ideas & reels/hooks",
            "Captions, launches and offers",
            "Ads, DMs & comment replies",
            "Email, hashtags/SEO and growth",
            "7-Day Kickstart plan",
        ],
        format="Instant download · 1 PDF (7 pages) · 50+ prompts · works with any AI chat",
        faqs=[
            ("Is this for any shop?","Yes — it's written for small shops and product businesses, online or local."),
            ("Do I need paid AI?","No, the prompts work in free ChatGPT, Claude or Gemini."),
        ],
    ),
]

# ---------------------------------------------------------------- BLOG (SEO content that ranks + funnels)
BLOG = [
    dict(
        slug="best-digital-planner-2026",
        title="The Best Digital Planner for 2026 (Hyperlinked, Undated & Print-Ready)",
        desc="How to choose a digital planner for 2026 that actually gets used — what hyperlinking, undated pages and GoodNotes support really mean, and a simple pick.",
        keyword="best digital planner 2026",
        product="2026-digital-planner",
        body=[
            ("h2","What makes a digital planner worth using?"),
            ("p","Most planners get abandoned by February. The three things that keep a digital planner in daily use are simple: it must be <strong>hyperlinked</strong> (one tap to any page), <strong>undated</strong> (so a bad week doesn't waste printed dates), and it must <strong>work in the app you already use</strong> — usually GoodNotes, Notability or Samsung Notes."),
            ("h2","Hyperlinked vs. scrolling"),
            ("p","A hyperlinked planner turns your tablet into a real planner: tap a month, tap a week, tap \u201chome\u201d to get back. Without links you're endlessly scrolling, and that friction is exactly why planners get dropped."),
            ("h2","Undated is the secret to actually finishing the year"),
            ("p","Undated weekly and daily pages mean you start any time and reuse the planner every year. You never feel behind, and you never waste pages."),
            ("h2","Our pick for 2026"),
            ("p","Our <a href=\"../products/2026-digital-planner.html\">2026 Digital Planner</a> is fully hyperlinked (776 links across 75 pages), undated where it matters, and imports straight into GoodNotes, Notability or Samsung Notes — and it prints cleanly too. It's a one-time \u00a312 instant download."),
        ],
    ),
    dict(
        slug="adhd-planner-that-actually-works",
        title="The ADHD Planner That Actually Works (No Guilt, No Broken Streaks)",
        desc="Why most planners fail ADHD brains, and the small design changes — one daily priority, brain dumps, task triage — that make a planner you'll actually keep using.",
        keyword="adhd planner that works",
        product="adhd-life-admin-planner",
        body=[
            ("h2","Why normal planners fail ADHD brains"),
            ("p","Standard planners assume you'll fill every box, keep every streak and remember to open them. For an ADHD brain that's a recipe for guilt and abandonment. The fix isn't more discipline — it's a planner designed around how the brain actually works."),
            ("h2","One priority beats a long to-do list"),
            ("p","Decision paralysis is real. A single \u201cThe ONE Thing\u201d each day removes the overwhelm of choosing and gives you a clear win to aim for."),
            ("h2","Brain dump, then triage"),
            ("p","Getting the loud, swirling thoughts out of your head and onto the page is half the battle. A quick <strong>Brain Dump</strong> followed by <strong>Task Triage</strong> (now / soon / someday / drop) turns chaos into a short, doable list."),
            ("h2","Forgiving by design"),
            ("p","Our <a href=\"../products/adhd-life-admin-planner.html\">ADHD Life-Admin Planner</a> is undated and guilt-free: no streaks to break, a dopamine menu, a focus log for body-doubling, and a Win List so progress is visible. It's a \u00a315 instant download you can use on any tablet or print."),
        ],
    ),
    dict(
        slug="how-to-build-a-budget-in-10-minutes",
        title="How to Build a Budget in 10 Minutes (Free Spreadsheet Method)",
        desc="A dead-simple way to build a monthly budget fast — the three numbers that matter, and how to make it update itself so you only do the work once.",
        keyword="how to build a budget spreadsheet",
        product="budget-savings-tracker",
        body=[
            ("h2","The only three numbers that matter"),
            ("p","Forget 40 categories. Start with three: <strong>money in</strong>, <strong>fixed bills</strong>, and <strong>everything else</strong>. Once those balance, you can add detail. Most people over-complicate budgeting and quit in week one."),
            ("h2","Make it update itself"),
            ("p","The reason budgets fail is manual maths. Use a spreadsheet where you log spending once and the dashboard — savings rate, remaining budget, net worth — recalculates automatically. You do the typing; the sheet does the sums."),
            ("h2","Excel or Google Sheets — either works"),
            ("p","You don't need paid software. Google Sheets is free, and a good template's formulas carry over when you import an .xlsx."),
            ("h2","Skip the setup"),
            ("p","Our <a href=\"../products/budget-savings-tracker.html\">Budget & Savings Tracker</a> is 8 connected tabs with the dashboard, bills, savings goals, debt payoff and net worth already built. Open it, type your numbers, done — a \u00a312 instant download for Excel or Google Sheets."),
        ],
    ),
    dict(
        slug="best-chatgpt-prompts-everyday-life",
        title="The Best ChatGPT Prompts for Everyday Life (Copy & Paste)",
        desc="The prompt-writing trick that makes ChatGPT, Claude and Gemini far more useful, plus copy-paste examples for email, money, work and admin.",
        keyword="best chatgpt prompts",
        product="ai-prompt-vault",
        body=[
            ("h2","The one trick behind every good prompt"),
            ("p","Give the AI a <strong>role</strong>, <strong>context</strong> and a <strong>format</strong>. \u201cWrite an email\u201d is weak; \u201cYou're my assistant. Reply to this landlord politely declining the rent rise, keep it under 120 words, friendly but firm\u201d gets a usable answer first time."),
            ("h2","Make it understand YOU first"),
            ("p","Before anything else, paste a short \u201cabout me\u201d so every later answer is tailored — your job, your tone, what you're trying to do. This single step transforms the quality of everything after it."),
            ("h2","Everyday examples"),
            ("p","Copy-paste prompts save the most time on the boring stuff: chasing an invoice, drafting a tricky message, planning a week, summarising a long document, or turning a rough idea into a plan."),
            ("h2","Skip the guesswork"),
            ("p","Our <a href=\"../products/ai-prompt-vault.html\">AI Prompt Vault</a> is 150 tested, copy-paste prompts across 15 everyday areas — email, money, work, admin, content and more — for \u00a314. Works with any AI chat, free or paid."),
        ],
    ),
]

# ---------------------------------------------------------------- HELPERS
def esc(s): return html.escape(str(s), quote=True)

def money(p): return f"\u00a3{p}"

def rel(depth):
    """prefix to reach site root from a page at given depth"""
    return "../"*depth if depth else "./"

def page_shell(title, desc, canonical, body, depth=0, og_image=None, extra_head=""):
    r = rel(depth)
    og = og_image or f"{BASE}/assets/logo.png"
    nav = f"""
<header class="site">
  <a class="brand" href="{r}index.html"><img src="{r}assets/logo.png" alt="SideHustleKits" width="34" height="34"><span>SideHustleKits</span></a>
  <nav>
    <a href="{r}index.html#products">Products</a>
    <a href="{r}index.html#blog">Guides</a>
    <a href="{r}index.html#about">About</a>
  </nav>
</header>"""
    foot = f"""
<footer class="site">
  <div class="wrap">
    <p><strong>SideHustleKits</strong> — time-saving digital kits for work &amp; life. Instant download, no subscription.</p>
    <p class="muted">Also on <a href="https://www.etsy.com/shop/SideHustleKitsUK" rel="nofollow">Etsy</a> &amp; <a href="https://bonaventure5.gumroad.com" rel="nofollow">Gumroad</a>. &copy; 2026 SideHustleKits. All products are digital; nothing is shipped.</p>
  </div>
</footer>"""
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow">
<link rel="icon" href="{r}assets/logo.png">
<link rel="stylesheet" href="{r}style.css">
{extra_head}
</head>
<body>
{nav}
<main>
{body}
</main>
{foot}
</body>
</html>"""

def jsonld(obj_dict_str):
    return f'<script type="application/ld+json">{obj_dict_str}</script>'

import json
def product_jsonld(p, url):
    d = {
        "@context":"https://schema.org","@type":"Product",
        "name":p["name"],"description":p["lede"],
        "image":f"{BASE}/assets/products/{p['slug']}.png",
        "brand":{"@type":"Brand","name":"SideHustleKits"},
        "category":p["cat"],
        "offers":{"@type":"Offer","url":url,"priceCurrency":"GBP","price":p["price"],
                  "availability":"https://schema.org/InStock",
                  "itemCondition":"https://schema.org/NewCondition"},
    }
    return json.dumps(d, ensure_ascii=False)

def faq_jsonld(faqs):
    d = {"@context":"https://schema.org","@type":"FAQPage",
         "mainEntity":[{"@type":"Question","name":q,
                        "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
    return json.dumps(d, ensure_ascii=False)

def breadcrumb_jsonld(items):
    d={"@context":"https://schema.org","@type":"BreadcrumbList",
       "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u}
                          for i,(n,u) in enumerate(items)]}
    return json.dumps(d, ensure_ascii=False)

# ---------------------------------------------------------------- BUILD
def build():
    # dirs
    for d in ["products","blog","assets","assets/products"]:
        os.makedirs(os.path.join(ROOT,d), exist_ok=True)
    # logo
    if os.path.exists(BRAND_LOGO):
        shutil.copy(BRAND_LOGO, os.path.join(ROOT,"assets","logo.png"))
    # covers
    for p in PRODUCTS:
        if p.get("img") and os.path.exists(p["img"]):
            shutil.copy(p["img"], os.path.join(ROOT,"assets","products",p["slug"]+".png"))

    urls = []  # (loc, lastmod, priority)

    # ---- index
    cards = ""
    for p in PRODUCTS:
        cards += f"""
      <a class="card" href="products/{p['slug']}.html">
        <div class="thumb"><img src="assets/products/{p['slug']}.png" alt="{esc(p['name'])}" loading="lazy"></div>
        <div class="cbody">
          <span class="cat">{esc(p['cat'])}</span>
          <h3>{esc(p['name'])}</h3>
          <p>{esc(p['tagline'])}</p>
          <div class="crow"><span class="price">{money(p['price'])}</span><span class="go">View &rarr;</span></div>
        </div>
      </a>"""
    blogcards = ""
    for b in BLOG:
        blogcards += f'<li><a href="blog/{b["slug"]}.html">{esc(b["title"])}</a><span>{esc(b["desc"])}</span></li>'

    org = json.dumps({
        "@context":"https://schema.org","@type":"Organization","name":"SideHustleKits",
        "url":BASE,"logo":f"{BASE}/assets/logo.png",
        "description":"Time-saving digital kits, planners and templates for work and life.",
        "sameAs":["https://www.etsy.com/shop/SideHustleKitsUK","https://bonaventure5.gumroad.com","https://www.instagram.com/sidehustlekits.uk"]
    }, ensure_ascii=False)
    website = json.dumps({
        "@context":"https://schema.org","@type":"WebSite","name":"SideHustleKits","url":BASE
    }, ensure_ascii=False)

    body = f"""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Instant digital downloads · no subscription</p>
    <h1>Time-saving digital kits for work &amp; life</h1>
    <p class="sub">Planners, trackers, templates and AI prompt packs that save you hours — professionally designed, delivered instantly, yours forever.</p>
    <div class="hctas"><a class="btn primary" href="#products">Browse products</a><a class="btn ghost" href="#blog">Read the guides</a></div>
  </div>
</section>

<section id="products" class="section">
  <div class="wrap">
    <h2>Digital products</h2>
    <p class="lead">Each kit is a one-time purchase, downloaded instantly. Buy on Gumroad or Etsy.</p>
    <div class="grid">{cards}
    </div>
  </div>
</section>

<section id="blog" class="section alt">
  <div class="wrap">
    <h2>Guides &amp; tips</h2>
    <p class="lead">Practical, no-fluff guides — and the tools to act on them.</p>
    <ul class="bloglist">{blogcards}</ul>
  </div>
</section>

<section id="about" class="section">
  <div class="wrap narrow">
    <h2>About SideHustleKits</h2>
    <p>SideHustleKits makes practical digital products that give you time back: planners that actually get used, trackers that do the maths for you, and templates that skip the blank page. Everything is an instant download — no waiting, no shipping, no subscription. Buy once, keep it forever.</p>
  </div>
</section>
{jsonld(org)}
{jsonld(website)}
"""
    idx = page_shell(
        "SideHustleKits — Digital Planners, Trackers & Templates (Instant Download)",
        "Time-saving digital kits for work & life: hyperlinked planners, budget & savings trackers, AI prompt packs and business kits. Instant download, no subscription.",
        f"{BASE}/index.html", body, depth=0)
    open(os.path.join(ROOT,"index.html"),"w",encoding="utf-8").write(idx)
    urls.append((f"{BASE}/", TODAY, "1.0"))

    # ---- product pages
    for p in PRODUCTS:
        url = f"{BASE}/products/{p['slug']}.html"
        inside = "".join(f"<li>{x}</li>" for x in p["inside"])
        faqs_html = "".join(
            f'<details class="faq"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
            for q,a in p["faqs"])
        buy_etsy = f'<a class="btn ghost" href="{p["etsy"]}" rel="nofollow">Buy on Etsy</a>' if p["etsy"] else ""
        kw = ", ".join(p["keywords"])
        crumbs = breadcrumb_jsonld([("Home",f"{BASE}/"),("Products",f"{BASE}/index.html#products"),(p["name"],url)])
        head = (jsonld(product_jsonld(p,url)) + jsonld(faq_jsonld(p["faqs"])) + jsonld(crumbs)
                + f'\n<meta name="keywords" content="{esc(kw)}">')
        pbody = f"""
<article class="product">
  <div class="wrap">
    <nav class="crumbs"><a href="../index.html">Home</a> / <a href="../index.html#products">Products</a> / <span>{esc(p['name'])}</span></nav>
    <div class="pgrid">
      <div class="pimg"><img src="../assets/products/{p['slug']}.png" alt="{esc(p['name'])}"></div>
      <div class="pinfo">
        <span class="cat">{esc(p['cat'])}</span>
        <h1>{esc(p['name'])}</h1>
        <p class="tag">{esc(p['tagline'])}</p>
        <div class="pprice">{money(p['price'])} <span>· instant download</span></div>
        <div class="pctas"><a class="btn primary" href="{p['gumroad']}" rel="nofollow">Buy on Gumroad</a>{buy_etsy}</div>
        <p class="fmt">{esc(p['format'])}</p>
      </div>
    </div>
    <div class="pbody narrow">
      <p class="lede">{esc(p['lede'])}</p>
      <h2>What's inside</h2>
      <ul class="inside">{inside}</ul>
      <h2>Frequently asked questions</h2>
      {faqs_html}
      <div class="endcta"><a class="btn primary" href="{p['gumroad']}" rel="nofollow">Get it for {money(p['price'])}</a>{buy_etsy}</div>
    </div>
  </div>
</article>
"""
        htmlpage = page_shell(
            f"{p['name']} — {money(p['price'])} Instant Download | SideHustleKits",
            p["tagline"],
            url, pbody, depth=1,
            og_image=f"{BASE}/assets/products/{p['slug']}.png",
            extra_head=head)
        open(os.path.join(ROOT,"products",p["slug"]+".html"),"w",encoding="utf-8").write(htmlpage)
        urls.append((url, TODAY, "0.9"))

    # ---- blog pages
    for b in BLOG:
        url = f"{BASE}/blog/{b['slug']}.html"
        prod = next((x for x in PRODUCTS if x["slug"]==b["product"]), None)
        secs = ""
        for tag,txt in b["body"]:
            secs += f"<{tag}>{txt}</{tag}>\n"
        art_ld = json.dumps({
            "@context":"https://schema.org","@type":"Article",
            "headline":b["title"],"description":b["desc"],
            "author":{"@type":"Organization","name":"SideHustleKits"},
            "publisher":{"@type":"Organization","name":"SideHustleKits","logo":{"@type":"ImageObject","url":f"{BASE}/assets/logo.png"}},
            "datePublished":TODAY,"mainEntityOfPage":url
        }, ensure_ascii=False)
        crumbs = breadcrumb_jsonld([("Home",f"{BASE}/"),("Guides",f"{BASE}/index.html#blog"),(b["title"],url)])
        cta = ""
        if prod:
            cta = f"""<aside class="prodcta">
      <img src="../assets/products/{prod['slug']}.png" alt="{esc(prod['name'])}">
      <div><h3>{esc(prod['name'])}</h3><p>{esc(prod['tagline'])}</p>
      <a class="btn primary" href="../products/{prod['slug']}.html">View — {money(prod['price'])} &rarr;</a></div>
    </aside>"""
        bbody = f"""
<article class="post">
  <div class="wrap narrow">
    <nav class="crumbs"><a href="../index.html">Home</a> / <a href="../index.html#blog">Guides</a> / <span>{esc(b['title'])}</span></nav>
    <h1>{esc(b['title'])}</h1>
    <p class="lede">{esc(b['desc'])}</p>
    {secs}
    {cta}
  </div>
</article>
{jsonld(art_ld)}
{jsonld(crumbs)}
"""
        htmlpage = page_shell(
            f"{b['title']} | SideHustleKits",
            b["desc"], url, bbody, depth=1)
        open(os.path.join(ROOT,"blog",b["slug"]+".html"),"w",encoding="utf-8").write(htmlpage)
        urls.append((url, TODAY, "0.7"))

    # ---- sitemap.xml
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc,lm,pr in urls:
        sm.append(f"  <url><loc>{loc}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write("\n".join(sm))

    # ---- robots.txt
    open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8").write(
        f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")

    # ---- .nojekyll so GitHub Pages serves everything as-is
    open(os.path.join(ROOT,".nojekyll"),"w",encoding="utf-8").write("")

    print(f"Built {len(PRODUCTS)} products + {len(BLOG)} posts + sitemap ({len(urls)} urls).")

if __name__ == "__main__":
    build()
