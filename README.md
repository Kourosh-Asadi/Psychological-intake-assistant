# Psychological Intake Assistant

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-LLM_API-FF4B00)](https://groq.com/)
[![llama-cpp-python](https://img.shields.io/badge/llama--cpp--python-Local_Inference-green)](https://github.com/abetlen/llama-cpp-python)

A local LLM-based conversational system designed to conduct structured psychological intake interviews. The assistant collects relevant background information, explores the user's main concerns, and prepares a structured summary that can later support therapist matching.

> **Disclaimer**: This project is intended for research and educational purposes only. It is not a substitute for professional mental health care.

## Overview

This project demonstrates the application of large language models to a real-world conversational workflow. It focuses on:

- Controlled multi-turn dialogue management
- System prompt design for domain-specific behavior
- Structured information collection
- Fully offline inference using quantized models

The system is built to run entirely locally, making it suitable for privacy-sensitive use cases.

## Features

- Multi-turn conversation management
- Domain-specific system prompt for psychological intake
- Fully local inference support
- Structured information collection
- Clean and modular codebase

## Tech Stack

- Python 3.10+
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- Quantized GGUF models (tested with Qwen2.5-7B-Instruct)

## Project Structure

```text
psychological-intake-assistant/
├── main.py
├── system_prompt.txt
├── requirements.txt
└── README.md

## Disclaimer

This project is developed for educational and research purposes only. 
It is **not** a medical device and should not be used as a substitute for professional mental health care.
