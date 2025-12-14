# Learning Rust: A Beginner's Guide

A comprehensive guide to learning the Rust programming language from scratch.

## Table of Contents

### Part 1: Getting Started

#### Chapter 1: Introduction to Rust
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_01_introduction_to_rust.ipynb)

- What is Rust?
- Why learn Rust?
- Rust's key features: safety, speed, and concurrency
- Installing Rust and setting up your development environment
- Your first Rust program: "Hello, World!"

#### Chapter 2: Basic Syntax and Concepts
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_02_basic_syntax_and_concepts.ipynb)

- Variables and mutability
- Data types: integers, floats, booleans, and characters
- Comments and documentation
- Functions and code organization
- Control flow: if/else statements

### Part 2: Core Concepts

#### Chapter 3: Ownership
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_03_ownership.ipynb)

- What is ownership?
- The ownership rules
- Stack vs heap memory
- Move semantics
- Clone and Copy traits

#### Chapter 4: References and Borrowing
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_04_references_and_borrowing.ipynb)

- References and borrowing basics
- Mutable vs immutable references
- The borrowing rules
- Dangling references
- Slices

#### Chapter 5: Structs and Enums
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_05_structs_and_enums.ipynb)

- Defining and instantiating structs
- Method syntax
- Enums and pattern matching
- The Option enum
- The Result enum for error handling

### Part 3: Building Programs

#### Chapter 6: Collections
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_06_collections.ipynb)

- Vectors
- Strings and string slices
- Hash maps
- When to use each collection type

#### Chapter 7: Error Handling
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_07_error_handling.ipynb)

- Unrecoverable errors with panic!
- Recoverable errors with Result
- Propagating errors with the ? operator
- Custom error types
- Best practices for error handling

#### Chapter 8: Generics and Traits
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_08_generics_and_traits.ipynb)

- Generic data types
- Trait definitions and implementations
- Trait bounds
- Default implementations
- Common standard library traits

### Part 4: Advanced Topics

#### Chapter 9: Lifetimes
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_09_lifetimes.ipynb)

- Understanding lifetimes
- Lifetime annotations
- Lifetime elision rules
- The static lifetime
- Generic lifetimes in functions and structs

#### Chapter 10: Testing
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_10_testing.ipynb)

- Writing unit tests
- Integration tests
- Test organization
- Running tests
- Documentation tests

#### Chapter 11: Cargo and Modules
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_11_cargo_and_modules.ipynb)

- Creating projects with Cargo
- Module system and privacy
- Use keyword for bringing items into scope
- Separating code into multiple files
- Publishing crates to crates.io

#### Chapter 12: Smart Pointers
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_12_smart_pointers.ipynb)

- Box<T> for heap allocation
- Rc<T> for reference counting
- RefCell<T> and interior mutability
- Memory leaks and reference cycles
- Weak<T> references

### Part 5: Concurrency and Beyond

#### Chapter 13: Fearless Concurrency
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_13_fearless_concurrency.ipynb)

- Threads and the thread::spawn function
- Message passing with channels
- Shared state concurrency with Mutex and Arc
- The Send and Sync traits
- Avoiding data races

#### Chapter 14: Object-Oriented Features
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_14_object_oriented_features.ipynb)

- Encapsulation
- Trait objects for polymorphism
- State pattern implementation
- When to use OOP patterns in Rust

#### Chapter 15: Patterns and Matching
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_15_patterns_and_matching.ipynb)

- Pattern syntax
- Destructuring structs and enums
- Match guards
- @ bindings
- Refutability

#### Chapter 16: Async Programming
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_16_async_programming.ipynb)

- Introduction to async/await
- Futures and executors
- Async functions and blocks
- Popular async runtimes (tokio, async-std)
- Common async patterns

### Part 6: Real-World Rust

#### Chapter 17: Building CLI Applications
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_17_building_cli_applications.ipynb)

- Parsing command-line arguments
- Reading from files and stdin
- Error handling in CLI apps
- Testing CLI applications

#### Chapter 18: Web Development with Rust
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_18_web_development.ipynb)

- HTTP clients and making requests
- Building web servers
- Popular web frameworks (Actix, Rocket, Axum)
- Working with JSON

#### Chapter 19: Unsafe Rust
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_19_unsafe_rust.ipynb)

- When and why to use unsafe
- Dereferencing raw pointers
- Calling unsafe functions
- Creating safe abstractions
- Foreign Function Interface (FFI)

#### Chapter 20: Next Steps
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adiel2012/rust-beginner/blob/main/chapter_20_next_steps.ipynb)

- Contributing to open source
- Exploring the Rust ecosystem
- Advanced topics to explore
- Community resources
- Career paths with Rust

## Appendices

### Appendix A: Rust Tooling
- rustc compiler
- Cargo package manager
- rustfmt code formatter
- clippy linter
- rust-analyzer IDE support

### Appendix B: Common Programming Concepts
- Iterators and closures
- File I/O
- Environment variables
- Command-line argument parsing

### Appendix C: Resources
- Official Rust documentation
- The Rust Book
- Rust by Example
- Community forums and chat
- Recommended practice projects

## How to Use This Guide

### Option 1: Interactive Learning with Google Colab (Recommended)
Click the "Open in Colab" badge next to any chapter to launch an interactive notebook in your browser:
1. **No installation required** - runs entirely in the cloud
2. Each notebook **automatically installs Rust** when you run the first cell
3. All code examples are **executable** - just click "Run" to see results
4. **Modify and experiment** with the code in real-time

### Option 2: Local Learning
1. Install Rust locally from [rustup.rs](https://rustup.rs)
2. Clone this repository
3. Work through chapters sequentially
4. Complete exercises at the end of each chapter
5. Build small projects to reinforce concepts

### General Tips
- Join the Rust community for support and collaboration
- Practice regularly - consistency is key to mastering Rust
- Don't rush through ownership and borrowing - these are fundamental
- Embrace compiler errors as teaching tools

## Prerequisites

- Basic programming knowledge in any language
- Familiarity with command-line interfaces
- Understanding of basic computer science concepts

## Learning Tips

- Don't rush through ownership and borrowing - these are fundamental
- Embrace compiler errors as teaching tools
- Write code daily, even if just for 30 minutes
- Read other people's Rust code
- Start with small projects and gradually increase complexity

Happy learning!
