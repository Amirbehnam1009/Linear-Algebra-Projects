# 📊 Linear Algebra Projects  
👨‍🏫**Under the Supervision of [Prof. Morteza Haghir Chehreghani](https://scholar.google.com/citations?user=8YBZPcAAAAAJ&hl=en)**  
🍂***Spring 2021***

This repository contains three projects focused on practical applications of linear algebra:  
1. **🔢 Solving Linear Equations with LU Decomposition**  
2. **📉 Denoising Bitcoin Price Data Using Least Squares**  
3. **🖼️ Compressing Bitmap Images via SVD Decomposition**  

---

## 🧮 Project 1: Linear Equations Solver with LU Decomposition  

### 📝 Overview  
A Python implementation to solve systems of linear equations using **LU decomposition** and forward/backward substitution. This method efficiently handles multiple systems with the same coefficient matrix but different right-hand-side vectors.  

### ⚙️ Requirements  
- Python 3.x  
- NumPy  

### 📥 Input Format  
The input consists of:  
1. Two integers `n` (size of the square matrix `A`) and `m` (number of vectors `b`)  
2. `n` lines representing the rows of matrix `A`  
3. `m` lines, each containing a vector `b`  

**📋 Example Input:**  
``` bash
3 5
5 6 2
4 5 2
2 4 8
18 7 2
4 5 8
15 7 6
11 9 5
13 12 12
```

### 📤 Output Format  
Solutions for each `b` are printed up to 4 decimal places.  

**📊 Example Output:**  

``` bash
75.0 -64.0 13.5
-14.0 13.0 -2.0
53.0 -45.0 10.0
0.5 1.5 -0.25
-10.0 11.0 -1.5
```
## 📉 Project 2: Denoising Bitcoin Price Data Using Least Squares  

### 📝 Overview  
Applies the **Least Squares Method** to smooth noisy Bitcoin price trends, revealing underlying patterns.  

### 🎨 Simulated Result  
![Denoised Bitcoin Price](https://github.com/Amirbehnam1009/Linear-Algebra-Projects/assets/117163007/61f69b7d-0735-4916-a998-4cf7e10c3613)  


## 🖼️ Project 3: Bitmap Image Compression via SVD Decomposition  

### 📝 Overview  
Compresses `.bmp` images using **Singular Value Decomposition (SVD)**, reducing file size while preserving visual quality.  

### ▶️ How to Run  
1. Provide the path to a `.bmp` image  
2. The script outputs a compressed version  

### 🎨 Simulated Result  
**Original vs. Compressed Image**  
![Image Compression Demo](https://github.com/Amirbehnam1009/Linear-Algebra-Projects/assets/117163007/45eb6e7d-43bd-4e32-87fd-9e8e634f0899)  

---

### ✨ Key Features  
- **🧩 Modular Code Structure** - Easy to understand and modify  
- **⚡ Efficient Algorithms** - Optimized implementations of core linear algebra operations  
- **📚 Academic Foundation** - Based on rigorous mathematical principles  

### 🚀 Getting Started  
1. Clone this repository  
2. Install dependencies: `pip install numpy matplotlib`  
3. Run individual project scripts  

### 📜 License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details  

### 🙏 Acknowledgments  
Special thanks to Prof. Chehreghani for guidance on these implementations
