// Hello World C++ Program Annotated

// The '#include' is a preprocessor directive used to include
// files in our program. The above code is including the contents
// of the 'iostream' file. This allows us to use 'cout' in our
// program to print output on the screen.
#include <iostream>

// A valid C++ program must have the 'main()' function. The
// curly braces indicate the start and the end of the function.
// The execution of code begins from this function.
int main() {
    // 'std::cout' prints the content inside the quotation marks.
    // It must be followed by '<<' followed by the format string.
    // In our example, "Hello World!" is the format string.
    std::cout << "Hello World!\n"; // ';' is used to indicate the 
                                 // end of a statement.
    // The 'return 0;' statement is the "Exit status" of the program.
    // In simple terms, the program ends with this statement.
    return 0;
}
