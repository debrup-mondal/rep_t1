import streamlit as st

# Draw a title and some text to the app:
"""
# This is the document title

This is some _markdown_.
"""

import pandas as pd

df = pd.DataFrame({"col1": [1, 2, 3]})
df  # 👈 Draw the dataframe

x = 10
"x", x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart


def get_user_name():
    return "John"


with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return "!!!"

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = "bar"
st.write("Done!")


import streamlit as st
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

my_table = st.table(df1)

df2 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

my_table.add_rows(df2)
# Now the table shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
my_chart.add_rows(df2)
# Now the chart shown in the Streamlit app contains the data for
# df1 followed by the data for df2.


import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.line_chart(df)

for tick in range(10):
    time.sleep(0.5)
    add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
    my_data_element.add_rows(add_df)

st.button("Regenerate")


import streamlit as st

animal_shelter = ["cat", "dog", "rabbit", "bird"]

animal = st.text_input("Type an animal")

if st.button("Check availability"):
    have_it = animal.lower() in animal_shelter
    "We have that animal!" if have_it else "We don't have that animal."


import streamlit as st

if "clicked" not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


st.button("Click me", on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write("Button clicked!")
    st.slider("Select a value")
