import torch
import pandas as pd
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from tqdm import tqdm
from nltk.tokenize import word_tokenize

def main():

    model_name = 'tuner007/pegasus_paraphrase'
    torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(
        model_name).to(torch_device)

    def get_response(input_text, num_return_sequences, num_beams, temperature):
        
        batch = tokenizer([input_text], truncation=True, padding='longest',
                          max_length=200, return_tensors="pt").to(torch_device)

        translated = model.generate(**batch, max_length=200, num_beams=num_beams,
                                    num_return_sequences=num_return_sequences, temperature=temperature)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text

    df = pd.read_csv('copilot-snippet-perturbated.csv',index_col='Unnamed: 0')

    pertubatedSentences = []
    originalSentences = list(df['parsedComments'])
    
    to_remove = []
    for (idx, row) in tqdm(df.iterrows()):
        

        sentence = row['parsedComments']
        try:
            if (len(word_tokenize(sentence))) > 40:
                to_remove.append(idx)
                continue
        except Exception:
            to_remove.append(idx)
            continue

     
        new_list = get_response(sentence, 3, 3, 1.0)

        to_set = ["".join(item.split()) for item in new_list]
        if len(to_set) != len(set(to_set)):
            to_remove.append(idx)
            continue

        pertubatedSentences.append(new_list)

    df = df.drop(to_remove)
    df['pertubatedComments'] = pertubatedSentences
    df.to_csv('copilot-snippet-perturbated.csv')


if __name__ == '__main__':
    main()
