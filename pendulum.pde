class Pendulo {

  PVector posicao;    // posição da bola do pendulo
  PVector origem;      // posição de origem
  float r;             // tamanho do pendulo
  float theta;         // angulo do pendulo
  float aVel;     // velocidade angular
  float aAcc; // aceleração angular

  float bolaR;         // raio da bola
  float amortecimento;       // arrasto

  boolean dragging = false;

  Pendulo(PVector origem_, float r_) {
    
    origem = origem_.get();
    posicao = new PVector();
    r = r_;
    theta = PI/4;

    aVel = 0.0;
    aAcc = 0.0;
    amortecimento = 0.995;   // armotecimentp
    bolaR = 20.0;      // raio da bola
  }

  void go() {
    update();
    drag();    //interações
    display();
  }

  void update() {
   
    if (!dragging) {
      float gravity = 0.98;                             
      aAcc = (-1 * gravity / r) * sin(theta);  
      aVel += aAcc;                 
      aVel *= amortecimento;                       
      theta += aVel;                         
    }
  }

  void display() {
    posicao.set(r*sin(theta), r*cos(theta), 0);  // coordenadas polares para cartesianas
    posicao.add(origem);                              

    stroke(0);
    strokeWeight(2);
    // Desenha o braço
    line(origem.x, origem.y, posicao.x, posicao.y);
    ellipseMode(CENTER);
    fill(175);
    if (dragging) fill(0);
    // Desenha a bola
    ellipse(posicao.x, posicao.y, bolaR, bolaR);
  }


  // mouse 

  // verifica o click do mouse
  void clicked(int mx, int my) {
    float d = dist(mx, my, posicao.x, posicao.y);
    if (d < bolaR) {
      dragging = true;
    }
  }

  
  void stopDragging() {
    if (dragging) {
      aVel = 0; 
      dragging = false;
    }
  }

  void drag() {
    
    if (dragging) {
      PVector diff = PVector.sub(origem, new PVector(mouseX, mouseY));      
      theta = atan2(-1*diff.y, diff.x) - radians(90);                      
    
    }
  }
}
