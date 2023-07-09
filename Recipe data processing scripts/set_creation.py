import pandas as pd
recipes = pd.read_pickle("processed_recipes.pkl")
train_set = recipes[:10000].combined.values
with open('train.txt', 'w') as f:
    f.write('\n'.join(train_set))
    
