import os

R = 20
F = 25
N = 200

loop = 201
start = 198
node_no = 2
for i in range(start,loop):
    print(i)
    log_filename = "logLmp_"+ str(i-1)+ ".dat"
    jobname = "i_"+str(i)+"n_"+str(N)+"f_"+str(F)+"r_"+str(R)
    # Write submit file
    filename = "submit_restart.sh"
    f = open(filename, "w")
    f.write('#!/bin/bash\n')
    f.write('#SBATCH -A p32010\n')
    f.write('#SBATCH -p short\n')
    f.write('#SBATCH -N '+str(node_no)+'\n')
    f.write('#SBATCH --ntasks-per-node=28\n')
    f.write('#SBATCH -t 3:59:59\n')
    f.write('#SBATCH --job-name="'+jobname+'"\n')
    f.write('module purge\n')
    f.write('module load mpi/openmpi-4.1.1-gcc.10.2.0 gcc/9.2.0 hdf5/1.8.10 fftw/3.3.8-openmpi-4.0.5-gcc-10.2.0\n')
    if i == 1:
        input_script = "generation.in"
        datafile = "reduced_fcc_R"+str(R)+"_F"+str(F)+"_N"+str(N)+".data"
        f.write('mpirun -np '+str(28*node_no)+' /home/spu8516/lammps2022Apr/build_quartic2/lmp -in '+input_script+' > '+log_filename+' -var input_data '+datafile+'\n')
    elif i < 26:
        input_script = "equilibrium_restart.in"
        f.write('mpirun -np '+str(28*node_no)+' /home/spu8516/lammps2022Apr/build_quartic2/lmp -in '+input_script+' > '+log_filename+'\n')
    else:
        input_script = "equilibrium_restart_1.in"
        f.write('mpirun -np '+str(28*node_no)+' /home/spu8516/lammps2022Apr/build_quartic2/lmp -in '+input_script+' > '+log_filename+'\n')   
    f.close()
    if i == start:
        os.system("sbatch submit_restart.sh")
    else:
        os.system("sbatch -d afterok:$(squeue --noheader --format %i --name "+last_jobname+") submit_restart.sh")
    last_jobname = jobname
    