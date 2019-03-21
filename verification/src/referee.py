from checkio_referee import RefereeRank


import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "between_markers"
    FUNCTION_NAMES = {
        "python_3": "between_markers",
        "js_node": "betweenMarkers"
    }