# import dependencies
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# page title
st.set_page_config(page_title="Fasta_Sequence_Analysis")
image = Image.open('logo.png')
st.image(image)

st.write("""
# FASTA SEQUENCE ANALYSIS
         
This app counts the nucleotide composition of query Sequence !
         
***
         
""")
st.subheader("What is FASTA Format? ")
st.write("""FASTA format is a text-based format for representing either nucleotide sequences or peptide sequences, in which base pairs or amino acids are represented using single-letter codes. A sequence in FASTA format begins with a single-line description, followed by lines of sequence data. The description line is distinguished from the sequence data by a greater-than (" >") symbol in the first column. It is recommended that all lines of text be shorter than 80 characters in length.""")

st.write("""
***
""")
# input text box
st.header('Enter The Sequence')
sequence_input = "Enter your sequence here..."

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write("""
***
""")

st.write("""
The nucleic acid codes are:

        A --> adenosine           M --> A C (amino)
        C --> cytidine            S --> G C (strong)
        G --> guanine             W --> A T (weak)
        T --> thymidine           B --> G T C
        U --> uridine             D --> G A T
        R --> G A (purine)        H --> A C T
        Y --> T C (pyrimidine)    V --> G C A
        K --> G T (keto)          N --> A G C T (any)
                                  -  gap of indeterminate length
         """)

st.write("""
***
""")
# print the input sequence
st.header("INPUT SEQUENCE ")
sequence

st.write("""
***
""")

# nucleotide count
st.header("OUTPUT(SEQUENCE ANALYSIS)")

# print dictionary


def nucleotide_count(seq):
    nucleotide = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
        ('U', seq.count('U')),
        ('R', seq.count('R')),
        ('Y', seq.count('Y')),
        ('K', seq.count('K')),
        ('M', seq.count('M')),
        ('S', seq.count('S')),
        ('B', seq.count('B')),
        ('D', seq.count('D')),
        ('H', seq.count('H')),
        ('V', seq.count('V')),
        ('N', seq.count('N'))
    ])
    return nucleotide


x = nucleotide_count(sequence)


# dispaly dataframe
st.subheader('DISPLAY NUCLEOTIDE COUNT')
df = pd.DataFrame.from_dict(x, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

st.write("""
***
""")

# display barchart
st.subheader("BAR CHART")
barchart = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
barchart = barchart.properties(
    width=alt.Step(80)
)
st.write(barchart)

st.write("""
***
""")

st.write("""
The accepted amino acid codes are:
         
            A ALA alanine                         P PRO proline
            B ASX aspartate or asparagine         Q GLN glutamine
            C CYS cystine                         R ARG arginine
            D ASP aspartate                       S SER serine
            E GLU glutamate                       T THR threonine
            F PHE phenylalanine                   U     selenocysteine
            G GLY glycine                         V VAL valine
            H HIS histidine                       W TRP tryptophan
            I ILE isoleucine                      Y TYR tyrosine
            K LYS lysine                          Z GLX glutamate or glutamine
            L LEU leucine                         X     any
            M MET methionine                      *     translation stop
            N ASN asparagine                      -     gap of indeterminate length
            """)

st.write("""
***
""")

st.write("""
## SUMMARY
         """)
st.write('There are ' + str(x['A'])+' Adenine(A)')
st.write('There are ' + str(x['T'])+' Thymine(T)')
st.write('There are ' + str(x['G'])+' Guanine(G)')
st.write('There are ' + str(x['C'])+' Cytosine(C)')
