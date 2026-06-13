import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

#Configure Gemini
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    st.error("API key not found.")
model = genai.GenerativeModel("gemini-2.5-flash")


st.set_page_config(
    page_title="AI Workout & Diet Planner",
    page_icon="💪",
    layout="wide"  # This forces the app to use the full width of the screen
)

st.markdown("""
<style>
.stApp{
   background-color:#000000;
}
h2{
    color: #00E5FF !important;
}

</style>
""",unsafe_allow_html=True)

# function for response
def get_ai_response(weight, height, age, gender, goals, fitness_level, food, budget, prompt_template):
    
    # ❌ check missing values
    if not all([weight, height, age, gender, goals, fitness_level, food, budget]):
        return "⚠️ Please fill all fields before generating response."

    prompt = prompt_template.format(
        weight=weight,
        height=height,
        age=age,
        gender=gender,
        goals=goals,
        fitness_level=fitness_level,
        food=food,
        budget=budget
    )

    response = model.generate_content(prompt)
    return response.text

#=============================sidebar=======================================

st.markdown("""
<style>
.stSidebar{
background-color:#111111
}
[data-testid="stSidebar"], [data-testid="stSidebar"] * {
    color: #FFFFFF!important;
</style>
""",unsafe_allow_html=True)


img=st.sidebar.image("apple.png",width=150)

st.sidebar.header("User Profile")
weight=st.sidebar.slider("Weight in kg:",30,200,50)
st.sidebar.text(f"{weight} Kg")

height=st.sidebar.slider("Height in cm:",0,185,50)
st.sidebar.text(f"{height} cm")

age=st.sidebar.number_input("Age",min_value=13,max_value=90,step=1)

options=["Male","Female"]
gender=st.sidebar.radio("Gender",options=options)
goals=st.sidebar.text_area("Goal",placeholder="enter your goal")
food=st.sidebar.text_area("Food preferences",placeholder="e.g: egg,rice,chapati")
budget=st.sidebar.selectbox("Spending level",["budget-friendly","Moderate","Premium"])

fitness_level=st.sidebar.selectbox("Fitness Level",["Begineer","Intermediate","Advanced"],key="f_level")


#================================main page=================================================

st.header("Personalized Workout💪 & Diet Planner 🍎with AI ")

st.markdown("""
<style>
   .st-key-data{
    border: 2px solid #00E5FF;
    padding: 20px;
    border-radius: 10px;
    background-color: #161616;
    color:#FFFFFF;
       }
</style>
""",unsafe_allow_html=True)
with st.container(key="data"):
    st.subheader('Your Personalized Plan')
    col1,col2=st.columns(2)
    with col1:
        st.write(f"Your Weight: {weight}")
        st.write(f"Your Height: {height}")
        st.write(f"Your Age: {age}")
        st.write(f"Your Gender: {gender}")
    with col2:
        st.write(f"Your goal: {goals}")
        st.write(f"Fitness Level: {fitness_level}")
        st.write(f"Food prefernces: {food}")
        st.write(f"Your budget: {budget}")

st.write("To change any information or fill any information fill from the sidebar.")


st.markdown("""
<style>
label[data-testid="stWidgetLabel"] p {
    font-size: 20px !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
   .st-key-result{
    border: 2px solid #39FF14;
    padding: 20px;
    border-radius: 10px;
    background-color: #161616;
    color:#FFFFFF;
       }
</style>
""",unsafe_allow_html=True)

page = st.segmented_control(
    "Select what you want to plan",
    ["Workout planner", "Diet Planner"],default="Workout planner"
)

