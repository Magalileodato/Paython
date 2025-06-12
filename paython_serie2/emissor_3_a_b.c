// Configurações
const int N = 10;  // Número de elementos de Fibonacci a enviar
const bool USE_CRC = false;  // true para usar CRC, false para enviar só os dados

// Polinómio gerador CRC-8 (x^8 + x^2 + x + 1): 0x07
const byte CRC_POLY = 0x07;

// Função para calcular o CRC-8 de um byte
byte calculaCRC(byte dado) {
  byte crc = dado;
  for (int i = 0; i < 8; i++) {
    if (crc & 0x80)
      crc = (crc << 1) ^ CRC_POLY;
    else
      crc <<= 1;
  }
  return crc;
}

// Gera número de Fibonacci na posição n
unsigned int fibonacci(int n) {
  if (n == 0) return 0;
  if (n == 1) return 1;
  unsigned int a = 0, b = 1, temp;
  for (int i = 2; i <= n; i++) {
    temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}

void setup() {
  Serial.begin(9600);
  delay(1000);  // Espera para ligação serial estabilizar

  for (int i = 0; i < N; i++) {
    unsigned int num = fibonacci(i);

    byte lowByte = num & 0xFF;
    byte highByte = (num >> 8) & 0xFF;

    // Enviar dados
    Serial.write(highByte);
    Serial.write(lowByte);

    if (USE_CRC) {
      byte crc1 = calculaCRC(highByte);
      byte crc2 = calculaCRC(lowByte);
      Serial.write(crc1);
      Serial.write(crc2);
    }

    delay(100);  // Pequeno atraso entre envios
  }
}

void loop() {
  // Nada aqui — comunicação simplex, apenas emissão no setup()
}
