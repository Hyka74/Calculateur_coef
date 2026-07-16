import streamlit as st
import streamlit.components.v1 as components

# Config de la page mobile
st.set_page_config(page_title="Calculateur Coef & Écotaxe", page_icon="🧮", layout="centered")

st.title("📝 Calcul Tarif + écotaxe")

# 1. Initialisation de la mémoire (Session State) pour nos cases
if "prix_input" not in st.session_state:
    st.session_state.prix_input = None
if "coeff_input" not in st.session_state:
    st.session_state.coeff_input = None
if "ecotaxe_input" not in st.session_state:
    st.session_state.ecotaxe_input = None

# Fonction pour tout vider d'un coup
def vider_champs():
    st.session_state.prix_input = None
    st.session_state.coeff_input = None
    st.session_state.ecotaxe_input = None

# 2. Zones de saisie liées à la mémoire
prix_achat = st.number_input(
    "Prix d'achat HT/TTC (€)", 
    key="prix_input",
    placeholder="Entrez un prix", 
    format="%.2f"
)

coefficient = st.number_input(
    "Coeff", 
    key="coeff_input",
    placeholder="Entrez un Coeff", 
    format="%.2f"
)

ecotaxe = st.number_input(
    "Écotaxe HT (€)", 
    key="ecotaxe_input",
    placeholder="Entrez une écotaxe", 
    format="%.2f"
)

# 3. Le bouton magique pour tout effacer en 1 clic
st.button("🧹 Vider toutes les cases", on_click=vider_champs, use_container_width=True)

st.write("---")

# 4. Sécurisation des valeurs vides
valeur_ecotaxe = ecotaxe if ecotaxe is not None else 0.0

# 5. Calcul complet
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
