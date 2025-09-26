{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa8c30d2-0a59-42af-81aa-6a38128eb492",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-09-26 09:51:09.016 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\USER1\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Load your trained model\n",
    "model = joblib.load(\"motor_maintenance_model.joblib\")\n",
    "\n",
    "st.title(\"⚙️ Motor Maintenance Prediction\")\n",
    "\n",
    "st.write(\"Enter motor parameters to predict if maintenance is needed.\")\n",
    "\n",
    "# Input fields\n",
    "temp = st.number_input(\"Temperature (°C)\", value=70.0)\n",
    "vib = st.number_input(\"Vibration (m/s²)\", value=0.5)\n",
    "current = st.number_input(\"Current (A)\", value=9.5)\n",
    "rpm = st.number_input(\"RPM\", value=1440.0)\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "    # Prepare the data for the model\n",
    "    data = np.array([[temp, vib, current, rpm]])\n",
    "    prediction = model.predict(data)[0]\n",
    "    result = \"No maintenance needed\" if prediction == 0 else \"Maintenance is needed\"\n",
    "    st.success(f\"Prediction: {result}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3e1f525-269d-473b-816f-2e438738f63d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
