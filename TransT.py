import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import math 

def get_positional_encoding(max_seq_len,embed_dim):
	positional_encoding = np.array([
		[pos / np.power(10000,2*i/embed_dim) for i in range(embed_dim)]
		if pos != 0 else np.zeros(embed_dim) for pos in range(max_seq_len)])

	positional_encoding[1:,0::2] = np.sin(positional_encoding[1:,0::2])
	positional_encoding[1:,1::2] = np.cos(positional_encoding[1:,1::2])
	return positional_encoding

positional_encoding = get_positional_encoding(max_seq_len=100,embed_dim=16)
plt.figure(figsize=(10,10))
sns.heatmap(positional_encoding)
plt.title("Sinusoidal Function")
plt.xlabel("hidden dimension")
plt.ylabel("sequence length")

plt.savefig("./test1.jpg")
plt.figure(figsize=(8, 5))
plt.plot(positional_encoding[1:, 1], label="dimension 1")
plt.plot(positional_encoding[1:, 2], label="dimension 2")
plt.plot(positional_encoding[1:, 3], label="dimension 3")
plt.legend()
plt.xlabel("Sequence length")
plt.ylabel("Period of Positional Encoding")
plt.savefig("./test2.jpg")
plt.pause(6)