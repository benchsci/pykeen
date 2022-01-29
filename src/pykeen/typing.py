# -*- coding: utf-8 -*-

"""Type hints for PyKEEN."""

from typing import Callable, Mapping, NamedTuple, Sequence, TypeVar, Union, cast

import numpy as np
import torch
from class_resolver import Hint, HintOrType, HintType
from typing_extensions import Literal

__all__ = [
    # General types
    "Hint",
    "HintType",
    "HintOrType",
    "Mutation",
    "OneOrSequence",
    # Triples
    "LabeledTriples",
    "MappedTriples",
    "EntityMapping",
    "RelationMapping",
    # Others
    "DeviceHint",
    "TorchRandomHint",
    # Tensor Functions
    "Initializer",
    "Normalizer",
    "Constrainer",
    "cast_constrainer",
    # Tensors
    "HeadRepresentation",
    "RelationRepresentation",
    "TailRepresentation",
    # Dataclasses
    "GaussianDistribution",
    "ScorePack",
    # prediction targets
    "Target",
    "LABEL_HEAD",
    "LABEL_RELATION",
    "LABEL_TAIL",
    "TargetColumn",
    "COLUMN_HEAD",
    "COLUMN_RELATION",
    "COLUMN_TAIL",
]

X = TypeVar("X")

#: A function that mutates the input and returns a new object of the same type as output
Mutation = Callable[[X], X]
OneOrSequence = Union[X, Sequence[X]]

LabeledTriples = np.ndarray
MappedTriples = torch.LongTensor
EntityMapping = Mapping[str, int]
RelationMapping = Mapping[str, int]

#: A function that can be applied to a tensor to initialize it
Initializer = Mutation[torch.FloatTensor]
#: A function that can be applied to a tensor to normalize it
Normalizer = Mutation[torch.FloatTensor]
#: A function that can be applied to a tensor to constrain it
Constrainer = Mutation[torch.FloatTensor]


def cast_constrainer(f) -> Constrainer:
    """Cast a constrainer function with :func:`typing.cast`."""
    return cast(Constrainer, f)


#: A hint for a :class:`torch.device`
DeviceHint = Hint[torch.device]
#: A hint for a :class:`torch.Generator`
TorchRandomHint = Union[None, int, torch.Generator]

Representation = TypeVar("Representation", bound=OneOrSequence[torch.FloatTensor])
#: A type variable for head representations used in :class:`pykeen.models.Model`,
#: :class:`pykeen.nn.modules.Interaction`, etc.
HeadRepresentation = TypeVar("HeadRepresentation", bound=OneOrSequence[torch.FloatTensor])
#: A type variable for relation representations used in :class:`pykeen.models.Model`,
#: :class:`pykeen.nn.modules.Interaction`, etc.
RelationRepresentation = TypeVar("RelationRepresentation", bound=OneOrSequence[torch.FloatTensor])
#: A type variable for tail representations used in :class:`pykeen.models.Model`,
#: :class:`pykeen.nn.modules.Interaction`, etc.
TailRepresentation = TypeVar("TailRepresentation", bound=OneOrSequence[torch.FloatTensor])


class GaussianDistribution(NamedTuple):
    """A gaussian distribution with diagonal covariance matrix."""

    mean: torch.FloatTensor
    diagonal_covariance: torch.FloatTensor


class ScorePack(NamedTuple):
    """A pair of result triples and scores."""

    result: torch.LongTensor
    scores: torch.FloatTensor


Sign = Literal[-1, 1]

#: the prediction target
Target = Literal["head", "relation", "tail"]
LABEL_HEAD: Target = "head"
LABEL_RELATION: Target = "relation"
LABEL_TAIL: Target = "tail"

#: the prediction target index
TargetColumn = Literal[0, 1, 2]
COLUMN_HEAD: TargetColumn = 0
COLUMN_RELATION: TargetColumn = 1
COLUMN_TAIL: TargetColumn = 2
