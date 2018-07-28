import logging

logger = logging.getLogger(__name__)

class Plot:
    def __init__(self):
        pass

    def plot(self, datetime_dict, value_labels, values_dim):
        raise NotImplementedError

class MatPlot(Plot):

    def __init__(self):
        try:
            import matplotlib.pyplot as plt
            self.plt = plt
        except ImportError:
            self.plt = None
            
    def plot(self, datetime_dict, value_labels, values_dim = 1):
        time_axis = sorted(datetime_dict.keys())
        values_arr = []
        for i in range(0, values_dim):
            values_arr.append([])
        for key, arr in sorted(datetime_dict.items()):
            assert len(arr) == values_dim
            for i in range(0, values_dim):
                values_arr[i].append(arr[i])
    
        for i in range(0, values_dim):
            self.plt.plot(time_axis, values_arr[i], value_labels[i])
        self.plt.show()

class PyPlot:
    def __init__(self):
        import numpy as np
        import plotly.graph_objs as go
        import plotly.plotly as py
        from plotly.offline import plot as plotly_plot
        self.np = np
        self.go = go
        self.py = py
        self.plotly_plot = plotly_plot

    def plot(self, datetime_dict, value_labels, values_dim):
        time_axis = sorted(datetime_dict.keys())
        values_arr = []
        for i in range(0, values_dim):
            values_arr.append([])
        for key, arr in sorted(datetime_dict.items()):
            assert len(arr) == values_dim
            for i in range(0, values_dim):
                values_arr[i].append(arr[i])

        data = []
        for i in range(0, values_dim):  
            trace = self.go.Scatter(
                x=time_axis,
                y=values_arr[i],
                name=value_labels[i]
            )
            data.append(trace)

        layout = self.go.Layout(
            # autosize=False,
            # width=900,
            # height=500,

            xaxis=dict(
                autorange=True
            ),
            yaxis=dict(
                autorange=True
            )
        )
        fig = self.go.Figure(data=data, layout=layout)
        plot_div = self.plotly_plot(fig, output_type='div', include_plotlyjs=False)
        #py.iplot(data, filename='line-mode')
        logger.info("Plotting number of points {}.".format(len(time_axis)))
        return plot_div