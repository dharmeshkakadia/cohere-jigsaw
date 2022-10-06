cohere-jigsaw
=============
This project tests [Cohere](https://cohere.ai/)'s [Toxicity model](https://docs.cohere.ai/classify-content-mod/) without any finetuning on [Jigsaw dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge).

You can use the following steps to get started:

1. Setup 

    ```
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    ```

2. Sign up, [get your API_KEYS](https://os.cohere.ai/) and make it available for the code.

    ```
    export COHERE_API_KEY=OrZ.....TCo
    ```

3. Download the Jigsaw [test data and test labels](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data), extract it and put in the current directory.

4. Run it! This will output classification report like below. By default, it will evaluate on first 100 raws of the test data, which you can change in the code

    ```
                      precision    recall  f1-score   support

               0       0.99      0.76      0.86        94
               1       0.18      0.83      0.29         6

        accuracy                           0.76       100
       macro avg       0.58      0.79      0.57       100
    weighted avg       0.94      0.76      0.82       100    
    ```
