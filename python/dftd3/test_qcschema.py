# This file is part of s-dftd3.
# SPDX-Identifier: LGPL-3.0-or-later
#
# s-dftd3 is free software: you can redistribute it and/or modify it under
# the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# s-dftd3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with s-dftd3.  If not, see <https://www.gnu.org/licenses/>.


from pytest import approx
from dftd3.qcschema import run_qcschema
import qcelemental as qcel
import numpy as np


def test_energy_r2scan_d3bj():
    thr = 1e-9

    atomic_input = qcel.models.AtomicInput(
        molecule={
            "symbols": "C C C C C C I H H H H H S H C H H H".split(" "),
            "geometry": [
                [-1.42754169820131, -1.50508961850828, -1.93430551124333],
                [+1.19860572924150, -1.66299114873979, -2.03189643761298],
                [+2.65876001301880, +0.37736955363609, -1.23426391650599],
                [+1.50963368042358, +2.57230374419743, -0.34128058818180],
                [-1.12092277855371, +2.71045691257517, -0.25246348639234],
                [-2.60071517756218, +0.67879949508239, -1.04550707592673],
                [-2.86169588073340, +5.99660765711210, +1.08394899986031],
                [+2.09930989272956, -3.36144811062374, -2.72237695164263],
                [+2.64405246349916, +4.15317840474646, +0.27856972788526],
                [+4.69864865613751, +0.26922271535391, -1.30274048619151],
                [-4.63786461351839, +0.79856258572808, -0.96906659938432],
                [-2.57447518692275, -3.08132039046931, -2.54875517521577],
                [-5.88211879210329, 11.88491819358157, +2.31866455902233],
                [-8.18022701418703, 10.95619984550779, +1.83940856333092],
                [-5.08172874482867, 12.66714386256482, -0.92419491629867],
                [-3.18311711399702, 13.44626574330220, -0.86977613647871],
                [-5.07177399637298, 10.99164969235585, -2.10739192258756],
                [-6.35955320518616, 14.08073002965080, -1.68204314084441],
            ],
        },
        driver="energy",
        model={
            "method": "r2scan",
        },
    )

    atomic_result = run_qcschema(atomic_input)

    assert atomic_result.success
    assert approx(atomic_result.return_result, abs=thr) == -0.005790963570050724


def test_energy_bp_d3zero():
    thr = 1e-9

    atomic_input = qcel.models.AtomicInput(
        molecule={
            "symbols": "C C C C C C I H H H H H S H C H H H".split(" "),
            "geometry": [
                [-1.42754169820131, -1.50508961850828, -1.93430551124333],
                [+1.19860572924150, -1.66299114873979, -2.03189643761298],
                [+2.65876001301880, +0.37736955363609, -1.23426391650599],
                [+1.50963368042358, +2.57230374419743, -0.34128058818180],
                [-1.12092277855371, +2.71045691257517, -0.25246348639234],
                [-2.60071517756218, +0.67879949508239, -1.04550707592673],
                [-2.86169588073340, +5.99660765711210, +1.08394899986031],
                [+2.09930989272956, -3.36144811062374, -2.72237695164263],
                [+2.64405246349916, +4.15317840474646, +0.27856972788526],
                [+4.69864865613751, +0.26922271535391, -1.30274048619151],
                [-4.63786461351839, +0.79856258572808, -0.96906659938432],
                [-2.57447518692275, -3.08132039046931, -2.54875517521577],
                [-5.88211879210329, 11.88491819358157, +2.31866455902233],
                [-8.18022701418703, 10.95619984550779, +1.83940856333092],
                [-5.08172874482867, 12.66714386256482, -0.92419491629867],
                [-3.18311711399702, 13.44626574330220, -0.86977613647871],
                [-5.07177399637298, 10.99164969235585, -2.10739192258756],
                [-6.35955320518616, 14.08073002965080, -1.68204314084441],
            ],
        },
        driver="energy",
        model={"method": ""},
        keywords={
            "params_tweaks": {
                "s8": 1.683,
                "rs6": 1.139,
            },
            "level_hint": "d3zero",
        },
    )

    atomic_result = run_qcschema(atomic_input)

    assert atomic_result.success
    assert approx(atomic_result.return_result, abs=thr) == -0.014107242765881673


