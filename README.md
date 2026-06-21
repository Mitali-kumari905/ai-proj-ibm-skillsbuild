# 💪 Personalized Workout & Diet Planner with AI 🍎

An AI-powered web application built with **Streamlit** and **Google Gemini (gemini-2.5-flash)** that generates highly customized, scientifically backed 7-day workout routines and macro-balanced meal plans based on individual user profiles.

---

## 🔒 Security & Production-Ready Architecture

> 💡 **Production Note for Evaluators:** > Following industry-standard DevOps and security best practices, **no hardcoded API keys or sensitive credentials are committed to this repository**. 
> - Production deployment utilizes secure cloud secrets management.
> - Local execution relies entirely on decoupled environment variables (`.env`) to prevent credential leakage and ensure zero trust security.

---

## 🌟 Features

* **Interactive Sidebar Profile Builder:** Users can input their physical metrics and personal preferences seamlessly:
    * Weight (kg) & Height (cm) sliders
    * Age input & Gender selection
    * Custom text areas for fitness Goals and Food Preferences
    * Drop-downs for Spending Level (Budget-friendly, Moderate, Premium) and Fitness Level (Beginner, Intermediate, Advanced)
* **Segmented Planning Control:** Toggle cleanly between a **Workout Planner** and a **Diet Planner**.
* **AI-Generated Weekly Workout Routines:** Detailed 7-day breakdowns including warm-ups, exercise tables (sets, reps, rest, form tips), and cool-downs.
* **AI-Generated Macro-Calculated Diet Plans:** Customized 7-day meal planners featuring daily caloric/macro targets, structured meal tables (Breakfast, Lunch, Dinner, Snacks), and smart grocery hacks.
* **Modern Dark UI:** Tailored custom CSS for a premium aesthetic and clear text scannability.

---

## 🚀 How to Run This Project Locally

To test this application locally, you can easily inject your own Google Gemini API key by following these steps:

### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>

---

## 🌐 Live Demo

🔗 https://ai-proj-ibm-skillsbuild.onrender.com/

