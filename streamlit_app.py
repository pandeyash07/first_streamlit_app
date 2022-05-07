import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom's new Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#let's put a pick list here so they can pick the fruit they want to include
fruit_selected = streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]
#Display the Table on the page.  
streamlit.dataframe(fruit_to_show)

'''#streamlit.text(fruityvice_response)
streamlit.header('Fruity Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get the information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
    fruityvice_normalize = pandas.json_normalize(fruityvice_response.json()) 
    streamlit.dataframe(fruityvice_normalize) 
except URLERROR as e:
  streamlit.error()'''
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
   fruityvice_normalize = pandas.json_normalize(fruityvice_response.json()) 
   streamlit.dataframe(fruityvice_normalize) 

streamlit.header('Fruity Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get the information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
 '''except URLERROR as e :
  streamlit.error()'''
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("fruit_load_list_contains")
streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_area("Fruit_select")
streamlit.title("Thanks for adding jackfruit",add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from test')");








