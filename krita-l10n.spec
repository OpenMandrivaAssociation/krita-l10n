# Supported l10n language
%define langlist af ar ast be bg br bs ca cs cy da de el en_GB eo es et eu fa fi fr fy ga gl he hi hne hr hu ia is it ja kk km ko lt lv mai mk mr ms nb nds ne nl nn oc pa pl pt pt_BR ro ru se sk sl sq sv ta tg th tr ug uk uz vi wa xh zh_CN zh_TW

%define appname krita
# Language descriptions

%define language_af Afrikaans
%define language_ar Arabic
%define language_ast Asturian
%define language_be Belarusian
%define language_bg Bulgarian
%define language_br Breton
%define language_bs Bosnian
%define language_ca Catalan
%define language_ca@valencia Catalan (Valencian)
%define language_cs Czech
%define language_cy Welsh
%define language_da Danish
%define language_de German
%define language_el Greek
%define language_en_GB British English
%define language_eo Esperanto
%define language_es Spanish
%define language_et Estonian
%define language_eu Basque
%define language_fa Farsi (Persian)
%define language_fi Finnish
%define language_fr French
%define language_fy Frisian
%define language_ga Irish Gaelic
%define language_gl Galician
%define language_he Hebrew
%define language_hi Hindi
%define language_hne Chhattisgarhi
%define language_hr Croatian
%define language_hu Hungarian
%define language_ia Interlingua
%define language_is Icelandic
%define language_it Italian
%define language_ja Japanese
%define language_kk Kazakh
%define language_km Khmer
%define language_ko Korean
%define language_lt Lithuanian
%define language_lv Latvian
%define language_mai Maithili
%define language_mk Macedonian
%define language_mr Marathi
%define language_ms Malay
%define language_nb Norwegian Bokmål
%define language_nds Low Saxon
%define language_ne Nepali
%define language_nl Dutch
%define language_nn Norwegian Nynorsk
%define language_oc Occitan
%define language_pa Punjabi/Panjabi
%define language_pl Polish
%define language_pt Portuguese
%define language_pt_BR Brazilian Portuguese
%define language_ro Romanian
%define language_ru Russian
%define language_se Northern Sami
%define language_sk Slovak
%define language_sl Slovenian
%define language_sq Albanian
%define language_sv Swedish
%define language_ta Tamil
%define language_tg Tajik
%define language_th Thai
%define language_tr Turkish
%define language_ug Uyghur
%define language_uk Ukrainian
%define language_uz Uzbek
%define language_uz@cyrillic Uzbek (Cyrillic)
%define language_vi Vietnamese
%define language_wa Walloon
%define language_xh Xhosa
%define language_zh_CN Chinese Simplified
%define language_zh_TW Chinese Traditional


# --- Danger line ---

# Locales
%{expand:%(for lang in %langlist; do echo "%%define locale_$lang `echo $lang | cut -d _ -f 1` "; done)}

Summary: Language files for krita
Name: krita-l10n
Version: 3.0
Release: 1
License: GPL
Group: System/Internationalization
Url: http://www.krita.org/
# localisation package
Source0: http://files.kde.org/krita/build/%{appname}-%{version}-l10n-win-current.tar.gz
Source1: %{name}-template.in
Source2: %{name}.rpmlintrc
BuildArch: noarch

%description
Language files for Krita.

# Expand all localisation packages descriptions.

%{expand:%(\
	for lang in %langlist; do\
		echo "%%{expand:%%(sed "s!__LANG__!$lang!g" %{_sourcedir}/%{name}-template.in 2> /dev/null)}";\
	done\
	)
}


%prep
%setup -D -T -n .

%build

%install
mkdir -p %{buildroot}%{_datadir}
cd %{buildroot}%{_datadir}
tar xf %{_sourcedir}/%{appname}-%{version}-l10n-win-current.tar.gz
rm -rf locale/all_languages locale/ca@valencia locale/uz@cyrillic
