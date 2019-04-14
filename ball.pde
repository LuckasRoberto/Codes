float cx;
float cy;

float c2x;
float c2y;

float l;
float l2;

float hbase;

float a = PI/6;

void setup(){
  size(640, 600);
  cx = 400;
  cy = 400;
  l2 = (l*sin(PI-a));
  

}
void draw(){
  background(100,100,100);
  fill(255);
  ellipse(cx,cy, 48, 48);
  ellipse(c2x,c2y, 24, 24);
  line(cx,cy,c2x,c2y);
  

}
  
