{
    "name": "MyLab MuK Backend Theme",
    "summary": "Odoo Community Backend Theme",
    "version": "16.0.1.0.6",
    "category": "Themes/Backend",
    "sequence": -96,
    "license": "LGPL-3",
    "author": "MuK IT",
    "website": "http://www.mukit.at",
    "live_test_url": "https://mukit.at/r/SgN",
    "contributors": [
        "Mathias Markl <mathias.markl@mukit.at>",
    ],
    "depends": [
        "base_setup",
        "web_editor",
        "mail",
    ],
    "excludes": [
        "web_enterprise",
    ],
    "data": [
        "templates/webclient.xml",
        "views/res_config_settings.xml",
        "views/res_users.xml",
        "views/ir_filters_myLab.xml",
    ],
    "assets": {
        "web._assets_primary_variables": [
            (
                "after",
                "web/static/src/scss/primary_variables.scss",
                "muk_web_theme/static/src/colors.scss",
            ),
        ],
        "web._assets_backend_helpers": [
            "muk_web_theme/static/src/variables.scss",
            "muk_web_theme/static/src/mixins.scss",
        ],
        "web.assets_backend": [
            "muk_web_theme/static/src/core/**/*.xml",
            "muk_web_theme/static/src/core/**/*.scss",
            "muk_web_theme/static/src/core/**/*.js",
            "muk_web_theme/static/src/webclient/**/*.xml",
            "muk_web_theme/static/src/webclient/**/*.scss",
            "muk_web_theme/static/src/webclient/**/*.js",
            "muk_web_theme/static/src/views/**/*.scss",
        ],
    },
    "images": [
        "static/description/banner.png",
        "static/description/theme_screenshot.png",
    ],
    "installable": True,
    "application": True,
    "auto_install": True,
    "uninstall_hook": "_uninstall_cleanup",
}
