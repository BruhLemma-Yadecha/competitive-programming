use std::io::{self, BufRead};

fn main() {
    // take in the number of lines
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let t = line.trim().parse::<u32>().unwrap();
    for _ in 0..t {
        line.clear();
        io::stdin().read_line(&mut line).unwrap();
        io::stdin().read_line(&mut line).unwrap();
        println!("{}", line.trim().chars().last().unwrap());
    }
}