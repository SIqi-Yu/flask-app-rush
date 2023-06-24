-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Jun 24, 2023 at 08:25 AM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tennisclub`
--

-- --------------------------------------------------------

--
-- Table structure for table `challenge`
--

CREATE TABLE `challenge` (
  `CID` int(11) NOT NULL,
  `ChallengerMEID` int(11) NOT NULL,
  `ChallengedMEID` int(11) NOT NULL,
  `DateOfChallenge` date NOT NULL,
  `Notes` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `challenge`
--

INSERT INTO `challenge` (`CID`, `ChallengerMEID`, `ChallengedMEID`, `DateOfChallenge`, `Notes`) VALUES
(1, 1, 2, '2023-06-02', 'hello'),
(6, 2, 3, '2023-06-08', 'You\'ll lose'),
(10, 2, 3, '2023-06-08', 'You\'ll lose'),
(66, 2, 1, '2023-07-08', 'You\'ll lose');

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `MEID` int(11) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `MPassword` varchar(30) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Age` int(11) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `UTR` float NOT NULL,
  `DateOfCreation` date NOT NULL,
  `is_admin` char(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`MEID`, `FirstName`, `LastName`, `Email`, `MPassword`, `Phone`, `Age`, `Gender`, `UTR`, `DateOfCreation`, `is_admin`) VALUES
(1, 'Alice', 'Dull', '123@qq.com', '1234567', '12345763408', 23, 'female', 3, '2023-06-19', 'NO'),
(2, 'Bob', 'Wen', '384@cm.com', '12345', '18283948576', 31, 'male', 4, '2322-06-10', 'NO'),
(3, 'Arey', 'R', '1335@ww.com', '00000', '38264736', 23, 'Male', 2, '2021-03-10', 'YES'),
(9, 'Jian', 'Men', '1608231235@qq.com', '2222222222', '1234560987', 17, 'female', 2, '2023-06-22', 'NO'),
(10, 'Mike', 'Wang', '16235@qq.com', '987654321', '1234560987', 26, 'male', 2, '2023-06-21', 'NO'),
(44, 'meng', 'jiang', '1236t826@kk.com', '1029384756', '111111111111', 33, 'female', 4, '2023-06-21', 'YES'),
(99, '3', '3', '2@qq.com', '3243', '3', 2, 'female', 3, '2023-06-24', 'NO'),
(555, 'Jiang', 'Meng', '1608231235@qq.com', '123456567', '243463', 21, 'female', 3, '2023-06-21', 'YES'),
(999, '3', '3', '2@qq.com', '32', '3', 2, 'female', 3, '2023-06-24', 'YES'),
(1111, 'de', 'de', '234@we.com', '1234567', '2345678', 27, 'female', 3, '2023-06-21', 'NO'),
(2345, 'dfvgbn', 'ergh', '2345@qw.com', '1234567', '234567', 56, 'male', 3, '2023-06-21', 'YES'),
(9999, '3', '3', '2@qq.com', '44', '3', 2, 'female', 3, '2023-06-24', 'admin'),
(99992, '3', '3', '2@qq.com', 'edded', '3', 2, 'female', 3, '2023-06-24', 'NO');

-- --------------------------------------------------------

--
-- Table structure for table `membership`
--

CREATE TABLE `membership` (
  `MSID` int(11) NOT NULL,
  `MEID` int(11) NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `InvoiceDate` date NOT NULL,
  `DueDate` date NOT NULL,
  `Amount` decimal(10,0) NOT NULL,
  `PaidDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `membership`
--

INSERT INTO `membership` (`MSID`, `MEID`, `StartDate`, `EndDate`, `InvoiceDate`, `DueDate`, `Amount`, `PaidDate`) VALUES
(3, 789, '2023-01-01', '2023-12-31', '2023-01-01', '2023-01-15', '150', NULL),
(4, 234, '2023-01-01', '2023-12-31', '2023-01-01', '2023-01-15', '90', '2023-01-10'),
(5, 567, '2023-01-01', '2023-12-31', '2023-01-01', '2023-01-15', '110', NULL),
(6, 890, '2023-01-01', '2023-12-31', '2023-01-01', '2023-01-15', '130', '2023-01-10'),
(7, 123, '2023-01-01', '2023-12-31', '2023-01-01', '2023-01-15', '100', NULL),
(8, 456, '2023-01-01', '2023-12-31', '2023-01-01', '2023-01-15', '120', '2023-01-10'),
(9, 789, '2023-01-01', '2023-12-31', '2023-01-01', '2023-01-15', '150', '2023-01-10'),
(11, 9, '2023-06-22', '2023-07-02', '2023-07-01', '2023-06-25', '6', '2023-06-11'),
(12, 9, '2023-06-22', '2023-07-02', '2023-07-01', '2022-06-25', '6', '2023-06-11');

-- --------------------------------------------------------

--
-- Table structure for table `tmatch`
--

CREATE TABLE `tmatch` (
  `MAID` int(11) NOT NULL,
  `CID` int(11) DEFAULT NULL,
  `DateOfMatch` date NOT NULL,
  `MEID1Set1Score` int(11) NOT NULL,
  `MEID2Set1Score` int(11) NOT NULL,
  `MEID1Set2Score` int(11) DEFAULT NULL,
  `MEID2Set2Score` int(11) DEFAULT NULL,
  `MEID1Set3Score` int(11) DEFAULT NULL,
  `MEID2Set3Score` int(11) DEFAULT NULL,
  `WinnerMEID` int(11) DEFAULT NULL,
  `LoserMEID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tmatch`
--

INSERT INTO `tmatch` (`MAID`, `CID`, `DateOfMatch`, `MEID1Set1Score`, `MEID2Set1Score`, `MEID1Set2Score`, `MEID2Set2Score`, `MEID1Set3Score`, `MEID2Set3Score`, `WinnerMEID`, `LoserMEID`) VALUES
(2, 6, '2023-06-10', 7, 0, 0, 7, 10, 0, 2, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `challenge`
--
ALTER TABLE `challenge`
  ADD PRIMARY KEY (`CID`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`MEID`);

--
-- Indexes for table `membership`
--
ALTER TABLE `membership`
  ADD PRIMARY KEY (`MSID`);

--
-- Indexes for table `tmatch`
--
ALTER TABLE `tmatch`
  ADD PRIMARY KEY (`MAID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `challenge`
--
ALTER TABLE `challenge`
  MODIFY `CID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `MEID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=99993;

--
-- AUTO_INCREMENT for table `membership`
--
ALTER TABLE `membership`
  MODIFY `MSID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `tmatch`
--
ALTER TABLE `tmatch`
  MODIFY `MAID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
