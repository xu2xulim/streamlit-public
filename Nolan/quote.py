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

warning = None
#@st.cache_data(suppress_st_warning=True)

st.title("The Scrub Perfect Cleaning")

if not st.session_state['stage']:
    with st.expander("Open for Simple Quotation"):
        with st.form("Your basic details"):
            st.write("Please fill in the following:")
            if warning:
                st.warning(warning)
                warning = None

            name = st.text_input('Your name')
            email = st.text_input('Your email *')
            phone = st.text_input('Your telephone')

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                if email:
                    pass
                else:
                    warning = "We will need your email"
                    st.rerun()
                    st.session_state['stage'] = 1

    
if st.session_state['stage'] > 0:
    with st.expander("Open for the quotation details"):   
        quote_menu = [{
			    "description": "Enter the number of bedrooms",
				"name": "Bedrooms",
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
        cta = st.radio(
            "Please select from one of the call to action options",
                [":rainbow[Call Back]", "***Place a booking***"],
                captions = ["You will be prompted to book date and time to call you", "Payment will be via Stripe"])

        if cta == ':rainbow[Call Back]':
            st.write('You selected for us to call you back.')
            st.link_button(":blue[Book Now]", "https://tidycal.com/milynnus/quick-chat")
            st.caption("Go ahead. Try it")
        else:
            st.write("You have decided to place a booking.")
            st.balloons()
            st.link_button(":blue[Checkout]", f"https://needyodddeletion.milynnus.repl.co/checkout/{st.session_state['order_key']}")
            st.caption("For purpose of demo, this button will not work")
            st.link_button(":blue[Book Now]", "https://tidycal.com/milynnus/proof-of-solution")
            st.caption("Go ahead. Try it")