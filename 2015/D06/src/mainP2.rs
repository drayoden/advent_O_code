use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    const MAXX: usize = 1000;
    const MAXY: usize = 1000;

    let mut light_array = [[0; MAXX]; MAXY];
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
                    
            let fromx: usize = from_vec[0].parse().unwrap(); 
            let fromy: usize = from_vec[1].parse().unwrap(); 
            let destx: usize = dest_vec[0].parse().unwrap(); 
            let desty: usize = dest_vec[1].parse().unwrap(); 

            println!("{},{} to {},{} -- turn {}", fromx,fromy,destx,desty,action);


            // action=off --1 (min of 0), action=on ++1
            
            for i in fromx ..= destx {
                for j in fromy ..= desty {
                    // println!("[{}][{}]", i, j); 
                    if action == "off" { 
                        if light_array[i][j] > 0 {
                            light_array[i][j] -= 1;
                        } 
                    } else {
                        light_array[i][j] += 1;
                    }
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
                    light_array[i][j] += 2;  
                }
            }
        }

        
    }
    getbrightness(light_array)
 
}

fn getbrightness(a: [[u16; 1000]; 1000]) {
    let mut brightness = 0u32;
    for i in 0 ..= 999 {
        for j in 0 ..= 999 {
            brightness += a[i][j] as u32;
        }
    }
    println!("brighness: {}", brightness)
}
