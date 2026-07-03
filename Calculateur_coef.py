import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page mobile
st.set_page_config(page_title="Calculateur Coef", page_icon="🧮", layout="centered")

st.title("🧮 Calculateur de Coefficient")

# 1. Tes zones de saisie numériques
# (Modifie les labels "Prix d'achat" etc. si tu veux d'autres textes)
valeur_1 = st.number_input("Première valeur (ex: Prix d'achat)", value=0.0, step=0.1, format="%.2f")
valeur_2 = st.number_input("Deuxième valeur (ex: Coefficient)", value=0.0, step=0.1, format="%.2f")

st.write("---")

# 2. Le calcul (Exemple de multiplication, à adapter selon ta formule)
# Si tu as besoin d'une division ou autre, change le signe * ci-dessous
try:
    resultat = valeur_1 * valeur_2
    st.metric(label="Résultat du calcul", value=f"{resultat:.2f}")
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
    // S'exécute immédiatement et boucle légèrement pour contrer le rechargement de Streamlit
    forceNumericKeyboard();
    setInterval(forceNumericKeyboard, 1000);
    </script>
    """,
    height=0,
)
