from ekp_sdk.ui import (Chart, Col, Div, Image, Link, Row, Span, commify,
                        ekp_map, format_currency, format_percent,
                        format_template, json_array, sort_by, Icon, format_age)


def embed_tile():
    return Div(
        context="$.data[0]",
        children=[
            Div(
                style={"width": "320px"},
                children=[
                    Div(
                        children=[
                            Image(
                                class_name="mb-1",
                                src="$.thumbnail",
                                style={"height": "150px", "width": "100%"}
                            ),
                        ]
                    ),
                    Div(
                        class_name="px-1",
                        children=[
                            Link(
                                href="$.page",
                                content="$.game_name",
                                external_icon=True
                            ),
                        ]
                    ),
                    Div(style={"height": "4px"}),
                    Div(
                        class_name="px-1",
                        children=[
                            Link(
                                class_name="font-small-3",
                                href="$.link",
                                external=True,
                                content="$.title",
                            ),
                        ]
                    ),
                    Div(style={"height": "8px"}),
                    Div(
                        class_name="px-1",
                        children=[
                            Row(
                                children=[
                                    Col(
                                        class_name="col-6",
                                        children=[
                                            Span("$.channel_name", "font-small-3")
                                        ]
                                    ),
                                    Col(
                                        class_name="col-6",
                                        children=[
                                            Icon(
                                                "users",
                                                size='sm',
                                                style={
                                                    "marginRight": "6px"
                                                }
                                            ),
                                            Span(
                                                format_template(
                                                    "{{ subscribers_count }} subs",
                                                    {"subscribers_count": "$.subscribers_count"}
                                                )
                                                , "font-small-2")
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    Div(style={"height": "8px"}),
                    Div(
                        class_name="px-1",
                        children=[
                            Row(
                                children=[
                                    Col(
                                        class_name="col-6",
                                        children=[
                                            Icon(
                                                "calendar",
                                                size='sm',
                                                style={
                                                    "marginRight": "6px"
                                                }
                                            ),
                                            Span(format_age("$.publish_time"), "font-small-2")
                                        ]
                                    ),
                                    Col(
                                        class_name="col-6",
                                        children=[
                                            Icon(
                                                "eye",
                                                size='sm',
                                                style={
                                                    "marginRight": "6px"
                                                }
                                            ),
                                            Span("$.view_count", "font-small-2")
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )

