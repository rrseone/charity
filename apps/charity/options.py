from apps.charity.models import OptionText, OptionFile


def create_default_options():
    # ---- TEXT OPTIONS ----

    default_texts = {
        # ================= SITE =================
        "site_title": {"value": "CharityCare", "priority": 1},
        "site_tagline": {"value": "Together for change", "priority": 2},
        "site_description": {
            "value": (
                "CharityCare is a nonprofit organization dedicated to supporting vulnerable communities "
                "through education, healthcare, and sustainable development initiatives that create "
                "long-term social impact."
            ),
            "priority": 3
        },

        # ================= ABOUT =================
        "about_title": {"value": "About", "priority": 20},
        "about_title_2": {"value": "Foundation", "priority": 21},
        "about_subtitle": {"value": "Driven by compassion", "priority": 22},
        "about_description": {
            "value": (
                "Our foundation works to uplift underprivileged individuals by providing access to "
                "basic needs, education, and healthcare. We believe in transparency, compassion, "
                "and sustainable solutions that empower people to improve their own lives."
            ),
            "priority": 23
        },

        # ================= SERVICES =================
        "services_title": {"value": "Services", "priority": 40},
        "services_subtitle": {"value": "Support that empowers lives", "priority": 41},
        "services_description": {
            "value": (
                "We deliver community-focused services including education support, medical assistance, "
                "emergency relief, and skill development programs designed to promote self-reliance "
                "and long-term growth."
            ),
            "priority": 42
        },

        # ================= CAMPAIGNS =================
        "campaigns_title": {"value": "Campaigns", "priority": 60},
        "campaigns_subtitle": {"value": "Causes that matter", "priority": 61},
        "campaigns_description": {
            "value": (
                "Explore our active charity campaigns focused on education, healthcare, disaster relief, "
                "and poverty reduction. Every contribution helps us reach more lives and create real change."
            ),
            "priority": 62
        },

        # ================= EVENTS =================
        "event_title": {"value": "Events", "priority": 80},
        "event_subtitle": {"value": "Bringing communities together", "priority": 81},
        "event_description": {
            "value": (
                "We organize charity events, awareness programs, and fundraising activities that bring "
                "communities together and inspire collective action for social good."
            ),
            "priority": 82
        },

        # ================= TEAM =================
        "team_title": {"value": "Team", "priority": 100},
        "team_subtitle": {"value": "People behind impact", "priority": 101},
        "team_description": {
            "value": (
                "Our team consists of passionate volunteers and professionals committed to making a "
                "difference. Their dedication and expertise help turn compassion into meaningful impact."
            ),
            "priority": 102
        },

        # ================= DONATIONS =================
        "donates_title": {"value": "Donations", "priority": 120},
        "donates_subtitle": {"value": "Every gift matters", "priority": 121},
        "donates_description": {
            "value": (
                "Your donations directly support our programs and help provide essential resources to "
                "those in need. Every contribution, big or small, makes a powerful difference."
            ),
            "priority": 122
        },

        # ================= BLOG =================
        "blog_title": {"value": "Stories", "priority": 180},
        "blog_subtitle": {"value": "Updates from the field", "priority": 181},
        "blog_description": {
            "value": (
                "Read inspiring stories, project updates, and insights from our ongoing charity work. "
                "Stay informed about how your support is helping transform lives."
            ),
            "priority": 182
        },

        # ================= CONTACT =================
        "contacts_title": {"value": "Contact", "priority": 200},
        "contacts_subtitle": {"value": "Let’s start a conversation", "priority": 201},
        "contacts_description": {
            "value": (
                "Get in touch with us for inquiries, partnerships, or volunteer opportunities. "
                "We value your questions and look forward to connecting with you."
            ),
            "priority": 202
        },
        "contacts_btn_text": {"value": "Get in Touch", "priority": 203},
        "contacts_btn_link": {"value": "http://127.0.0.1:8000/contact", "priority": 204},
        "contact_email": {"value": "rrseone@gmail.com", "priority": 205},
        "contact_phone": {"value": "+8801916132438", "priority": 206},
        "contact_address": {"value": "Your address goes here, your demo address.", "priority": 207},

        "newsletter_title": {"value": "Newsletter", "priority": 220},
        "newsletter_subtitle": {"value": "Heaven fruitful doesn't over lesser in days. Appear creeping.", "priority": 221},
        "newsletter_description": {"value": "Heaven fruitful doesn't over lesser in days. Appear creeping.", "priority": 222},
        "newsletter_email_placeholder": {"value": "noreply@demain.com", "priority": 225},
        "newsletter_btn_label": {"value": "Submit", "priority": 226},

        # ================= VOLUNTEER =================
        "become_volunteer_title": {"value": "Volunteer", "priority": 301},
        "become_volunteer_btn": {"value": "Join the mission", "priority": 303},
        "become_volunteer_link": {"value": "http://127.0.0.1:8000/volunteer", "priority": 305},
    }

    for key, data in default_texts.items():
        OptionText.objects.get_or_create(
            key=key,
            defaults={
                "value": data["value"],
                "priority": data["priority"]
            }
        )

    default_files = {
        "site_logo": {"value": "images/logo/logo.png", "Charity Care": "", "priority": 1},
        "site_logo_reverse": {"value": "images/logo/logo_reverse.png", "Charity Care": "", "priority": 2},
        "site_favicon": {"value": "images/favicons/favicon.ico", "caption": "", "priority": 2},
        "site_favicon_16": {"value": "images/favicons/favicon-16x16.png", "caption": "", "priority": 3},
        "site_favicon_32": {"value": "images/favicons/favicon-32x32.png", "caption": "", "priority": 4},
        "site_favicon_apple": {"value": "images/favicons/favicon-32x32.png", "caption": "", "priority": 5},
        "site_favicon_safari": {"value": "images/favicons/safari-pinned-tab.svg", "caption": "", "priority": 6},
        "about_us_1": {"value": "images/aboutus/about1.png", "About Us": "", "priority": 10},
        "about_us_2": {"value": "images/aboutus/about2.png", "About Us": "", "priority": 10},
        "home_banner": {"value": "images/hero/1.png", "Our charity foundations": "", "priority": 101},
        "section_bg_one": {"value": "images/aboutus/section_bg01.png", "Become a volunteer": "", "priority": 103},
        "footer_bg": {"value": "images/footer/bg_dark.png", "Become a volunteer": "", "priority": 105},
        "campaigns_banner": {"value": "images/hero/2.png", "Our Campaigns": "", "priority": 203},


        "send_icon": {"value": "images/icons/send.png", "Send": "", "priority": 300},
    }

    for key, filedata in default_files.items():
        OptionFile.objects.get_or_create(
            key=key,
            defaults={
                "file": filedata["value"],
                "caption": filedata.get("caption", "File Caption"),
                "priority": filedata.get("priority", 50),
            }
        )