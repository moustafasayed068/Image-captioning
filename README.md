# Multimodal Image Captioning System

## 📌 Project Overview

This project presents a multimodal system that combines Computer Vision and Natural Language Processing to automatically generate captions for images collected from the web.

The system uses web scraping techniques to build a custom dataset, then applies multiple multimodal models to understand and describe images.

---

## 🎯 Objectives

* Collect images from the internet using web scraping
* Build a custom dataset
* Apply multimodal models for image captioning
* Enhance and analyze generated captions
* Compare results and evaluate performance

---

## 🧠 Pipeline

1. Web Scraping
2. Data Collection & Dataset Creation
3. Data Preprocessing
4. Image Captioning using BLIP
5. Second Multimodal Model (e.g., VILT)
6. Post-processing
7. Evaluation
8. Results Presentation

---

## 🤖 Models Used

* BLIP (for image captioning)
* VILT (for image-text understanding and enhancement)

---

## 🛠️ Technologies

* Python
* BeautifulSoup (Web Scraping)
* PyTorch
* HuggingFace Transformers
* PIL (Image Processing)

---

## 📂 Project Structure

```
project/
│── data/
│   └── images/
│
│── scraping/
│   └── scraper.py
│
│── preprocessing/
│   └── preprocess.py
│
│── models/
│   ├── blip_model.py
│   └── vilt_model.py
│
│── results/
│   └── captions.csv
│
│── main.py
│── README.md
```

---

## 🚀 How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run web scraping:

```
python scraper.py
```

3. Run the main pipeline:

```
python main.py
```

---

## 📊 Results

The system generates captions for images and demonstrates how combining multiple multimodal models improves understanding and output quality.

---

## 👥 Team Members

* Member 1
* Member 2
* Member 3
* Member 4
* Member 5

---

## 📌 Future Work

* Add Arabic caption generation
* Improve model accuracy
* Build a user-friendly interface

---

## 📎 Conclusion

This project demonstrates the effectiveness of multimodal learning by integrating image and text processing into a complete pipeline system.
