import streamlit as st
from phonenumbers import geocoder, carrier, timezone
import phonenumbers
def main():
    st.title("Định vị SĐT và nhà cung cấp dịch vụ")
    mobile_number=st.text_input("Nhập số điện thoại: ",type="password")
    if st.button("Track"):
        ch_number=phonenumbers.parse(mobile_number,'CH')
        st.success("Quốc gia: {}".format(geocoder.description_for_number(ch_number,"en")))
        services_operator=phonenumbers.parse(mobile_number, 'RO')
        st.success("Nhà cung cấp: {}".format(carrier.name_for_number(services_operator, "en")))
        gb_number = phonenumbers.parse(mobile_number, "GB")
        st.success("TimeZone: {}".format(timezone.time_zones_for_number(gb_number)))
if __name__=="__main__":
    main()