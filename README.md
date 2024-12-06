# Zero-shot Image Classification using Hugging Face CLIP

## Project Overview
This project utilizes the Hugging Face CLIP model to perform zero-shot image classification on uploaded images.  
Zero-shot classification allows the model to predict new classes without additional training by leveraging its pre-trained knowledge.

---

## Demo

![Example Image](images/opensource_term.jpg)
![Result Image](images/term_result.jpg)

### Classification Results
- **Predicted Class**: an orange  
- **Class Probabilities**:
  - an apple: 0.1816
  - an orange: 0.7374
  - a flower: 0.0598
  - a leaf: 0.0126
  - a broccoli: 0.0085 

---

## Dependencies and Versions
The following packages are required for this project.
  - Transformers 4.46.2
  - Pillow 11.0.0
To install them, use the command:  
`pip install -r requirements.txt`.

### `requirements.txt`
