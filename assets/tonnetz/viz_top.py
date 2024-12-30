from viz_imports import *

""" independent figures """

for raag, gt_nodes in raag_gt_nodes.items():
    fig = go.Figure(
        data=[
            go.Scatter(
                x=tn.coords3d[0],
                y=tn.coords3d[1],
                mode="text+markers",
                marker=dict(
                    size=DOT_SIZE,
                    symbol="circle",
                    color=[
                        NODE_ORANGE if coord in gt_nodes else DARK_GREY
                        for coord in tn.node_coordinates
                    ],
                ),
                text=tn.node_names,
                textposition="middle center",
                textfont=dict(family="Overpass", size=DOT_LABEL_SIZE, color="white"),
            )
        ]
    )

    # axes
    fig.update_layout(
        # title=f"Raag {raag}",
        xaxis_title="powers of 3",
        yaxis_title="powers of 5",
        plot_bgcolor=BG_GREY,
        width=820,
        height=500,
    )
    fig.update_xaxes(tickvals=np.arange(-4, 5))
    fig.update_yaxes(tickvals=np.arange(-2, 3))

    fig.update_layout(margin=dict(l=60, r=30, t=30, b=60))
    fig.write_image(f"images/raag_{raag.lower()}.png", scale=1.5)
