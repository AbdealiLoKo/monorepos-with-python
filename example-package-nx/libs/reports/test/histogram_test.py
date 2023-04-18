import plotly.graph_objects as go

from corridor.data_lake.dataset import Dataset
from corridor.reports.histogram import HistogramChart


def test_histogram_create() -> None:
    ownsership_data = Dataset(name="home_ownership")
    chart = HistogramChart(ownsership_data, "home_ownership", "age")
    assert isinstance(chart.create_figure(), go.Figure)
