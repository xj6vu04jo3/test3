import streamlit as st

x = st.slider('Select a value')

def ds():
    print("D=S：a-bp=c+dp")
    a=st.slider('a=')
    b=st.slider('b=')
    c=st.slider('c=')
    d=st.slider('d=')
    p=(a-c)/(b+d)
    q=a-b*p
    st.write('均衡價格與數量')
    return p,q

def tax():
   st.slider("Pd=Ps+t")
    a=st.slider('需求線截距')
    b=st.slider('需求線斜率(絕對值)')
    c=st.slider('供給線截距')
    d=st.slider('供給線斜率')
    t=st.slider('稅'))
    p1=(a-c)/(b+d)
    ps=(a-c-b*t)/(b+d)
    pd=ps+t
    q2=a-b*pd
    eq=(round(pd,2),round(q2,2))
    q=round(pd-p1,2)
    w=round((pd-p1)/t,2)
    e=round(p1-ps,2)
    r=round((p1-ps)/t,2)
   st.write('稅後均衡價格與數量：')
   st.write(eq)
   st.write('轉嫁給消費者的稅：')
   st.write((q,w))
   st.write('轉嫁給生產者的稅：')
   st.write((e,r))
