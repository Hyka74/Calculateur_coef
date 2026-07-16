import streamlit as st
import streamlit.components.v1 as components

# Config de la page mobile
st.set_page_config(page_title="Calculateur Coef & Écotaxe", page_icon="🧮", layout="centered")

st.title("📝 Calcul Tarif + écotaxe")

# 1. Zones de saisie
prix_achat = st.number_input("Prix d'achat HT/TTC (€)", value=None, placeholder="Entrez un prix", format="%.2f")
coefficient = st.number_input("Coeff", value=None, placeholder="Entrez un Coeff", format="%.2f")
ecotaxe = st.number_input("Écotaxe HT (€)", value=None, placeholder="Entrez une écotaxe", format="%.2f")

st.write("---")

# 2. Sécurisation des valeurs vides
# Si l'écotaxe est vide (None), on la transforme en 0 pour éviter les bugs de calcul
valeur_ecotaxe = ecotaxe if ecotaxe is not None else 0.0

# 3. Calcul complet
# On ne lance le calcul que si l'utilisateur a rempli les deux valeurs obligatoires
if prix_achat is not None and coefficient is not None:
    try:
        # Formule classique : (Prix d'achat * Coefficient) + Écotaxe TTC (Écotaxe * 1.2)
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
    # Message d'attente discret tant que les cases ne sont pas remplies
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
