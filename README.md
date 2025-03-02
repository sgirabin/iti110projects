# ITI110 Project: Spam Detection with Deep Learning


## Reference

- Report: https://docs.google.com/document/d/17o-SNPd9ri9ZjznsM4cSbHs4PPL_-NVDaBv_bSBLnDA/edit?usp=sharing
- Jupiter Notebook: https://colab.research.google.com/drive/1wr0OGTzai7ZXg1K47RKfp3_-Cl_9Ty9e?usp=sharing 
- HuggingFace Deployment: https://huggingface.co/spaces/sgirabin/ITI110-Project 
- Google Drive: https://drive.google.com/drive/u/1/folders/1IfxD8gXyZSGNf0_P7GgPTjnfPdgBEWIO 
- Github:  https://github.com/sgirabin/iti110projects 

## Model

| Model | Batch Size| Dense Layer| Learning Rate| Test Loss| Accuracy| Precision| Recall| F1-Score| AUC | ROC | 
|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------| 
| CNN | 16 | [256, 128] | 0.0001 | 0.1889 | 98.04% | 97.34% | 98.88% | 98.10% | 99.77% | 
| CNN + LSTM | | 16 | [128, 64] | 0.0001 | 0.0486 | 98.36% | 98.27% | 98.54% | 98.40% | 99.82% |
| LSTM | 32 | [128, 64] | 0.0005 | 0.0537 | 98.70% | 98.17% | 99.31% | 98.74% | 99.87% |
-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|






