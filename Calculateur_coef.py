import streamlit as st

# Configuration de la page (Optionnel, mais fait plus pro)
st.set_page_config(page_title="Calculateur Interne", page_icon="📊", layout="centered")

st.title("Calcul Tarifs fournisseurs📊")

# 1. Zone de saisie des données principales
# st.number_input bloque automatiquement les lettres et gère les nombres à virgule
coef = st.number_input("Entrez le Coefficient :", value=.0, step=0.1, format="%.2f")
tarif = st.number_input("Tarif HT / TTC (€) :", value=.0, step=1.0, format="%.2f")

# 2. Gestion de l'Écotaxe avec le Switch (st.checkbox fait office de switch/interrupteur)
etat_switch = st.checkbox("Activer l'Écotaxe")

# Si l'interrupteur est activé, on affiche le champ supplémentaire
if etat_switch:
    ecotaxe_saisie = st.number_input("Écotaxe HT(€) :", value=0.0, step=0.1, format="%.2f")
    ecotaxe_ttc = ecotaxe_saisie * 1.20
    # On affiche l'écotaxe TTC juste en dessous du champ
    st.info(f"Ecotaxe TTC : {ecotaxe_ttc:.2f} €")
else:
    ecotaxe_ttc = 0.0

# 3. Bouton pour lancer le calcul
if st.button("Calculer le résultat", type="primary"):
    # La logique mathématique de ton script initial
    if not etat_switch:
        resultat = tarif * coef
    else:
        resultat = (tarif * coef) + ecotaxe_ttc
        
    # 4. Affichage du résultat final dans un grand encadré vert
    st.success(f"### Prix TTc : {resultat:.2f} €")