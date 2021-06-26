fn main() -> wry::Result<()> {
    use wry::{
        application::{
            event_loop::{ControlFlow, EventLoop},
            window::WindowBuilder,
        },
        webview::WebViewBuilder,
    };
    let event_loop = EventLoop::new();
    let window = WindowBuilder::new()
        .with_title("Discord Rust")
        .build(&event_loop)?;
    let _webview = WebViewBuilder::new(window)?
        .with_url("https://discord.com/app")?
        .build()?;
    event_loop.run(move |event, _, control_flow| {
        *control_flow = ControlFlow::Wait;

        match event {
            _ => (),
        }
    });
}
