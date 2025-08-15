import reflex as rx

config = rx.Config(
    app_name="AIAgentPlatform",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)