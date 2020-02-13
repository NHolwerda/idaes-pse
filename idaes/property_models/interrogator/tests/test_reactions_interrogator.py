#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Reaction Interrogator Tool

@author: alee
"""
import pytest

from pyomo.environ import ConcreteModel

from idaes.core import FlowsheetBlock
from idaes.unit_models import CSTR, PFR
from idaes.property_models.interrogator import (
        PropertyInterrogatorBlock, ReactionInterrogatorBlock)


def test_interrogator_parameter_block():
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": False})

    m.fs.params = PropertyInterrogatorBlock()
    m.fs.rxn_params = ReactionInterrogatorBlock(
            default={"property_package": m.fs.params})

    # Check that parameter block has expected attributes
    assert isinstance(m.fs.rxn_params.required_properties, dict)
    assert len(m.fs.rxn_params.required_properties) == 0


def test_interrogator_rxn_block_unindexed_call():
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": False})

    m.fs.params = PropertyInterrogatorBlock()
    m.fs.rxn_params = ReactionInterrogatorBlock(
            default={"property_package": m.fs.params})

    m.fs.props = m.fs.params.state_block_class(
            [0],
            default={"parameters": m.fs.params})
    m.fs.rxns = m.fs.rxn_params.reaction_block_class(
            [0],
            default={"parameters": m.fs.rxn_params,
                     "state_block": m.fs.props})

    # Check get_term methods return an unindexed dummy var
    assert m.fs.rxns[0].prop_unindexed is \
        m.fs.rxns[0]._dummy_var

    # Call again to make sure duplicates are skipped in required_properties
    assert m.fs.rxns[0].prop_unindexed is \
        m.fs.rxns[0]._dummy_var

    # Check that get_term calls were logged correctly
    assert m.fs.rxn_params.required_properties == {
            "prop_unindexed": ["fs.rxns"]}


def test_interrogator_rxn_block_phase_call():
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": False})

    m.fs.params = PropertyInterrogatorBlock()
    m.fs.rxn_params = ReactionInterrogatorBlock(
            default={"property_package": m.fs.params})

    m.fs.props = m.fs.params.state_block_class(
            [0],
            default={"parameters": m.fs.params})
    m.fs.rxns = m.fs.rxn_params.reaction_block_class(
            [0],
            default={"parameters": m.fs.rxn_params,
                     "state_block": m.fs.props})

    # Check get_term methods return an unindexed dummy var
    assert m.fs.rxns[0].prop_phase["Liq"] is \
        m.fs.rxns[0]._dummy_var_phase["Liq"]
    assert m.fs.rxns[0].prop_phase["Vap"] is \
        m.fs.rxns[0]._dummy_var_phase["Vap"]

    # Check that get_term calls were logged correctly
    assert m.fs.rxn_params.required_properties == {
            "prop_phase": ["fs.rxns"]}


def test_interrogator_rxn_block_comp_call():
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": False})

    m.fs.params = PropertyInterrogatorBlock()
    m.fs.rxn_params = ReactionInterrogatorBlock(
            default={"property_package": m.fs.params})

    m.fs.props = m.fs.params.state_block_class(
            [0],
            default={"parameters": m.fs.params})
    m.fs.rxns = m.fs.rxn_params.reaction_block_class(
            [0],
            default={"parameters": m.fs.rxn_params,
                     "state_block": m.fs.props})

    # Check get_term methods return an unindexed dummy var
    assert m.fs.rxns[0].prop_comp["A"] is \
        m.fs.rxns[0]._dummy_var_comp["A"]
    assert m.fs.rxns[0].prop_comp["B"] is \
        m.fs.rxns[0]._dummy_var_comp["B"]

    # Check that get_term calls were logged correctly
    assert m.fs.rxn_params.required_properties == {
            "prop_comp": ["fs.rxns"]}


def test_interrogator_rxn_block_phase_comp_call():
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": False})

    m.fs.params = PropertyInterrogatorBlock()
    m.fs.rxn_params = ReactionInterrogatorBlock(
            default={"property_package": m.fs.params})

    m.fs.props = m.fs.params.state_block_class(
            [0],
            default={"parameters": m.fs.params})
    m.fs.rxns = m.fs.rxn_params.reaction_block_class(
            [0],
            default={"parameters": m.fs.rxn_params,
                     "state_block": m.fs.props})

    # Check get_term methods return an unindexed dummy var
    assert m.fs.rxns[0].prop_phase_comp["Liq", "A"] is \
        m.fs.rxns[0]._dummy_var_phase_comp["Liq", "A"]
    assert m.fs.rxns[0].prop_phase_comp["Vap", "B"] is \
        m.fs.rxns[0]._dummy_var_phase_comp["Vap", "B"]

    # Check that get_term calls were logged correctly
    assert m.fs.rxn_params.required_properties == {
            "prop_phase_comp": ["fs.rxns"]}


def test_interrogator_rxn_block_reaction_rate_call():
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": False})

    m.fs.params = PropertyInterrogatorBlock()
    m.fs.rxn_params = ReactionInterrogatorBlock(
            default={"property_package": m.fs.params})

    m.fs.props = m.fs.params.state_block_class(
            [0],
            default={"parameters": m.fs.params})
    m.fs.rxns = m.fs.rxn_params.reaction_block_class(
            [0],
            default={"parameters": m.fs.rxn_params,
                     "state_block": m.fs.props})

    # Check get_term methods return an unindexed dummy var
    assert m.fs.rxns[0].reaction_rate["R1"] is \
        m.fs.rxns[0]._dummy_reaction_idx["R1"]
    assert m.fs.rxns[0].reaction_rate["R1"] is \
        m.fs.rxns[0]._dummy_reaction_idx["R1"]

    # Check that get_term calls were logged correctly
    assert m.fs.rxn_params.required_properties == {
            "reaction_rate": ["fs.rxns"]}


def test_interrogator_rxn_block_dh_rxn_call():
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": False})

    m.fs.params = PropertyInterrogatorBlock()
    m.fs.rxn_params = ReactionInterrogatorBlock(
            default={"property_package": m.fs.params})

    m.fs.props = m.fs.params.state_block_class(
            [0],
            default={"parameters": m.fs.params})
    m.fs.rxns = m.fs.rxn_params.reaction_block_class(
            [0],
            default={"parameters": m.fs.rxn_params,
                     "state_block": m.fs.props})

    # Check get_term methods return an unindexed dummy var
    assert m.fs.rxns[0].dh_rxn["R1"] is \
        m.fs.rxns[0]._dummy_reaction_idx["R1"]
    assert m.fs.rxns[0].dh_rxn["R1"] is \
        m.fs.rxns[0]._dummy_reaction_idx["R1"]

    # Check that get_term calls were logged correctly
    assert m.fs.rxn_params.required_properties == {
            "dh_rxn": ["fs.rxns"]}


def test_interrogator_initialize_method():
    # Initialize method should return an TypeError
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": False})

    m.fs.params = PropertyInterrogatorBlock()
    m.fs.rxn_params = ReactionInterrogatorBlock(
            default={"property_package": m.fs.params})

    m.fs.props = m.fs.params.state_block_class(
            [0],
            default={"parameters": m.fs.params})
    m.fs.rxns = m.fs.rxn_params.reaction_block_class(
            [0],
            default={"parameters": m.fs.rxn_params,
                     "state_block": m.fs.props})

    with pytest.raises(TypeError,
                       match="Models constructed using the Reaction "
                       "Interrogator package cannot be used to solve a "
                       "flowsheet. Please rebuild your flowsheet using a "
                       "valid reaction package."):
        m.fs.rxns.initialize()


@pytest.fixture(scope="module")
def model():
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": True})

    m.fs.params = PropertyInterrogatorBlock()
    m.fs.rxn_params = ReactionInterrogatorBlock(
            default={"property_package": m.fs.params})

    m.fs.R01 = CSTR(default={"property_package": m.fs.params,
                             "reaction_package": m.fs.rxn_params,
                             "has_heat_of_reaction": True})

    m.fs.R02 = PFR(default={"property_package": m.fs.params,
                            "reaction_package": m.fs.rxn_params})

    return m


# Test for physical parameters too, as these can not be checked without having
# a reaction package too.
def test_interrogate_flowsheet(model):
    assert model.fs.params.required_properties == {
            "material flow terms": ["fs.R01", "fs.R02"],
            "enthalpy flow terms": ["fs.R01", "fs.R02"],
            "material density terms": ["fs.R01", "fs.R02"],
            "energy density terms": ["fs.R01", "fs.R02"],
            "pressure": ["fs.R01", "fs.R02"]}

    assert model.fs.rxn_params.required_properties == {
            "reaction_rate": ["fs.R01", "fs.R02"],
            "dh_rxn": ["fs.R01"]}


def test_list_required_properties(model):
    prop_list = model.fs.params.list_required_properties()
    assert prop_list == ["material density terms",
                         "material flow terms",
                         "enthalpy flow terms",
                         "energy density terms",
                         "pressure"]

    rxn_list = model.fs.rxn_params.list_required_properties()
    assert rxn_list == ["dh_rxn", "reaction_rate"]


def test_list_models_requiring_property(model):
    for k in model.fs.params.required_properties.keys():
        model_list = model.fs.params.list_models_requiring_property(k)
        assert model_list == ["fs.R01", "fs.R02"]


def test_list_properties_required_by_model_by_name(model):
    prop_list = model.fs.rxn_params.list_properties_required_by_model("fs.R01")

    assert prop_list == ["dh_rxn",
                         "reaction_rate"]


def test_list_properties_required_by_model_by_object(model):
    prop_list = model.fs.rxn_params.list_properties_required_by_model(
            model.fs.R01)

    assert prop_list == ["dh_rxn",
                         "reaction_rate"]


def test_list_properties_required_by_model_invalid_model(model):
    with pytest.raises(ValueError):
        model.fs.rxn_params.list_properties_required_by_model("foo")


def test_print_required_properties(model, capsys):
    model.fs.params.print_required_properties()
    model.fs.rxn_params.print_required_properties()

    captured = capsys.readouterr()
    assert captured.out == """
==========================================================================
Property Interrogator Summary

The Flowsheet requires the following properties (times required):

    material density terms                                               2
    material flow terms                                                  2
    enthalpy flow terms                                                  2
    energy density terms                                                 2
    pressure                                                             2

==========================================================================
Reaction Property Interrogator Summary

The Flowsheet requires the following reaction properties (times required):

    dh_rxn                                                               1
    reaction_rate                                                        2
"""


def test_print_models_requiring_property(model, capsys):
    model.fs.rxn_params.print_models_requiring_property("reaction_rate")

    captured = capsys.readouterr()
    assert captured.out == """
The following models in the Flowsheet require reaction_rate:
    fs.R01
    fs.R02
"""


def test_print_properties_reqruied_by_model(model, capsys):
    model.fs.rxn_params.print_properties_required_by_model("fs.R01")

    captured = capsys.readouterr()
    assert captured.out == """
The following reaction properties are required by model fs.R01:
    dh_rxn
    reaction_rate
"""
