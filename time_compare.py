import timeit, subprocess, platform, json

def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)

fprint("Testing Script - Counting the prime numbers between 1 and 100000 using Python, NodeJS, Java, and C.")
fprint("Platform Information:")
fprint(f"{platform.platform()=}")
fprint(f"{platform.architecture()=}")
fprint(f"{platform.machine()=}")
fprint(f"{platform.processor()=}")
fprint(f"{platform.system()=}")

fprint("Selected Runtimes: ")

fprint("\nPython (Runtime):")
subprocess.run(["python", "--version"])

fprint("\nNodeJS (Runtime):")
subprocess.run(["node", "--version"])

fprint("\nJava (Compiler):")
subprocess.run(["javac", "--version"])

fprint("\nJava (Runtime):")
subprocess.run(["java", "--version"])

fprint("\nC (Compiler):")
subprocess.run(["clang", "--version"])

fprint("****")

fprint("-> Timing Python Test:")
time_py = timeit.timeit(lambda: subprocess.run(
    [
        "python",
        "./prime_calc_python.py"
    ]
), number=1)

fprint("-> Timing NodeJS Test:")
time_node = timeit.timeit(lambda: subprocess.run(
    [
        "node",
        "./prime_calc_javascript.js"
    ]
), number=1)

fprint("-> Precompiling Java Class...")
subprocess.run(
    [
        "javac",
        "./PrimeCalcJava.java"
    ]
)

fprint("-> Timing Java Test:")
time_java = timeit.timeit(lambda: subprocess.run(
    [
        "java",
        "PrimeCalcJava"
    ]
), number=1)

fprint("-> Precompiling C Binary with -O2 Optimization...")
subprocess.run(
    [
        "clang",
        "./prime_calc_c.c",
        "-O2",
        "-o",
        "./prime_calc_c.exe"
    ]
)

fprint("-> Timing C Test:")
time_c = timeit.timeit(lambda: subprocess.run(
    [
        "./prime_calc_c.exe",
    ]
), number=1)

print("****")
print("Results:")
print(f"-> Python: {time_py} Seconds")
print(f"-> NodeJS: {time_node} Seconds")
print(f"-> Java: {time_java} Seconds")
print(f"-> C: {time_c} Seconds")