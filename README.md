# 🏛️ AI Civic Complaint-to-Resolution Platform

A beginner-friendly prototype for an AI-powered civic complaint intake and prioritization system built with Streamlit.

## 📋 Features

✅ **Complaint Intake**: Simple text interface to submit civic complaints  
✅ **AI Classification**: Automatically categorizes complaints into Roads, Waste, Water, or Other  
✅ **Urgency Prioritization**: AI assigns priority levels (High, Medium, Low)  
✅ **Ticket Generation**: Creates unique ticket IDs for tracking  
✅ **Beautiful UI**: Clean, intuitive Streamlit interface with emojis  
✅ **No API Keys Required**: Uses mock AI with keyword matching  

## 🚀 Quick Start

### 1. Install Python (if not already installed)
Download from [python.org](https://www.python.org/downloads/)

### 2. Clone the Repository
```bash
git clone https://github.com/pavankumar-1511/ai-civic-complaint-platform.git
cd ai-civic-complaint-platform
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## 📝 How to Use

1. **Enter Complaint**: Type your civic complaint in the text area
2. **Process**: Click the "🚀 Process Complaint" button
3. **View Results**: See AI classification, urgency level, and ticket number
4. **Track**: Your complaint gets a unique ticket ID for follow-up

## 🧪 Test Examples

Try these examples:

- **"There is a massive pothole on Main Street"**
  - Category: Roads
  - Urgency: Medium

- **"Water pipe leak flooding the basement"**
  - Category: Water
  - Urgency: High

- **"Garbage overflow at the corner park"**
  - Category: Waste
  - Urgency: Medium

## 🤖 How the AI Works

This prototype uses **keyword matching** for demonstration purposes:

### Classification
- **Roads**: Looks for keywords like "pothole", "street", "pavement", "broken", etc.
- **Waste**: Looks for keywords like "garbage", "trash", "litter", "dump", etc.
- **Water**: Looks for keywords like "water", "leak", "pipe", "flooding", "drain", etc.

### Urgency Prioritization
- **High**: Triggered by "dangerous", "hazard", "injury", "accident", "flooding", "emergency"
- **Medium**: Triggered by "broken", "damaged", "leak", "hole", "problem"
- **Low**: Default for mild complaints

## 📦 What's Included

```
ai-civic-complaint-platform/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🛠️ Technology Stack

- **Python 3.8+**
- **Streamlit** - Web UI framework
- **Standard Library** - `json`, `datetime`

## 🎓 For Beginners

This project is perfect for learning:
- How to build web apps with Python
- Basic AI/NLP concepts (keyword matching)
- Streamlit UI components
- Git and GitHub workflows

## 🔧 Customization

You can easily customize:
- **Categories**: Edit `classify_complaint()` function to add more categories
- **Keywords**: Modify the keyword lists to match your city's complaint types
- **Urgency Rules**: Update `prioritize_urgency()` for different logic
- **UI**: Streamlit widgets make it easy to add new features

## 📈 Future Enhancements

Potential improvements:
- Integration with real LLM APIs (OpenAI, Hugging Face)
- Database to store complaints
- Email notifications
- Admin dashboard
- Geolocation integration
- Real-time status updates

## 📄 License

MIT License - Feel free to use and modify!

## 💬 Support

For questions or issues, please open a GitHub issue in the repository.

---

**Built for learning and civic engagement** 🌍