def test_gradient_b97d_d3bj():
    thr = 1e-9

    atomic_input = qcel.models.AtomicInput(
        molecule={
            "symbols": "C C C C C C I H H H H H S H C H H H".split(" "),
            "geometry": [
                [-1.42754169820131, -1.50508961850828, -1.93430551124333],
                [+1.19860572924150, -1.66299114873979, -2.03189643761298],
                [+2.65876001301880, +0.37736955363609, -1.23426391650599],
                [+1.50963368042358, +2.57230374419743, -0.34128058818180],
                [-1.12092277855371, +2.71045691257517, -0.25246348639234],
                [-2.60071517756218, +0.67879949508239, -1.04550707592673],
                [-2.86169588073340, +5.99660765711210, +1.08394899986031],
                [+2.09930989272956, -3.36144811062374, -2.72237695164263],
                [+2.64405246349916, +4.15317840474646, +0.27856972788526],
                [+4.69864865613751, +0.26922271535391, -1.30274048619151],
                [-4.63786461351839, +0.79856258572808, -0.96906659938432],
                [-2.57447518692275, -3.08132039046931, -2.54875517521577],
                [-5.88211879210329, 11.88491819358157, +2.31866455902233],
                [-8.18022701418703, 10.95619984550779, +1.83940856333092],
                [-5.08172874482867, 12.66714386256482, -0.92419491629867],
                [-3.18311711399702, 13.44626574330220, -0.86977613647871],
                [-5.07177399637298, 10.99164969235585, -2.10739192258756],
                [-6.35955320518616, 14.08073002965080, -1.68204314084441],
            ],
        },
        driver="gradient",
        model={
            "method": "b97d-d3(bj)",
        },
        keywords={},
    )
    gradient = np.array(
        [
            [-2.24433991e-4, -5.91159526e-4, -2.33293415e-4],
            [+1.50251962e-4, -2.82533931e-4, -1.15148366e-4],
            [+6.40226887e-4, -1.93115854e-4, -8.52423564e-5],
            [-3.87182065e-4, +3.37740546e-4, +1.46371614e-4],
            [-1.50798525e-4, +2.77860025e-4, +1.34824868e-4],
            [-5.43402577e-5, +4.87397219e-4, +2.01618868e-4],
            [+4.25239249e-4, -1.03529619e-3, +5.41876182e-4],
            [+2.52388808e-4, -4.75708161e-4, -1.94060963e-4],
            [+5.04286531e-4, +2.56544859e-4, +9.91417162e-5],
            [+5.71245411e-4, -3.79228268e-5, -2.29708658e-5],
            [-5.26293984e-4, -2.18210867e-4, -7.77720060e-5],
            [-3.14471753e-4, -4.45969134e-4, -1.74705390e-4],
            [-4.72419849e-4, +5.77895012e-4, +6.33913403e-4],
            [-4.42956654e-4, +4.42890118e-5, +2.99133275e-4],
            [-5.55327298e-5, +5.01284843e-4, -2.37457630e-4],
            [+1.66366211e-4, +2.98464282e-4, -1.78290559e-4],
            [-4.65822318e-5, +2.55746443e-4, -4.74549498e-4],
            [-3.49930186e-5, +2.42694248e-4, -2.63388877e-4],
        ]
    )

    atomic_result = run_qcschema(atomic_input)

    print(atomic_result.return_result)
    assert atomic_result.success
    assert approx(atomic_result.return_result, abs=thr) == gradient


