# Do not RUN - Just for Sample
# data is dataframe

def findInitialN(data):
    d = data.shape[1]
    if d<8: return d
    elif d>=8 and d<30 : return int(d*0.8)
    else: return int(d*0.7)


def validateIndices(indices,data):
    initial_n = findInitialN(data)
    d = data.shape[1]

    if initial_n<8:
        if indices>1 and indices<7:
            return indices

    elif initial_n>=8 and initial_n<24 : 
        if indices>d*0.3 and indices<d*0.8:
            return indices

    else:
        if indices>d*0.2 and indices<d*0.7:
            return indices

# Select columns with features only
features = data.drop(target, axis=1)

n = findInitialN(data)

# Perform PCA
pca = PCA(n_components=n)  # You can adjust the number of components as needed
pca_result = pca.fit_transform(features)

def validatePCA(pca):
    coverage = 0
    indices = 0
    for i in pca.explained_variance_ratio_:
        coverage += i*100
        indices += 1
        if coverage > 95:
            break
    validate = validateIndices(indices,data)
    if validate == true:
        return indices
    else:
        return 0

new_n = validatePCA(pca)

if new_n == 0:
   exit()
else:
    pca = PCA(n_components=new_n)  # You can adjust the number of components as needed
    pca_result = pca.fit_transform(features)
    # Add PCA results back to the dataset
    for i in range(new_n):
        data['PCA'+str(i+1)] = pca_result[:, i]

    # Drop original feature columns
    data = data.drop(features.columns, axis=1)

# use data variable for further analysis