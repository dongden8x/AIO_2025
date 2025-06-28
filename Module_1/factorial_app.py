import streamlit as st

USERS = ['admin']

def fact(n):
    if n== 0 or n ==1:
        return 1
    return n * fact(n-1)


def login():
    st.title("Trang đăng nhập")
    username = st.text_input("Nhập tên người dùng")
    if st.button("Đăng nhập"):
        if username: #nếu có nhập vào username
            if username in USERS: #nếu username nhập vào thuộc danh sách được cấp quyền
                st.session_state.logged_in = True
                st.session_state.user_name = username
            else:
                st.session_state.logged_in = False
                st.session_state.user_name = username
        else:
            st.warning("Vui lòng nhập tên người dùng")
    
def factorial_calculator():
    st.write(f"Xin chào, {st.session_state.username}")
    if st.button("Đang xuất"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        st.rerun()
    number = st.number_input("Nhập vào một số:", min_value = 0, max_value=900)
    if st.button("Tính giai thừa"): 
        result = fact(number)
        st.write(f"Giai thừa của {number} sẽ là {result}")

def main():
    st.title("Ứng dụng tính giai thừa")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    if "username" not in st.session_state:
        st.session_state.username = ""

    if st.session_state.logged_in:
        factorial_calculator()
    else:
        login()


if __name__ == "__main__":
    main()
