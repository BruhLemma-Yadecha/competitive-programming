use std::io;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();
    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();
    let mut a = s.split_whitespace().map(|x| x.parse::<u32>().unwrap()).collect::<Vec<u32>>();
    a.sort();
    let mut time = 0;
    let mut satisfied = 0;
    for i in 0..n {
        if time <= a[i] {
            time += a[i];
            satisfied += 1;
        }
    }
    println!("{}", satisfied);
}