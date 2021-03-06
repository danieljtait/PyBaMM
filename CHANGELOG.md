# [Unreleased](https://github.com/pybamm-team/PyBaMM)

## Features

-   Added `DummySolver` for empty models ([#915](https://github.com/pybamm-team/PyBaMM/pull/915))
-   Added functionality to broadcast to edges ([#891](https://github.com/pybamm-team/PyBaMM/pull/891))
-   Reformatted and cleaned up `QuickPlot` ([#886](https://github.com/pybamm-team/PyBaMM/pull/886))
-   Added thermal effects to lead-acid models ([#885](https://github.com/pybamm-team/PyBaMM/pull/885))
-   Add new symbols `VariableDot`, representing the derivative of a variable wrt time, 
    and `StateVectorDot`, representing the derivative of a state vector wrt time 
    ([#858](https://github.com/pybamm-team/PyBaMM/issues/858))
-   Added additional notebooks showing how to create and compare models ([#877](https://github.com/pybamm-team/PyBaMM/pull/877))
-   Added `Minimum`, `Maximum` and `Sign` operators
    ([#876](https://github.com/pybamm-team/PyBaMM/pull/876))
-   Added a search feature to `FuzzyDict` ([#875](https://github.com/pybamm-team/PyBaMM/pull/875))
-   Add ambient temperature as a function of time ([#872](https://github.com/pybamm-team/PyBaMM/pull/872))
-   Added `CasadiAlgebraicSolver` for solving algebraic systems with CasADi ([#868](https://github.com/pybamm-team/PyBaMM/pull/868))
-   Added electrolyte functions from Landesfeind ([#860](https://github.com/pybamm-team/PyBaMM/pull/860))

## Bug fixes

-   Fixed bug raised if function returns a scalar ([#919](https://github.com/pybamm-team/PyBaMM/pull/919))
-   Fixed event handling in `ScipySolver` ([#905](https://github.com/pybamm-team/PyBaMM/pull/905))
-   Made input handling clearer in solvers ([#905](https://github.com/pybamm-team/PyBaMM/pull/905))
-   Updated Getting started notebook 2 ([#903](https://github.com/pybamm-team/PyBaMM/pull/903))
-   Reformatted external circuit submodels ([#879](https://github.com/pybamm-team/PyBaMM/pull/879))
-   Some bug fixes to generalize specifying models that aren't battery models, see [#846](https://github.com/pybamm-team/PyBaMM/issues/846)
-   Reformatted interface submodels to be more readable ([#866](https://github.com/pybamm-team/PyBaMM/pull/866))
-   Removed double-counted "number of electrodes connected in parallel" from simulation ([#864](https://github.com/pybamm-team/PyBaMM/pull/864))

## Breaking changes

-   Changed keyword argument `u` for inputs (when evaluating an object) to `inputs` ([#905](https://github.com/pybamm-team/PyBaMM/pull/905))
-   Removed "set external temperature" and "set external potential" options. Use "external submodels" option instead ([#862](https://github.com/pybamm-team/PyBaMM/pull/862))

# [v0.2.0](https://github.com/pybamm-team/PyBaMM/tree/v0.2.0) - 2020-02-26

This release introduces many new features and optimizations. All models can now be solved using the pip installation - in particular, the DFN can be solved in around 0.1s. Other highlights include an improved user interface, simulations of experimental protocols (GITT, CCCV, etc), new parameter sets for NCA and LGM50, drive cycles, "input parameters" and "external variables" for quickly solving models with different parameter values and coupling with external software, and general bug fixes and optimizations.

## Features

-   Added LG M50 parameter set ([#854](https://github.com/pybamm-team/PyBaMM/pull/854))
-   Changed rootfinding algorithm to CasADi, scipy.optimize.root still accessible as an option ([#844](https://github.com/pybamm-team/PyBaMM/pull/844))
-   Added capacitance effects to lithium-ion models ([#842](https://github.com/pybamm-team/PyBaMM/pull/842))
-   Added NCA parameter set ([#824](https://github.com/pybamm-team/PyBaMM/pull/824))
-   Added functionality to `Solution` that automatically gets `t_eval` from the data when simulating drive cycles and performs checks to ensure the output has the required resolution to accurately capture the input current ([#819](https://github.com/pybamm-team/PyBaMM/pull/819))
-   Added `Citations` object to print references when specific functionality is used ([#818](https://github.com/pybamm-team/PyBaMM/pull/818))
-   Updated `Solution` to allow exporting to matlab and csv formats ([#811](https://github.com/pybamm-team/PyBaMM/pull/811))
-   Allow porosity to vary in space ([#809](https://github.com/pybamm-team/PyBaMM/pull/809))
-   Added functionality to solve DAE models with non-smooth current inputs ([#808](https://github.com/pybamm-team/PyBaMM/pull/808))
-   Added functionality to simulate experiments and testing protocols ([#807](https://github.com/pybamm-team/PyBaMM/pull/807))
-   Added fuzzy string matching for parameters and variables ([#796](https://github.com/pybamm-team/PyBaMM/pull/796))
-   Changed ParameterValues to raise an error when a parameter that wasn't previously defined is updated ([#796](https://github.com/pybamm-team/PyBaMM/pull/796))
-   Added some basic models (BasicSPM and BasicDFN) in order to clearly demonstrate the PyBaMM model structure for battery models ([#795](https://github.com/pybamm-team/PyBaMM/pull/795))
-   Allow initial conditions in the particle to depend on x ([#786](https://github.com/pybamm-team/PyBaMM/pull/786))
-   Added the harmonic mean to the Finite Volume method, which is now used when computing fluxes ([#783](https://github.com/pybamm-team/PyBaMM/pull/783))
-   Refactored `Solution` to make it a dictionary that contains all of the solution variables. This automatically creates `ProcessedVariable` objects when required, so that the solution can be obtained much more easily. ([#781](https://github.com/pybamm-team/PyBaMM/pull/781))
-   Added notebook to explain broadcasts ([#776](https://github.com/pybamm-team/PyBaMM/pull/776))
-   Added a step to discretisation that automatically compute the inverse of the mass matrix of the differential part of the problem so that the underlying DAEs can be provided in semi-explicit form, as required by the CasADi solver ([#769](https://github.com/pybamm-team/PyBaMM/pull/769))
-   Added the gradient operation for the Finite Element Method ([#767](https://github.com/pybamm-team/PyBaMM/pull/767))
-   Added `InputParameter` node for quickly changing parameter values ([#752](https://github.com/pybamm-team/PyBaMM/pull/752))
-   Added submodels for operating modes other than current-controlled ([#751](https://github.com/pybamm-team/PyBaMM/pull/751))
-   Changed finite volume discretisation to use exact values provided by Neumann boundary conditions when computing the gradient instead of adding ghost nodes([#748](https://github.com/pybamm-team/PyBaMM/pull/748))
-   Added optional R(x) distribution in particle models ([#745](https://github.com/pybamm-team/PyBaMM/pull/745))
-   Generalized importing of external variables ([#728](https://github.com/pybamm-team/PyBaMM/pull/728))
-   Separated active and inactive material volume fractions ([#726](https://github.com/pybamm-team/PyBaMM/pull/726))
-   Added submodels for tortuosity ([#726](https://github.com/pybamm-team/PyBaMM/pull/726))
-   Simplified the interface for setting current functions ([#723](https://github.com/pybamm-team/PyBaMM/pull/723))
-   Added Heaviside operator ([#723](https://github.com/pybamm-team/PyBaMM/pull/723))
-   New extrapolation methods ([#707](https://github.com/pybamm-team/PyBaMM/pull/707))
-   Added some "Getting Started" documentation ([#703](https://github.com/pybamm-team/PyBaMM/pull/703))
-   Allow abs tolerance to be set by variable for IDA KLU solver ([#700](https://github.com/pybamm-team/PyBaMM/pull/700))
-   Added Simulation class ([#693](https://github.com/pybamm-team/PyBaMM/pull/693)) with load/save functionality ([#732](https://github.com/pybamm-team/PyBaMM/pull/732))
-   Added interface to CasADi solver ([#687](https://github.com/pybamm-team/PyBaMM/pull/687), [#691](https://github.com/pybamm-team/PyBaMM/pull/691), [#714](https://github.com/pybamm-team/PyBaMM/pull/714)). This makes the SUNDIALS DAE solvers (Scikits and KLU) truly optional (though IDA KLU is recommended for solving the DFN).
-   Added option to use CasADi's Algorithmic Differentiation framework to calculate Jacobians ([#687](https://github.com/pybamm-team/PyBaMM/pull/687))
-   Added method to evaluate parameters more easily ([#669](https://github.com/pybamm-team/PyBaMM/pull/669))
-   Added `Jacobian` class to reuse known Jacobians of expressions ([#665](https://github.com/pybamm-team/PyBaMM/pull/670))
-   Added `Interpolant` class to interpolate experimental data (e.g. OCP curves) ([#661](https://github.com/pybamm-team/PyBaMM/pull/661))
-   Added interface (via pybind11) to sundials with the IDA KLU sparse linear solver ([#657](https://github.com/pybamm-team/PyBaMM/pull/657))
-   Allowed parameters to be set by material or by specifying a particular paper ([#647](https://github.com/pybamm-team/PyBaMM/pull/647))
-   Set relative and absolute tolerances independently in solvers ([#645](https://github.com/pybamm-team/PyBaMM/pull/645))
-   Added basic method to allow (a part of) the State Vector to be updated with results obtained from another solution or package ([#624](https://github.com/pybamm-team/PyBaMM/pull/624))
-   Added some non-uniform meshes in 1D and 2D ([#617](https://github.com/pybamm-team/PyBaMM/pull/617))

## Optimizations

-   Now simplifying objects that are constant as soon as they are created ([#801](https://github.com/pybamm-team/PyBaMM/pull/801))
-   Simplified solver interface ([#800](https://github.com/pybamm-team/PyBaMM/pull/800))
-   Added caching for shape evaluation, used during discretisation ([#780](https://github.com/pybamm-team/PyBaMM/pull/780))
-   Added an option to skip model checks during discretisation, which could be slow for large models ([#739](https://github.com/pybamm-team/PyBaMM/pull/739))
-   Use CasADi's automatic differentation algorithms by default when solving a model ([#714](https://github.com/pybamm-team/PyBaMM/pull/714))
-   Avoid re-checking size when making a copy of an `Index` object ([#656](https://github.com/pybamm-team/PyBaMM/pull/656))
-   Avoid recalculating `_evaluation_array` when making a copy of a `StateVector` object ([#653](https://github.com/pybamm-team/PyBaMM/pull/653))

## Bug fixes

-   Fixed a bug where current loaded from data was incorrectly scaled with the cell capacity ([#852](https://github.com/pybamm-team/PyBaMM/pull/852))
-   Moved evaluation of initial conditions to solver ([#839](https://github.com/pybamm-team/PyBaMM/pull/839))
-   Fixed a bug where the first line of the data wasn't loaded when parameters are loaded from data ([#819](https://github.com/pybamm-team/PyBaMM/pull/819))
-   Made `graphviz` an optional dependency ([#810](https://github.com/pybamm-team/PyBaMM/pull/810))
-   Fixed examples to run with basic pip installation ([#800](https://github.com/pybamm-team/PyBaMM/pull/800))
-   Added events for CasADi solver when stepping ([#800](https://github.com/pybamm-team/PyBaMM/pull/800))
-   Improved implementation of broadcasts ([#776](https://github.com/pybamm-team/PyBaMM/pull/776))
-   Fixed a bug which meant that the Ohmic heating in the current collectors was incorrect if using the Finite Element Method ([#767](https://github.com/pybamm-team/PyBaMM/pull/767))
-   Improved automatic broadcasting ([#747](https://github.com/pybamm-team/PyBaMM/pull/747))
-   Fixed bug with wrong temperature in initial conditions ([#737](https://github.com/pybamm-team/PyBaMM/pull/737))
-   Improved flexibility of parameter values so that parameters (such as diffusivity or current) can be set as functions or scalars ([#723](https://github.com/pybamm-team/PyBaMM/pull/723))
-   Fixed a bug where boundary conditions were sometimes handled incorrectly in 1+1D models ([#713](https://github.com/pybamm-team/PyBaMM/pull/713))
-   Corrected a sign error in Dirichlet boundary conditions in the Finite Element Method ([#706](https://github.com/pybamm-team/PyBaMM/pull/706))
-   Passed the correct dimensional temperature to open circuit potential ([#702](https://github.com/pybamm-team/PyBaMM/pull/702))
-   Added missing temperature dependence in electrolyte and interface submodels ([#698](https://github.com/pybamm-team/PyBaMM/pull/698))
-   Fixed differentiation of functions that have more than one argument ([#687](https://github.com/pybamm-team/PyBaMM/pull/687))
-   Added warning if `ProcessedVariable` is called outside its interpolation range ([#681](https://github.com/pybamm-team/PyBaMM/pull/681))
-   Updated installation instructions for Mac OS ([#680](https://github.com/pybamm-team/PyBaMM/pull/680))
-   Improved the way `ProcessedVariable` objects are created in higher dimensions ([#581](https://github.com/pybamm-team/PyBaMM/pull/581))

## Breaking changes

-   Time for solver should now be given in seconds ([#832](https://github.com/pybamm-team/PyBaMM/pull/832))
-   Model events are now represented as a list of `pybamm.Event` ([#759](https://github.com/pybamm-team/PyBaMM/issues/759)
-   Removed `ParameterValues.update_model`, whose functionality is now replaced by `InputParameter` ([#801](https://github.com/pybamm-team/PyBaMM/pull/801))
-   Removed `Outer` and `Kron` nodes as no longer used ([#777](https://github.com/pybamm-team/PyBaMM/pull/777))
-   Moved `results` to separate repositories ([#761](https://github.com/pybamm-team/PyBaMM/pull/761))
-   The parameters "Bruggeman coefficient" must now be specified separately as "Bruggeman coefficient (electrolyte)" and "Bruggeman coefficient (electrode)"
-   The current classes (`GetConstantCurrent`, `GetUserCurrent` and `GetUserData`) have now been removed. Please refer to the [`change-input-current` notebook](https://github.com/pybamm-team/PyBaMM/blob/master/examples/notebooks/change-input-current.ipynb) for information on how to specify an input current
-   Parameter functions must now use pybamm functions instead of numpy functions (e.g. `pybamm.exp` instead of `numpy.exp`), as these are then used to construct the expression tree directly. Generally, pybamm syntax follows numpy syntax; please get in touch if a function you need is missing.
-   The current must now be updated by changing "Current function [A]" or "C-rate" instead of "Typical current [A]"


# [v0.1.0](https://github.com/pybamm-team/PyBaMM/tree/v0.1.0) - 2019-10-08

This is the first official version of PyBaMM.
Please note that PyBaMM in still under active development, and so the API may change in the future.

## Features

### Models

#### Lithium-ion

- Single Particle Model (SPM)
- Single Particle Model with electrolyte (SPMe)
- Doyle-Fuller-Newman (DFN) model

with the following optional physics:

- Thermal effects
- Fast diffusion in particles
- 2+1D (pouch cell)

#### Lead-acid

- Leading-Order Quasi-Static model
- First-Order Quasi-Static model
- Composite model
- Full model

with the following optional physics:

- Hydrolysis side reaction
- Capacitance effects
- 2+1D


### Spatial discretisations

- Finite Volume (1D only)
- Finite Element (scikit, 2D only)

### Solvers

- Scipy
- Scikits ODE
- Scikits DAE
- IDA KLU sparse linear solver (Sundials)
- Algebraic (root-finding)
