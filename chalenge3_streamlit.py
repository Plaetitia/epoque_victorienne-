import streamlit as st

from streamlit_option_menu import option_menu

from streamlit_authenticator import Authenticate

# changer le fond de la page en beige
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5dc;  /* Couleur beige */
    }
    </style>
    """, unsafe_allow_html=True
)


# code de la quête

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)
authenticator.login()
def accueil():
      st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")


if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

# Création du menu pour afficher les choix 
selection = option_menu(
            menu_title=None,
            options=["Accueil", "Livres"]
        )

if selection == "Accueil":
    st.write("Bienvenue dans l'époque Victorienne ! ")
    col1, col2 = st.columns(2) 
    
    with col1:
        st.image("page_accueil_epoque_victorienne.jpeg",width=400) 

    with col2:
        st.image("page_accueil_epoque_victorienne_b.jpeg",width=400) 

elif selection == "Livres":
    st.write("Mes recommandations de livres")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.text("Sense and Sensibility, Jane Austen")
        st.image("couverture_ss_austen.jpeg")

    with col2:
        st.text("Pride and Prejudice, Jane Austen")
        st.image("couverture_pj_austen.jpeg")
   
    with col3:
        st.text("Jane Eyre, Charlotte Brontë")
        st.image("couverture_je_cbronte.jpeg")
        
    with col4:
        st.text("Wuthering Heights, Emily Brontë")
        st.image("couverture_wh_ebronte.jpg")
