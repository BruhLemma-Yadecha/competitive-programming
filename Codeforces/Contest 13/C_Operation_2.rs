use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut input = input.split_whitespace();
    let a: i32 = input.next().unwrap().parse().unwrap();
    let mut b: i32 = input.next().unwrap().parse().unwrap();
    let mut operations = 0;
    while b > a {
        operations += 1;
        if b % 2 == 0 {
            b /= 2;
        } else {
            b += 1;
        }
    }
    println!("{}", operations + a - b);
}