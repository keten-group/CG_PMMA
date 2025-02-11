# CG_PMMA
LAMMPS model for coarse grained PMMA

# LAMMPS datafile
CG_PMMA_M100_150_chain.data - PMMA with CG beads generated using self-avoiding random walk algorithm. The system consists of 150 chain, each having 100 monomers.

More details about the CG parameters can be found - 
Hsu, David D., et al. "Systematic method for thermomechanically consistent coarse-graining: a universal model for methacrylate-based polymers." Journal of chemical theory and computation 10.6 (2014): 2514-2527.

# Equilibration
The equlibration of the CG PMMA is done through three steps.
1. generation.in - Initially a soft potential is turned on to remove any kind of overlapping. After that consecutive NPT ensembles are used to equilibrate the density of the system at high pressure and tmeperature.
2. equilibrium_restart.in - Multiple long NVT cycles with truncated LJ potential are used to extend polymer chains.
3. equilibrium_restart_1.in -  Multiple long NVT cycles with full LJ potential are used to extend polymer chains.

Note - MSID of the polymer chains are used to establish adequate equilibration.

More details about the process can be found - 
Wu, Zhenghao, Subhadeep Pal, and Sinan Keten. "Implicit Chain Particle Model for Polymer-Grafted Nanoparticles." Macromolecules 56.9 (2023): 3259-3271.

Auhl, Rolf, et al. "Equilibration of long chain polymer melts in computer simulations." The Journal of chemical physics 119.24 (2003): 12718-12728.
