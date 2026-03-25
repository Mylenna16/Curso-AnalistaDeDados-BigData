-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 08-Nov-2024 às 23:09
-- Versão do servidor: 5.7.36
-- versão do PHP: 8.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `escolar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos`
--

CREATE TABLE `alunos` (
  `matricula` smallint(6) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `idade` smallint(6) NOT NULL,
  `sexo` varchar(60) NOT NULL,
  `numero` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `alunos`
--

INSERT INTO `alunos` (`matricula`, `nome`, `idade`, `sexo`, `numero`) VALUES
(1122, 'Alessandro Vieira', 50, 'M', 1101),
(1133, 'Maria Penha', 80, 'F', 1101),
(1144, 'Eduarda Silva', 20, 'F', 1301),
(1155, 'Dirceu Amorim', 70, 'M', 1201),
(1166, 'Pedro José', 15, 'M', 1201),
(1177, 'Suelen Costa', 17, 'F', 1001),
(1188, 'Erika Coimbra', 16, 'F', 1001);

-- --------------------------------------------------------

--
-- Estrutura da tabela `disciplina`
--

CREATE TABLE `disciplina` (
  `codigo` smallint(6) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `carga_horaria` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `estuda`
--

CREATE TABLE `estuda` (
  `matricula` smallint(6) NOT NULL,
  `codigo` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `professor`
--

CREATE TABLE `professor` (
  `matricula` smallint(6) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `codigo` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `turmas`
--

CREATE TABLE `turmas` (
  `numero` smallint(6) NOT NULL,
  `sala` smallint(6) NOT NULL,
  `andar` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `turmas`
--

INSERT INTO `turmas` (`numero`, `sala`, `andar`) VALUES
(1001, 101, 1),
(1002, 102, 1),
(1100, 103, 1),
(1201, 201, 2),
(1301, 301, 3);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `numero` (`numero`);

--
-- Índices para tabela `disciplina`
--
ALTER TABLE `disciplina`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices para tabela `estuda`
--
ALTER TABLE `estuda`
  ADD PRIMARY KEY (`matricula`,`codigo`),
  ADD KEY `codigo` (`codigo`);

--
-- Índices para tabela `professor`
--
ALTER TABLE `professor`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `codigo` (`codigo`);

--
-- Índices para tabela `turmas`
--
ALTER TABLE `turmas`
  ADD PRIMARY KEY (`numero`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `alunos`
--
ALTER TABLE `alunos`
  MODIFY `matricula` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1189;

--
-- AUTO_INCREMENT de tabela `disciplina`
--
ALTER TABLE `disciplina`
  MODIFY `codigo` smallint(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `turmas`
--
ALTER TABLE `turmas`
  MODIFY `numero` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1302;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `alunos`
--
ALTER TABLE `alunos`
  ADD CONSTRAINT `alunos_ibfk_1` FOREIGN KEY (`numero`) REFERENCES `turmas` (`numero`);

--
-- Limitadores para a tabela `estuda`
--
ALTER TABLE `estuda`
  ADD CONSTRAINT `estuda_ibfk_1` FOREIGN KEY (`matricula`) REFERENCES `aluno` (`matricula`),
  ADD CONSTRAINT `estuda_ibfk_2` FOREIGN KEY (`codigo`) REFERENCES `disciplina` (`codigo`);

--
-- Limitadores para a tabela `professor`
--
ALTER TABLE `professor`
  ADD CONSTRAINT `professor_ibfk_1` FOREIGN KEY (`codigo`) REFERENCES `disciplina` (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
