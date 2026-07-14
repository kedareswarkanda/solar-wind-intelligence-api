from app.data_sources.nasa_power import NASAPowerClient


class SolarFeatureEngineer:
    """
    Service responsible for engineering solar resource features using the NASA POWER client.
    """

    def __init__(self, nasa_client: NASAPowerClient):
        """
        Initialize the SolarFeatureEngineer with a NASAPowerClient.

        Args:
            nasa_client (NASAPowerClient): The injected client for NASA POWER dataset.
        """
        self._nasa_client = nasa_client
