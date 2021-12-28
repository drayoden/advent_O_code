use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    const MAXX: usize = 1000;
    const MAXY: usize = 1000;

    let mut light_array = [[false; MAXX]; MAXY];
    let fname =  "./input.txt"; 

    let _f = File::open(fname).expect("file not found...");
    let _r = BufReader::new(_f);

    for(_l, line) in _r.lines().enumerate() {
        let line = line.unwrap();
        let line = line.trim(); 
        let mut _light: bool = true;

        // first split -- length will determine if we have 'turn' or 'toggle'
        let line_vec:Vec<&str> = line.split(' ').collect();

        // line_vec.len() = 5 --> 'turn' we need elements 1, 2 & 4
        if line_vec.len() == 5 {
            let from_vec: Vec<&str> = line_vec[2].split(',').collect();  
            let dest_vec: Vec<&str> = line_vec[4].split(',').collect(); 
            let action = line_vec[1];
            
            // will the light be turned on or off: 
            let _light = if action == "off" { false } else { true };
            
            let fromx: usize = from_vec[0].parse().unwrap(); 
            let fromy: usize = from_vec[1].parse().unwrap(); 
            let destx: usize = dest_vec[0].parse().unwrap(); 
            let desty: usize = dest_vec[1].parse().unwrap(); 

            println!("{},{} to {},{} -- turn {}", fromx,fromy,destx,desty,action);

            // set the lights to on (true) or off (false)
            for i in fromx ..= destx {
                for j in fromy ..= desty {
                    // println!("[{}][{}]", i, j); 
                    light_array[i][j] = _light; 
                }
            }
        
        // line_vec.len() = 4 --> 'toggle' we need elements 1 & 3
        } else {
            let from_vec: Vec<&str> = line_vec[1].split(',').collect();  
            let dest_vec: Vec<&str> = line_vec[3].split(',').collect();  

            let fromx: usize = from_vec[0].parse().unwrap(); 
            let fromy: usize = from_vec[1].parse().unwrap(); 
            let destx: usize = dest_vec[0].parse().unwrap(); 
            let desty: usize = dest_vec[1].parse().unwrap(); 

            println!("{},{} to {},{} -- {}", fromx,fromy,destx,desty,"toggle");

            // toggle the light in light_array:
            for i in fromx ..= destx {
                for j in fromy ..= desty {
                    light_array[i][j] = !light_array[i][j];  
                }
            }
        }

        
    }
    countlights(&mut light_array)
 
}

fn countlights(a: &mut [[bool; 1000]; 1000]) {
    let mut on_lights = 0;
    for i in 0 ..= 999 {
        for j in 0 ..= 999 {
            if a[i][j] {
                on_lights += 1; 
            }
        }
    }
    println!("lights turned on: {}", on_lights)
}
