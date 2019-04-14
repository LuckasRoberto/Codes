float r1 = 150;
float r2 = 150;
float m1 = 10;
float m2 = 10;
float a1 = PI/4;
float a2 = PI/2;
float a1_vel = 0;
float a2_vel = 0;
float g = 1;

PGraphics canv;

void setup() {
  size(720, 640);
  canv = createGraphics(720, 640);
  canv.beginDraw();
  canv.background(0);
  canv.endDraw();
}

void draw() {
  float num1 = -g * (2 * m1 + m2) * sin(a1);
  float num2 = -m2 * g * sin(a1-2*a2);
  float num3 = -2*sin(a1-a2)*m2;
  float num4 = a2_vel*a2_vel*r2+a1_vel*a1_vel*r1*cos(a1-a2);
  float den = r1 * (2*m1+m2-m2*cos(2*a1-2*a2));
  float a1_acc = (num1 + num2 + num3*num4) / den;

  num1 = 2 * sin(a1-a2);
  num2 = (a1_vel*a1_vel*r1*(m1+m2));
  num3 = g * (m1 + m2) * cos(a1);
  num4 = a2_vel*a2_vel*r2*m2*cos(a1-a2);
  den = r2 * (2*m1+m2-m2*cos(2*a1-2*a2));
  float a2_acc = (num1*(num2+num3+num4)) / den;
  
  //background(0);
  image(canv,0,0);
  stroke(255, 0, 0);
  strokeWeight(2);
  
  translate(350, 250);
  
  float x1 = r1 * sin(a1);
  float y1 = r1 * cos(a1);
  
  float x2 = x1 + r2 * sin(a2);
  float y2 = y1 + r2 * cos(a2);
  
  line(0, 0, x1, y1);
  fill(255);
  ellipse(x1, y1, m1, m2);

  line(x1, y1, x2, y2);
  fill(255);
  ellipse(x2, y2, m2, m2);
  
  a1_vel += a1_acc;
  a2_vel += a2_acc;
  a1 += a1_vel;
  a2 += a2_vel;
  
  canv.beginDraw();
  canv.translate(350, 250);
  canv.strokeWeight(4);
  canv.stroke(255);
  canv.point(x2, y2);
  canv.endDraw();
}
