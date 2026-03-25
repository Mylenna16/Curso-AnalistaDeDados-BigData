-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 08-Nov-2024 às 23:10
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
-- Banco de dados: `restaurante_tanoshimi`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cardapio`
--

CREATE TABLE `cardapio` (
  `codigo_prato` int(11) NOT NULL,
  `nome_prato` varchar(60) NOT NULL,
  `preço_prato` float NOT NULL,
  `descrição` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `CPF` int(11) NOT NULL,
  `nome` varchar(60) DEFAULT NULL,
  `função` varchar(60) DEFAULT NULL,
  `telefone` varchar(60) DEFAULT NULL,
  `RG` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `mesas`
--

CREATE TABLE `mesas` (
  `numero_mesa` int(11) NOT NULL,
  `quantidade_cadeiras` int(11) NOT NULL,
  `numero_setor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pedidos`
--

CREATE TABLE `pedidos` (
  `numero_pedido` int(11) NOT NULL,
  `nome_pedido` varchar(60) NOT NULL,
  `codigo_prato` int(11) NOT NULL,
  `CPF_funcionario` int(11) NOT NULL,
  `numero_mesa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `setor`
--

CREATE TABLE `setor` (
  `numero_setor` int(11) NOT NULL,
  `nome_setor` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cardapio`
--
ALTER TABLE `cardapio`
  ADD PRIMARY KEY (`codigo_prato`);

--
-- Índices para tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`CPF`);

--
-- Índices para tabela `mesas`
--
ALTER TABLE `mesas`
  ADD PRIMARY KEY (`numero_mesa`),
  ADD KEY `numero_setor` (`numero_setor`);

--
-- Índices para tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD KEY `codigo_prato` (`codigo_prato`),
  ADD KEY `CPF_funcionario` (`CPF_funcionario`),
  ADD KEY `numero_mesa` (`numero_mesa`);

--
-- Índices para tabela `setor`
--
ALTER TABLE `setor`
  ADD PRIMARY KEY (`numero_setor`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `mesas`
--
ALTER TABLE `mesas`
  ADD CONSTRAINT `mesas_ibfk_1` FOREIGN KEY (`numero_setor`) REFERENCES `setor` (`numero_setor`);

--
-- Limitadores para a tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`codigo_prato`) REFERENCES `cardapio` (`codigo_prato`),
  ADD CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`CPF_funcionario`) REFERENCES `funcionario` (`CPF`),
  ADD CONSTRAINT `pedidos_ibfk_3` FOREIGN KEY (`numero_mesa`) REFERENCES `mesas` (`numero_mesa`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
