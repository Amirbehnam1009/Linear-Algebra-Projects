#include <iostream>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <cmath>

using namespace std;

#define max 10000
int n = 10;
int m = 10;

float mat[max][max];
float b[max][max];
float y[max] = { 0 };
float x[max] = { 0 };
float lower[max][max] = { 0 };
float upper[max][max] = { 0 };



void luDecomposition()
{
	for (int i = 0; i < n; i++)
	{
		for (int k = i; k < n; k++)
		{
			float sum = 0;
			for (int j = 0; j < i; j++)
				sum += (lower[i][j] * upper[j][k]);

			upper[i][k] = mat[i][k] - sum;
		}

		for (int k = i; k < n; k++)
		{
			if (i == k)
				lower[i][i] = 1;
			else
			{
				float sum = 0;
				for (int j = 0; j < i; j++)
					sum += (lower[k][j] * upper[j][i]);
				lower[k][i]
					= (mat[k][i] - sum) / upper[i][i];
			}
		}
	}
}

void forward(int index) {
	float sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum = 0;
		for (int j = 0; j < i; j++)
		{
			sum += lower[i][j] * y[j];
		}
		y[i] = (b[index][i] - sum) / lower[i][i];
	}
}

void back() {
	float sum = 0;
	for (int i = n - 1; i > -1; i--)
	{
		sum = 0;
		for (int j = n - 1; j > i; j--)
		{
			sum += upper[i][j] * x[j];
		}
		x[i] = (y[i] - sum) / upper[i][i];
	}
}


void PrintMatrix(float a[][max], int n)
{
	cout << endl;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			cout << a[i][j] << " ";
		cout << endl;
	}
}

int main() {
	//std::cout << std::setprecision(2);

	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> mat[i][j];
		}
	}

	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> b[i][j];
		}
	}
	luDecomposition();
	//PrintMatrix(mat, n);
	//PrintMatrix(upper, n);
	//PrintMatrix(lower, n);
	for (int i = 0; i < m; i++)
	{
		forward(i);
		back();
		for (int j = 0; j < n; j++)
		{
			x[j] = round(x[j] * 100);

			if(((int)x[j]/10) * 10 == x[j])
			cout << setprecision(1) << fixed << x[j]/100 << " ";
			else
				cout << setprecision(2) << fixed << x[j]/100 << " " ;
		}
		cout << endl;
	}

}

/*
3 5
5 6 2
4 5 2
2 4 8
18 7 2
4 5 8
15 7 6
11 9 5
13 12 12
*/