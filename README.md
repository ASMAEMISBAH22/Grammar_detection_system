# Grammar Correction system (English + French)

## Overview

This project implements a **Grammar Error Correction (GEC)** system using the **pre-trained GEC-T5 model (clang8)**. The model uses the **T5 sequence-to-sequence architecture** to automatically detect and correct grammatical errors in **English and French sentences**.  

This project provides a robust baseline for GEC without task-specific fine-tuning, enabling multilingual grammar correction in a zero-shot setting.

---

## Features

- Grammar correction for English and French
- Pre-trained GEC-T5 model for zero-shot correction
- Evaluation using **BLEU, ROUGE-L, and Word Error Rate (WER)**
- Supports large-scale datasets with automatic preprocessing
- Ready-to-use inference pipeline for sentence correction

---

## Dataset

Multilingual grammar correction dataset

Format: source,target

Filtered for English and French

Split: train / validation / test
## Results

English (pre-trained GEC-T5 model):

BLEU: 67.71

ROUGE-L F1: 0.8646

WER: 0.4778

French:

BLEU: 52.59

ROUGE-L F1: 0.7841

WER: 0.5871
