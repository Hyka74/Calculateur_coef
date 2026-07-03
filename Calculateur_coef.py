import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page mobile
st.set_page_config(page_title="Calculateur Coef & Écotaxe", page_icon="🧮", layout="centered")

st.title("🧮 Calculateur de Coefficient Prix")

# 1. Tes zones de saisie numériques
prix_achat = st.number_input("Prix d'achat HT/TTC (€)", value=0.0, step=0.1, format="%.2f")
coefficient = st.number_input("Coefficient", value=0.0, step=0.1, format="%.2f")
ecotaxe = st.number_input("Écotaxe HT (€)", value=0.0, step=0.01, format="%.2f")

st.write("---")

# 2. Le calcul complet
try:
    # Formule classique : (Prix d'achat * Coefficient) + Écotaxe
    # N'hésite pas à me dire s'il faut appliquer le coefficient différemment !
    base_prix = prix_achat * coefficient
    resultat_final = base_prix + ecotaxe
    
    st.metric(label="Prix de vente Final (€)", value=f"{resultat_final:.2f}")
    
    if ecotaxe > 0:
        st.caption(f"Dont {ecotaxe:.2f}€ d'écotaxe incluse.")
        
except Exception as e:
    st.error("Erreur dans le calcul. Vérifie les valeurs saisies.")

# ==============================================================================
# ASTUCE INVISIBLE : Force le pavé numérique avec virgule sur iPhone et Android
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
