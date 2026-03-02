"""
╔═══════════════════════════════════════════════════════════════════════════╗
║          CustomTkinter — Vitrine Complète des Widgets                    ║
║          Tous les attributs sont modifiables dans ce fichier source      ║
╚═══════════════════════════════════════════════════════════════════════════╝

Prérequis : pip install customtkinter
Lancer    : python ctk_showcase.py

Navigation : chaque onglet présente un widget avec TOUS ses paramètres
             définis dans des dictionnaires en haut de chaque section.
"""

import customtkinter as ctk

# ═══════════════════════════════════════════════════════════════════════════
#  CONFIGURATION GLOBALE
# ═══════════════════════════════════════════════════════════════════════════

ctk.set_appearance_mode("dark")       # "light" | "dark" | "system"
ctk.set_default_color_theme("blue")   # "blue"  | "green" | "dark-blue"


# ═══════════════════════════════════════════════════════════════════════════
#  ❶  CTkButton — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
BTN = {
    "text"               : "Clique-moi !",
    "width"              : 200,
    "height"             : 50,
    "corner_radius"      : 12,
    "border_width"       : 2,
    "border_color"       : "#3a7ebf",
    "border_spacing"     : 2,
    "fg_color"           : "#1f538d",
    "hover_color"        : "#14375e",
    "text_color"         : "#ffffff",
    "text_color_disabled": "#6b6b6b",
    "font"               : ("Courier New", 16, "bold"),
    "image"              : None,
    "compound"           : "left",
    "state"              : "normal",   # "normal" | "disabled"
    "cursor"             : "hand2",
    "anchor"             : "center",
}


# ═══════════════════════════════════════════════════════════════════════════
#  ❷  CTkLabel — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
LBL = {
    "text"          : "Bonjour, CustomTkinter !",
    "width"         : 0,               # 0 = taille automatique
    "height"        : 0,
    "corner_radius" : 8,
    "fg_color"      : "transparent",   # fond du label ("transparent" | couleur)
    "text_color"    : "#ffffff",
    "font"          : ("Courier New", 20, "bold"),
    "image"         : None,
    "compound"      : "left",
    "anchor"        : "center",
    "justify"       : "center",        # "left" | "center" | "right"
    "wraplength"    : 0,               # 0 = pas de retour à la ligne forcé
    "cursor"        : "arrow",
    "padx"          : 0,
    "pady"          : 0,
}


# ═══════════════════════════════════════════════════════════════════════════
#  ❸  CTkEntry — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
ENT = {
    "width"              : 280,
    "height"             : 40,
    "corner_radius"      : 8,
    "border_width"       : 2,
    "border_color"       : "#3a7ebf",
    "fg_color"           : "#2b2b2b",
    "text_color"         : "#ffffff",
    "placeholder_text"   : "Tape quelque chose ici...",
    "placeholder_text_color": "#707070",
    "font"               : ("Courier New", 14),
    "show"               : "",         # "" = normal | "*" = mot de passe
    "state"              : "normal",   # "normal" | "disabled" | "readonly"
    "cursor"             : "xterm",
    "justify"            : "left",     # "left" | "center" | "right"
}


# ═══════════════════════════════════════════════════════════════════════════
#  ❹  CTkCheckBox — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
CHK = {
    "text"               : "Activer l'option",
    "width"              : 200,
    "height"             : 24,
    "corner_radius"      : 6,
    "border_width"       : 2,
    "border_color"       : "#3a7ebf",
    "fg_color"           : "#1f538d",
    "hover_color"        : "#14375e",
    "checkmark_color"    : "#ffffff",
    "text_color"         : "#ffffff",
    "text_color_disabled": "#6b6b6b",
    "font"               : ("Courier New", 14),
    "state"              : "normal",
    "cursor"             : "hand2",
    "onvalue"            : "on",
    "offvalue"           : "off",
}
CHK_INITIAL = True   # True = coché au démarrage