def test_gradient_tpss_d3zero():
    thr = 1.0e-9

    atomic_input = qcel.models.AtomicInput(
        molecule={
            "symbols": "O C C F O F H".split(),
            "geometry": [
                [+4.877023733, -3.909030492, +1.796260143],
                [+6.112318716, -2.778558610, +0.091330457],
                [+7.360520527, -4.445334728, -1.932830640],
                [+7.978801077, -6.767751279, -1.031771494],
                [+6.374499300, -0.460299457, -0.213142194],
                [+5.637581753, -4.819746139, -3.831249370],
                [+9.040657008, -3.585225944, -2.750722946],
            ],
            "molecular_charge": -1,
        },
        driver="gradient",
        model={
            "method": "",
        },
        keywords={
            "params_tweaks": {
                "rs6": 1.166,
                "s8": 1.105,
            },
            "level_hint": "d3zero",
        },
    )
    gradient = np.array(
        [
            [+8.5996173284231875e-5, +1.3305418701321822e-4, -4.9354196253270805e-5],
            [+1.6831911035550991e-4, -3.6665426078002247e-4, -3.6501997130204884e-4],
            [-1.5843252070729541e-4, +1.9764727640629749e-4, +2.4586001791105944e-4],
            [-1.2283817052613589e-4, +4.7671652867694957e-4, -2.2634306691291976e-4],
            [-6.5711912664060220e-5, -7.6482146814930930e-5, +1.3704210420643919e-4],
            [+4.1919929190184019e-4, -7.9186660275995670e-6, +2.4311185926693921e-4],
            [-3.2653197164409062e-4, -3.5636291847391242e-4, +1.4703253083801523e-5],
        ]
    )

    atomic_result = run_qcschema(atomic_input)

    print(atomic_result.return_result)
    assert atomic_result.success
    assert approx(atomic_result.return_result, abs=thr) == gradient
    assert "energy" in atomic_result.extras["dftd3"]
    assert "gradient" in atomic_result.extras["dftd3"]
    assert "virial" in atomic_result.extras["dftd3"]


def test_error_noargs():
    thr = 1e-9

    atomic_input = qcel.models.AtomicInput(
        molecule={
            "symbols": "C C C C N C S H H H H H".split(),
            "geometry": [
                [-2.56745685564671, -0.02509985979910, 0.00000000000000],
                [-1.39177582455797, +2.27696188880014, 0.00000000000000],
                [+1.27784995624894, +2.45107479759386, 0.00000000000000],
                [+2.62801937615793, +0.25927727028120, 0.00000000000000],
                [+1.41097033661123, -1.99890996077412, 0.00000000000000],
                [-1.17186102298849, -2.34220576284180, 0.00000000000000],
                [-2.39505990368378, -5.22635838332362, 0.00000000000000],
                [+2.41961980455457, -3.62158019253045, 0.00000000000000],
                [-2.51744374846065, +3.98181713686746, 0.00000000000000],
                [+2.24269048384775, +4.24389473203647, 0.00000000000000],
                [+4.66488984573956, +0.17907568006409, 0.00000000000000],
                [-4.60044244782237, -0.17794734637413, 0.00000000000000],
            ],
        },
        driver="energy",
        model={"method": ""},
        keywords={},
    )
    error = qcel.models.ComputeError(
        error_type="input error",
        error_message="new_param() missing 3 required keyword-only arguments: 's8', 'a1', and 'a2'",
    )

    atomic_result = run_qcschema(atomic_input)

    assert not atomic_result.success
    assert atomic_result.error == error


def test_error_nomethod():
    thr = 1e-9

    atomic_input = qcel.models.AtomicInput(
        molecule={
            "symbols": "C C C C N C S H H H H H".split(),
            "geometry": [
                [-2.56745685564671, -0.02509985979910, 0.00000000000000],
                [-1.39177582455797, +2.27696188880014, 0.00000000000000],
                [+1.27784995624894, +2.45107479759386, 0.00000000000000],
                [+2.62801937615793, +0.25927727028120, 0.00000000000000],
                [+1.41097033661123, -1.99890996077412, 0.00000000000000],
                [-1.17186102298849, -2.34220576284180, 0.00000000000000],
                [-2.39505990368378, -5.22635838332362, 0.00000000000000],
                [+2.41961980455457, -3.62158019253045, 0.00000000000000],
                [-2.51744374846065, +3.98181713686746, 0.00000000000000],
                [+2.24269048384775, +4.24389473203647, 0.00000000000000],
                [+4.66488984573956, +0.17907568006409, 0.00000000000000],
                [-4.60044244782237, -0.17794734637413, 0.00000000000000],
            ],
        },
        driver="energy",
        model={
            "method": "this-method-does-not-exist",
        },
        keywords={
            "level_hint": "d3bj",
        },
    )
    error = qcel.models.ComputeError(
        error_type="input error",
        error_message="No entry for 'this-method-does-not-exist' present",
    )

    atomic_result = run_qcschema(atomic_input)

    assert not atomic_result.success
    assert atomic_result.error == error


