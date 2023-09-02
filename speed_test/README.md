# ⚡ Exploring Execution Speed: A Comparison between Python and C ⚡

This repository aims to challenge the common misconception that "Python is slow" by conducting a ⏱️ speed test that demonstrates the efficiency of calling C programs from Python. The intention is to showcase that Python can achieve competitive performance by leveraging C integration.

## 🔬 How to Replicate the Speed Test

Follow these steps to replicate the speed test and observe the execution times of Python and C programs:

1. Open the `fib.py` file using your preferred text editor, such as `nvim`:
   ```
   nvim fib.py
   ```

2. Run the Python 🐍 program using the `time` command to measure execution time:
   ```
   time python3 fib.py
   ```

3. Open the `fib.c` file using your preferred text editor:
   ```
   nvim fib.c
   ```

4. Compile the C 🖥️ program using `gcc` to generate an executable named `fib`:
   ```
   gcc fib.c -o fib
   ```

5. Measure the execution time of the compiled C 🖥️ program using the `time` command:
   ```
   time ./fib
   ```

6. If desired, you can also explore the `fib2.py` file and compare its execution time with the original Python 🐍 program:
   ```
   nvim fib2.py
   time python3 fib.py
   ```

## 🎯 Purpose and Conclusion

The main goal of this speed test is to illustrate that the claim "Python is slow" can be misleading when it comes to execution speed. By integrating C 🖥️ code with Python 🐍, it is possible to achieve performance levels comparable to those of lower-level programming languages. This experiment encourages developers to consider the strengths of both Python 🐍 and C 🖥️ and to make informed decisions based on the specific requirements of their projects.

Feel free to experiment with different implementations and optimize the code further to explore the potential for achieving even better performance.
