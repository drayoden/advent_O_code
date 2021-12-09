// 2015 Day3 part 2

// answer1: 2499 -- high 
// answer2: 2361 -- high -> this does not account for the origin (0,0) in both vectors
// answer3: 2360 -- Yeah!

use std::fs;
 

fn main() {
    let fname = "./input.txt";

    // read entire file
    let _input = fs::read_to_string(fname).expect("file not found..."); 
    let mut dir = "";

    // need to keep track of the coordinates
    // of each santa:
    let mut sacoor_x = 0i32;
    let mut sacoor_y = 0i32;
    let mut rscoor_x = 0i32;
    let mut rscoor_y = 0i32;
    
    // using two vectors; santa (sa) and robo santa (rs)
    let mut sa_coord = vec![(0i32,0i32)];  // initialize with coorXY: 0,0 
    let mut rs_coord = vec![(0i32,0i32)];  // initialize with coorXY: 0,0
    
    // bool to toggle between santa and robo santa: 
    // true = santa, false = robo santa, starts with santa
    let mut santa = true; 

    // temp touple       
    let mut t_tuple : (i32,i32);  

    println!("both santas start here: {:?}",sa_coord);

    for c in _input.chars() {

        match c {
            '>' => {
                dir = "E"; 
                if santa { sacoor_x += 1 } else { rscoor_x += 1 }
                }
            'v' => {
                dir = "S"; 
                if santa { sacoor_y -= 1 } else { rscoor_y -= 1 }
                }
            '<' => {
                dir = "W"; 
                if santa { sacoor_x -= 1 } else {rscoor_x -= 1 }
            }
            '^' => {
                dir = "N"; 
                if santa { sacoor_y += 1 } else {rscoor_y += 1 }
            } 
            _ => {},  // all other cases
        }
 
        // create iterators for both vectors:
        let mut sa_iter = sa_coord.iter();
        let mut rs_iter = rs_coord.iter();


        if santa {  // santa -- check robo santa vector first
            t_tuple = (sacoor_x,sacoor_y);
            if rs_iter.find(|&&x| x == t_tuple) == None {
                if sa_iter.find(|&&x| x == t_tuple) == None {
                    sa_coord.push(t_tuple);
                }
            }
        } else {    // robo santa -- check santa vector first
            t_tuple = (rscoor_x,rscoor_y);
            if sa_iter.find(|&&x| x == t_tuple) == None {
                if rs_iter.find(|&&x| x == t_tuple) == None {
                    rs_coord.push(t_tuple);
                } 
            }
        }

        println!("char: {} -- dir: {} -- SAcoor: ({},{}) -- RScoor: ({},{}) -- SAt: {} -- RSt: {}" ,c ,dir, sacoor_x, sacoor_y, rscoor_x, rscoor_y, sa_coord.len(), rs_coord.len() ); 

        santa = !santa; // toggle santa
    }
}