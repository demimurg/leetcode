fn main() {
    for i in 0..9 {
        for j in 0..9 {
            let box_id = i / 3 * 3 + j / 3;
            println!("[{i}][{j}] - {box_id} box")
        }
    }
}
