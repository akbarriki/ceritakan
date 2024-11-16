from transformers import pipeline
import warnings, torch
from xutils import *

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

warnings.filterwarnings("ignore")

# configs = getConfig()
# model_dir = configs['model_dir']
# model_dir = getConfig()['model_dir']
model_dir = "pipe_indobert"

labels = {
    "LABEL_0": "mengkhawatirkan",
    "LABEL_1": "waspada",
    "LABEL_2": "normal"
}

def predict(teks, model=model_dir):
    pipe = pipeline("text-classification", model=model, device=device)
    return labels[pipe(teks)[0]['label']]


if __name__=="__main__":
    teks = "ingin mati aja. Lelah"
    print(predict(teks))

