import streamlit as st
import pandas as pd
import time
import os
import pymysql as p

conn=p.connect(host="localhost",password="10062007",user="root",database='w')

st.set_page_config(
    page_title="Student Record Manager",
    page_icon=os.path.join(os.getcwd(), "static", "image.png"),
    layout="wide",
    initial_sidebar_state="expanded")
st.markdown("""
<style>
.stApp{   
     background-color: #172554;
    color: #F59E0B;
    font-family: Arial, sans-serif;
}
h1{
   color: #6764b9;
   font-size: 50px;    
}
       }
/* Main Add Student Button/*
.stButton > button,
.stFormSubmitButton > button {
       background-color: #2563EB;
       color: white;
       border: none;
       border-radius: 10px;
       padding: 10px 24px;
       font-size: 16px;
       font-weight: bold;
       box-shadow: 0px 4px 12px rgba(34,54,123,0.4)
       transition: all 0.3s ease;
/* Button hover effect */
.stButton > button:hover,
.stFormSubmitForm > button:hover {
       background: #1D4ED8;
       color: white;
       transform: translateY(-2px);
       box-shadow: 0px 6px 16px rgba(56,78,321,.8)
}
/* Button click effect */
.stButton > button:active,
.stFormSubmitButton > button:active {
    transform: scale(0.96);
/* Input focus effect */
.stTextInput input:focus {
    border: 2px solid #3B82F6;
    box-shadow: 0px 0px 10px rgba(59, 130, 246, 0.5);
/* Number input */
.stNumberInput input {
    border-radius: 8px;
}
/* Select boxes */
.stSelectbox [data-baseweb="select"] {
    border-radius: 8px;
    transition: all 0.3s ease;
}

/* Dataframe */
.stDataFrame {
    border: 1px solid #3B82F6;
    border-radius: 10px;
}

/* Smooth animation */
* {
    scroll-behavior: smooth;
}

       </style>""", unsafe_allow_html=True)
st.title("Student Record Manager")

ch=st.selectbox("Choose an option",["Add student","View students","Update student","Remove student"])
if ch=="Add student":
        cursor=conn.cursor()
        with st.form("Add_Student_Form"):
              name=st.text_input("Enter name of student:")
              students_id=st.number_input("Enter id of student:")
              grade=st.selectbox("Choose Grade",["A+","A",'B+','B','C+','C','D','F'])
              cgpa=st.number_input("Enter CGPA:",min_value=0.0,max_value=10.0,step=0.1)
              submitted=st.form_submit_button("Add Student")
              if submitted:
                     cursor.execute("select students_id from student_managers where students_id=%s",(int(students_id)))
              if not name.strip() :
                    st.info("Enter students name")
              elif cursor.fetchone():
                    st.error("This Student ID Already Exist")   
              else:
                     with st.spinner("Processing..."):
                            time.sleep(1)
                            cursor.execute(
    "INSERT INTO student_managers(name, students_id, grade, cgpa) VALUES(%s, %s, %s, %s)",
    (name, students_id, grade, cgpa)
)
                            conn.commit()
                            st.success("Student Added")

elif ch=="View students":
        st.subheader("All Student Records")
        cursor=conn.cursor()
        cursor.execute("Select * from student_managers")
        df = pd.DataFrame(
    cursor.fetchall(),
    columns=['Name', 'Student ID', 'Grade', 'CGPA']
)
        if not df.empty:
               df['CGPA']=df['CGPA'].astype(float)
               st.dataframe(df,use_container_width=True,hide_index=True)
        else:
               st.info("No students records availiable.")       
elif ch=="Update student":
        cursor=conn.cursor()
        cursor.execute("select students_id from student_managers")
        ids=[r[0] for r in cursor.fetchall()]
        if not ids:
               st.info("No Student Record Found")
        else:
            students_id=st.selectbox("Select Student ID",ids)
            s=st.selectbox("Choose the Data you want to change",['Name','Grade','CGPA']) 
            if s=='Name':
                   new_value=st.text_input("Enter new Name:")
            elif s=="Grade":
               new_value=st.selectbox("Choose New Grade",["A+","A",'B+','B','C+','C','D','F'])            
            else:
               new_value=st.number_input("Enter new CGPA",min_value=0.0,max_value=10.0)       
       
        if st.button("Update Student"):
               with st.spinner("Processing..."):
                    time.sleep(1)
               if s=="Name":
                      if new_value.strip():
                            cursor.execute("UPDATE student_managers SET name=%s WHERE students_id=%s",(new_value.strip(), int(students_id)))
                            st.success("Students detail Updated successfully!")
                      else:
                             st.info("Enter new value")      
               elif s=="Grade":
                        cursor.execute("UPDATE student_managers SET grade=%s WHERE students_id=%s",(new_value, students_id))
                        conn.commit()
                        st.success("Students detail Updated successfully!")
                      
               elif s=="CGPA":
                      cursor.execute("update student_managers set cgpa=%s where students_id=%s",(new_value,students_id))
                      conn.commit()
                      st.success("Students detail Updated successfully!")
                      
                    
elif ch=="Remove student":
       cursor=conn.cursor()
       cursor.execute("select students_id from student_managers")
       ids=[r[0] for r in cursor.fetchall()]
       if not ids:
              st.info("No students record was found")
       else:
              students_id=st.selectbox('Select Student ID',ids)
              cursor.execute("Select * from student_managers where students_id=%s",(students_id,))
              data=cursor.fetchone()
              df=pd.DataFrame([data],columns=['Name','Student ID','Grade','CGPA'])
              st.write("Students Details:",df) 
              confirm=st.checkbox("Are you sure you want remove this student")
              if st.button("Remove Student"):
                     with st.spinner("Processing..."):
                            time.sleep(1)
                     if confirm:
                            cursor.execute("delete from student_managers where students_id=%s",(students_id,))
                            st.success("Student Removed") 
                            conn.commit()
                     else:
                            st.warning("Please confirm before removing the student")
              else: 
                     st.write("No student was removed")
