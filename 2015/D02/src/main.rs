//use std::env; 
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let fname = "./input.txt";

    let _f = File::open(fname).expect("file not found...");
    let _r = BufReader::new(_f);

    let mut gtotal: u32 = 0;
    let mut ribbon: u32 = 0; 

    for(_i, line) in _r.lines().enumerate() {
        let tline = line.unwrap();
        let tline = tline.trim();

        println!("{}", tline);

        // split the line with delimiter 'x':
        let vline:Vec<&str> = tline.split('x').collect();

        let l: u32 = vline[0].parse().unwrap_or(0);
        let w: u32 = vline[1].parse().unwrap_or(0);
        let h: u32 = vline[2].parse().unwrap_or(0);
        let mut min: u32 = 0;
        let vol: u32 = l * w * h; 
        let mut per: u32 = 0; 

        let lw = l*w;
        let wh = w*h;
        let lh = l*h;

        // find the smallest side (square units) and 
        // calculate the permimeter of that side:
        if lw < wh {
            min = lw;
            per = l+l+w+w;  
        } else {
            min = wh;
            per = w+w+h+h;
        }

        if lh < min {
            min = lh;
            per = l+l+h+h;
        }




        //let min = if lw < wh { lw } else { wh };
        //let min = if lh < min { lh } else { min }; 

        // find the smallest perimeter:
        //let per = if min == lw {l+l+w+w} else {0};
        //let per = if min == wh {w+w+h+h} else {0};
        //let per = if min == lh {l+l+h+h} else {0};
        

        let total = 2*lw + 2*wh + 2*lh + min;
        gtotal += total; 
        ribbon += (per + vol);


        println!("LW:{} WH:{} LH:{}", lw,wh,lh); 
        println!("min: {}", min);
        println!("box perimeter: {}", per);
        println!("box paper: {}", total);
        println!("box ribbon: {}\n", per + vol);
        
    }
    println!("Total paper: {}", gtotal);
    println!("Total ribbon: {}", ribbon);
}

