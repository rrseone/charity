from apps.charity.models import OptionText, OptionFile


def create_default_options():
    # ---- TEXT OPTIONS ----

    default_texts = {
        "site_title": {"value": "Charity Solutions", "priority": 1},
        "site_tagline": {"value": "Trusted software solutions for businesses", "priority": 2},
        "site_description": {
            "value": "We build secure, modern, and scalable digital products that help businesses grow online through technology-driven innovation and reliable software solutions.",
            "priority": 3
        },

        "about_title": {"value": "About Us", "priority": 21},
        "about_subtitle": {"value": "Trusted software solutions for businesses", "priority": 23},
        "about_description": {
            "value": "We build secure, modern, and scalable digital products that help businesses grow online through technology-driven innovation and reliable software solutions.",
            "priority": 25
        },

        "services_title": {"value": "Service Title", "priority": 41},
        "services_subtitle": {"value": "Service Subtitle", "priority": 43},
        "services_description": {
            "value": "We build secure, modern, and scalable digital products that help businesses grow online through technology-driven innovation and reliable software solutions.",
            "priority": 45
        },

        "campaigns_title": {"value": "Our Cases you can see", "priority": 61},
        "campaigns_subtitle": {"value": "Explore our latest causes that we works", "priority": 63},
        "campaigns_description": {
            "value": "We build secure, modern, and scalable digital products that help businesses grow online through technology-driven innovation and reliable software solutions.",
            "priority": 65
        },

        "event_title": {"value": "What we are boing", "priority": 81},
        "event_subtitle": {"value": "We arrange many social events for charity donations", "priority": 83},
        "event_description": {
            "value": "We build secure, modern, and scalable digital products that help businesses grow online through technology-driven innovation and reliable software solutions.",
            "priority": 85
        },

        "become_volunteer_title": {"value": "Lets Change The World With Humanity", "priority": 101},
        "become_volunteer_btn": {"value": "Become A Volunteer", "priority": 103},
        "become_volunteer_link": {"value": "http://127.0.0.1:8000/", "priority": 105},

        "team_title": {"value": "What we are doing", "priority": 121},
        "team_subtitle": {"value": "Our Expert Volunteer Always ready", "priority": 123},
        "team_description": {
            "value": "We build secure, modern, and scalable digital products that help businesses grow online through technology-driven innovation and reliable software solutions.",
            "priority": 125
        },

        "blog_title": {"value": "Our recent blog", "priority": 201},
        "blog_subtitle": {"value": "Latest News from our recent blog", "priority": 203},
        "blog_description": {
            "value": "We build secure, modern, and scalable digital products that help businesses grow online through technology-driven innovation and reliable software solutions.",
            "priority": 205
        },
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
        "site_logo": {"value": "images/logo.svg", "caption": "", "priority": 1},
        "site_favicon": {"value": "images/favicons/favicon.ico", "caption": "", "priority": 2},
        "site_favicon_16": {"value": "images/favicons/favicon-16x16.png", "caption": "", "priority": 3},
        "site_favicon_32": {"value": "images/favicons/favicon-32x32.png", "caption": "", "priority": 4},
        "site_favicon_apple": {"value": "images/favicons/favicon-32x32.png", "caption": "", "priority": 5},
        "site_favicon_safari": {"value": "images/favicons/safari-pinned-tab.svg", "caption": "", "priority": 6},
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