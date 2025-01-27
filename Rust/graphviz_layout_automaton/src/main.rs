use layout::backends::svg::SVGWriter;
use layout::core::base::Orientation;
use layout::core::color::Color;
use layout::core::format::{RenderBackend, Renderable, Visible};
use layout::core::geometry::{segment_rect_intersection, Point};
use layout::core::style::{LineStyleKind, StyleAttr};
use layout::core::utils::save_to_file;
use layout::std_shapes::render;
use layout::std_shapes::render::get_shape_size;
use layout::std_shapes::shapes::*;

fn main() {
    // Initialize SVG Writer
    let mut svg = SVGWriter::new();

    // Define state size and style
    let state_size = Point::new(100.0, 100.0);
    let mut state_style = StyleAttr::simple();
    state_style.fill_color = Some(Color::fast("lightblue"));
    state_style.line_color = Color::fast("black");

    // Create states
    let mut start_state = Element::create(
        ShapeKind::new_circle("Start"),
        state_style.clone(),
        Orientation::LeftToRight,
        state_size,
    );

    let mut accept_state = Element::create(
        ShapeKind::new_double_circle("Accept"),
        state_style.clone(),
        Orientation::LeftToRight,
        state_size,
    );

    let mut state_q1 = Element::create(
        ShapeKind::new_circle("q1"),
        state_style.clone(),
        Orientation::LeftToRight,
        state_size,
    );

    // Position states
    start_state.move_to(Point::new(100.0, 200.0));
    state_q1.move_to(Point::new(300.0, 200.0));
    accept_state.move_to(Point::new(500.0, 200.0));

    // Render states
    start_state.render(false, &mut svg);
    state_q1.render(false, &mut svg);
    accept_state.render(false, &mut svg);

    // Define transition style
    let transition_style = StyleAttr::simple();
    let transition = Arrow::new(
        LineEndKind::None,
        LineEndKind::Arrow,
        LineStyleKind::Normal,
        "a",
        &transition_style,
        &None,
        &None,
    );

    // Render transitions
    render::render_arrow(
        &mut svg,
        false,
        &[start_state.clone(), state_q1.clone()],
        &transition,
    );

    render::render_arrow(
        &mut svg,
        false,
        &[state_q1.clone(), accept_state.clone()],
        &transition,
    );

    render::render_arrow(
        &mut svg,
        false,
        &[accept_state.clone(), state_q1.clone()],
        &transition,
    );

    // Save the SVG file
    let content = svg.finalize();
    let filename = "/Users/youngermaster/GitHub/Youngermaster/Learning-Programming-Languages/Rust/graphviz_layout_automaton/automaton.svg";
    save_to_file(filename, &content).expect("Failed to save SVG");
    println!("SVG file saved at {}", filename);
}
