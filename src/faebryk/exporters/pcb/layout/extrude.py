# This file is part of the faebryk project
# SPDX-License-Identifier: MIT

import logging
from dataclasses import dataclass

from faebryk.core.core import (
    Node,
)
from faebryk.exporters.pcb.layout.layout import Layout
from faebryk.library.has_pcb_position import has_pcb_position
from faebryk.library.has_pcb_position_defined_relative_to_parent import (
    has_pcb_position_defined_relative_to_parent,
)

logger = logging.getLogger(__name__)


@dataclass
class LayoutExtrude(Layout):
    vector: tuple[float, float]

    def apply(self, *node: Node):
        """
        Tip: Make sure at least one parent of node has an absolute position defined
        """
        for i, n in enumerate(node):
            pos = (self.vector[0] * i, self.vector[1] * i)
            n.add_trait(
                has_pcb_position_defined_relative_to_parent(
                    (pos[0], pos[1], 0, has_pcb_position.layer_type.NONE)
                )
            )
