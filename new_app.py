import streamlit as st
import pandas as pd

def load_data():
    manufacturers = pd.DataFrame({
        'Name': ['Gar Labs', 'Lily\'s', 'Beauty Private Label', 'Federal Packaging', 'Twincraft', 
                 'Coughlin Companies', 'Sinoscan', 'KKT', 'Goodkind Co'],
        'MOQ': [5000, 10000, 3000, 5000, 15000, 5000, 10000, 5000, 10000],
        'Time': [14, 16, 12, 15, 20, 14, 16, 15, 17], # dummy data for illustration
        'Price_per_unit': [2.00, 5.50, 4.50, 5.00, 2.50, 4.50, 3.50, 5.00, 3.00],
        'Email': ['tom@garlabs.com', 'hello@moesgroup.org', 'Sales@bqgmanufacturing.com', 'info@federalpackage.com', 
                  'jackson.berman@twincraft.com', 'info@contactcoghlin.com', 'info@sinoscan.com', 'krupa@kktconsultants.com', 
                  'info@nutracapusa.com']
    })
    return manufacturers

def main():
    st.title('CPG Brand - Manufacturer Matching')
    manufacturers = load_data()
    
    st.sidebar.subheader('Manufacturers Information')
    st.sidebar.write(manufacturers)

    st.subheader('Company Information')
    company_name = st.text_input('Company Name', 'Pit Stop')
    product_type = st.text_input('Product Type', 'Deodorant')
    segment = st.text_input('Segment', 'Health and Beauty')
    annual_units = st.number_input('Annual Units', 4500)
    website_url = st.text_input('Website URL', 'www.hammondherbs.com')
    revenue_last_year = st.number_input('Revenue in the last 12 months ($)', 67000)
    price_per_unit = st.number_input('Price Per Unit ($)', 2.00)
    projected_revenue = st.number_input('Projected Revenue for the next 12 months ($)', 75000)
    ideal_monthly_units = st.number_input('Ideal Monthly Units', 1000)
    differentiation = st.text_input('Company Differentiation', 'All natural, biodegradable, and chemical free, essential oils')
    monthly_revenue = st.number_input('Average Monthly Revenue ($)', 5583.30)
    monthly_expense = st.number_input('Average Monthly Expense ($)', 2800)

    # Changed the names in the select box to match dataframe column names
    criteria = st.selectbox('Choose your main criteria', ['MOQ', 'Time', 'Price_per_unit'])
    if st.button('Find Best Manufacturer'):
        best_manufacturer = manufacturers.loc[manufacturers[criteria].idxmin()]
        st.subheader('Best Manufacturer Based on Selected Criteria')
        st.write(f"{best_manufacturer['Name']} is the best manufacturer based on {criteria} criteria. It has {best_manufacturer[criteria]} {criteria}.")
        st.subheader('Contact Information')
        st.write(f"You can contact {best_manufacturer['Name']} via email at {best_manufacturer['Email']}.")

if __name__ == "__main__":
    main()
