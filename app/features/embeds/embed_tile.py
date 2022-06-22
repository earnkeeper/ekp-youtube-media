from ekp_sdk.ui import (Chart, Col, Div, Image, Link, Row, Span, commify,
                        ekp_map, format_currency, format_percent,
                        format_template, json_array, sort_by, Icon)


def embed_tile():
    return Div(
        context="$.data[0]",
        children=[
            Row(
                [
                    chart_row,
                    Col(
                        "col-12 px-2",
                        [
                            Div(
                                style={"marginTop": "-12px"},
                                children=[
                                    Row(
                                        [
                                            details_row,
                                        ]
                                    )

                                ]
                            ),

                        ]
                    )
                ],
                "p-0"
            )
        ]
    )


details_row = Col(
    "col-12",
    [
        Div(
            style={"marginTop": "8px"},
            children=[
                Div(
                    style={
                        "position": "absolute",
                        "top": 0,
                        "left": 0,
                        "zIndex": 0,
                        "width": "320px",
                        "marginLeft": "7px",
                        "height": "103px",
                        "borderRadius": "0px 0px 5px 5px",
                        "background": format_template("url({{{ bg }}})", {
                            "bg": "$.banner_url"
                        }),
                        "backgroundRepeat": "no-repeat",
                        "backgroundSize": "cover",
                    },
                ),
                Div(
                    class_name="right-to-left-fade",
                    style={
                        "position": "absolute",
                        "top": 0,
                        "left": 0,
                        "zIndex": 1,
                        "width": "320px",
                        "marginLeft": "7px",
                        "height": "103px",
                        "borderRadius": "0px 0px 5px 5px",
                    },
                ),
                Div(
                    style={
                        "position": "absolute",
                        "top": 0,
                        "left": 7,
                        "width": "314px",
                        "zIndex": 2,
                        "marginLeft": "8px"
                    },
                    children=[
                        Div(style={"height": "8px"}),
                        Link(
                            href="$.page",
                            content=format_template("{{ rank }}. {{ name }}", {
                                "rank": "$.rank",
                                "name": "$.game_name"
                            }),
                            external_icon=True
                        ),
                        Div(style={"height": "8px"}),
                        Span("New Followers (24h)",
                             "d-block font-small-3"),
                        Span(
                            commify("$.change_24h"),
                            format_template(
                                "d-block font-small-2 text-{{ color }}",
                                {
                                    "color": "$.change_24h_color"
                                }
                            )
                        ),
                        Div(style={"height": "3px"}),
                        # Span("Change (24h)",
                        #      "d-block font-small-3"),
                        # Span(
                        #     format_percent(
                        #         "$.change_24h_pc",
                        #         True,
                        #         3
                        #     ),
                        #     format_template(
                        #         "d-block font-small-2 text-{{ color }}",
                        #         {
                        #             "color": "$.change_24h_color"
                        #         }
                        #     )
                        # ),
                    ]
                )
            ])

    ]
)

chart_row = Col(
    "col-12 px-0",
    [
        Div(
            style={"marginRight": "4px", "marginLeft": "-8px"},
            children=[
                Chart(
                    title="",
                    height=174,
                    type="line",
                    data="$.chart.*",
                    card=False,
                    options={
                        "legend": {
                            "show": False
                        },
                        "chart": {
                            "zoom": {
                                "enabled": False,
                            },
                            "toolbar": {
                                "show": False,
                            },
                            "stacked": False,
                            "type": "line"
                        },
                        "xaxis": {
                            "type": "datetime",
                            "labels": {"show": False}
                        },
                        "yaxis": [
                            {
                                "labels": {
                                    "show": False,
                                    "formatter": commify("$")
                                },
                            },
                        ],
                        "colors": ["#F76D00"],
                        "labels": ekp_map(
                            sort_by(
                                json_array(
                                    "$.chart.*"
                                ),
                                "$.timestamp_ms"
                            ), "$.timestamp_ms"
                        ),
                        "stroke": {
                            "width": [4, 4],
                            "curve": 'smooth',
                            "colors": ["#F76D00"]
                        }
                    },
                    series=[
                        {
                            "name": "New Followers",
                            "type": "line",
                            "data": ekp_map(
                                    sort_by(
                                        json_array("$.chart.*"),
                                        "$.timestamp_ms"
                                    ),
                                "$.value"
                            ),
                        },
                    ],
                )
            ]),

    ]
)
