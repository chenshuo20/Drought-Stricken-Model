# Build your model and solve the ODEs
We use the ODEs like below:
$$
\dot{x_i}=r_ix_i-\beta_ix_i(x_i+\sum_{j\neq i}\alpha_{ij}x_j)
$$
## Run your first model
To start the the program, you can run the such command:

```shell
git clone https://github.com/anepsilon/Drought-Stricken-Model.git
cd ode_solve
pip install numpy
pip install scipy
pip install matplotlib
```

And you can use the command to run your first model:

```shell
python run.py
```

Our file model.py contains the 3 model, respectively the number of the species are 1,3,5.
## Build your own model
To build your own model, you should add your own function in the ```model.py```. All the paraments can by changed in the function ```make_para()```
