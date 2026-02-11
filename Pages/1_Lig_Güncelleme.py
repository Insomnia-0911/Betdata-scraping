import os
import json
import streamlit

Execution_Path = os.getcwd()
Database_Folder = os.path.join(Execution_Path, 'Database')
Database_Countries_Leagues_Dictionary_Name = 'Countries_Leagues_Dictionary.json'
Database_Countries_Leagues_Dictionary_Path = os.path.join(Database_Folder, Database_Countries_Leagues_Dictionary_Name)

# Klasör yoksa oluştur
if not os.path.exists(Database_Folder):
    os.makedirs(Database_Folder)

streamlit.set_page_config(layout="wide")

if 'PAGE' not in streamlit.session_state:
    streamlit.session_state['PAGE'] = 'PAGE_01'
else:
    if streamlit.session_state['PAGE'] != 'PAGE_01':
        streamlit.session_state.clear()

streamlit.write('## Ülkeler & Ligler ##')

# Sözlüğü yükle
if 'Countries_Leagues_Dictionary' not in streamlit.session_state:
    try:
        with open(Database_Countries_Leagues_Dictionary_Path, "r") as json_file:
            data = json.load(json_file)
            if isinstance(data, dict):
                streamlit.session_state.Countries_Leagues_Dictionary = data
            else:
                streamlit.warning("JSON formatı hatalı, yeni sözlük oluşturuluyor.")
                streamlit.session_state.Countries_Leagues_Dictionary = {}
    except FileNotFoundError:
        streamlit.session_state.Countries_Leagues_Dictionary = {}

def Save_Json():
    with open(Database_Countries_Leagues_Dictionary_Path, "w") as json_file:
        json.dump(streamlit.session_state.Countries_Leagues_Dictionary, json_file, indent=4)

def Add_Country():
    country = streamlit.session_state.text_input_country.strip()
    if country:
        if country not in streamlit.session_state.Countries_Leagues_Dictionary:
            streamlit.session_state.Countries_Leagues_Dictionary[country] = []
            Save_Json()
        streamlit.session_state.text_input_country = ""
    else:
        streamlit.warning("Lütfen bir ülke ismi giriniz.")

def Remove_Country():
    if 'multiselect_countries' in streamlit.session_state and streamlit.session_state.multiselect_countries:
        for Country_To_Remove in streamlit.session_state.multiselect_countries:
            if Country_To_Remove in streamlit.session_state.Countries_Leagues_Dictionary:
                del streamlit.session_state.Countries_Leagues_Dictionary[Country_To_Remove]
        Save_Json()
    else:
        streamlit.warning("Silinecek ülke seçilmedi.")

def Add_League():
    league = streamlit.session_state.text_input_league.strip()
    if 'multiselect_countries' in streamlit.session_state and streamlit.session_state.multiselect_countries:
        selected_country = streamlit.session_state.multiselect_countries[0]
        if league:
            if league not in streamlit.session_state.Countries_Leagues_Dictionary[selected_country]:
                streamlit.session_state.Countries_Leagues_Dictionary[selected_country].append(league)
                Save_Json()
            streamlit.session_state.text_input_league = ""
        else:
            streamlit.warning("Lütfen bir lig ismi giriniz.")
    else:
        streamlit.warning("Lütfen önce bir ülke seçiniz.")

def Remove_League():
    if 'multiselect_countries' in streamlit.session_state and streamlit.session_state.multiselect_countries:
        selected_country = streamlit.session_state.multiselect_countries[0]
        if 'multiselect_leagues' in streamlit.session_state and streamlit.session_state.multiselect_leagues:
            for League_To_Remove in streamlit.session_state.multiselect_leagues:
                if League_To_Remove in streamlit.session_state.Countries_Leagues_Dictionary[selected_country]:
                    streamlit.session_state.Countries_Leagues_Dictionary[selected_country].remove(League_To_Remove)
            Save_Json()
        else:
            streamlit.warning("Silinecek lig seçilmedi.")
    else:
        streamlit.warning("Lütfen önce bir ülke seçiniz.")

# Arayüz Düzeni
firstRow = streamlit.columns(3)
secondRow = streamlit.columns(3)
thirdRow = streamlit.columns(3)

if 'Disable_Text_Country' not in streamlit.session_state:
    streamlit.session_state.Disable_Text_Country = False
    streamlit.session_state.Disable_Add_Country = False
    streamlit.session_state.Disable_Remove_Country = False
    streamlit.session_state.Disable_Text_League = False
    streamlit.session_state.Disable_Add_League = False
    streamlit.session_state.Disable_Remove_League = False

with firstRow[0]:
    streamlit.text_input('Ülke', key='text_input_country')
with secondRow[0]:
    streamlit.button('Ülke Ekle', key='button_add_country', on_click=Add_Country, use_container_width=True)
with thirdRow[0]:
    streamlit.button('Ülke Sil', key='button_remove_country', on_click=Remove_Country, use_container_width=True)

with firstRow[1]:
    streamlit.text_input('Lig', key='text_input_league')
with secondRow[1]:
    streamlit.button('Lig Ekle', key='button_add_league', on_click=Add_League, use_container_width=True)
with thirdRow[1]:
    streamlit.button('Lig Sil', key='button_remove_league', on_click=Remove_League, use_container_width=True)

streamlit.multiselect('Ülkeler', list(streamlit.session_state.Countries_Leagues_Dictionary.keys()), key='multiselect_countries')

current_leagues = []
if streamlit.session_state.multiselect_countries:
    selected_country = streamlit.session_state.multiselect_countries[0]
    current_leagues = streamlit.session_state.Countries_Leagues_Dictionary.get(selected_country, [])

streamlit.multiselect('Ligler', current_leagues, key='multiselect_leagues')