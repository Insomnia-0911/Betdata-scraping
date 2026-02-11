import os
import pandas
import sqlite3
import streamlit

Execution_Path = os.getcwd()
Database_Folder = Execution_Path + '/Database/'
Database_Name = 'Betting_Database.db'
Database_Path = Database_Folder + Database_Name
Output_Folder = Execution_Path + '/Output/'

streamlit.set_page_config(layout="wide")

if 'PAGE' not in streamlit.session_state:
    streamlit.session_state['PAGE'] = 'PAGE_05'
else:
    if streamlit.session_state['PAGE'] != 'PAGE_05':
        streamlit.session_state.clear()
    else:
        pass

streamlit.write('## Veri Tabanı Excel Aktarma Ekranı ##')

streamlit.button('Excele aktar', key='button_export')
if streamlit.session_state.button_export:
    # Connect to the SQLite database
    conn = sqlite3.connect(Database_Path)

    # Query the database and load data into a DataFrame
    query = "SELECT * FROM match_bet_data;"  # Replace 'your_table' with your table name
    df = pandas.read_sql_query(query, conn)

    df = df.drop(['home_team_goal_time_1', 'home_team_goal_time_2', 'home_team_goal_time_3', 'home_team_goal_time_4', 'home_team_goal_time_5', 'away_team_goal_time_1', 'away_team_goal_time_2', 'away_team_goal_time_3', 'away_team_goal_time_4', 'away_team_goal_time_5'], axis=True)

    # Export DataFrame to an Excel file
    excel_file_path = 'Output/Veritabanı.xlsx'  # Replace with your desired Excel file path
    df[['order_hour', 'order_minute']] = df['hour'].str.split(':', expand=True).astype(int)

    df['order_date'] = df.apply(lambda row: pandas.Timestamp(year=row['year'],
                                                   month=row['month'],
                                                   day=row['day'],
                                                   hour=row['order_hour'],
                                                   minute=row['order_minute']), axis=1)

    # df['order_date'] = pandas.to_datetime(df[['year', 'month', 'day', 'order_hour', 'order_minute']])
    df = df.sort_values(by='order_date', ascending=False)
    df = df.drop(columns=['order_date', 'order_hour', 'order_minute'])
    df.to_excel(excel_file_path, index=False, engine='openpyxl')

    # Close the connection
    conn.close()