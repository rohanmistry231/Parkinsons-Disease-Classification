import streamlit as st

# Sidebar configuration
st.sidebar.success("Select a page from the above options.")

# Title and Introduction
st.title(":green[Parkinson's Disease]")

# Function to display a section with a title and content
def display_section(title, content):
    """Displays a section with a title and content."""
    st.subheader(title)
    for paragraph in content:
        st.write(paragraph)

# Function to display a list of items with subheaders
def display_list_with_subheaders(items):
    """Displays a list of items with subheaders and descriptions."""
    for item, description in items.items():
        st.subheader(item)
        st.write(description)

# Section 1: What is Parkinson's Disease?
display_section(":blue[1. What is Parkinson's Disease?]", [
    "Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly, often beginning with a barely noticeable tremor in one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement.",
    "In the early stages, your face may show little or no expression, and your arms may not swing when you walk. Speech may become soft or slurred. Symptoms worsen as the condition progresses.",
    "Although Parkinson's disease cannot be cured, medications may significantly improve symptoms. In some cases, surgery may be recommended to regulate certain regions of the brain."
])

# Section 2: Symptoms of Parkinson's Disease
display_section(":blue[2. Symptoms of Parkinson's Disease]", [
    "Parkinson's symptoms can vary for everyone. Early symptoms are often mild and go unnoticed, beginning on one side of the body and usually remaining worse on that side.",
    "Common symptoms include:"
])

symptoms = {
    "Tremor": "Rhythmic shaking, often starting in a limb, like your hand or fingers. A pill-rolling tremor may occur, and shaking may decrease during tasks.",
    "Slowed movement (bradykinesia)": "Tasks become more difficult and time-consuming. Steps may shorten, and dragging or shuffling feet while walking is common.",
    "Rigid muscles": "Stiff muscles can occur anywhere, causing pain and limiting motion.",
    "Impaired posture and balance": "Stooped posture, balance issues, and falls are common.",
    "Loss of automatic movements": "Reduced ability to perform unconscious movements, like blinking, smiling, or swinging arms while walking.",
    "Speech changes": "Speech may become soft, quick, slurred, or monotonous.",
    "Writing changes": "Writing may become difficult, with smaller or cramped text."
}

display_list_with_subheaders(symptoms)

# Section 3: Causes of Parkinson's Disease
display_section(":blue[3. Causes of Parkinson's Disease]", [
    "Parkinson's disease occurs when certain nerve cells (neurons) in the brain break down or die. This leads to reduced dopamine levels, causing abnormal brain activity and movement issues.",
    "Potential factors include:"
])

causes = {
    "Genes": "Certain genetic mutations can increase the risk of Parkinson's. These are rare and typically affect those with many affected family members.",
    "Environmental triggers": "Exposure to certain toxins or environmental factors may increase risk, but the risk is relatively small.",
    "Presence of Lewy bodies": "Clumps of substances within brain cells, known as Lewy bodies, are markers of Parkinson's disease.",
    "Alpha-synuclein in Lewy bodies": "A specific protein found in Lewy bodies that researchers believe plays a role in Parkinson's."
}

display_list_with_subheaders(causes)

# Section 4: Risk Factors
display_section(":blue[4. Risk Factors of Parkinson's Disease]", [
    "Risk factors for Parkinson's include:"
])

risk_factors = {
    "Age": "Risk increases with age, typically beginning around 60 or older.",
    "Heredity": "Having close relatives with Parkinson's slightly increases risk, especially with multiple affected family members.",
    "Sex": "Men are more likely to develop Parkinson's than women.",
    "Exposure to toxins": "Prolonged exposure to herbicides and pesticides may slightly increase risk."
}

display_list_with_subheaders(risk_factors)

# Section 5: Prevention
display_section(":blue[5. Prevention of Parkinson's Disease]", [
    "Since the exact cause is unknown, there are no proven prevention methods.",
    "Research suggests that regular aerobic exercise and caffeine consumption (in coffee, tea, or cola) may reduce the risk, but more evidence is needed.",
    "Green tea may also be associated with a lower risk of Parkinson's disease."
])

# Section: How to Use the Prediction System
st.title(":green[How to Use the Prediction System]")
st.write(
    "Enter all required parameters on the Prediction page and click on :blue[Prediction Test Result] to view your results."
)
