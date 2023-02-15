<!-- # Calculate-Protein-Mass-with-Python
Author: Hajer Abbas
Calculate Protein Mass
Abstract: Proteins control the basic processes of life, and the beautiful and varied ways in which they do this have been the 
focus of much biomedical research for the past 50 years. What bioinformatics stands for is the use of the Machine Learning 
model in biological systems analysis, and this paper will represent a process using the Machine Learning model to quantify 
the protein sequence. Using a program as a method, we were able to calculate the protein sequence. What this program aims 
to do, is to take the protein sequence as an input, and return its mass as an input. We achieved the same results, which are the 
protein mass as an output, by testing the program several times, providing the protein sequence as an input. This paper clearly 
demonstrated how we easily measured protein mass by using the Machine Learning model but also raised a question about 
what progress bioinformatics can achieve. Further studies could address more complex methods that give a better analysis of 
biological molecules.

Introduction 
The basic processes of life are regulated by proteins, and for the past 50 years, the beautiful and varied 
ways in which they do this have been the subject of much biomedical study. The ability for protein-based materials 
is to address a huge array of technological challenges. Functions mediated by naturally occurring proteins include 
the use of solar energy to generate complex molecules; ultrasensitive detection of small molecules (olfactory 
receptors) and light (rhodopsin); the conversion of pH gradients into chemical bonds (ATP synthase); and the 
conversion of chemical energy into working energy (ATP synthase) (actin and myosin). These functions are not 
only exceptional but are encoded with the intense economy in amino acid sequences. The three-dimensional 
structure of the proteins is defined by such sequences, and the spontaneous folding into these structures of 
extended polypeptide chains is the simplest case of biological self-organization. Despite the technological 
advancements of the last 100 years, human-made devices cannot compete with the nano-scale accuracy of protein 
function and cannot be created by self-assembly.
To help protein design and engineering, Machine Learning. has been used to predict protein properties 
from protein sequences. The Machine Learning models are useful because they do not need such knowledge of 
particular physical or biological mechanisms to predict the effects of complex processes, such as how a protein 
sequence encodes structure. Instead, Machine Learning models infer the properties of unseen sequences after 
practicing with calculated sequences. A model able to predict the properties of unseen protein sequences allows 
sequences with ideal properties to be predicted and discovered. We must encode the protein sequence in a manner 
consistent with the mathematical operations used in the Machine Learning models in order for the Machine 
Learning models to learn about protein sequences. This usually needs the protein sequence to be encoded as a 
numeric vector or matrix. What can be learned decides how each protein sequence is encoded. If incorrect 
encoding is used, even the most powerful models yield bad results. We demonstrate that learning these data 
encodings will streamline machine-learning pipelines while achieving high predictive precision. 
Using the Machine Learning model in analyzing biological systems is what bioinformatics stands for, 
and This paper will represent a method to calculate protein sequence using the Machine Learning model. 
Methodology
Using the following program, we will be able to calculate the protein sequence. What this program aims to do, is 
to take the protein sequence as an input, and return its mass as an output.
The program will take the input and apply some analysis to it in order to return the desired output.
prot = input('Enter protein sequence:')
mss = {
 'G': 57.02146,
 'A': 71.03711,
 'S': 87.03203,
 'P': 97.05276,
 'V': 99.06841,
 'T': 101.04768,
 'C': 103.00919,
 'L': 113.08406,
 'I': 113.08406,
 'N': 114.04293,
 'D': 115.02694,
 'Q': 128.05858,
 'K': 128.09496,
 'E': 129.04259,
 'M': 131.04049,
 'H': 137.05891,
 'F': 147.06841,
 'U': 150.95364,
 'R': 156.10111,
 'Y': 163.06333,
 'W': 186.07931,
 'O': 237.14773,
}
def calculate(mass):
 final = 0
 mass = list(mass)
 for i in mass:
 amount = mss.get(i)
 final += amount
 return final
print(calculate(prot))
What we did in this program that we took the input which is the protein, and we built a dictionary in the program 
that links each amino acid with its mass. The program takes the protein string as an input, converts it into a list, 
then takes each amino acid in a loop that takes each amino acid value and adds it to a variable. In each round, we 
reassign the value of this variable by adding the next amino acid mass. The final output is the sum of all amino 
acid values. Finally, the program prints out the protein mass.
Results 
Input: SKADYEK
Output: 821.3919199999999
The program took the protein sequence as input then replaced each amino acid with its mass, then sum them 
together to give us the protein mass as an output.
By testing this program many times, we get the same results which are the protein mass as an output, providing 
the protein sequence as an input. So, as you can see it is much simpler and more precise to use this model to 
measure protein mass, and that is why bioinformatics is considered a very important field to be studied.
Conclusion 
This paper clearly shows how by using the Machine Learning model, we calculated protein mass easily, 
but also raises a question that what progress bioinformatic can reach? And what abilities this progress would assist 
us to have. Proteins are an extremely important molecule in our bodies that we cannot survive without, and by 
analyzing it accurately, we will get more benefits. And that is the reason why we used the Machine Learning 
model. Further studies could address more complex methods that give a better analysis of biological molecules 
and may provide us an artificial intelligence environment that gives an accurate result of how this molecule would 
behave, or analyzing its structure in a 3D environment. Making progress in studying these molecules using the 
Machine Learning model, will lead us to a better understanding and discoveries in this field.
References
Arnold, F. H. (2015). The nature of chemical innovation: New enzymes by evolution. Quarterly 
Reviews of Biophysics, 48(4), 404–410. https://doi.org/10.1017/S003358351500013X
Chen, C., Huang, H., & Wu, C. H. (2017). Protein Bioinformatics Databases and Resources. Methods in 
Molecular Biology (Clifton, N.J.), 1558, 3–39. https://doi.org/10.1007/978-1-4939-6783-4_1
Huang, P.-S., Boyken, S. E., & Baker, D. (2016). The coming of age of de novo protein design. Nature, 
537(7620), 320–327. https://doi.org/10.1038/nature19946
Karaca, E., Melquiond, A. S. J., de Vries, S. J., Kastritis, P. L., & Bonvin, A. M. J. J. (2010). Building 
macromolecular assemblies by information-driven docking: Introducing the HADDOCK 
multibody docking server. Molecular & Cellular Proteomics : MCP, 9(8), 1784–1794. 
https://doi.org/10.1074/mcp.M000051-MCP201
Yang, K. K., Wu, Z., Bedbrook, C. N., & Arnold, F. H. (2018). Learned protein embeddings for machine 
learning. Bioinformatics (Oxford, England), 34(15), 2642–2648. 
https://doi.org/10.1093/bioinformatics/bty178
_________ -->