def test_error_level():
    thr = 1e-9

    atomic_input = qcel.models.AtomicInput(
        molecule={
            "symbols": "C C C C N C S H H H H H".split(),
            "geometry": [
                [-2.56745685564671, -0.02509985979910, 0.00000000000000],
                [-1.39177582455797, +2.27696188880014, 0.00000000000000],
                [+1.27784995624894, +2.45107479759386, 0.00000000000000],
                [+2.62801937615793, +0.25927727028120, 0.00000000000000],
                [+1.41097033661123, -1.99890996077412, 0.00000000000000],
                [-1.17186102298849, -2.34220576284180, 0.00000000000000],
                [-2.39505990368378, -5.22635838332362, 0.00000000000000],
                [+2.41961980455457, -3.62158019253045, 0.00000000000000],
                [-2.51744374846065, +3.98181713686746, 0.00000000000000],
                [+2.24269048384775, +4.24389473203647, 0.00000000000000],
                [+4.66488984573956, +0.17907568006409, 0.00000000000000],
                [-4.60044244782237, -0.17794734637413, 0.00000000000000],
            ],
        },
        driver="energy",
        model={
            "method": "SCAN",
        },
        keywords={
            "level_hint": "D42",
        },
    )
    error = qcel.models.ComputeError(
        error_type="input error",
        error_message="Level 'D42' is invalid for this dispersion correction",
    )

    atomic_result = run_qcschema(atomic_input)

    assert not atomic_result.success
    assert atomic_result.error == error


def test_ghost_pbe_d3bj():
    thr = 1e-9

    atomic_input = qcel.models.AtomicInput(
        molecule={
            "symbols": "Pb H H H H Bi H H H".split(),
            "geometry": [
                [-0.00000020988889, -4.98043478877778, +0.00000000000000],
                [+3.06964045311111, -6.06324400177778, +0.00000000000000],
                [-1.53482054188889, -6.06324400177778, -2.65838526500000],
                [-1.53482054188889, -6.06324400177778, +2.65838526500000],
                [-0.00000020988889, -1.72196703577778, +0.00000000000000],
                [-0.00000020988889, +4.77334244722222, +0.00000000000000],
                [+1.35700257511111, +6.70626379422222, -2.35039772300000],
                [-2.71400388988889, +6.70626379422222, +0.00000000000000],
                [+1.35700257511111, +6.70626379422222, +2.35039772300000],
            ],
            "real": [True] * 5 + [False] * 4,
        },
        driver="gradient",
        model={
            "method": "pbe",
        },
    )
    gradient = np.array(
        [
            [+0.00000000e-0, +1.15093229e-7, +0.00000000e-0],
            [+5.37509663e-5, -1.90067439e-5, +0.00000000e-0],
            [-2.68754977e-5, -1.90067527e-5, -4.65496968e-5],
            [-2.68754977e-5, -1.90067527e-5, +4.65496968e-5],
            [+0.00000000e-0, +5.69051561e-5, +0.00000000e-0],
            [+0.00000000e-0, +0.00000000e-0, +0.00000000e-0],
            [+0.00000000e-0, +0.00000000e-0, +0.00000000e-0],
            [+0.00000000e-0, +0.00000000e-0, +0.00000000e-0],
            [+0.00000000e-0, +0.00000000e-0, +0.00000000e-0],
        ]
    )

    atomic_result = run_qcschema(atomic_input)

    assert atomic_result.success
    assert approx(atomic_result.return_result, abs=thr) == gradient
