import streamlit as st
import json
from datetime import datetime

# ============================================
# MOCK AI PROCESSING (No API key needed)
# ============================================

def classify_complaint(complaint_text):
    """
    Mock AI classification function.
    Categorizes complaints into: Roads, Waste, or Water
    """
    complaint_lower = complaint_text.lower()
    
    # Simple keyword matching (mock AI)
    road_keywords = ["pothole", "road", "street", "pavement", "crack", "broken", "highway", "lane"]
    waste_keywords = ["garbage", "trash", "litter", "waste", "dump", "debris", "rubbish", "bins"]
    water_keywords = ["water", "leak", "pipe", "flooding", "drain", "sewage", "tap", "hydrant"]
    
    road_score = sum(1 for keyword in road_keywords if keyword in complaint_lower)
    waste_score = sum(1 for keyword in waste_keywords if keyword in complaint_lower)
    water_score = sum(1 for keyword in water_keywords if keyword in complaint_lower)
    
    scores = {"Roads": road_score, "Waste": waste_score, "Water": water_score}
    category = max(scores, key=scores.get)
    
    # Default to "Other" if no keywords matched
    if max(scores.values()) == 0:
        category = "Other"
    
    return category


def prioritize_urgency(complaint_text, category):
    """
    Mock AI urgency prioritization function.
    Returns: High, Medium, or Low
    """
    complaint_lower = complaint_text.lower()
    
    # High urgency indicators
    high_keywords = ["dangerous", "hazard", "injury", "accident", "flooding", "severe", "emergency", "urgent", "critical"]
    
    # Medium urgency indicators
    medium_keywords = ["broken", "damaged", "leak", "hole", "issue", "problem", "needs"]
    
    # Count keyword matches
    high_count = sum(1 for keyword in high_keywords if keyword in complaint_lower)
    medium_count = sum(1 for keyword in medium_keywords if keyword in complaint_lower)
    
    if high_count > 0:
        urgency = "High"
    elif medium_count > 0:
        urgency = "Medium"
    else:
        urgency = "Low"
    
    return urgency


def generate_ticket_id():
    """Generate a unique complaint ticket ID"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"COMPLAINT-{timestamp}"


# ============================================
# STREAMLIT UI
# ============================================

st.set_page_config(page_title="AI Civic Complaint Platform", layout="wide")

st.title("🏛️ AI Civic Complaint-to-Resolution Platform")
st.markdown("**Submit civic complaints and let AI help categorize and prioritize them!**")

# Sidebar for instructions
with st.sidebar:
    st.header("📋 Instructions")
    st.write("""
    1. Describe your civic complaint
    2. Click 'Process Complaint'
    3. View AI classification and urgency level
    4. Your complaint gets a ticket number
    """)
    st.divider()
    st.subheader("Example Complaints:")
    st.caption("• There is a massive pothole on Main Street")
    st.caption("• Garbage overflow at the corner park")
    st.caption("• Water pipe leak near residential area")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Submit Your Complaint")
    complaint_text = st.text_area(
        label="Describe the civic issue:",
        placeholder="Example: There is a massive pothole on Main Street that's causing accidents...",
        height=120,
        key="complaint_input"
    )

with col2:
    st.subheader("ℹ️ Info")
    st.info("This is a beginner-friendly prototype. AI uses keyword matching for mock classification.")

# Process button
if st.button("🚀 Process Complaint", type="primary", use_container_width=True):
    if complaint_text.strip():
        # Show processing spinner
        with st.spinner("🤖 AI is analyzing your complaint..."):
            # Call mock AI functions
            category = classify_complaint(complaint_text)
            urgency = prioritize_urgency(complaint_text, category)
            ticket_id = generate_ticket_id()
        
        # Display results
        st.divider()
        st.success("✅ Complaint processed successfully!")
        
        # Results in columns
        result_col1, result_col2, result_col3 = st.columns(3)
        
        with result_col1:
            st.metric(label="Category", value=category)
        
        with result_col2:
            urgency_color = "🔴" if urgency == "High" else "🟡" if urgency == "Medium" else "🟢"
            st.metric(label="Urgency Level", value=f"{urgency_color} {urgency}")
        
        with result_col3:
            st.metric(label="Ticket ID", value=ticket_id)
        
        # Detailed summary
        st.subheader("📄 Complaint Summary")
        summary = {
            "Ticket ID": ticket_id,
            "Submitted At": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Category": category,
            "Urgency": urgency,
            "Complaint": complaint_text,
            "Status": "Received & Queued for Review"
        }
        
        # Display as JSON
        st.json(summary)
        
        # Next steps
        st.info(f"✨ **Next Steps**: Your complaint (Ticket: {ticket_id}) has been categorized as **{category}** with **{urgency}** urgency. The relevant department will review and contact you soon.")
        
    else:
        st.error("⚠️ Please enter a complaint before processing.")

# Footer
st.divider()
st.markdown("""
---
**About this platform**: This is a beginner-friendly prototype demonstrating AI-powered civic complaint intake.
The AI uses simple keyword matching for demo purposes. A production system would integrate with real LLM APIs.
""")