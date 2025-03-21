struct MemorySimulator {
    memory: Vec<i32>,
}

impl MemorySimulator {
    fn new(size: usize, initial_value: i32) -> Self {
        MemorySimulator {
            memory: vec![initial_value; size],
        }
    }

    fn read(&self, address: usize) -> Option<i32> {
        self.memory.get(address).copied()
    }

    fn write(&mut self, address: usize, value: i32) -> Result<(), String> {
        if address < self.memory.len() {
            self.memory[address] = value;
            Ok(())
        } else {
            Err(String::from("Invalid address"))
        }
    }
}