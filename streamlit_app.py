import streamlit as st
import datetime

# Center content using Streamlit's container and markdown
with st.container():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    # Add logo image and x5make it larger by adjusting the width
    st.image("https://cdn.prod.website-files.com/66c72983bae166134aceff30/66c72e9088b2843fa5edb28d_Sailor%20Logo%20Green-p-500.png", width=300)

    # Calculate day difference and display counter
    start_date = datetime.date(2024, 7, 1)  # August 1, 2024
    current_date = datetime.date.today()
    day_diff = (current_date - start_date).days + 1

    # Display day counter
    st.title(f"{day_diff} days")

    # Google search form with HTML
    st.markdown(
        """
        <form action="https://www.google.com/search" method="GET" target="_self">
            <input type="text" name="q" placeholder="Search Google" style="width: 60%; padding: 10px; font-size: 1.2em;">
            <input type="submit" value="Search" style="display: none;">
        </form>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)