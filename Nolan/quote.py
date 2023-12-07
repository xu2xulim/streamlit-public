import streamlit as st
#import pandas as pd
#import numpy as np
#import streamlit.components.v1 as components
#import streamlit_authenticator as stauth
#from streamlit_folium import folium_static
#import folium

#import os
#from datetime import datetime
from deta import Deta
#import json


if 'stage' not in st.session_state:
    st.session_state.stage = False

if 'order_key' not in st.session_state:
    st.session_state.order_key = False

#@st.cache_data(suppress_st_warning=True)

st.title("The Scrub Perfect Cleaning")

if not st.session_state['stage']:
    with st.expander("Open for Simple Quotation"):
    
        
        quote_menu = [{
			    "description": "Enter the number of bedrooms",
				"name": "Bedroom",
		        "unit_amount": 22000,
                "display_price": 220.00,
		        "quantity": 0
	            },
	            {
				"description": "Enter the number of bathrooms",
				"name": "Bathrooms",
			    "unit_amount": 24000,
                "display_price": 240.00,
		        "quantity": 0
	            }]

        selection = st.data_editor(quote_menu,
                        column_config={
                            "display_price": st.column_config.NumberColumn(
                            "Price (in USD)",
                            help="The price of the product in USD",
                            min_value=0,
                            max_value=1000,
                            step=None,
                            format="$ %8.2f",
                            )
                        },
                        hide_index=True, 
                        disabled=("description", "name", "display_price"),
                        column_order=("name", "description", "display_price", "quantity"))
        
        #st.write(selection)
        sum = 0.0
        items = []
        for sx in selection :
            if sx['quantity'] != 0:
                temp = {
		            "price_data": {
			            "currency": "usd",
			            "product_data": {
				            "description": sx['description'],
				            "name": sx['name']
			            },
			            "unit_amount": sx['unit_amount']
		            },
		            "quantity": str(sx['quantity'])
	                }
                sum += sx['quantity'] * sx['unit_amount']/100
                items.append(temp)
        
        st.write(f"Our quotation based on the information you have given us is ${sum}")
        st.write("Please confirm your order quantity before you checkout. Thanks")
        st.link_button(":blue[Checkout]", f"https://needyodddeletion.milynnus.repl.co/checkout/{st.session_state['order_key']}")

        