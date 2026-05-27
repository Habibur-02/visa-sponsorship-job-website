"""
Real seed data: 20 countries, verified URLs.
Focus: government portals + entry-level friendly + free / pay-after sites.

NOTE: URLs verified at time of writing but the web changes.
Re-check periodically and update.
"""

COUNTRIES_DATA = [
    # ==================== GERMANY ====================
    {
        "name": "Germany", "slug": "germany", "iso_code": "DEU",
        "flag_emoji": "🇩🇪", "continent": "Europe",
        "summary": "EU Blue Card + Opportunity Card (Chancenkarte). Strong tech demand, English-friendly companies.",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 65000, "currency": "EUR",
        "notes": "Opportunity Card (2024+) lets job-seekers stay 1 year to find work. Many Berlin/Munich tech roles are English-only.",
        "job_sites": [
            {"name": "Make it in Germany", "url": "https://www.make-it-in-germany.com/en/looking-for-foreign-professionals/jobs",
             "description": "Official German government portal for skilled migration. Job listings, visa info, language support.",
             "site_type": "government", "is_government": True, "rank": 1,
             "notes": "🏛️ Official. Start here."},
            {"name": "Arbeitsagentur (Federal Employment Agency)", "url": "https://www.arbeitsagentur.de/en/welcome",
             "description": "Germany's official federal employment agency.",
             "site_type": "government", "is_government": True, "rank": 2},
            {"name": "EURES", "url": "https://eures.europa.eu/index_en",
             "description": "European Commission's official EU-wide job portal.",
             "site_type": "government", "is_government": True, "rank": 3},
            {"name": "arbeitnow", "url": "https://www.arbeitnow.com/english-speaking-jobs",
             "description": "English-speaking jobs in Germany, visa sponsorship filter.",
             "site_type": "job_board", "is_government": False, "rank": 4},
            {"name": "Relocate.me", "url": "https://relocate.me/jobs-in-germany",
             "description": "Tech jobs with relocation/visa support, free for candidates.",
             "site_type": "free_agency", "is_government": False, "rank": 5},
            {"name": "Honeypot", "url": "https://www.honeypot.io/",
             "description": "Tech-focused, candidates get offers from companies. Free for candidates.",
             "site_type": "pay_after", "pay_after_hire": True, "rank": 6,
             "notes": "Companies pay only if they hire. Candidate side is free."},
            {"name": "StepStone", "url": "https://www.stepstone.de/en/",
             "description": "One of Germany's largest job boards.",
             "site_type": "job_board", "rank": 7},
            {"name": "Xing Jobs", "url": "https://www.xing.com/jobs",
             "description": "Germany/Austria/Switzerland professional network, LinkedIn equivalent.",
             "site_type": "job_board", "rank": 8},
        ],
    },

    # ==================== NETHERLANDS ====================
    {
        "name": "Netherlands", "slug": "netherlands", "iso_code": "NLD",
        "flag_emoji": "🇳🇱", "continent": "Europe",
        "summary": "Highly Skilled Migrant visa, fast (~2 weeks). 30% tax ruling for expats. Very English-friendly.",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 60000, "currency": "EUR",
        "notes": "Employer must be IND-recognized sponsor. Tech, finance, agriculture strong.",
        "job_sites": [
            {"name": "Werk.nl (UWV)", "url": "https://www.werk.nl/werkzoekenden/",
             "description": "Official Dutch employment service.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "IND Recognized Sponsors List", "url": "https://ind.nl/en/public-register-recognised-sponsors",
             "description": "Official list of companies that can sponsor work visas.",
             "site_type": "government", "is_government": True, "rank": 2,
             "notes": "🎯 Apply only to companies on this list."},
            {"name": "Together Abroad", "url": "https://www.togetherabroad.nl/jobs",
             "description": "English-speaking jobs in the Netherlands.",
             "site_type": "job_board", "rank": 3},
            {"name": "Undutchables", "url": "https://www.undutchables.nl/",
             "description": "Recruiter for international candidates in NL. Free for candidates.",
             "site_type": "free_agency", "rank": 4},
            {"name": "Adams Multilingual Recruitment", "url": "https://www.adamsrecruitment.com/",
             "description": "Free recruiter for multilingual candidates.",
             "site_type": "free_agency", "rank": 5},
            {"name": "Indeed Netherlands", "url": "https://nl.indeed.com/jobs?q=visa+sponsorship",
             "description": "Visa sponsorship search filter.",
             "site_type": "job_board", "rank": 6},
        ],
    },

    # ==================== CANADA ====================
    {
        "name": "Canada", "slug": "canada", "iso_code": "CAN",
        "flag_emoji": "🇨🇦", "continent": "North America",
        "summary": "Express Entry, PNP, Global Talent Stream (2-week processing for tech). Welcoming to entry-level.",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 70000, "currency": "CAD",
        "notes": "Global Talent Stream (GTS) is gold for tech: 2-week work permit. LMIA usually needed but GTS streamlines.",
        "job_sites": [
            {"name": "Job Bank Canada", "url": "https://www.jobbank.gc.ca/findajob",
             "description": "Government of Canada official job bank. Filter by 'LMIA approved'.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Global Talent Stream Employer List", "url": "https://www.canada.ca/en/employment-social-development/services/foreign-workers/global-talent.html",
             "description": "Companies that use the fast-track GTS program.",
             "site_type": "government", "is_government": True, "rank": 2},
            {"name": "Canada Visa Jobs", "url": "https://canadavisajobs.com/",
             "description": "Aggregator for visa-sponsored Canadian jobs.",
             "site_type": "job_board", "rank": 3},
            {"name": "VanHack", "url": "https://www.vanhack.com/",
             "description": "Tech recruitment for international candidates → Canada. Free for candidates.",
             "site_type": "free_agency", "is_free": True, "rank": 4,
             "notes": "🆓 Free for candidates. Hosts virtual hiring events."},
            {"name": "Workopolis", "url": "https://www.workopolis.com/",
             "description": "Major Canadian job board.",
             "site_type": "job_board", "rank": 5},
        ],
    },

    # ==================== AUSTRALIA ====================
    {
        "name": "Australia", "slug": "australia", "iso_code": "AUS",
        "flag_emoji": "🇦🇺", "continent": "Oceania",
        "summary": "Skilled visa (subclass 482/186/189). Points-based. Tech, healthcare, engineering in demand.",
        "visa_difficulty": 3, "entry_friendly": True,
        "avg_salary_usd": 75000, "currency": "AUD",
        "notes": "TSS 482 visa needs employer sponsor. Check Skilled Occupation List (SOL).",
        "job_sites": [
            {"name": "Workforce Australia", "url": "https://www.workforceaustralia.gov.au/individuals/jobs",
             "description": "Australian Government's official job platform.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Seek", "url": "https://www.seek.com.au/jobs?keywords=visa+sponsorship",
             "description": "Australia's biggest job site. Search 'visa sponsorship'.",
             "site_type": "job_board", "rank": 2},
            {"name": "Jora", "url": "https://au.jora.com/",
             "description": "Australian job aggregator.",
             "site_type": "job_board", "rank": 3},
            {"name": "LiveHire", "url": "https://www.livehire.com/",
             "description": "Direct connection with sponsoring employers.",
             "site_type": "job_board", "rank": 4},
        ],
    },

    # ==================== UK ====================
    {
        "name": "United Kingdom", "slug": "united-kingdom", "iso_code": "GBR",
        "flag_emoji": "🇬🇧", "continent": "Europe",
        "summary": "Skilled Worker visa. Must apply to a 'licensed sponsor' company.",
        "visa_difficulty": 3, "entry_friendly": True,
        "avg_salary_usd": 60000, "currency": "GBP",
        "notes": "🎯 Only sponsor-licensed companies can sponsor you. Check the official register first.",
        "job_sites": [
            {"name": "Find a job (gov.uk)", "url": "https://www.gov.uk/find-a-job",
             "description": "UK Government's official job search.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "UK Sponsor License Register", "url": "https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers",
             "description": "Official list of companies that can sponsor work visas.",
             "site_type": "government", "is_government": True, "rank": 2,
             "notes": "🎯 Download CSV; filter by industry."},
            {"name": "Tier 2 Sponsors", "url": "https://www.tier2sponsors.com/",
             "description": "Curated list of UK companies that sponsor Skilled Worker visas.",
             "site_type": "job_board", "rank": 3},
            {"name": "Reed", "url": "https://www.reed.co.uk/jobs/visa-sponsorship-jobs",
             "description": "UK's largest job site, visa sponsorship section.",
             "site_type": "job_board", "rank": 4},
            {"name": "Totaljobs", "url": "https://www.totaljobs.com/",
             "description": "Major UK job board.",
             "site_type": "job_board", "rank": 5},
        ],
    },

    # ==================== IRELAND ====================
    {
        "name": "Ireland", "slug": "ireland", "iso_code": "IRL",
        "flag_emoji": "🇮🇪", "continent": "Europe",
        "summary": "Critical Skills Employment Permit. Big tech hubs (Google, Meta, Microsoft EMEA HQs).",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 65000, "currency": "EUR",
        "notes": "Critical Skills list is generous to tech roles. Salary threshold lower than UK.",
        "job_sites": [
            {"name": "JobsIreland", "url": "https://www.jobsireland.ie/",
             "description": "Irish Government's official jobs portal.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Critical Skills Occupations List", "url": "https://enterprise.gov.ie/en/what-we-do/workplace-and-skills/employment-permits/employment-permit-eligibility/highly-skilled-eligible-occupations-list/",
             "description": "Official list of jobs eligible for fast-tracked permits.",
             "site_type": "government", "is_government": True, "rank": 2},
            {"name": "IrishJobs", "url": "https://www.irishjobs.ie/",
             "description": "One of Ireland's largest job boards.",
             "site_type": "job_board", "rank": 3},
        ],
    },

    # ==================== NEW ZEALAND ====================
    {
        "name": "New Zealand", "slug": "new-zealand", "iso_code": "NZL",
        "flag_emoji": "🇳🇿", "continent": "Oceania",
        "summary": "Accredited Employer Work Visa (AEWV). Green List jobs get fast-track residence.",
        "visa_difficulty": 3, "entry_friendly": True,
        "avg_salary_usd": 55000, "currency": "NZD",
        "notes": "Employer must be accredited. Green List = priority occupations.",
        "job_sites": [
            {"name": "New Zealand Now", "url": "https://www.newzealandnow.govt.nz/",
             "description": "Official immigration + jobs portal.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Accredited Employers List", "url": "https://www.immigration.govt.nz/employ-migrants/employer-accreditation",
             "description": "Companies that can hire international workers.",
             "site_type": "government", "is_government": True, "rank": 2},
            {"name": "Seek New Zealand", "url": "https://www.seek.co.nz/",
             "description": "Major NZ job board.",
             "site_type": "job_board", "rank": 3},
            {"name": "Trade Me Jobs", "url": "https://www.trademe.co.nz/a/jobs",
             "description": "Popular NZ job site.",
             "site_type": "job_board", "rank": 4},
        ],
    },

    # ==================== SWEDEN ====================
    {
        "name": "Sweden", "slug": "sweden", "iso_code": "SWE",
        "flag_emoji": "🇸🇪", "continent": "Europe",
        "summary": "Work permit relatively straightforward. Tech sector huge (Spotify, Klarna, King).",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 50000, "currency": "SEK",
        "notes": "Employer must offer collective-agreement equivalent salary.",
        "job_sites": [
            {"name": "Arbetsförmedlingen (Public Employment Service)", "url": "https://arbetsformedlingen.se/platsbanken/?lang=en",
             "description": "Sweden's official job bank with English filter.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "TheLocal Jobs Sweden", "url": "https://jobs.thelocal.se/",
             "description": "English-language jobs in Sweden.",
             "site_type": "job_board", "rank": 2},
        ],
    },

    # ==================== DENMARK ====================
    {
        "name": "Denmark", "slug": "denmark", "iso_code": "DNK",
        "flag_emoji": "🇩🇰", "continent": "Europe",
        "summary": "Positive List + Pay Limit Scheme. Easy if you fit a shortage occupation.",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 70000, "currency": "DKK",
        "job_sites": [
            {"name": "Jobnet (Denmark)", "url": "https://job.jobnet.dk/CV/FindWork",
             "description": "Danish official job portal.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Workindenmark", "url": "https://www.workindenmark.dk/",
             "description": "Government portal for foreign skilled workers.",
             "site_type": "government", "is_government": True, "rank": 2},
        ],
    },

    # ==================== FINLAND ====================
    {
        "name": "Finland", "slug": "finland", "iso_code": "FIN",
        "flag_emoji": "🇫🇮", "continent": "Europe",
        "summary": "Specialist permit fast for tech. Work in Finland program actively recruits internationals.",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 50000, "currency": "EUR",
        "job_sites": [
            {"name": "Työmarkkinatori (Job Market)", "url": "https://tyomarkkinatori.fi/en",
             "description": "Finland's official employment service.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Work in Finland", "url": "https://www.workinfinland.com/",
             "description": "Government-backed initiative to attract international talent.",
             "site_type": "government", "is_government": True, "rank": 2},
        ],
    },

    # ==================== NORWAY ====================
    {
        "name": "Norway", "slug": "norway", "iso_code": "NOR",
        "flag_emoji": "🇳🇴", "continent": "Europe",
        "summary": "Skilled worker permit. High salaries, high cost of living.",
        "visa_difficulty": 3, "entry_friendly": False,
        "avg_salary_usd": 70000, "currency": "NOK",
        "job_sites": [
            {"name": "NAV (Public Employment)", "url": "https://arbeidsplassen.nav.no/en/",
             "description": "Norway's official labor and welfare office.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Finn Jobb", "url": "https://www.finn.no/job",
             "description": "Norway's largest job site.",
             "site_type": "job_board", "rank": 2},
        ],
    },

    # ==================== JAPAN ====================
    {
        "name": "Japan", "slug": "japan", "iso_code": "JPN",
        "flag_emoji": "🇯🇵", "continent": "Asia",
        "summary": "Engineer/Specialist visa. Highly Skilled Professional (points-based) gives faster PR.",
        "visa_difficulty": 3, "entry_friendly": True,
        "avg_salary_usd": 45000, "currency": "JPY",
        "notes": "Japanese helps but many global companies operate in English (Rakuten, Mercari, PayPay).",
        "job_sites": [
            {"name": "HelloWork (MHLW)", "url": "https://www.hellowork.mhlw.go.jp/",
             "description": "Japan's official government employment service.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Japan Dev", "url": "https://japan-dev.com/",
             "description": "Curated list of dev jobs in Japan, English-friendly companies.",
             "site_type": "job_board", "rank": 2,
             "notes": "🎯 Tech-focused, English roles."},
            {"name": "TokyoDev", "url": "https://www.tokyodev.com/jobs",
             "description": "Software dev jobs in Japan for foreigners.",
             "site_type": "job_board", "rank": 3},
            {"name": "GaijinPot Jobs", "url": "https://jobs.gaijinpot.com/",
             "description": "Jobs for foreigners in Japan.",
             "site_type": "job_board", "rank": 4},
        ],
    },

    # ==================== SINGAPORE ====================
    {
        "name": "Singapore", "slug": "singapore", "iso_code": "SGP",
        "flag_emoji": "🇸🇬", "continent": "Asia",
        "summary": "Employment Pass (EP) for professionals. Points-based COMPASS system.",
        "visa_difficulty": 3, "entry_friendly": False,
        "avg_salary_usd": 60000, "currency": "SGD",
        "notes": "Min salary S$5,000 (S$5,500 for finance). COMPASS scoring matters.",
        "job_sites": [
            {"name": "MyCareersFuture", "url": "https://www.mycareersfuture.gov.sg/",
             "description": "Singapore's official government job portal.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "JobStreet Singapore", "url": "https://www.jobstreet.com.sg/",
             "description": "Major Southeast Asia job board.",
             "site_type": "job_board", "rank": 2},
        ],
    },

    # ==================== UAE ====================
    {
        "name": "United Arab Emirates", "slug": "uae", "iso_code": "ARE",
        "flag_emoji": "🇦🇪", "continent": "Asia",
        "summary": "Employment visa sponsored by employer. Tax-free salary. Golden Visa for skilled workers.",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 50000, "currency": "AED",
        "job_sites": [
            {"name": "MOHRE (Ministry of HR)", "url": "https://www.mohre.gov.ae/en/jobs.aspx",
             "description": "UAE official labor ministry portal.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Bayt", "url": "https://www.bayt.com/",
             "description": "Middle East's biggest job site.",
             "site_type": "job_board", "rank": 2},
            {"name": "Naukrigulf", "url": "https://www.naukrigulf.com/",
             "description": "Gulf jobs, popular among South Asian candidates.",
             "site_type": "job_board", "rank": 3},
            {"name": "GulfTalent", "url": "https://www.gulftalent.com/",
             "description": "Professional job board for the Gulf region.",
             "site_type": "job_board", "rank": 4},
        ],
    },

    # ==================== AUSTRIA ====================
    {
        "name": "Austria", "slug": "austria", "iso_code": "AUT",
        "flag_emoji": "🇦🇹", "continent": "Europe",
        "summary": "Red-White-Red Card for skilled workers. Points-based.",
        "visa_difficulty": 3, "entry_friendly": True,
        "avg_salary_usd": 55000, "currency": "EUR",
        "job_sites": [
            {"name": "AMS (Public Employment Service)", "url": "https://www.ams.at/arbeitsuchende",
             "description": "Austria's official employment service.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Migration Austria - Jobs", "url": "https://www.migration.gv.at/en/types-of-immigration/permanent-immigration/",
             "description": "Official portal for skilled migration to Austria.",
             "site_type": "government", "is_government": True, "rank": 2},
        ],
    },

    # ==================== FRANCE ====================
    {
        "name": "France", "slug": "france", "iso_code": "FRA",
        "flag_emoji": "🇫🇷", "continent": "Europe",
        "summary": "Talent Passport visa: 4-year multi-entry for skilled workers, researchers, founders.",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 50000, "currency": "EUR",
        "job_sites": [
            {"name": "France Travail (Pôle Emploi)", "url": "https://www.francetravail.fr/accueil/",
             "description": "France's official public employment service.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Welcome to the Jungle", "url": "https://www.welcometothejungle.com/en/jobs",
             "description": "Modern French job platform, lots of startups.",
             "site_type": "job_board", "rank": 2},
            {"name": "Choose Paris Region", "url": "https://www.chooseparisregion.org/",
             "description": "Government-backed initiative to attract international talent.",
             "site_type": "government", "is_government": True, "rank": 3},
        ],
    },

    # ==================== BELGIUM ====================
    {
        "name": "Belgium", "slug": "belgium", "iso_code": "BEL",
        "flag_emoji": "🇧🇪", "continent": "Europe",
        "summary": "Single Permit (combined work + residence). EU institutions hub.",
        "visa_difficulty": 3, "entry_friendly": True,
        "avg_salary_usd": 55000, "currency": "EUR",
        "job_sites": [
            {"name": "VDAB (Flanders)", "url": "https://www.vdab.be/vindeenjob",
             "description": "Flemish region's public employment service.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Actiris (Brussels)", "url": "https://www.actiris.brussels/",
             "description": "Brussels regional employment service.",
             "site_type": "government", "is_government": True, "rank": 2},
            {"name": "Le Forem (Wallonia)", "url": "https://www.leforem.be/",
             "description": "Walloon region employment service.",
             "site_type": "government", "is_government": True, "rank": 3},
        ],
    },

    # ==================== SPAIN ====================
    {
        "name": "Spain", "slug": "spain", "iso_code": "ESP",
        "flag_emoji": "🇪🇸", "continent": "Europe",
        "summary": "Highly Qualified Professional visa + Digital Nomad visa (since 2023).",
        "visa_difficulty": 3, "entry_friendly": True,
        "avg_salary_usd": 35000, "currency": "EUR",
        "notes": "Lower salaries but lower cost of living. Digital Nomad visa is very accessible for remote workers.",
        "job_sites": [
            {"name": "SEPE (Public Employment)", "url": "https://www.sepe.es/HomeSepe",
             "description": "Spain's official employment service.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "InfoJobs", "url": "https://www.infojobs.net/",
             "description": "Spain's largest job site.",
             "site_type": "job_board", "rank": 2},
            {"name": "Tecnoempleo", "url": "https://www.tecnoempleo.com/",
             "description": "Spanish tech-specific job board.",
             "site_type": "job_board", "rank": 3},
        ],
    },

    # ==================== PORTUGAL ====================
    {
        "name": "Portugal", "slug": "portugal", "iso_code": "PRT",
        "flag_emoji": "🇵🇹", "continent": "Europe",
        "summary": "Job-seeker visa (120 days). Tech Visa for sponsored employees, fast-tracked.",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 35000, "currency": "EUR",
        "notes": "Very welcoming to remote/tech workers. Lisbon and Porto are tech hubs.",
        "job_sites": [
            {"name": "IEFP (Public Employment)", "url": "https://www.iefp.pt/",
             "description": "Portugal's official employment service.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Landing.jobs", "url": "https://landing.jobs/",
             "description": "Portugal-based tech recruiter, focus on EU. Free for candidates.",
             "site_type": "free_agency", "is_free": True, "rank": 2,
             "notes": "🆓 Free for candidates."},
            {"name": "Net-Empregos", "url": "https://www.net-empregos.com/",
             "description": "Major Portuguese job board.",
             "site_type": "job_board", "rank": 3},
        ],
    },

    # ==================== ESTONIA ====================
    {
        "name": "Estonia", "slug": "estonia", "iso_code": "EST",
        "flag_emoji": "🇪🇪", "continent": "Europe",
        "summary": "Digital-first country. Startup visa, Digital Nomad visa. e-Residency program.",
        "visa_difficulty": 2, "entry_friendly": True,
        "avg_salary_usd": 30000, "currency": "EUR",
        "notes": "Wise, Bolt, Pipedrive are based here. Tech-friendly. Lower salaries but lower cost.",
        "job_sites": [
            {"name": "Tööturuamet (EURES Estonia)", "url": "https://www.tootukassa.ee/en",
             "description": "Estonia's official labor market authority.",
             "site_type": "government", "is_government": True, "rank": 1},
            {"name": "Work in Estonia", "url": "https://www.workinestonia.com/",
             "description": "Government-backed portal for international talent.",
             "site_type": "government", "is_government": True, "rank": 2},
            {"name": "MeetFrank", "url": "https://meetfrank.com/",
             "description": "Anonymous job-matching app, strong in Baltics.",
             "site_type": "job_board", "rank": 3},
        ],
    },
]


# ==================== GLOBAL CROSS-COUNTRY SITES ====================
# These are listed under multiple countries via separate seeding logic
GLOBAL_SITES_INFO = """
Cross-country free/pay-after-hire resources you can apply through worldwide:

- VanHack (vanhack.com) — free for candidates, virtual hiring events
- Relocate.me (relocate.me) — tech jobs with relocation/visa
- Honeypot (honeypot.io) — companies apply to you, free for you
- Talent.io (talent.io) — Europe tech, free for candidates
- Wellfound (wellfound.com) — startups, often visa
- Y Combinator Work at a Startup (workatastartup.com) — YC startups
- LinkedIn (#OpenToWork + visa filter)
- AngelList → Wellfound
- Stack Overflow Jobs (closed 2022, archived for reference)
"""
