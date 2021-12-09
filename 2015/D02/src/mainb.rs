use std::io;


fn main() {

    let mut gtotal = 0;


    // infinite loop to take stdin from a piped file
    loop {
        

        // mutable variable
        let mut input = String::new();
        let mut total : u32 = 0;

       
        // like a try/catch:
        match io::stdin().read_line(&mut input) {
            Ok(len) => if len == 0 {
                return;
            } else {
                                
                // remove newline: 
                let input = input.trim(); 

                print!("{}\n", input);

                // split the line with delimiter 'x':
                let vline:Vec<&str> = input.split('x').collect();

                let l: u32 = vline[0].parse().unwrap_or(0);
                let w: u32 = vline[1].parse().unwrap_or(0);
                let h: u32 = vline[2].parse().unwrap_or(0);

                let mut ivec: Vec<u32> = vec![]; 

                let lw = l*w;
                let lh = l*h;
                let wh = w*h; 

                ivec.push(lw);
                ivec.push(wh);
                ivec.push(lh); 

                let min = ivec.iter().min(); 

                total = (2*lw) + (2*lh) + (2*wh);
                print!("LW:{}  WH:{}  LH:{}\n", lw,wh,lh);
                
                match min {
                    None => println!("Oops!"),
                    Some(i) => println!("min: {}", i)
                }
                print!("total: {}\n\n",total);

                gtotal += total; 

            }

            Err(error) => {
                eprintln!("ERR: {}", error);
                
                break;
            }
        }
        
    }
    println!("{}", gtotal); 
    println!("done...");


}