if page == "Workout planner":
    st.title("💪Plan Your Weekly Workout Routine")
    if st.button("Generate Plan"):
        WorkPlan=f"""
You are an elite, AI-powered Personal Trainer and Fitness Coach. Your task is to generate a highly customized, scientifically backed 7-day Weekly Workout Routine based on the user's specific profile provided below.
### USER PROFILE:
- Age:{age}
- Gender:{gender}
- Height:{height}
- Weight:{weight}
- Fitness Level:{fitness_level}
- Primary Goals:{goals}
- Diet/Food Preferences:{food}
- Budget:{budget}
### OUTPUT FORMATTING REQUIREMENTS:
1. **Tone:** Motivating, professional, and clear.
2. **Structure:** Provide an overview summary, followed by a day-by-day breakdown (Day 1 to Day 7).
3. **No Walls of Text:** Use Markdown tables, bold text, and bullet points to ensure the workout is easy to read at a glance.
4. **Precision:** For every exercise, you MUST include the number of sets, repetitions (or duration), and rest periods.

### EXPECTED OUTPUT LAYOUT:
## 🏋️‍♂️ Weekly Workout Overview
*Briefly explain the training split (e.g., Push/Pull/Legs, Upper/Lower) and why it perfectly fits their goal and fitness level.*

## 🗓️ Day-by-Day Breakdown

### Day 1: [Insert Focus, e.g., Upper Body - Push]
* **Warm-up:** [Insert 5-10 min warm-up details]
* **Workout Table:**

| Exercise | Sets | Reps / Duration | Rest | Notes / Form Tip |
| :--- | :--- | :--- | :--- | :--- |
| e.g., Bench Press | 4 | 8-10 reps | 90 sec | Keep elbows at a 45-degree angle |
| e.g., Overhead Press | 3 | 10 reps | 60 sec | Core tight, do not arch lower back |

* **Cool-down:** [Insert 5 min stretching details]

[...Repeat this explicit markdown structure for Day 2 through Day 7. Clearly label active recovery or rest days...]

## 💡 Coach's Progressive Overload & Tracking Tips
*Provide 2-3 actionable bullets on how the user should scale weights weekly and stay safe based on their specific level.*"""

        with st.container(key="result"):
            st.write(get_ai_response(weight, height, age, gender, goals, fitness_level, food, budget,WorkPlan))

elif page == "Diet Planner":
    st.title("🍎 Plan Your Weekly Diet")
    if st.button("Generate Plan"):
        diet=f"""You are an expert AI Dietitian and Clinical Nutritionist. Your task is to generate a highly customized, macro-calculated 7-day Weekly Diet Plan based on the user's profile provided below.

### USER PROFILE:
- Age:{age}
- Gender:{gender}
- Height:{height}
- Weight:{weight}
- Fitness Level:{fitness_level}
- Primary Goals:{goals}
- Diet/Food Preferences:{food}
- Budget:{budget}
### OUTPUT FORMATTING & NUTRITION REQUIREMENTS:
1. **Target Macros:** Estimate and display the target daily Calories, Protein (g), Carbs (g), and Fats (g) required to meet their goal.
2. **Structure:** Provide a clean Markdown Table for each day (Day 1 to Day 7) split into: Breakfast, Lunch, Dinner, and Snacks.
3. **Budget & Realism:** Ensure the meal ingredients strictly reflect their budget level and food preferences. Keep instructions concise.
4. **No Walls of Text:** Use bold text for key ingredients and cleanly formatted tables for the meals.

---

### EXPECTED OUTPUT LAYOUT:

## 🥑 Daily Nutritional Targets
*Based on your profile, here is your recommended daily caloric intake and macronutrient split:*
* **Total Calories:** ~[X,XXX] kcal / day
* **Protein:** [XXX]g | **Carbs:** [XXX]g | **Fats:** [XX]g

---

## 🗓️ 7-Day Meal Planner

### Day 1
| Meal Type | Menu Item & Core Ingredients | Estimated Macros | Budget & Prep Tip |
| :--- | :--- | :--- | :--- |
| **Breakfast** | **Oatmeal** with 1 scoop whey protein, **banana**, and 1 tbsp **peanut butter**. | ~450 kcal, 35g P | Batch-cook oats to save time. |
| **Lunch** | Grilled **chicken breast** (150g) with **brown rice** and steamed **broccoli**. | ~600 kcal, 45g P | Use frozen broccoli to stay under budget. |
| **Snack** | Greek **yogurt** (200g) with a handful of **mixed berries**. | ~200 kcal, 20g P | Buy bulk tubs of plain yogurt. |
| **Dinner** | Baked **salmon fillet** (150g) with roasted **sweet potato** and **asparagus**. | ~550 kcal, 38g P | Swap salmon for tilapia if budget is tight. |

[...Repeat this explicit markdown table structure for Day 2 through Day 7...]

---

## 🛒 Smart Grocery & Meal Prep Hacks
*Provide 3 actionable, highly specific tips on how the user can meal prep efficiently or shop smartly based on their stated budget and diet preference.*"""

        with st.container(key="result"):
            st.write(get_ai_response(weight, height, age, gender, goals, fitness_level, food, budget,diet))