# ═══════════════════════════════════════════════════════════════════════════
#  ❺  CTkRadioButton — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
RDB = {
    "width"              : 200,
    "height"             : 24,
    "corner_radius"      : 1000,       # grand = cercle parfait
    "border_width_checked"  : 6,
    "border_width_unchecked": 3,
    "fg_color"           : "#1f538d",
    "hover_color"        : "#14375e",
    "border_color"       : "#3a7ebf",
    "text_color"         : "#ffffff",
    "text_color_disabled": "#6b6b6b",
    "font"               : ("Courier New", 14),
    "state"              : "normal",
    "cursor"             : "hand2",
}
RDB_OPTIONS = ["Option Alpha", "Option Beta", "Option Gamma"]
RDB_DEFAULT = 1   # index (0, 1 ou 2)


# ═══════════════════════════════════════════════════════════════════════════
#  ❻  CTkSwitch — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
SWT = {
    "width"              : 52,
    "height"             : 26,
    "corner_radius"      : 1000,
    "border_width"       : 3,
    "switch_width"       : 52,
    "switch_height"      : 26,
    "fg_color"           : "#3a3a3a",
    "progress_color"     : "#1f538d",
    "button_color"       : "#ffffff",
    "button_hover_color" : "#cccccc",
    "text"               : "Activer le mode",
    "text_color"         : "#ffffff",
    "text_color_disabled": "#6b6b6b",
    "font"               : ("Courier New", 14),
    "state"              : "normal",
    "cursor"             : "hand2",
    "onvalue"            : 1,
    "offvalue"           : 0,
}
SWT_INITIAL = True   # True = activé au démarrage


# ═══════════════════════════════════════════════════════════════════════════
#  ❼  CTkSlider — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
SLD = {
    "width"          : 300,
    "height"         : 16,
    "corner_radius"  : 1000,
    "border_width"   : 6,
    "button_corner_radius": 1000,
    "fg_color"       : "#3a3a3a",
    "progress_color" : "#1f538d",
    "button_color"   : "#3a7ebf",
    "button_hover_color": "#5a9edd",
    "from_"          : 0,       # valeur minimale
    "to"             : 100,     # valeur maximale
    "number_of_steps": 100,     # None = continu
    "orientation"    : "horizontal",  # "horizontal" | "vertical"
    "state"          : "normal",
    "cursor"         : "hand2",
}
SLD_INITIAL = 40   # valeur de départ


# ═══════════════════════════════════════════════════════════════════════════
#  ❽  CTkProgressBar — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
PRG = {
    "width"          : 300,
    "height"         : 16,
    "corner_radius"  : 1000,
    "border_width"   : 0,
    "fg_color"       : "#3a3a3a",
    "progress_color" : "#1f538d",
    "border_color"   : "#3a7ebf",
    "orientation"    : "horizontal",  # "horizontal" | "vertical"
    "mode"           : "determinate", # "determinate" | "indeterminate"
    "indeterminate_speed": 1,         # vitesse si mode indeterminate
    "determinate_speed"  : 1,
}
PRG_INITIAL = 0.6   # entre 0.0 et 1.0


# ═══════════════════════════════════════════════════════════════════════════
#  ❾  CTkComboBox — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
CMB = {
    "width"              : 280,
    "height"             : 40,
    "corner_radius"      : 8,
    "border_width"       : 2,
    "border_color"       : "#3a7ebf",
    "fg_color"           : "#2b2b2b",
    "button_color"       : "#1f538d",
    "button_hover_color" : "#14375e",
    "dropdown_fg_color"  : "#2b2b2b",
    "dropdown_hover_color": "#3a3a3a",
    "dropdown_text_color": "#ffffff",
    "text_color"         : "#ffffff",
    "font"               : ("Courier New", 14),
    "dropdown_font"      : ("Courier New", 13),
    "state"              : "normal",   # "normal" | "readonly" | "disabled"
    "cursor"             : "hand2",
    "justify"            : "left",
}
CMB_VALUES  = ["Choix Alpha", "Choix Beta", "Choix Gamma", "Choix Delta"]
CMB_DEFAULT = "Choix Alpha"


