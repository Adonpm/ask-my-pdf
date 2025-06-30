# AskMyPDF - Smart Document Assistant

An intelligent PDF document analysis tool powered by advanced AI technologies that allows users to upload PDF documents and ask contextual questions about their content.

![AskMyPDF Banner](https://img.shields.io/badge/AskMyPDF-Smart%20Document%20Assistant-blue?style=for-the-badge)

## ✨ Features

- **📄 PDF Upload & Processing**: Seamlessly upload and process PDF documents
- **🤖 AI-Powered Q&A**: Ask intelligent questions about your document content
- **🔍 Semantic Chunking**: Advanced context understanding for better answers
- **⚡ Fast Processing**: Optimized RAG (Retrieval-Augmented Generation) pipeline
- **🎨 Modern UI**: Clean, responsive interface with interactive elements
- **🔒 Secure**: Local processing with no data persistence concerns

## 🛠️ Technology Stack

### Backend
- **DeepSeek-R1**: Advanced Large Language Model for intelligent responses
- **LangChain**: AI orchestration and prompt management
- **Hugging Face**: Vector embeddings
- **Flask**: High-performance web framework
- **MILVUS**: Vector database for efficient similarity search
- **Python**: Core backend language

### Frontend
- **HTML5**: Modern markup structure
- **CSS3**: Advanced styling with glassmorphism effects
- **JavaScript**: Interactive frontend functionality
- **Font Awesome**: Beautiful icons and visual elements

## 📁 Project Structure

```
ASK-MY-PDF/
├── .github/
│   └── workflows/
│       └──  deploy.yml
│ 
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── chunker.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── pdf_utils.py
│   │   │   ├── rag_chain.py
│   │   │   └── vector_store.py
│   │   └── workflows/
│   │       ├── __init__.py
│   │       └── rag_pipeline.py
│   └── server/
│       └── main.py
├── frontend/
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
├── requirements.txt
├── Dockerfile
├── .env
├── .dockerignore
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Adonpm/ask-my-pdf.git
   cd ask-my-pdf
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a .env file in the project root directory.
   - Add your API keys and settings as shown in the configuration section below.

## 🔧 Configuration

The application can be configured through environment variables in the `.env` file:

```env
# API Configuration
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_hf_token
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_langchain_project
LANGCHAIN_TRACING_V2="true"
MILVUS_API_KEY=your_milvus_api_key
MILVUS_URI=your_milvus_uri
MILVUS_TOKEN=your_milvus_token

# Application Settings
DEBUG=True
MAX_FILE_SIZE=10MB
ALLOWED_EXTENSIONS=pdf
```

### Running the Application

**Current Version (Local Development)**
```bash
# Make sure you're in the project root directory and virtual environment is activated
(venv) python -m backend.server.main
```

The application will start on `http://127.0.0.1:7860/` 

## 🎯 Usage

1. **Upload PDF**: Click on the upload area or drag and drop your PDF file
2. **Ask Questions**: Type your question about the document content
3. **Optional**: Enable semantic chunking for enhanced context understanding
4. **Get Answers**: Click "Ask Your PDF" to receive AI-generated responses

## 🌟 Features in Detail

### Semantic Chunking
When enabled, the system uses advanced NLP techniques to break down documents into semantically meaningful chunks, improving answer accuracy and context understanding.

### RAG Pipeline
The Retrieval-Augmented Generation pipeline combines:
- Document preprocessing and chunking
- Vector embedding generation
- Similarity search in vector database
- Context-aware answer generation

## 🔮 Future Versions

This project is currently in local development phase. Future versions will include:

- **Web Deployment**: Published as a fully accessible website
- **User Authentication**: Secure user accounts and document management
- **Enhanced File Support**: Support for additional document formats
- **API Integration**: REST API for third-party integrations
- **Advanced Analytics**: Document analysis and insights
- **Multi-language Support**: Support for documents in various languages

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- **DeepSeek** for providing the advanced language model
- **LangChain** for the excellent AI orchestration framework
- **Hugging Face** for the vector embeddings
- **FastAPI** for the robust web framework
- **MILVUS** for the efficient vector database solution

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the [Issues](https://github.com/Adonpm/ask-my-pdf/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the issue

---

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by Adon