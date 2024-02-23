
from torch.utils.data import Dataset
import h5py

class H5Dataset(Dataset):
    """
    - `directions` - 3 momentum of the incoming particle
    - `energies` - energy of the incoming particle
    - `event_data` - (charge, time) from unrolled barrel of the detector 
    - `event_data_{top, bottom}` - (charge, time) from caps of the detector
    - `labels` - label corresponding to particle class 
    - `mask` - mask out pixels that are outside of the caps (applying the mask returns a circle)
    - `pids` - pid of the particle
    - `positions` - vertex of event
    """
    def __init__(
            self, 
            h5_file='/global/cfs/cdirs/dune/users/rradev/sbi/WCSim_mu-_npztoh5_test.h5'
        ):
        self.file = h5py.File(h5_file, 'r')
        self.events = self.file['event_data']
        self.energy = self.file['energies']


    def __len__(self):
        return len(self.events)

    def __getitem__(self, idx):
        event_charge, _ = self.events[idx].T
        return event_charge, self.energy[idx]   


if __name__ == '__main__':
    ds = H5Dataset()
    print(ds[0])