import numpy as np
import pandas as pd

# Load labels
labelf = 'fs_gm.csv'
labeldf = pd.read_csv(labelf, names=['RegionName','Label'])
roinames = labeldf.RegionName.values

# Generate fake pet data
subjects = ['Subject_%s' % (n) for n in range(1, 15)]
# PIB-PET
sub_df = pd.DataFrame(np.random.permutation(subjects)[:10], columns=['Subject'])
pib_pet_dat = np.random.gamma(shape=2., scale=0.5, size=800).reshape(10,80)
pib_pet_df = pd.concat([sub_df, pd.DataFrame(pib_pet_dat, columns=roinames)], axis=1)
pib_pet_df.to_excel('fake_pib_pet_data.xlsx')
# FDG-PET
sub_df = pd.DataFrame(np.random.permutation(subjects)[:8], columns=['Subject'])
fdg_pet_dat = np.random.gamma(shape=2., scale=0.5, size=640).reshape(8,80)
fdg_pet_df = pd.concat([sub_df, pd.DataFrame(fdg_pet_dat, columns=roinames)], axis=1)
fdg_pet_df.to_excel('fake_fdg_pet_data.xlsx')