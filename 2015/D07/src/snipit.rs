use std::fs::File;
use std::io::{BufRead, BufReader};

// AND, OR, NOT, LSHIFT, RSHIFT

fn main() {
    let fname =  "./input.txt"; 
    let file = File::open(fname).unwrap();
    
    for line in BufReader::new(file).lines() {
        
        let line_vec:Vec<&str> = line.split("->").collect(); 
        // let ow = line_vec[1];
        // let gate_vec:Vec<&str> = line_vec[0].split(' ').collect();

        println!("[0]{}", line_vec[0]);


        // match action {
        //     "AND" => {}
        //     "OR" => {}
        //     "NOT" => {}
        //     "RSHIFT" => {}
        //     "LSHIFT" => {}
            
        //     _ => {},
        // }
    
    }
    
}
