import streamlit as st
import chain
import vectordb

def code_generator_app():
    """
    Generates Code Generator App with Streamlit, providing user input and displaying output.
    Includes a sidebar with two sections: Code Generator and File Ingestion for RAG.
    """

    # Sidebar configuration
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/907/907457.png", width=80)
        st.title("🚀 AI Code Generator")
        section = st.radio("📌 Choose a Section:", ["Code Generator RAG", "RAG File Ingestion"], index=0)
        st.markdown("---")
        st.caption("Built with ❤️ using Streamlit")

    # db initialization
    vectordatabase = vectordb.initialize_chroma()

    # Code Generation Page
    if section == "Code Generator RAG":
        st.markdown("## 🎯Code Generator!")
        st.markdown("Provide details about your problem, and let AI generate the best solution for you.")
        
        with st.form("code_generator"):
            col1, col2 = st.columns([2, 3])
            
            with col1:
                language = st.selectbox("🔧 Select Programming Language:", ["Python", "JavaScript", "C++", "Java", "Ruby", "Go", "PHP"], index=0)
                toggle_state = st.checkbox("✨ Enable RAG for better suggestions")
            
            with col2:
                problem = st.text_area("📝 Describe the Task or Problem:", height=150)
            
            submitted = st.form_submit_button("🚀 Generate Code")
            
            if submitted:
                if toggle_state:
                    response = chain.generate_code_rag_chain(language, problem, vectordatabase)
                else:
                    response = chain.generate_code_chain(language, problem)
                
                st.success("✅ Code Generated Successfully!")
                st.code(response, language=language.lower())
    
    # File Ingestion Page
    elif section == "RAG File Ingestion":
        st.markdown("## 📂 Upload Documents for RAG Processing")
        st.markdown("Enhance AI code generation by adding reference materials to the VectorDB.")
        
        uploaded_file = st.file_uploader("📁 Upload a File", type=["txt", "csv", "docx", "pdf"])
        
        if uploaded_file is not None:
            vectordb.store_pdf_in_chroma(uploaded_file, vectordatabase)
            st.success(f"✅ '{uploaded_file.name}' uploaded and stored successfully in VectorDB!")

code_generator_app()