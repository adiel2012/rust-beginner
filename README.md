# Learning Rust: Complete Training Series

Comprehensive LaTeX Beamer presentations for learning Rust programming from zero to expert level.

## Choose Your Level

📚 **[Beginner Presentation](beginner/PRESENTATION.md)** - Start here if you're new to Rust
🚀 **[Intermediate Presentation](intermediate/PRESENTATION.md)** - Advanced topics for experienced developers
⚡ **[Advanced Presentation](advanced/PRESENTATION.md)** - Expert-level techniques and internals

## Beginner Track (35 slides)

Perfect for developers new to Rust. Covers fundamentals without assuming prior Rust knowledge:

### 1. Introduction
- What is Rust and why learn it
- Key features: safety, speed, and concurrency
- Installation and "Hello, World!"

### 2. Basic Syntax and Concepts
- Variables, mutability, and data types
- Functions and control flow
- Pattern matching fundamentals

### 3. Ownership System
- Ownership rules and the borrow checker
- Move semantics and references
- Stack vs. heap memory

### 4. Structs and Enums
- Defining custom types
- Methods and associated functions
- Option and Result types

### 5. Collections
- Vectors, strings, and hash maps
- Working with common data structures

### 6. Error Handling
- Result type and the ? operator
- Creating custom error types
- Best practices

### 7. Generics and Traits
- Generic programming
- Trait definitions and implementations
- Trait bounds

### 8. Fearless Concurrency
- Threads and message passing
- Shared state with Mutex and Arc
- The Send and Sync traits

### 9. Summary and Resources
- Key takeaways
- Learning resources
- Community and next steps

### 10. Additional Topics (Brief Coverage)
- Lifetimes, testing, cargo, and modules
- Smart pointers and async programming

## Intermediate Track (34 slides)

For developers with Rust fundamentals. Covers advanced patterns and techniques:

### 1. Advanced Trait Patterns
- Associated types vs generic parameters
- Trait objects and dynamic dispatch
- Higher-Ranked Trait Bounds (HRTB)
- Blanket implementations

### 2. Advanced Lifetimes
- Lifetime variance (covariant, contravariant, invariant)
- Multiple lifetime parameters and bounds
- Complex lifetime relationships

### 3. Macro Programming
- Declarative macros (`macro_rules!`)
- Procedural macros (derive, attribute, function-like)
- Token parsing and code generation

### 4. Advanced Async Programming
- Async traits and pinning
- Custom Future implementation
- Async cancellation and select patterns

### 5. Unsafe Rust and FFI
- Unsafe superpowers and responsibilities
- Safe abstractions over unsafe code
- Foreign Function Interface (calling C from Rust)

### 6. Performance Optimization
- Zero-cost abstractions in practice
- Memory layout and alignment control
- SIMD and platform-specific code

### 7. Advanced Error Handling
- Error type design with thiserror/anyhow
- Error context and chaining
- Library vs application error patterns

### 8. Advanced Concurrency Patterns
- Lock-free data structures
- Atomic operations and memory orderings
- Actor pattern implementation

### 9. Type System Techniques
- Phantom types and compile-time state machines
- Const generics
- Generic Associated Types (GATs)

### 10. Summary and Next Steps
- Specialization paths
- Advanced resources
- Contributing to the ecosystem

## Advanced Track (39 slides)

For expert-level developers ready to master Rust internals and build production systems:

### 1. Compiler Internals and MIR
- Rust compilation pipeline
- Mid-level Intermediate Representation
- Working with MIR output
- Custom compiler plugins and lints

### 2. Advanced Procedural Macros
- Complex derive macro implementation
- Custom syntax parsing with syn
- Token manipulation and hygiene
- Advanced code generation patterns

### 3. Custom Allocators
- Implementing GlobalAlloc trait
- Arena allocators
- Per-collection allocators
- Memory pool strategies

### 4. No-Std and Embedded Systems
- Bare metal Rust programming
- Hardware Abstraction Layer (HAL)
- Volatile memory access and MMIO
- Interrupt handling

### 5. WebAssembly Deep Dive
- wasm-bindgen advanced patterns
- JavaScript interop optimization
- Binary size optimization
- Custom sections and threading

### 6. Async Runtime Internals
- Building custom executors
- Waker implementation
- Reactor pattern for I/O
- Work-stealing schedulers

### 7. Advanced Lock-Free Algorithms
- ABA problem and solutions
- Tagged pointers
- Epoch-based reclamation
- Implementing lock-free data structures

### 8. Building Language Tooling
- rust-analyzer APIs
- Custom cargo subcommands
- LSP server implementation
- Syntax tree manipulation

### 9. Performance Profiling
- Benchmarking with Criterion
- CPU profiling (perf, flamegraph)
- Memory profiling (dhat, valgrind)
- Profile-guided optimization

### 10. Contributing to Rust
- Compiler development setup
- RFC process
- Writing compiler tests
- Working with Rust teams

### 11. Summary and Mastery Path
- Expert project ideas
- The complete learning journey

## How to Use These Presentations

### Building the Presentations

1. **Prerequisites**: Install a LaTeX distribution (see presentation guides for details)

2. **Compile**:
   ```bash
   # Beginner presentation
   cd beginner && make

   # Intermediate presentation
   cd intermediate && make

   # Advanced presentation
   cd advanced && make
   ```

3. **View**: The compiled PDFs will be:
   - `beginner/rust_presentation.pdf` (35 slides)
   - `intermediate/rust_intermediate.pdf` (34 slides)
   - `advanced/rust_advanced.pdf` (39 slides)

### Using for Teaching

- **Beginner Course**: Start with the beginner presentation (60-90 minutes)
- **Intermediate Workshop**: For experienced developers (90-120 minutes)
- **Advanced/Expert Training**: For systems programmers and contributors (120-150 minutes)
- **Complete Series**: All three presentations for comprehensive zero-to-expert training
- **Self-Study**: Work through presentations at your own pace
- **Topic-Specific**: Focus on individual sections as needed

### Customization

All presentations use Beamer's Madrid theme and can be easily customized:
- Change theme/colors by editing the `.tex` files
- Adjust code font sizes in the lstset configuration
- Add or modify slides to suit your teaching style

See the presentation guides for detailed instructions:
- [Beginner Guide](beginner/PRESENTATION.md)
- [Intermediate Guide](intermediate/PRESENTATION.md)
- [Advanced Guide](advanced/PRESENTATION.md)

## Features

- **Three-Track System**: Complete progression from beginner to expert
- **Professional Design**: Madrid Beamer theme with clean, readable layouts
- **Syntax Highlighting**: Custom Rust code formatting with the listings package
- **Comprehensive Coverage**: 108 total slides covering zero to expert level
- **Teaching-Ready**: Structured for classroom, workshop, or self-study use
- **Code-Heavy**: Extensive runnable code examples for every concept
- **Progressive Learning**: Each track builds on the previous
  - **Beginner**: Zero to fundamentals (35 slides)
  - **Intermediate**: Fundamentals to advanced patterns (34 slides)
  - **Advanced**: Advanced patterns to expert internals (39 slides)

## Additional Resources

For learners using this presentation:
- [The Rust Book](https://doc.rust-lang.org/book/) - Official comprehensive guide
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/) - Learn through examples
- [Rustlings](https://github.com/rust-lang/rustlings) - Interactive exercises
- [Rust Playground](https://play.rust-lang.org/) - Try code in your browser

## License

This educational material is provided for learning purposes.

---

**Happy Teaching/Learning!**
