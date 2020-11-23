# Molecular Orbital Theory
> Huckel theory for pi-molecular orbitals
> ### Theoretical references:
> Book refrence <a href="http://www.qfa.uam.es/qcomp/libros/l1.pdf">Computational Chemistry and Molecular Modeling</a>(Cha. 4)
> <a href="https://en.wikipedia.org/wiki/H%C3%BCckel_method">wikipedia</a><br>
> <a href="https://chem.libretexts.org/Bookshelves/Inorganic_Chemistry/Map%3A_Inorganic_Chemistry_(Housecroft)/04%3A_Experimental_techniques/4.13%3A_Computational_Methods/4.13C%3A_H%C3%BCckel_MO_Theory#:~:text=The%20H%C3%BCckel%20approximation%20is%20used,the%20the%20%CF%83%2Dbonding%20framework.">chem.libretexts.org</a><br>
> <a href="http://www.columbia.edu/itc/chemistry/chem-c2407_archive/recitations/huckel.pdf">columbia</a><br>
> ### Key words
> ***eigenvector,eigenvalue,state density,boundary condition,Conjugated***

From the <a href="https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation">Schrödinger</a> equation:

![equation](https://latex.codecogs.com/gif.latex?\hat{H}&space;\vert&space;\Psi_{i}&space;\rangle&space;=&space;E_{i}&space;\vert&space;\Psi_{i}&space;\rangle)

Where H is the Hamiltonian operator,<semantics><mstyle displaystyle="true" scriptlevel="0"><mi><em>&#x03C8;<!-- ψ --></em></mi></mstyle></semantics> is the state vector of the quantum system, and E is a constant equal to the energy level of the system (H is not dependent on time explicitly).

Since ***Huckel theory*** is a special consideration of molecular orbital theory, the molecular orbitals <semantics><mstyle displaystyle="true" scriptlevel="0"><mo fence="false" stretchy="false">|</mo><mi mathvariant="bold">&#x03C8;<!-- ψ --><sub>i</sub></mi><mo fence="false" stretchy="false"><em>&#x27E9;<!-- ⟩ --></em></mo></mstyle></semantics> can be discribed as a linear combination of the <em>2p<sub>z</sub></em> atomic orbitals <semantics><mstyle displaystyle="true" scriptlevel="0"><mi><em>&straightphi;<!-- ψ --></em></mi></mstyle></semantics> at carbon with their corresponding c coefficients:

![equation](https://latex.codecogs.com/gif.latex?{\psi_{i}}=\sum_{i=1}^{n}&space;c_{i}&space;\phi_{i})

So, the Huckel approximtion is used to determine the energies and shapes of the π molecular orbitals. In other words, the Huckel approximation assumes that the electrons in the π bonds "feel" an electrostatic potential due to the entire σ (sigma) bonding framework in the molecule.

### Hückel characteristics
- it limits itself to <a href="https://en.wikipedia.org/wiki/Conjugated_system">conjugated</a> hydrocarbons.
- Only <a href="https://en.wikipedia.org/wiki/Pi_bond">π electron</a> molecular orbitals are included because these determine much of the chemical and spectral properties of these molecules. The <a href="https://en.wikipedia.org/wiki/Sigma_bond">σ electrons</a> are assumed to form the framework of the molecule and σ connectivity is used to determine whether two π orbitals interact. However, the orbitals formed by σ electrons are ignored and assumed not to interact with π electrons. This is referred to as σ-π separability. It is justified by the orthogonality of σ and π orbitals in planar molecules. For this reason, the Hückel method is limited to systems that are planar or nearly so.
- The method is based on applying the <a href="https://en.wikipedia.org/wiki/Variational_method_(quantum_mechanics)">variational method</a> to <a href="https://en.wikipedia.org/wiki/Linear_combination_of_atomic_orbitals">linear combination of atomic orbitals</a> and making simplifying assumptions regarding the overlap, resonance and Coulomb integrals of these atomic orbitals. It does not attempt to solve the <a href="https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation">Schrödinger equation</a>, and neither the functional form of the basis atomic orbitals nor details of the <a href="https://en.wikipedia.org/wiki/Hamiltonian_(quantum_mechanics)">Hamiltonian</a> are involved.
- For hydrocarbons, the method takes atomic connectivity as the only input; empirical parameters are only needed when heteroatoms are introduced.
- The method predicts how many energy levels exist for a given molecule, which levels are <a href="https://en.wikipedia.org/wiki/Degenerate_energy_levels">degenerate</a> and it expresses the molecular orbital energies in terms of two parameters, called α, the energy of an electron in a 2p orbital, and β, the interaction energy between two 2p orbitals (the extent to which an electron is stabilized by allowing it to delocalize between two orbitals). The usual sign convention is to let both α and β be negative numbers. To understand and compare systems in a qualitative or even semi-quantitative sense, explicit numerical values for these parameters are typically not required.
- In addition the method also enables calculation of <a href="https://en.wikipedia.org/wiki/Charge_density">charge density</a> for each atom in the π framework, the fractional <a href="https://en.wikipedia.org/wiki/Bond_order">bond order</a> between any two atoms, and the overall <a href="https://en.wikipedia.org/wiki/Dipole#Molecular_dipoles">molecular dipole moment</a>.

***For linear and cyclic systems (with N atoms), general solution exist:***
- Linear system:  

![equation](https://latex.codecogs.com/gif.latex?{\displaystyle&space;E_{k}=\alpha&space;&plus;2\beta&space;\cos&space;{\frac&space;{(k&plus;1)\pi&space;}{N&plus;1}}\quad&space;(k=0,1,\ldots&space;,N-1)})

- Cyclic system:

 ![equation](https://latex.codecogs.com/gif.latex?{\displaystyle&space;E_{k}=\alpha&space;&plus;2\beta&space;\cos&space;{\frac&space;{2k\pi&space;}{N}}\quad&space;(k=0,1,\ldots&space;,\lfloor&space;N/2\rfloor&space;)})

 ***The values of α and β***<br>
 The value of α is the energy of an electron in a 2p orbital, relative to an unbound electron at infinity. This quantity is negative, since the electron is stabilized by being electrostatically bound to the positively charged nucleus. For carbon this value is known to be approximately –11.4 eV. Since Hückel theory is generally only interested in energies relative to a reference localized system, the value of α is often immaterial and can be set to zero without affecting any conclusions. Roughly speaking, β physically represents the energy of stabilization experienced by an electron allowed to delocalize in a π molecular orbital formed from the 2p orbitals of adjacent atoms, compared to being localized in an isolated 2p atomic orbital. As such, it is also a negative number, although it is often spoken of in terms of its absolute value.<hr>

# Code configuration

All calculations for obtaining energy and coefficients (Molecule and a and b) are expressed in two general coding structures [Huckel.py](https://github.com/SMNIK/Molecular-Orbital-Theory/Huckel.py) and [graphene.py](https://github.com/SMNIK/Molecular-Orbital-Theory/graphene.py).<br>
Then, for a general view of the various structural states and lattice energy connections of carbon, [Zigzag.py](https://github.com/SMNIK/Molecular-Orbital-Theory/Zigzag.py), [Armchair.py](https://github.com/SMNIK/Molecular-Orbital-Theory/Armchair.py), and [nanotube.py](https://github.com/SMNIK/Molecular-Orbital-Theory/nanotube.py) are used, which we will examine below.



1. The [Huckel.py](https://github.com/SMNIK/Molecular-Orbital-Theory/Huckel.py) file involves the basic configuration for manipulating the structure of our H matrix. The functional operator inside this file works as the pi-molecular orbitals builder. As a Huckel theory for pi-molecular orbitals, for a given Huckel matrix, with Alpha diagonals and Beta off-diagonals, we will determine the Eigenvalues and Eigenvectors. For the Huckel Effective Hamiltonian and use them to create an energy level diagram for the electronic configuration of the molecule. For the short and long leg of the triangle shape, we need two coefficients to use for the matrix elements; So, first generalize the symbols that we can use them in our fancy matrix (here a and b). Molecule class represents	a molecule with a Huckel matrix and associated methodes and inside associate the Eigenvalues. As I said inside the theoretical structure at the first of this repository, Alpha and Beta are mandatory coefficients to calculate the enery of each levels([wikipedia](https://en.wikipedia.org/wiki/H%C3%BCckel_method">wikipedia))
As an example of generation of H matrix for linear carbon chain, look at this:
```python
    def generate_H(self):
        N = self.num_carbons
        H = np.zeros((N, N)).tolist()
        
        for i in range(N):
            H[i][i] = a
            if i==0:
                H[i][i+1] = b
            elif i == N - 1:
                H[i][i-1] = b
            else:
                H[i][i+1] = b
                H[i][i-1] = b
        self.H = np.matrix(H)
```
Later than generarting the H matrix, there needs the arm connections between carbon atoms. So, adds connection (con) to the Huckel matrix, take a list of lists and inserts beta into H at the specified cordinates. Now, it is time to find the eigenvalue and eigenvector for the H matrix. Then for a more deep view of code structure, you can look at the code ([Huckel.py](https://github.com/SMNIK/Molecular-Orbital-Theory/Huckel.py)), line by line, there is a short explanation for each part.

2. For the basic construction of carbon modulation, we need imagine one of the carbon lattice structure to evaluate the molecule paramiters. It depends to the materials and chanis of molecules that later you will use for. According to the materials that I want to explaine, I consider the [Graphene.py](https://github.com/SMNIK/Molecular-Orbital-Theory/Graphene.py) lattice stracture. So, we extend our molecule class to be able to calculate the various properties of types of Graphene.
Absolutely, inside the chain, we need to identify the carbons' atoms.
```python
self.id = id
```
Then, listed the carbon atoms and stores the id of the most recently generated carbon; The same for row of hexagones that the most recently generated carbon belongs to.
```python
class Graphene(Molecule):
    def __init__(self, *args):
        super(Graphene, self).__init__(*args)
        self.carbons = []
        self.prev_id = 0
        self.current_row = 1
```
For the generating graphene, the molecule shape is hexagonal, for this, by considering two elements as the rows and columns and then create the linking carbons lines, you could shape your hexagon structure of graphene. Look at the code for more information.

3. In the third part I use nanotube for testing the Huckel and Graphene codes. Besides, for calculating the charge density and delocalization energy. First, the nanotube needs armchair for correct connections between atoms. As you see inside the [testing-nanotube.py](https://github.com/SMNIK/Molecular-Orbital-Theory/testing-nanotube.py) file, for nanotube, the structure will be closed after 42 atoms. For more cells you could generate more connections. Finaly, for this part you could plot them and print the results. However, I left the seperates files of nanotube for who wants to change them.

![image](https://github.com/SMNIK/Molecular-Orbital-Theory/blob/master/images/testing-nanotube.png)

4. Now for testing the zigzag connections of carbos' atoms, I prepaired the file [testing-zigzag.py](https://github.com/SMNIK/Molecular-Orbital-Theory/testing-zigzag.py) which include the zigzag connections and plots (that I left the seperate files for who wants to change).

![image](https://github.com/SMNIK/Molecular-Orbital-Theory/blob/master/images/testing-zigzag.png)
