import matplotlib.pyplot as plt
alphabet = "abcdefghijklmnopqrstuvwxyz"

# change plot title
plot_title = "Letter Frequency (Text 1)"

# change output file name
file_name = "output1.png"

# add text below
code = """

"""

letter_counts = [code.count(l) for l in alphabet]
letter_colors = plt.cm.hsv([0.8*i/max(letter_counts) for i in letter_counts])

plt.bar(range(26), letter_counts, color=letter_colors)
plt.xticks(range(26), alphabet) # letter labels on x-axis
plt.tick_params(axis="x", bottom=False) # no ticks, only labels on x-axis
plt.title(plot_title)
plt.savefig(file_name)