# ═══════════════════════════════════════════════════════════════════════════
#  ❿  CTkOptionMenu — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
OPT = {
    "width"              : 280,
    "height"             : 40,
    "corner_radius"      : 8,
    "fg_color"           : "#1f538d",
    "button_color"       : "#14375e",
    "button_hover_color" : "#0d2540",
    "dropdown_fg_color"  : "#2b2b2b",
    "dropdown_hover_color": "#3a3a3a",
    "dropdown_text_color": "#ffffff",
    "text_color"         : "#ffffff",
    "text_color_disabled": "#6b6b6b",
    "font"               : ("Courier New", 14),
    "dropdown_font"      : ("Courier New", 13),
    "state"              : "normal",
    "cursor"             : "hand2",
    "anchor"             : "w",
    "dynamic_resizing"   : True,
}
OPT_VALUES  = ["Pomme", "Banane", "Cerise", "Mangue"]
OPT_DEFAULT = "Pomme"


# ═══════════════════════════════════════════════════════════════════════════
#  ⓫  CTkTextbox — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
TXB = {
    "width"          : 400,
    "height"         : 160,
    "corner_radius"  : 8,
    "border_width"   : 2,
    "border_color"   : "#3a7ebf",
    "border_spacing" : 3,
    "fg_color"       : "#2b2b2b",
    "text_color"     : "#ffffff",
    "scrollbar_button_color"      : "#3a7ebf",
    "scrollbar_button_hover_color": "#5a9edd",
    "font"           : ("Courier New", 13),
    "state"          : "normal",   # "normal" | "disabled"
    "wrap"           : "word",     # "none" | "char" | "word"
    "cursor"         : "xterm",
    "activate_scrollbars": True,
}
TXB_CONTENT = (
    "Bienvenue dans la CTkTextbox !\n\n"
    "Ce widget est une zone de texte multi-lignes.\n"
    "Il supporte le scrollbar automatique, le wrapping,\n"
    "et peut être mis en lecture seule via state='disabled'.\n\n"
    "Modifie TXB dans le code source pour changer son apparence."
)


# ═══════════════════════════════════════════════════════════════════════════
#  ⓬  CTkFrame — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
FRM = {
    "width"          : 340,
    "height"         : 180,
    "corner_radius"  : 16,
    "border_width"   : 2,
    "border_color"   : "#3a7ebf",
    "fg_color"       : "#1a1a2e",
}


# ═══════════════════════════════════════════════════════════════════════════
#  ⓭  CTkScrollableFrame — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
SCF = {
    "width"          : 360,
    "height"         : 200,
    "corner_radius"  : 12,
    "border_width"   : 2,
    "border_color"   : "#3a7ebf",
    "fg_color"       : "#1a1a2e",
    "scrollbar_button_color"      : "#3a7ebf",
    "scrollbar_button_hover_color": "#5a9edd",
    "label_text"     : "Scrollable Frame",
    "label_font"     : ("Courier New", 12, "bold"),
    "label_text_color": "#3a7ebf",
    "label_fg_color" : "transparent",
    "orientation"    : "vertical",    # "vertical" | "horizontal"
}
SCF_ITEM_COUNT = 12   # nombre d'éléments dans la liste défilante


# ═══════════════════════════════════════════════════════════════════════════
#  ⓮  CTkSegmentedButton — Paramètres
# ═══════════════════════════════════════════════════════════════════════════
SGB = {
    "width"              : 360,
    "height"             : 40,
    "corner_radius"      : 8,
    "border_width"       : 2,
    "fg_color"           : "#2b2b2b",
    "selected_color"     : "#1f538d",
    "selected_hover_color": "#14375e",
    "unselected_color"   : "#2b2b2b",
    "unselected_hover_color": "#3a3a3a",
    "text_color"         : "#ffffff",
    "text_color_disabled": "#6b6b6b",
    "font"               : ("Courier New", 13, "bold"),
    "state"              : "normal",
    "cursor"             : "hand2",
}
SGB_VALUES  = ["Jour", "Semaine", "Mois", "Année"]
SGB_DEFAULT = "Semaine"


