:

# SymbolicPhysicsLearner

### generate data
To generate training and testing datasets for Nguyen's benchmark problems, run
```
python regression_task/make_datasets.py --task=nguyen-1
```

## Run Model
Job configurations for Nguyen's benchmark problems are already included. To run experiments with Symbolic Physics Learner, use
```
import sys
import numpy as np
sys.path.append(r'../')
from spl_train import run_spl

output_folder = 'results_dump/' ## directory to save discovered results
save_eqs = True                ## if true, discovered equations are saved to "output_folder" dir

task = 'nguyen-1'
all_eqs, success_rate, all_times = run_spl(task, 
                                           num_run=100, 
                                           transplant_step=10000)
                                           
if save_eqs:
    output_file = open(output_folder + task + '.txt', 'w')
    for eq in all_eqs:
        output_file.write(eq + '\n')
    output_file.close()

print('success rate :', "{:.0%}".format(success_rate))
print('average discovery time is', np.round(np.mean(all_times), 3), 'seconds')                                          
```
To