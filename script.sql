--DATABASE LEVEL 1
CREATE TABLE AGRICULTOR(
    IDAGRICULTOR INT PRIMARY KEY AUTO_INCREMENT,
	NOME VARCHAR(30) NOT NULL,
	SEXO ENUM('M', 'F') NOT NULL,
	EMAIL VARCHAR(50) NOT NULL UNIQUE,
	CPF VARCHAR(15) UNIQUE
);

CREATE TABLE END_TERRAS(
	IDTERRAS INT PRIMARY KEY AUTO_INCREMENT,
	RUA VARCHAR(30) NOT NULL,
	BAIRRO VARCHAR(30) NOT NULL,
	CIDADE VARCHAR(30) NOT NULL,
	ESTADO CHAR(2) NOT NULL,
	FOREIGN KEY (ID_AGRICULTOR) REFERENCES AGRICULTOR(IDAGRICULTOR)
);

CREATE TABLE PLANTACAO(
	IDPLANTACAO INT PRIMARY KEY AUTO_INCREMENT,
	TIPO VARCHAR(30) NOT NULL,
	LUCRO_MENSAL DOUBLE NOT NULL,
	LUCRO_ANUAL DOUBLE NOT NULL,
	INFLUENCIA VARCHAR(30) NOT NULL,
	ID_AGRICULTOR INT NOT NULL,
	ID_TERRAS INT NOT NULL,
	FOREIGN KEY(ID_AGRICULTOR) REFERENCES AGRICULTOR(IDAGRICULTOR),
	FOREIGN KEY(ID_TERRAS) REFERENCES END_TERRAS(IDTERRAS)
);


