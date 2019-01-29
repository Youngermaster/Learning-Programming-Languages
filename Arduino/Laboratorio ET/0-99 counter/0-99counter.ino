/* Contador decimal de dos Digigitos en 7 Segmentos usando multiplexacion

 Conexiones:  Las conexiones entre el Arduino y el Display deben realizarse
              con una resistencia de 1K ohmio.

 ARDUINO  -    Display 7 Segmentos (catodo comun)
   2            a
   3            b
   4            c
   5            d
   6            e
   7            f
   8            g
   9            P
  
   10           COM digito izquierdo usando Transistor NPN
   11           COM digito derecho  usando Transistor NPN
*/

int retardo=10;       // tiempo que dura encendido cada 7 seg (10 mili segundos)
int var=0;            // Valor del digito que se va a desplegar por el 7 seg.

int unidad=0;         // cuenta las unidades (derecha)
int decena=0;         // cuenta las decenas (izquierda)
int conmutador=0;     // multiplexacion de uno a otro 7 segmentos
int cont=0;           // contador de ciclos de espera para cambiar de numero

void setup() {              
  pinMode(2, OUTPUT);  //seg a
  pinMode(3, OUTPUT);  //seg b
  pinMode(4, OUTPUT);  //seg c
  pinMode(5, OUTPUT);  //seg d
  pinMode(6, OUTPUT);  //seg e
  pinMode(7, OUTPUT);  //seg f
  pinMode(8, OUTPUT);  //seg g
 
  pinMode(10, OUTPUT);  // activa digito 1 derecha (unidad)
  pinMode(11, OUTPUT);  // activa digito 2 izquierda (decena)
   
}

void loop() {
  delay(10);               // tiempo que dura encendido cada 7seg antes de cambiar al otro
  cont++;                      // incrementa el contador de ciclos en Uno
  if (cont==100){              // cada cuanto tiempo (ciclos)cambia un numero
    cont=0;                 // inicializa el contador de ciclos  
    unidad++;		          // incrementa la unidad, primer 7seg
    if (unidad >= 10){        // cuando la unidad llegue a 10 incrementa la decena
      decena++;      // incrementa la decena,  segundo 7seg
      unidad=0;               // regresa la unidad a cero
      if (decena>=10){        // cuando la decena llegue a 10 se inicializa a cero   
        decena=0;
      }     
    }
 }

   
    if (conmutador == 0) {    // hace la multiplexacion conmutando entre los dos 7seg  izq y der
      digitalWrite(10, 1);    // enciende el derecho
      digitalWrite(11, 0);    // apaga el izquierdo
      var=unidad;             // iguala la variable que escribe el numero en el 7seg al valor de la unidad
      conmutador=1;           // cambia el conmutador para que en el siguiente ciclo cumpla la otra condicion
     
    }
    else{
     digitalWrite(10, 0);       // apaga el derecho
      digitalWrite(11, 1);      // enciende el izquierdo
      var=decena;               // iguala la variable que escribe el numero en el 7seg al valor de la decena
      conmutador=0;             // cambia el conmutador para que en el siguiente ciclo cumpla la otra condicion
     
    }
  asignador(var);
}

/**
 * Como su nombre lo indica asigna el numero que se va a mostrar en el display de 7
 * segmentos. Funciona con un condicional switch que mendiante una variable de tipo 
 * Integer o entera que le pasaremos como parámetro determinará que numero debe salir.
 * En este caso la variable global contador que declaramos y asignamos anteriormente.
 */
void asignador(int counter){

  switch(counter){
    
    case 0:
    encender (1,1,1,1,1,1,0); //escribe 0
    break;
    
    case 1:
    encender (0,1,1,0,0,0,0); //escribe 1
    break;
    
    case 2:
    encender (1,1,0,1,1,0,1); //escribe 2
    break;
    
    case 3:
    encender (1,1,1,1,0,0,1); //escribe 3
    break;
    
    case 4:
    encender (0,1,1,0,0,1,1); //escribe 4
    break;
    
    case 5:
    encender (1,0,1,1,0,1,1); //escribe 5
    break;
    
    case 6:
    encender (1,0,1,1,1,1,1); //escribe 6
    break;
    
    case 7:
    encender (1,1,1,0,0,0,0); //escribe 7
    break;
    
    case 8:
    encender (1,1,1,1,1,1,1); //escribe 8
    break;
    
    case 9:
    encender (1,1,1,0,0,1,1); //escribe 9
    break;
  }
}

/**
 * Este método tiene la función de encender el LED dependiendo de los parámetros
 * que se le den.
 */
void encender (int a, int b, int c, int d, int e, int f, int g)

{
  digitalWrite (7,a);   
  digitalWrite (8,b);   
  digitalWrite (9,c);
  digitalWrite (10,d);
  digitalWrite (11,e);
  digitalWrite (12,f);
  digitalWrite (13,g);
}