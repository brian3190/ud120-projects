def doPCA():
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca

pca = doPCA()
print pca.explained_variance_ratio_
first_pc = pca.components_[0]
second_pc = pca.components_[1]

transformed_data = pca.transform(data)
for ii, jj in zip(transformed_data, data):
    plt.scatter( first_pc[0]*ii[0], first_pc[1]*ii[0], color="r")
    plt.scatter( second_pc[0]*ii[1], second_pc[1]*ii[1], color="c")

plt.xlabel("bonus")
plt.ylabel("long-term-incentive")
plt.show()
