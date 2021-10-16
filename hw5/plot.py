import matplotlib.pyplot as plt

latency = [21.26, 16.43, 0.252]
DSP = [3, 8, 320]
BRAM = [76, 76, 300]
plt.plot(latency, DSP, 'C0', lw = 2)
plt.scatter(latency, DSP, marker = '*', s = 120)
# plt.text(latency[0], DSP[0], 'baseline')
# plt.text(latency[1], DSP[1], 'unroll')
# plt.text(latency[2], DSP[2], 'pipeline')
plt.plot(latency, BRAM, 'C1', lw = 2)

plt.scatter(latency, BRAM, marker = 'o', s = 120)
# plt.text(latency[0], BRAM[0], 'baseline')
# plt.text(latency[1], BRAM[1], 'unroll')
# plt.text(latency[2], BRAM[2], 'pipeline')
plt.xlabel("latency(ms)")
plt.ylabel("# of DSP/BRAM")
plt.legend(labels=['DSP', 'BRAM'], loc='best')
plt.savefig('Q6')
plt.show()