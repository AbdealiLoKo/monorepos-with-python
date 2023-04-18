import plotly.graph_objects as go

from corridor.data_lake.dataset import Dataset


class HistogramChart:
    def __init__(self, dataset: Dataset, x: str, y: str) -> None:
        self.dataset = dataset
        self.x = x
        self.y = y

    def create_figure(self) -> go.Figure:
        df = self.dataset.read()
        histogram = df.groupby(self.x)[self.y].mean().to_frame().reset_index()

        return go.Figure(
            data=[go.Bar(x=histogram[self.x], y=histogram[self.y])],
            layout=go.Layout(
                title={"text": "Histogram"},
                xaxis={"title": {"text": "Values / Bins"}},
                yaxis={"title": {"text": "Count"}},
            ),
        )

    def show(self) -> None:
        """Show the figure (if using jupyter notebooks)"""
        fig = self.create_figure()
        fig.plot()

    def save(self, location: str) -> None:
        fig = self.create_figure()
        fig.write_png(location)
