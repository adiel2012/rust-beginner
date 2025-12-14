# Learning Rust: A Beginner's Guide

A comprehensive LaTeX Beamer presentation for learning the Rust programming language from scratch.

📊 **[View Presentation Guide](beginner/PRESENTATION.md)**

## What's Included

This presentation covers Rust programming from beginner to intermediate level, organized into 10 comprehensive sections:

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

## How to Use This Presentation

### Building the Presentation

1. **Prerequisites**: Install a LaTeX distribution (see [beginner/PRESENTATION.md](beginner/PRESENTATION.md) for details)

2. **Compile**:
   ```bash
   cd beginner
   make
   ```

3. **View**: The compiled PDF will be `beginner/rust_presentation.pdf`

### Using for Teaching

- **Classroom Setting**: Full presentation flow (60-90 minutes)
- **Workshop**: Focus on specific sections as modules
- **Online Course**: One section per video/lesson
- **Self-Study**: Work through slides at your own pace

### Customization

The presentation uses Beamer's Madrid theme and can be easily customized:
- Change theme/colors by editing `rust_presentation.tex`
- Adjust code font sizes in the lstset configuration
- Add or modify slides to suit your teaching style

See the [full presentation guide](beginner/PRESENTATION.md) for detailed instructions.

## Features

- **Professional Design**: Madrid Beamer theme with clean, readable layouts
- **Syntax Highlighting**: Custom Rust code formatting with the listings package
- **Comprehensive Coverage**: 35 slides covering essential Rust concepts
- **Teaching-Ready**: Structured for classroom, workshop, or self-study use
- **Code Examples**: All major concepts include runnable code snippets

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
