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
                        children=[
                            Link(
                                class_name="pl-1 pr-2",
                                href="$.page",
                                content="$.search_query",
                                external_icon=True
                            ),
                        ]
                    ),
                    Div(
                        class_name="pl-1 pr-2",
                        children=[
                            Link(
                                class_name="font-small-3",
                                href="$.link",
                                external=True,
                                content="$.title",
                            ),
                        ]
                    ),
                    Div(
                        class_name="ml-1 mr-2 mt-1",
                        children=[
                            Row(
                                children=[
                                    Col(
                                        class_name="col-auto",
                                        children=[
                                            # Icon(
                                            #     "user",
                                            #     size='sm',
                                            #     style={
                                            #         "marginRight": "6px"
                                            #     }
                                            # ),
                                            Span("$.channel_name", "font-small-3")
                                        ]
                                    ),
                                    Col(
                                        class_name="col-auto",
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
                    Div(
                        class_name="ml-1 mr-2 mt-1",
                        children=[
                            Row(
                                children=[
                                    Col(
                                        class_name="col-auto",
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
                                        class_name="col-auto",
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

