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

    // Create a shape
    let box_shape = ShapeKind::new_box("Example Box");
    let mut style = StyleAttr::simple();
    style.fill_color = Some(Color::fast("lightblue"));
    style.line_color = Color::fast("black");

    // Define size and orientation
    let size = Point::new(200.0, 100.0);
    let mut element = Element::create(box_shape, style, Orientation::LeftToRight, size);

    // Position the shape
    element.move_to(Point::new(100.0, 100.0));
    element.render(false, &mut svg);

    // Save the SVG file
    let content = svg.finalize();
    save_to_file("/Users/youngermaster/GitHub/Youngermaster/Learning-Programming-Languages/Rust/graphviz_layout_automaton/example.svg", &content).expect("Failed to save SVG");
    println!("SVG file saved at /Users/youngermaster/GitHub/Youngermaster/Learning-Programming-Languages/Rust/graphviz_layout_automaton/example.svg");
}
