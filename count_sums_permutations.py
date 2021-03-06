from matplotlib import pyplot as plt

vals = []
counts = []
for n in range(100,300):
	count=0
	for x in range(10,100):
		for y in range(10,100):
			for z in range(10,100):
				if x + y + z == n:
					count+=1
	vals.append(n)
	counts.append(count)
	
plt.plot(vals, counts)
plt.show()

for i,n in zip(vals, counts):
	print(i, " : ", n)


'''
100  :  2556
101  :  2628
102  :  2701
103  :  2775
104  :  2850
105  :  2926
106  :  3003
107  :  3081
108  :  3160
109  :  3240
110  :  3321
111  :  3403
112  :  3486
113  :  3570
114  :  3655
115  :  3741
116  :  3828
117  :  3916
118  :  4005
119  :  4095
120  :  4183
121  :  4269
122  :  4353
123  :  4435
124  :  4515
125  :  4593
126  :  4669
127  :  4743
128  :  4815
129  :  4885
130  :  4953
131  :  5019
132  :  5083
133  :  5145
134  :  5205
135  :  5263
136  :  5319
137  :  5373
138  :  5425
139  :  5475
140  :  5523
141  :  5569
142  :  5613
143  :  5655
144  :  5695
145  :  5733
146  :  5769
147  :  5803
148  :  5835
149  :  5865
150  :  5893
151  :  5919
152  :  5943
153  :  5965
154  :  5985
155  :  6003
156  :  6019
157  :  6033
158  :  6045
159  :  6055
160  :  6063
161  :  6069
162  :  6073
163  :  6075
164  :  6075
165  :  6073
166  :  6069
167  :  6063
168  :  6055
169  :  6045
170  :  6033
171  :  6019
172  :  6003
173  :  5985
174  :  5965
175  :  5943
176  :  5919
177  :  5893
178  :  5865
179  :  5835
180  :  5803
181  :  5769
182  :  5733
183  :  5695
184  :  5655
185  :  5613
186  :  5569
187  :  5523
188  :  5475
189  :  5425
190  :  5373
191  :  5319
192  :  5263
193  :  5205
194  :  5145
195  :  5083
196  :  5019
197  :  4953
198  :  4885
199  :  4815
200  :  4743
201  :  4669
202  :  4593
203  :  4515
204  :  4435
205  :  4353
206  :  4269
207  :  4183
208  :  4095
209  :  4005
210  :  3916
211  :  3828
212  :  3741
213  :  3655
214  :  3570
215  :  3486
216  :  3403
217  :  3321
218  :  3240
219  :  3160
220  :  3081
221  :  3003
222  :  2926
223  :  2850
224  :  2775
225  :  2701
226  :  2628
227  :  2556
228  :  2485
229  :  2415
230  :  2346
231  :  2278
232  :  2211
233  :  2145
234  :  2080
235  :  2016
236  :  1953
237  :  1891
238  :  1830
239  :  1770
240  :  1711
241  :  1653
242  :  1596
243  :  1540
244  :  1485
245  :  1431
246  :  1378
247  :  1326
248  :  1275
249  :  1225
250  :  1176
251  :  1128
252  :  1081
253  :  1035
254  :  990
255  :  946
256  :  903
257  :  861
258  :  820
259  :  780
260  :  741
261  :  703
262  :  666
263  :  630
264  :  595
265  :  561
266  :  528
267  :  496
268  :  465
269  :  435
270  :  406
271  :  378
272  :  351
273  :  325
274  :  300
275  :  276
276  :  253
277  :  231
278  :  210
279  :  190
280  :  171
281  :  153
282  :  136
283  :  120
284  :  105
285  :  91
286  :  78
287  :  66
288  :  55
289  :  45
290  :  36
291  :  28
292  :  21
293  :  15
294  :  10
295  :  6
296  :  3
297  :  1
298  :  0
299  :  0
'''