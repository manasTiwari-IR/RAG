import streamlit as st
from data_ingestion import load_data_from_user as load_data
from model_api import load_model
from embedding import download_gemini_embedding

def main():
    st.set_page_config("QA with Documents")
    st.title("QA System using LamaIndex and Gemini")
    st.write("This is a simple QA system built using LamaIndex and Gemini. You can ask any question related to the document you have uploaded, and the system will provide you with an answer based on the content of the document.")
    doc = None  # None means no document has been uploaded yet
    try:
        doc=st.file_uploader("Upload your document")
    except Exception as e:
        st.write("An error occurred while uploading the document. Please try again.")
        doc = None
    if(doc is not None):
        st.write("Document uploaded successfully!")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            document=load_data(doc)
            model=load_model()
            query_engine=download_gemini_embedding(model,document)
                
            response = query_engine.query(user_question)
                
            st.write(response.response)
            
            
if __name__ == "__main__":
    main()