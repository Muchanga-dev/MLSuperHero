import streamlit as st
import pathlib
import logging
import shutil
from bs4 import BeautifulSoup

#Conficuração da Página
def Conf_pagina(icon):
   st.set_page_config(
     page_title="Super Heróis ML App",
     page_icon=icon,
     layout="wide",
     initial_sidebar_state="auto"
     )

   hide_st_style="""
         <style>
         MainMenu {visibility: hidden;}
         footer {visibility: hidden;}
         header{visibility: hidden;}
         </style>
          """
   margins_css = """ 
        <style>
        .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
                }
        </style>"""


   st.markdown(hide_st_style, unsafe_allow_html=True)
   st.markdown(margins_css, unsafe_allow_html=True)
   
   return

def modify_tag_content(tag_name, new_content):
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    logging.info(f'editing {index_path}')
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    
    target_tag = soup.find(tag_name)  # find the target tag

    if target_tag:  # if target tag exists
        target_tag.string = new_content  # modify the tag content
    else:  # if target tag doesn't exist, create a new one
        target_tag = soup.new_tag(tag_name)
        target_tag.string = new_content
        try:
            if tag_name in ['title', 'script', 'noscript'] and soup.head:
                soup.head.append(target_tag)
            elif soup.body:
                soup.body.append(target_tag)
        except AttributeError as e:
            print(f"Error when trying to append {tag_name} tag: {e}")
            return

    # Save the changes
    bck_index = index_path.with_suffix('.bck')
    if not bck_index.exists():
        shutil.copy(index_path, bck_index)  # keep a backup
    index_path.write_text(str(soup))

   

def configure_app(path):
    # Configuração inicial
    Conf_pagina(path)
    modify_tag_content('title', 'Super-Heróis')
    modify_tag_content('noscript', 'Super-Heróis')

#Metadados de Pesquisa da Página