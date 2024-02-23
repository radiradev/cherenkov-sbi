# SBI for Water Cherenkov Detectors

Exploring the use of SBI to learn a likelihood function for events from a Water Cherenkov detector.

## Data 
On perlmutter currently it's in `/global/cfs/cdirs/dune/users/rradev/sbi/WCSim_mu-_npztoh5_test.h5`
It is in `hdf5` format and contains the following fields:

- `directions` - 3 momentum of the incoming particle
- `energies` - energy of the incoming particle
- `event_data` - (charge, time) from unrolled barrel of the detector 

- `event_data_{top, bottom}` - (charge, time) from caps of the detector

- `labels` - label corresponding to particle class 
- `mask` - mask out pixels that are outside of the caps (applying the mask returns a circle)
- `pids` - pid of the particle
- `positions` - vertex of event

## Issues with current representation
- Not adhering the to the symmetry of the problem - should exploit cylindrical symmetry. Big problem could be the discontinuities cause by unrolling the barrel. 