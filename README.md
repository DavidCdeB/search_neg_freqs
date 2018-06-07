# 
<!-- Attempt of improved/general code:
~/Trabajo/structures/Explanation_of_Scripts/Eos_2_Phonons/trials_Eos_2_Phonons/trial_calcite_III
-->


# Table of Contents

1. [What is the `search_neg_freqs` program ?](#example)
2. [Data flow](#example2)
3. [Test](#example3)
4. [How to cite](#example4)
5. [Contributing](#example5)


<a name="example"></a>
## What is the `search_neg_freqs` program ?

* `search_neg_freqs` is a program for computational chemistry and physics that
will print out the negative frequencies found over a set of volumes.

* The information obtained from the scripts on this repository 
is used to run the scripts on the [EOS_2_phonons](https://github.com/DavidCdeB/EOS_2_phonons) repository.

* The [EOS_2_phonons](https://github.com/DavidCdeB/EOS_2_phonons) repository contains the scripts necessary to automate the runs for frequency calculations, and breaking symmetry over different volumes.
The programs on [EOS_2_phonons](https://github.com/DavidCdeB/EOS_2_phonons) repository allow to obtain the needed outputs in order to further perform a quasi-harmonic approximation analyisis with the [`QHA_2D` program](https://github.com/DavidCdeB/QHA_2D)

The program was developed as part of [David Carrasco de Busturia PhD project](https://www.imperial.ac.uk/people/d.carrasco-de-busturia/) at [Prof. Nicholas Harrison's Computational Materials Science Group](http://www.imperial.ac.uk/computational-materials-science/), Imperial College London. The program was used to investigate the phase diagram and phase transitions mechanisms on the calcium carbonate system.

<a name="example2"></a>
## Data flow

* Get the code: `git clone https://github.com/DavidCdeB/search_neg_freqs.git`

* Copy to the folder `search_neg_freqs` created, all the freqcuency outputs, one per volume. These outputs have to end in `*.out`. 

* Run the program `bash extract_neg_freqs_v3.sh`. 
* The output is the following:

```
You can now open the 'neg_freqs_grabbing_more_decimals.txt' file, with the summary for all the negative freqs
Counting the number of negative freqs...
./P3221_1143.965721.out

./P3221_1114.515627.out

./P3221_1071.300672.out

./P3221_1085.572503.out

len(negatives) =  1 

./P3221_1099.984555.out

len(negatives) =  1 

./P3221_1043.035120.out

len(negatives) =  25 

./P3221_1167.320319.out

len(negatives) =  1 

./P3221_1129.183195.out

./P3221_1057.078411.out

len(negatives) =  2 

./P3221_1029.133371.out

len(negatives) =  27 

./P3221_1015.402996.out

len(negatives) =  27
```

This output is showing the number of negative frequencies
each volume has.

* Open the file: `neg_freqs_grabbing_more_decimals.txt`.
This file shows 
in which dispersion k-point
the negative frecuency has been found, and the value of this frequency.
The following is an extract of that file. We can easily see that the volumes
1143.965721 and 1114.515627 do not contain negative frequencies.
On the contrary, 1043.035120 and 1029.133371 contain
lots of negative frequencies at finite k-points.
The value of the frequencies is shown in square brackets.

```
./P3221_1143.965721.out
 * WITH SHRINKING FACTORS: IS1 =     3 IS2 =     3 IS3 =     1                 *
  DISPERSION K POINT NUMBER     1 COORD:  R(  0  0  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     2 COORD:  C(  0  1  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     3 COORD:  C(  0  2  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     4 COORD:  C(  1  0  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     5 COORD:  C(  1  1  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     6 COORD:  C(  1  2  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     7 COORD:  C(  2  0  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     8 COORD:  C(  2  1  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     9 COORD:  C(  2  2  0 )    WEIGHT:    1.

./P3221_1114.515627.out
 * WITH SHRINKING FACTORS: IS1 =     3 IS2 =     3 IS3 =     1                 *
  DISPERSION K POINT NUMBER     1 COORD:  R(  0  0  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     2 COORD:  C(  0  1  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     3 COORD:  C(  0  2  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     4 COORD:  C(  1  0  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     5 COORD:  C(  1  1  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     6 COORD:  C(  1  2  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     7 COORD:  C(  2  0  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     8 COORD:  C(  2  1  0 )    WEIGHT:    1.
  DISPERSION K POINT NUMBER     9 COORD:  C(  2  2  0 )    WEIGHT:    1.

./P3221_1043.035120.out
 * WITH SHRINKING FACTORS: IS1 =     3 IS2 =     3 IS3 =     1                 *
  DISPERSION K POINT NUMBER     1 COORD:  R(  0  0  0 )    WEIGHT:    1.
['-27.4323']
  DISPERSION K POINT NUMBER     2 COORD:  C(  0  1  0 )    WEIGHT:    1.
['-33.7374']
['-20.3996']
['-13.8545']
  DISPERSION K POINT NUMBER     3 COORD:  C(  0  2  0 )    WEIGHT:    1.
['-33.7374']
['-20.3996']
['-13.8545']
  DISPERSION K POINT NUMBER     4 COORD:  C(  1  0  0 )    WEIGHT:    1.
['-33.7374']
['-20.3996']
['-13.8545']
  DISPERSION K POINT NUMBER     5 COORD:  C(  1  1  0 )    WEIGHT:    1.
['-40.3447']
['-28.9624', '-28.9624']
  DISPERSION K POINT NUMBER     6 COORD:  C(  1  2  0 )    WEIGHT:    1.
['-33.7374']
['-20.3996']
['-13.8545']
  DISPERSION K POINT NUMBER     7 COORD:  C(  2  0  0 )    WEIGHT:    1.
['-33.7374']
['-20.3996']
['-13.8545']
  DISPERSION K POINT NUMBER     8 COORD:  C(  2  1  0 )    WEIGHT:    1.
['-33.7374']
['-20.3996']
['-13.8545']
  DISPERSION K POINT NUMBER     9 COORD:  C(  2  2  0 )    WEIGHT:    1.
['-40.3447']
['-28.9624', '-28.9624']

./P3221_1029.133371.out
 * WITH SHRINKING FACTORS: IS1 =     3 IS2 =     3 IS3 =     1                 *
  DISPERSION K POINT NUMBER     1 COORD:  R(  0  0  0 )    WEIGHT:    1.
['-46.4928']
['-37.8698', '-37.8698']
  DISPERSION K POINT NUMBER     2 COORD:  C(  0  1  0 )    WEIGHT:    1.
['-52.2115']
['-44.6610']
['-39.7488']
  DISPERSION K POINT NUMBER     3 COORD:  C(  0  2  0 )    WEIGHT:    1.
['-52.2115']
['-44.6610']
['-39.7488']
  DISPERSION K POINT NUMBER     4 COORD:  C(  1  0  0 )    WEIGHT:    1.
['-52.2115']
['-44.6610']
['-39.7488']
  DISPERSION K POINT NUMBER     5 COORD:  C(  1  1  0 )    WEIGHT:    1.
['-53.6360']
['-47.1959', '-47.1959']
  DISPERSION K POINT NUMBER     6 COORD:  C(  1  2  0 )    WEIGHT:    1.
['-52.2115']
['-44.6610']
['-39.7488']
  DISPERSION K POINT NUMBER     7 COORD:  C(  2  0  0 )    WEIGHT:    1.
['-52.2115']
['-44.6610']
['-39.7488']
  DISPERSION K POINT NUMBER     8 COORD:  C(  2  1  0 )    WEIGHT:    1.
['-52.2115']
['-44.6610']
['-39.7488']
  DISPERSION K POINT NUMBER     9 COORD:  C(  2  2  0 )    WEIGHT:    1.
['-53.6360']
['-47.1959', '-47.1959']
```
<p align="left">
  <img width="256" height="256" src="https://github.com/DavidCdeB/search_neg_freqs/blob/master/Images_for_README_md/file_system.svg">
</p>

<a name="example3"></a>
## Test

Under the `TEST` folder, you will find all the programs
needed, together with a `*out` folder
with the frequency output.


<a name="example4"></a>
## How to cite

Please cite the following reference when using this code:

Carrasco-Busturia, D., Erba, A., Mallia, G., Mellan, T. A. and Harrison, N. M. "Computed phase stability and phase transition mechanisms in CaCO3 at finite temperature and pressure" _In progress_

<a name="example5"></a>
## Contributing

`QHA` is free software released under the Gnu Public Licence version 3.
All contributions to improve this code are more than welcome.

* Have a look at GitHub's ["How to contribute"](https://guides.github.com/activities/contributing-to-open-source/#contributing).

* If you are familiar with `git`: fork this repository and submit a pull request.

* If you are not familiar with `git`:

    * If something should be improved, open an issue here on GitHub
    * If you think a new feature would be interesting, open an issue
    * If you need a particular feature for your project contact me directly.


