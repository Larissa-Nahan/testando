from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mjtd-o14wi83+l&4ci5nb@ij7py@wv#0$)p5vt+tz!8#5koynx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

USE_DJANGO_JQUERY = True


# Application definition

INSTALLED_APPS = [
    'jazzmin',   # pip install -U django-jazzmin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'smart_selects',    # pip install django-smart-selects
    'django_cleanup.apps.CleanupConfig',    # pip install django-cleanup
    'users',
    'desempenho',
    'avaliacao',
    'diretoria_e_gerencia',
    'avaliar_usuario',
    'avaliar_colaborador',
    'edital',
]

AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Temas do Jazzmin
# https://django-jazzmin.readthedocs.io/ui_customisation/
# https://djangocentral.com/making-django-admin-jazzy-with-django-jazzmin/
JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-dark",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-primary",
    },
}

JAZZMIN_SETTINGS = {
    # Titulo do site na aba [por padrao eh current_admin_site.site_title]
    "site_title": "Avaliação 360º",

    # Alt do logo login???
    "site_header": "Logo da Avaliação 360º",

    # Titulo ao lado da logo no menu lateral (19 chars max) [por padrao eh current_admin_site.site_header]
    # Nao pode ser vazio pois causa problemas no design - mudar no css/html depois
    "site_brand": "Codata",

    # Logo no menu lateral (tem de estar na pasta static)
    # Retirar a classe .elevation-3 no html
    "site_logo": "/admin/imgs/logo-fundo-escuro.png",

    # Logo login (tem de estar na pasta static) [por padrao eh site_logo]
    # OBS: add style="max-width: 500px; width: 100%;" na tag img no /jazzmin/templates/registration/base.html
    "login_logo": "/admin/imgs/logo-fundo-escuro.png",

    # Logo login tema escuto (tem de estar na pasta static) [por padrao eh site_logo]
    # So deus sabe o pq ta havendo essa confusao entre o claro e escuro - investigar
    "login_logo_dark": "/admin/imgs/logo-fundo-claro.png",

    # CSS: classe para o logo no menu lateral classes that are applied to the logo above
    "site_logo_classes": "",

    # Favicon (preferencia de tamanho 32x32 px) [por padrao eh site_logo]
    "site_icon": "/admin/imgs/favicon.png",

    # Mensagem de bem vindo na pag de login
    "welcome_sign": "",

    # Copyright no footer
    "copyright": "CODATA - Companhia de Processamento de Dados da Paraíba",

    # Nao funciona??? 
    "search_model": "",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    # ???
    "user_avatar": "None",

    ##########################
    # Menu Superior (header) #
    ##########################

    # Links ao lado do menu superior
    "topmenu_links": [

        # Link para a Home page
        # (, "permissions": ["auth.view_user"]) nao se aplica?
        {"name": "Home",  "url": "admin:index"},

        # Link para um model
        {"model": "users.CustomUser"},

        # Link para uma pagina fora
        # Abre uma nova pag
        {"name": "CODATA", "url": "https://codata.pb.gov.br/", "new_window": True},
    ],

    ###################
    # Menu do Usuario #
    ###################

    # Links no menu do usuario
    "usermenu_links": [
        {"name": "Site da CODATA", "url": "https://codata.pb.gov.br/", "new_window": True},
        {"model": "users.CustomUser"},
    ],

    ################
    # Menu Lateral #
    ################

    # Exibir o menu lateral
    "show_sidebar": True,

    # Exibir submenus ja abertos
    # Com false ele cria um dropdown
    "navigation_expanded": False,

    # Hide these apps when generating side menu e.g (auth)
    # ????
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    # ????
    "hide_models": [],

    # Ordem dos elementos exibidos no menu lateral
    "order_with_respect_to": ["users", "edital",],

    # Icones no menu lateral
    # https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    "icons": {
        "users.CustomUser": "fas fa-users",
        "edital.AdicionarEdital": "fas fa-file",
        "avaliar_usuario.AvaliarUsuario": "fas fa-list",
        "avaliar_colaborador.AvaliarColaborador": "fas fa-list",
        "desempenho.FatorDesempenhoMerito": "fas fa-plus",
        "desempenho.FatorDesempenhoDemerito": "fas fa-minus",
    },
    # Icones default
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    # ????
    "related_modal_active": False,

    # #############
    # # UI Tweaks #
    # #############
    # # Relative paths to custom CSS/JS scripts (must be present in static files)
    # "custom_css": None,
    # "custom_js": None,
    # # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    # "use_google_fonts_cdn": True,
    # # Whether to show the UI customizer on the sidebar
    # "show_ui_builder": False,

    ###############
    # Visualizacao #
    ###############
    # Opcoes:
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format_overrides": {"users.CustomUser": "vertical_tabs", 
                                    "avaliacao.Criterio": "collapsible",},
}
