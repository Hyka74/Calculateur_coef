import streamlit as st
import streamlit.components.v1 as components

# Config de la page mobile
st.set_page_config(page_title="Calculateur Coef & Écotaxe", page_icon="🧮", layout="centered")

st.title("📝 Calcul Tarif + écotaxe")

# 1. Initialisation de la mémoire pour chaque champ
if "prix" not in st.session_state:
    st.session_state.prix = None
if "coeff" not in st.session_state:
    st.session_state.coeff = None
if "ecotaxe" not in st.session_state:
    st.session_state.ecotaxe = None

# Fonctions pour vider chaque champ individuellement
def vider_prix():
    st.session_state.prix = None

def vider_coeff():
    st.session_state.coeff = None

def vider_ecotaxe():
    st.session_state.ecotaxe = None

# 2. Zones de saisie avec leurs boutons d'effacement individuels

# --- CHAMP 1 : Prix d'achat ---
col_prix1, col_prix2 = st.columns([6, 1])  # 6/7 de largeur pour la saisie, 1/7 pour le bouton
with col_prix1:
    prix_achat = st.number_input(
        "Prix d'achat HT/TTC (€)", 
        key="prix",
        placeholder="Entrez un prix", 
        format="%.2f"
    )
with col_prix2:
    # On ajoute un espace vide pour aligner le bouton avec la case de saisie
    st.write("##") 
    st.button("❌", key="btn_prix", on_click=vider_prix, help="Vider le prix")

# --- CHAMP 2 : Coefficient ---
col_coef1, col_coef2 = st.columns([6, 1])
with col_coef1:
    coefficient = st.number_input(
        "Coeff", 
        key="coeff",
        placeholder="Entrez un Coeff", 
        format="%.2f"
    )
with col_coef2:
    st.write("##")
    st.button("❌", key="btn_coeff", on_click=vider_coeff, help="Vider le coefficient")

# --- CHAMP 3 : Écotaxe ---
col_eco1, col_eco2 = st.columns([6, 1])
with col_eco1:
    ecotaxe = st.number_input(
        "Écotaxe HT (€)", 
        key="ecotaxe",
        placeholder="Entrez une écotaxe", 
        format="%.2f"
    )
with col_eco2:
    st.write("##")
    st.button("❌", key="btn_eco", on_click=vider_ecotaxe, help="Vider l'écotaxe")


st.write("---")

# 3. Sécurisation des valeurs vides
valeur_ecotaxe = ecotaxe if ecotaxe is not None else 0.0

# 4. Calcul complet
if prix_achat is not None and coefficient is not None:
    try:
        base_prix = prix_achat * coefficient
        resultat_final = base_prix + (valeur_ecotaxe * 1.2)
        
        # Affichage du tarif final
        st.metric(label="Tarif final TTC (€) avec écotaxe incluse", value=f"{resultat_final:.2f} €")
        
        # Affichage de l'écotaxe uniquement si elle est supérieure à 0
        if valeur_ecotaxe > 0:
            ecotaxe_ttc = valeur_ecotaxe * 1.2
            st.metric(label="Écotaxe TTC (€)", value=f"{ecotaxe_ttc:.2f} €")
            
    except Exception as e:
        st.error("Erreur dans le calcul. Vérifie les valeurs saisies.")
else:
    st.info("Veuillez saisir un prix d'achat et un coefficient pour afficher le tarif.")
# ==============================================================================
# Gestion du clavier téléphone
# ==============================================================================
components.html(
    """
    <script>
    function forceNumericKeyboard() {
        var inputs = window.parent.document.querySelectorAll('input[type="number"]');
        inputs.forEach(function(input) {
            if (input.getAttribute('inputmode') !== 'decimal') {
                input.setAttribute('inputmode', 'decimal');
            }
        });
    }
    forceNumericKeyboard();
    setInterval(forceNumericKeyboard, 1000);
    </script>
    """,
    height=0,
)