# ═══════════════════════════════════════════════════════════════════════════
#  HELPERS COMMUNS
# ═══════════════════════════════════════════════════════════════════════════

FONT_TITLE    = ("Courier New", 13, "bold")
FONT_SUBTITLE = ("Courier New", 10)
COLOR_ACCENT  = "#3a7ebf"
COLOR_MUTED   = "#808080"
COLOR_NOTE    = "#555555"


def make_tab_header(parent, title: str, description: str):
    """Bloc titre + sous-titre en haut de chaque onglet."""
    ctk.CTkLabel(parent, text=title, font=FONT_TITLE, text_color=COLOR_ACCENT).pack(pady=(24, 2))
    ctk.CTkLabel(parent, text=description, font=FONT_SUBTITLE, text_color=COLOR_MUTED).pack(pady=(0, 16))
    ctk.CTkFrame(parent, height=1, fg_color="#2a2a2a").pack(fill="x", padx=40, pady=(0, 22))


def make_feedback(parent, initial="—"):
    """Label de retour d'état sous le widget."""
    lbl = ctk.CTkLabel(parent, text=initial, font=FONT_SUBTITLE, text_color=COLOR_NOTE)
    lbl.pack(pady=(12, 0))
    return lbl


def make_code_hint(parent, hint: str):
    """Indice en bas pour rappeler où modifier."""
    ctk.CTkLabel(parent, text=hint, font=("Courier New", 9), text_color="#3a3a5a").pack(side="bottom", pady=8)


# ═══════════════════════════════════════════════════════════════════════════
#  APPLICATION PRINCIPALE
# ═══════════════════════════════════════════════════════════════════════════

class ShowcaseApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter — Vitrine des Widgets")
        self.geometry("640x540")
        self.minsize(580, 480)

        # ── TabView principal ──────────────────────────────────────────────
        self.tabs = ctk.CTkTabview(
            self,
            width=620,
            height=500,
            corner_radius=12,
            border_width=2,
            border_color="#2a2a2a",
            fg_color="#1a1a1a",
            segmented_button_fg_color="#111111",
            segmented_button_selected_color="#1f538d",
            segmented_button_selected_hover_color="#14375e",
            segmented_button_unselected_color="#111111",
            segmented_button_unselected_hover_color="#2a2a2a",
            text_color="#ffffff",
            text_color_disabled="#6b6b6b",
        )
        self.tabs.pack(padx=10, pady=10, fill="both", expand=True)

        # ── Création de tous les onglets ───────────────────────────────────
        tabs_data = [
            ("Button",   self._build_button_tab),
            ("Label",    self._build_label_tab),
            ("Entry",    self._build_entry_tab),
            ("CheckBox", self._build_checkbox_tab),
            ("Radio",    self._build_radio_tab),
            ("Switch",   self._build_switch_tab),
            ("Slider",   self._build_slider_tab),
            ("Progress", self._build_progress_tab),
            ("ComboBox", self._build_combobox_tab),
            ("OptionMenu", self._build_optionmenu_tab),
            ("Textbox",  self._build_textbox_tab),
            ("Frame",    self._build_frame_tab),
            ("Scrollable", self._build_scrollable_tab),
            ("Segmented", self._build_segmented_tab),
        ]

        for name, builder in tabs_data:
            self.tabs.add(name)
            builder(self.tabs.tab(name))

    # ──────────────────────────────────────────────────────────────────────
    #  ❶  CTkButton
    # ──────────────────────────────────────────────────────────────────────
    def _build_button_tab(self, parent):
        make_tab_header(parent,
            "CTkButton",
            "Bouton cliquable — modifie le dict BTN dans le code source")

        self._btn_count = 0

        btn = ctk.CTkButton(parent, **BTN, command=self._on_btn_click)
        btn.pack(pady=4)

        self._btn_feedback = make_feedback(parent, "— pas encore cliqué —")
        ctk.CTkLabel(parent, text=f'state = "{BTN["state"]}"',
                     font=FONT_SUBTITLE, text_color=COLOR_ACCENT).pack(pady=4)
        make_code_hint(parent, "→ modifie BTN{} en haut du fichier")

    def _on_btn_click(self):
        self._btn_count += 1
        self._btn_feedback.configure(
            text=f"✓ cliqué {self._btn_count} fois", text_color=COLOR_ACCENT)

    # ──────────────────────────────────────────────────────────────────────
    #  ❷  CTkLabel
    # ──────────────────────────────────────────────────────────────────────
    def _build_label_tab(self, parent):
        make_tab_header(parent,
            "CTkLabel",
            "Étiquette de texte — modifie le dict LBL dans le code source")

        lbl = ctk.CTkLabel(parent, **LBL)
        lbl.pack(pady=20)

        info_lines = [
            f'font          = {LBL["font"]}',
            f'text_color    = "{LBL["text_color"]}"',
            f'fg_color      = "{LBL["fg_color"]}"',
            f'anchor        = "{LBL["anchor"]}"',
            f'justify       = "{LBL["justify"]}"',
        ]
        for line in info_lines:
            ctk.CTkLabel(parent, text=line, font=("Courier New", 10),
                         text_color=COLOR_NOTE).pack(pady=1)

        make_code_hint(parent, "→ modifie LBL{} en haut du fichier")

    # ──────────────────────────────────────────────────────────────────────
    #  ❸  CTkEntry
    # ──────────────────────────────────────────────────────────────────────
    def _build_entry_tab(self, parent):
        make_tab_header(parent,
            "CTkEntry",
            "Champ de saisie — modifie le dict ENT dans le code source")

        self._entry = ctk.CTkEntry(parent, **ENT)
        self._entry.pack(pady=4)

        self._ent_feedback = make_feedback(parent, "— aucune saisie —")

        ctk.CTkButton(
            parent, text="Lire la valeur", width=160, height=34,
            font=("Courier New", 12), cursor="hand2",
            command=self._on_ent_read
        ).pack(pady=8)

        ctk.CTkLabel(parent, text=f'show = "{ENT["show"]}"  /  state = "{ENT["state"]}"',
                     font=FONT_SUBTITLE, text_color=COLOR_ACCENT).pack(pady=4)
        make_code_hint(parent, "→ modifie ENT{} en haut du fichier")

    def _on_ent_read(self):
        val = self._entry.get()
        self._ent_feedback.configure(
            text=f'valeur : "{val}"' if val else "— champ vide —",
            text_color=COLOR_ACCENT if val else COLOR_NOTE)

    # ──────────────────────────────────────────────────────────────────────
    #  ❹  CTkCheckBox
    # ──────────────────────────────────────────────────────────────────────
    def _build_checkbox_tab(self, parent):
        make_tab_header(parent,
            "CTkCheckBox",
            "Case à cocher — modifie le dict CHK dans le code source")

        self._chk_var = ctk.StringVar(value=CHK["onvalue"] if CHK_INITIAL else CHK["offvalue"])
        chk = ctk.CTkCheckBox(parent, **CHK, variable=self._chk_var,
                              command=self._on_chk_toggle)
        chk.pack(pady=10)

        self._chk_feedback = make_feedback(
            parent, f"état : {'coché' if CHK_INITIAL else 'décoché'}")
        make_code_hint(parent, "→ modifie CHK{} et CHK_INITIAL en haut du fichier")

    def _on_chk_toggle(self):
        val = self._chk_var.get()
        self._chk_feedback.configure(
            text=f"état : {'coché' if val == CHK['onvalue'] else 'décoché'}",
            text_color=COLOR_ACCENT)

    # ──────────────────────────────────────────────────────────────────────
    #  ❺  CTkRadioButton
    # ──────────────────────────────────────────────────────────────────────
    def _build_radio_tab(self, parent):
        make_tab_header(parent,
            "CTkRadioButton",
            "Bouton radio — modifie le dict RDB dans le code source")

        self._rdb_var = ctk.IntVar(value=RDB_DEFAULT)

        for i, label in enumerate(RDB_OPTIONS):
            ctk.CTkRadioButton(
                parent, **RDB,
                text=label, variable=self._rdb_var, value=i,
                command=self._on_rdb_select
            ).pack(pady=5)

        self._rdb_feedback = make_feedback(
            parent, f"sélection : {RDB_OPTIONS[RDB_DEFAULT]}")
        make_code_hint(parent, "→ modifie RDB{}, RDB_OPTIONS, RDB_DEFAULT en haut du fichier")

    def _on_rdb_select(self):
        idx = self._rdb_var.get()
        self._rdb_feedback.configure(
            text=f"sélection : {RDB_OPTIONS[idx]}", text_color=COLOR_ACCENT)

    # ──────────────────────────────────────────────────────────────────────
    #  ❻  CTkSwitch
    # ──────────────────────────────────────────────────────────────────────
    def _build_switch_tab(self, parent):
        make_tab_header(parent,
            "CTkSwitch",
            "Interrupteur toggle — modifie le dict SWT dans le code source")

        swt = ctk.CTkSwitch(parent, **SWT, command=self._on_swt_toggle)
        if SWT_INITIAL:
            swt.select()
        else:
            swt.deselect()
        swt.pack(pady=10)

        self._swt_feedback = make_feedback(
            parent, f"état : {'activé' if SWT_INITIAL else 'désactivé'}")
        make_code_hint(parent, "→ modifie SWT{} et SWT_INITIAL en haut du fichier")

        self._swt_widget = swt

    def _on_swt_toggle(self):
        val = self._swt_widget.get()
        self._swt_feedback.configure(
            text=f"état : {'activé' if val == SWT['onvalue'] else 'désactivé'}",
            text_color=COLOR_ACCENT)

    # ──────────────────────────────────────────────────────────────────────
    #  ❼  CTkSlider
    # ──────────────────────────────────────────────────────────────────────
    def _build_slider_tab(self, parent):
        make_tab_header(parent,
            "CTkSlider",
            "Curseur glissant — modifie le dict SLD dans le code source")

        self._sld_feedback = make_feedback(parent, f"valeur : {SLD_INITIAL}")

        sld = ctk.CTkSlider(parent, **SLD, command=self._on_sld_move)
        sld.set(SLD_INITIAL)
        sld.pack(pady=12)

        ctk.CTkLabel(parent,
                     text=f'from_={SLD["from_"]}  to={SLD["to"]}  '
                          f'steps={SLD["number_of_steps"]}  '
                          f'orientation="{SLD["orientation"]}"',
                     font=FONT_SUBTITLE, text_color=COLOR_NOTE).pack(pady=4)
        make_code_hint(parent, "→ modifie SLD{} et SLD_INITIAL en haut du fichier")

    def _on_sld_move(self, val):
        self._sld_feedback.configure(
            text=f"valeur : {val:.1f}", text_color=COLOR_ACCENT)

    # ──────────────────────────────────────────────────────────────────────
    #  ❽  CTkProgressBar
    # ──────────────────────────────────────────────────────────────────────
    def _build_progress_tab(self, parent):
        make_tab_header(parent,
            "CTkProgressBar",
            "Barre de progression — modifie le dict PRG dans le code source")

        self._prg = ctk.CTkProgressBar(parent, **PRG)
        self._prg.set(PRG_INITIAL)
        self._prg.pack(pady=16)

        self._prg_label = make_feedback(parent, f"valeur : {PRG_INITIAL:.0%}")

        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(pady=8)

        ctk.CTkButton(row, text="−10 %", width=90, height=32,
                      font=("Courier New", 12), cursor="hand2",
                      command=lambda: self._adjust_prg(-0.1)).pack(side="left", padx=6)
        ctk.CTkButton(row, text="+10 %", width=90, height=32,
                      font=("Courier New", 12), cursor="hand2",
                      command=lambda: self._adjust_prg(0.1)).pack(side="left", padx=6)

        ctk.CTkLabel(parent, text=f'mode="{PRG["mode"]}"',
                     font=FONT_SUBTITLE, text_color=COLOR_ACCENT).pack(pady=4)
        make_code_hint(parent, "→ modifie PRG{} et PRG_INITIAL en haut du fichier")

        self._prg_value = PRG_INITIAL

    def _adjust_prg(self, delta):
        self._prg_value = max(0.0, min(1.0, self._prg_value + delta))
        self._prg.set(self._prg_value)
        self._prg_label.configure(
            text=f"valeur : {self._prg_value:.0%}", text_color=COLOR_ACCENT)

    # ──────────────────────────────────────────────────────────────────────
    #  ❾  CTkComboBox
    # ──────────────────────────────────────────────────────────────────────
    def _build_combobox_tab(self, parent):
        make_tab_header(parent,
            "CTkComboBox",
            "Liste déroulante éditable — modifie le dict CMB dans le code source")

        self._cmb_feedback = make_feedback(parent, f"sélection : {CMB_DEFAULT}")

        cmb = ctk.CTkComboBox(
            parent, **CMB,
            values=CMB_VALUES,
            command=self._on_cmb_select
        )
        cmb.set(CMB_DEFAULT)
        cmb.pack(pady=12)

        ctk.CTkLabel(parent, text=f'state = "{CMB["state"]}"',
                     font=FONT_SUBTITLE, text_color=COLOR_ACCENT).pack(pady=4)
        make_code_hint(parent, "→ modifie CMB{}, CMB_VALUES, CMB_DEFAULT en haut du fichier")

    def _on_cmb_select(self, val):
        self._cmb_feedback.configure(
            text=f"sélection : {val}", text_color=COLOR_ACCENT)

    # ──────────────────────────────────────────────────────────────────────
    #  ❿  CTkOptionMenu
    # ──────────────────────────────────────────────────────────────────────
    def _build_optionmenu_tab(self, parent):
        make_tab_header(parent,
            "CTkOptionMenu",
            "Menu d'options — modifie le dict OPT dans le code source")

        self._opt_feedback = make_feedback(parent, f"sélection : {OPT_DEFAULT}")

        opt = ctk.CTkOptionMenu(
            parent, **OPT,
            values=OPT_VALUES,
            command=self._on_opt_select
        )
        opt.set(OPT_DEFAULT)
        opt.pack(pady=12)

        ctk.CTkLabel(parent, text=f'dynamic_resizing = {OPT["dynamic_resizing"]}',
                     font=FONT_SUBTITLE, text_color=COLOR_ACCENT).pack(pady=4)
        make_code_hint(parent, "→ modifie OPT{}, OPT_VALUES, OPT_DEFAULT en haut du fichier")

    def _on_opt_select(self, val):
        self._opt_feedback.configure(
            text=f"sélection : {val}", text_color=COLOR_ACCENT)

    # ──────────────────────────────────────────────────────────────────────
    #  ⓫  CTkTextbox
    # ──────────────────────────────────────────────────────────────────────
    def _build_textbox_tab(self, parent):
        make_tab_header(parent,
            "CTkTextbox",
            "Zone de texte multi-lignes — modifie le dict TXB dans le code source")

        txb = ctk.CTkTextbox(parent, **TXB)
        txb.insert("0.0", TXB_CONTENT)
        txb.pack(pady=4)

        ctk.CTkLabel(parent, text=f'wrap="{TXB["wrap"]}"  state="{TXB["state"]}"',
                     font=FONT_SUBTITLE, text_color=COLOR_ACCENT).pack(pady=6)
        make_code_hint(parent, "→ modifie TXB{} et TXB_CONTENT en haut du fichier")

    # ──────────────────────────────────────────────────────────────────────
    #  ⓬  CTkFrame
    # ──────────────────────────────────────────────────────────────────────
    def _build_frame_tab(self, parent):
        make_tab_header(parent,
            "CTkFrame",
            "Conteneur visuel — modifie le dict FRM dans le code source")

        frame = ctk.CTkFrame(parent, **FRM)
        frame.pack(pady=8)

        ctk.CTkLabel(frame, text="Je suis dans un CTkFrame",
                     font=("Courier New", 13, "bold"),
                     text_color=COLOR_ACCENT).pack(padx=20, pady=(20, 4))
        ctk.CTkLabel(frame, text="Les widgets enfants s'y placent normalement",
                     font=("Courier New", 10), text_color=COLOR_MUTED).pack(padx=20, pady=(0, 20))

        ctk.CTkLabel(parent,
                     text=f'corner_radius={FRM["corner_radius"]}  '
                          f'border_width={FRM["border_width"]}',
                     font=FONT_SUBTITLE, text_color=COLOR_NOTE).pack(pady=6)
        make_code_hint(parent, "→ modifie FRM{} en haut du fichier")

    # ──────────────────────────────────────────────────────────────────────
    #  ⓭  CTkScrollableFrame
    # ──────────────────────────────────────────────────────────────────────
    def _build_scrollable_tab(self, parent):
        make_tab_header(parent,
            "CTkScrollableFrame",
            "Conteneur défilant — modifie le dict SCF dans le code source")

        scf = ctk.CTkScrollableFrame(parent, **SCF)
        scf.pack(pady=4)

        for i in range(1, SCF_ITEM_COUNT + 1):
            ctk.CTkLabel(scf, text=f"  Élément #{i:02d}  —  défile pour voir la suite",
                         font=("Courier New", 12), text_color="#cccccc",
                         anchor="w").pack(fill="x", padx=10, pady=3)

        ctk.CTkLabel(parent, text=f'orientation="{SCF["orientation"]}"  '
                                  f'items={SCF_ITEM_COUNT}',
                     font=FONT_SUBTITLE, text_color=COLOR_NOTE).pack(pady=6)
        make_code_hint(parent, "→ modifie SCF{} et SCF_ITEM_COUNT en haut du fichier")

    # ──────────────────────────────────────────────────────────────────────
    #  ⓮  CTkSegmentedButton
    # ──────────────────────────────────────────────────────────────────────
    def _build_segmented_tab(self, parent):
        make_tab_header(parent,
            "CTkSegmentedButton",
            "Sélecteur segmenté — modifie le dict SGB dans le code source")

        self._sgb_feedback = make_feedback(parent, f"sélection : {SGB_DEFAULT}")

        sgb = ctk.CTkSegmentedButton(
            parent, **SGB,
            values=SGB_VALUES,
            command=self._on_sgb_select
        )
        sgb.set(SGB_DEFAULT)
        sgb.pack(pady=12)

        ctk.CTkLabel(parent, text=f'state = "{SGB["state"]}"',
                     font=FONT_SUBTITLE, text_color=COLOR_ACCENT).pack(pady=4)
        make_code_hint(parent, "→ modifie SGB{}, SGB_VALUES, SGB_DEFAULT en haut du fichier")

    def _on_sgb_select(self, val):
        self._sgb_feedback.configure(
            text=f"sélection : {val}", text_color=COLOR_ACCENT)


# ═══════════════════════════════════════════════════════════════════════════
#  POINT D'ENTRÉE
# ═══════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = ShowcaseApp()
    app.mainloop()
