from numpy import *
import matplotlib.pyplot as plt
from collections import Counter
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in malesuada quam. Nam vitae augue non urna egestas malesuada ut at turpis. Phasellus quis neque vitae odio tempor suscipit vel ac velit. Proin sagittis rutrum lectus, a pulvinar massa sollicitudin sed. Integer euismod ullamcorper lacus, id egestas velit vestibulum vitae. Morbi accumsan nunc ac nunc euismod dapibus. Nulla sit amet accumsan nibh. Mauris tempor sem ut vulputate pretium. Etiam justo neque, lobortis nec pretium vel, consectetur dictum urna. Sed at diam vel nisi egestas tempor. Ut augue nulla, consectetur eget aliquet non, maximus at justo. Aliquam egestas lacus augue, eu sodales tortor mollis at. Proin porttitor hendrerit nulla in maximus. In sed velit sed ante molestie gravida eu at justo."
labels, values = zip(*Counter(text).items())
indexes = arange(len(labels))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.savefig('graph.png', dpi=200)