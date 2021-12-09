// 2015 Day3 part 1

use std::fs;
//use std::env; 

fn main() {
    let fname = "./input.txt";

    // read entire file?
    let _input = fs::read_to_string(fname).expect("file not found..."); 
    let mut dir = "";
    let mut coor_x = 0i32;
    let mut coor_y = 0i32; 
    let mut house_coord = vec![(0i32,0i32)];  // initialize with coorXY: 0,0 
    let mut t_tuple : (i32,i32);  // temp touple       

    println!("starting corr: {:?}",house_coord);

    for c in _input.chars() {

        match c {
            '>' => {
                dir = "E"; 
                coor_x += 1
                }
            'v' => {
                dir = "S"; 
                coor_y -= 1
                }
            '<' => {
                dir = "W"; 
                coor_x -= 1
            }
            '^' => {
                dir = "N"; 
                coor_y += 1
            } 
            _ => {},  // all other cases
        }

        // create a vector of touples (x,y):
        t_tuple = (coor_x,coor_y); 
        
        // create an iterator from the current house_coord vector:
        let mut iter = house_coord.iter();

        // if the current t_tuple does not exist in the vector, add it:
        if iter.find( |&&x| x == t_tuple ) == None {
            house_coord.push(t_tuple);
        }

        println!("char: {} -- dir: {} -- coor: {:?} -- ht: {}" ,c ,dir, t_tuple, house_coord.len() ); 

    }

    // number of houses visited will be the length of the vector.
 
    
    
}