Pendulo p;

void setup() {
  size(900,900);
  
  p = new Pendulo(new PVector(width/2,0),400);

}

void draw() {

  background(255);
  p.go();
}

void mousePressed() {
  p.clicked(mouseX,mouseY);
}

void mouseReleased() {
  p.stopDragging();
}
