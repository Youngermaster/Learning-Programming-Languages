fn main() -> wry::Result<()> {
    let video_url = "https://www.youtube.com/channel/UCyuYHymUH4Adj2YytTdtD4g/videos";
    let program_name = "YouTube WRY Test";
    use wry::{
        application::{
            event::{Event, StartCause, WindowEvent},
            event_loop::{ControlFlow, EventLoop},
            window::WindowBuilder,
        },
        webview::WebViewBuilder,
    };

    let event_loop = EventLoop::new();
    let window = WindowBuilder::new()
        .with_title(program_name)
        .build(&event_loop)?;
    let _webview = WebViewBuilder::new(window)?.with_url(video_url)?.build()?;

    event_loop.run(move |event, _, control_flow| {
        *control_flow = ControlFlow::Wait;

        match event {
            Event::NewEvents(StartCause::Init) => println!("Wry has started!"),
            Event::WindowEvent {
                event: WindowEvent::CloseRequested,
                ..
            } => *control_flow = ControlFlow::Exit,
            _ => (),
        }
    });
}
