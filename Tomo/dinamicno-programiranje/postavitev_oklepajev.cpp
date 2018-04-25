//https://www.geeksforgeeks.org/dynamic-programming-set-37-boolean-parenthesization-problem/
#include<iostream>
#include<cstring>
using namespace std;

// Vrne seštevek vseh možnih razporeditev, ki vrnejo true
// za resniènosti izraz s simboli T (true) in f (false)
// in operatorje  & (in), | (ali), ^ (strogi-ali) polnjeni med simboli
int countParenth(char symb[], char oper[], int n)
{
    int F[n][n], T[n][n];

    // Napolni diagonalne elemente
    // Vsi diagonalni elementi v T[i][i] so 1, èe je T (true)
    // Podobno vse vrednosti F[i][i] so 1 èe
    // symbol[i] je F (False)
    for (int i = 0; i < n; i++)
    {
        F[i][i] = (symb[i] == 'F')? 1: 0;
        T[i][i] = (symb[i] == 'T')? 1: 0;
    }

    // Napolni T[i][i+1], T[i][i+2], T[i][i+3]... v redu
    // in F[i][i+1], F[i][i+2], F[i][i+3]... v redu
    for (int gap=1; gap<n; ++gap)
    {
        for (int i=0, j=gap; j<n; ++i, ++j)
        {
            T[i][j] = F[i][j] = 0;
            for (int g=0; g<gap; g++)
            {
                // Najdi oklepaje
                // 
                int k = i + g;

                // Shrani Total[i][k] in Total[k+1][j]
                int tik = T[i][k] + F[i][k];
                int tkj = T[k+1][j] + F[k+1][j];

                // Rekruzivne formule https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-0d7c58bf0b746f103f62d1afe9934c4d_l3.png
                // https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-733311fe2b6baaa37e513a1c32eda64c_l3.png
                if (oper[k] == '&')
                {
                    T[i][j] += T[i][k]*T[k+1][j];
                    F[i][j] += (tik*tkj - T[i][k]*T[k+1][j]);
                }
                if (oper[k] == '|')
                {
                    F[i][j] += F[i][k]*F[k+1][j];
                    T[i][j] += (tik*tkj - F[i][k]*F[k+1][j]);
                }
                if (oper[k] == '^')
                {
                    T[i][j] += F[i][k]*T[k+1][j] + T[i][k]*F[k+1][j];
                    F[i][j] += T[i][k]*T[k+1][j] + F[i][k]*F[k+1][j];
                }
            }
        }
    }
    return T[0][n-1];
}

// Funkcija za testiranje
int main()
{
    char symbols[] = "TFTT";
    char operators[] = "&&|";
    int n = strlen(symbols);

    // 3-je naèini
    // ((T&F)&T)|T, (T&(F&T))|T, T&((F&T)|T)
    cout << countParenth(symbols, operators, n);
    return 0;
}

