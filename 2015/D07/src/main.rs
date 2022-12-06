
fn main() {
    let and = Gate::AND('&');
    let ls  = Gate::LS("<<".to_string());
    let not = Gate::NOT('&');
    let or  = Gate::OR('|');
    let rs = Gate::RS(">>".to_string());

    println!("testing struct/enums...");

    println!("parse the node line...");
    let node = Node {
        wL: 2,
        wR: 6,
        wO: 0,
        GT: and,
    };

    println!("node: {} {} {} {}", node.wL, node.wR, node.wO, node.GT);
}

struct Node {
    wL: i32,
    wR: i32,
    wO: i32,
    GT: Gate,
}

enum Gate {
    AND(char),
    LS(String),
    NOT(char),
    OR(char),
    RS(String), 
}

trait Printgate {
    fn print_gate(&self){}
}

impl Printgate for String {
    fn print_gate(&self){}
}

impl Printgate for char {
    fn print_gate(&self){}
}

impl std::fmt::Display for Gate {
    fn fmt($self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let x =
        write!(f,)
    }
}

