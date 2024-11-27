#include <iostream>
using namespace std;
class complex
{
  private:
  int real,img;
  public:
  void input();
  void display();
  complex add(complex,complex);
};
void complex :: input()
{
  cout<<"Enter the real part"<<endl;
   cin>>real;
  cout<<"Enter the imaginary part"<<endl;
   cin>>img;
}
void complex :: display()
{
  cout<<"The numer is = "<<real<<"+i"<<img<<endl;
}
complex complex :: add(complex c1,complex c2)
{
  complex c;
  c.real = c1.real + c2.real;
  c.img = c1.img + c2.img;
  return c;
}
int main()
{
  complex c1,c2,c3;
  c1.input();
  c2.input();
  c3=c3.add(c1,c2);
  cout<<"After addtion of complex numbers"<<endl;
  c3.display();
  return 0;
}