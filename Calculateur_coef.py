import streamlit as st
import streamlit.components.v1 as components

# Config de la page mobile
st.set_page_config(page_title="Calculateur Coef & Écotaxe", page_icon="🧮", layout="centered")

st.title("📝 Calcul Tarif + écotaxe")

# 1. Zones de saisie
prix_achat = st.number_input("Prix d'achat HT/TTC (€)", value is none, format="%.2f")
coefficient = st.number_input("Coeff", format="%.2f")
ecotaxe = st.number_input("Écotaxe HT (€)", format="%.2f")

st.write("---")

# 2. calcul complet
try:
    # Formule classique : (Prix d'achat * Coefficient) + Écotaxe
    base_prix = prix_achat * coefficient
    resultat_final = base_prix + (ecotaxe * 1.2)
    
    st.metric(label="Tarif final TTC (€) avec écotaxe inclus", value=f"{resultat_final:.2f}")
    
    if ecotaxe > 0:
        st.metric(label="Ecotaxe TTC (€)", value=f"{ecotaxe * 1.2}", format="%.2f")
        
except Exception as e:
    st.error("Erreur dans le calcul. Vérifie les valeurs saisies.")

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
