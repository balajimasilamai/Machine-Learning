import pickle
file_name='finalized_model.sav'
loaded_model = pickle.load(open(file_name, 'rb'))
result = loaded_model.predict([[-0.869144323,0.389309751]])

print(result)
print (loaded_model.decision_function([[-0.869144323,0.389309751]]))
