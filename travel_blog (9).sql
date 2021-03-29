-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 12, 2021 at 10:41 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `travel_blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact_me`
--

CREATE TABLE `contact_me` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `msg` varchar(200) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact_me`
--

INSERT INTO `contact_me` (`sno`, `name`, `email`, `phone`, `msg`, `date`) VALUES
(1, 'Yogendra ', 'shastri.yogendra32@gmail.com', '9770985677', 'till now your code is working fine', '2020-06-28 17:02:35'),
(4, 'Rajendra Mishra ', 'mishrarajendra377@gmail.com', '7859642351', 'yogi you are great ', NULL),
(13, 'Dhairya sheel rastogi', 'drs@gmail.com', '9856472365', 'chal chai pine jayega\r\n', NULL),
(14, 'Yogendra shastri', 'shastri.yogendra32@gmail.com', '09770985677', 'bhai accha website banaye ho .. keep it up ..', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `sno` int(11) NOT NULL,
  `title` varchar(20) NOT NULL,
  `description` varchar(200) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`sno`, `title`, `description`, `date`) VALUES
(1, '12 th All subjects ', 'we provide coaching guidance and notes for 12th standards.', '2020-07-14 00:00:00'),
(2, '11th class ', 'Provides a good quality of learning ', '2020-07-18 00:00:00'),
(3, '3rd Subject', 'this course is best', '2020-07-18 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `sno` int(50) NOT NULL,
  `image` varchar(20) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `details` varchar(200) NOT NULL,
  `phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`sno`, `image`, `name`, `details`, `phone`) VALUES
(4, 'img.jpeg', 'yogendra shastri', 'mca from nit ', '+91 9770985677'),
(5, 'vivek.jpeg', 'Vivek Ranjan  Pradha', 'new faculty member', '8517087837'),
(6, 'kishan.jpeg', 'Kishan Patel', 'Our New faculty member', '7693036650');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(10) NOT NULL,
  `img_file` varchar(26) NOT NULL,
  `title` varchar(20) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` varchar(200) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `img_file`, `title`, `slug`, `content`, `date`) VALUES
(1, 'asdasdas', 'kishan patel', 'sfasdasd', 'dasd', '2020-07-15 00:00:00'),
(3, 'dfsdsf', 'third_post edited', 'sdfsdf', 'dsfsdf', '0000-00-00 00:00:00'),
(5, '', 'fifth post ', 'fifth_post ', 'this is fith number of  post bad boys bad boys what you gonna do', '0000-00-00 00:00:00'),
(6, '', '6th post ', 'sixth_post', 'this is the sixth post what you gonna do ', '0000-00-00 00:00:00'),
(8, 'sdfdsf', 'xcvcxv', 'sdfdsfs', 'fsdfdsf', '2020-07-08 00:00:00'),
(9, 'sdfdsf', 'dxfsdf', 'dsfsdf', 'sdfdsf', '2020-07-08 00:00:00'),
(11, 'tenth_post.jpg', '10th post ', 'post-tenth', 'this is the 10th newly added post. you can see that.', '2020-07-10 00:00:00'),
(12, 'tenth_post.jpg', '10th post  extended', 'post-tenth', 'this is the 10th newly added post. you can see that.', '2020-07-10 00:00:00'),
(13, 'jdjfhdhf', 'kishan chutiya ', 'kishn', 'kishan is akand chodu adami ', '2020-07-18 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `video_tutorials`
--

CREATE TABLE `video_tutorials` (
  `sno` int(50) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(200) NOT NULL,
  `link` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `video_tutorials`
--

INSERT INTO `video_tutorials` (`sno`, `title`, `description`, `link`) VALUES
(3, 'death note ep2', 'second episode of death note', 'https://www.youtube.com/embed/2zx68_8jR5g'),
(4, 'Bootstrap-4 team section', 'this video is to tell how to use bootstrap 4.', 'https://www.youtube.com/embed/riJNC42oJaw'),
(5, 'death-note ep 3', 'third episode of death note ', 'https://www.youtube.com/embed/Sejl9v2EQMA');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact_me`
--
ALTER TABLE `contact_me`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `video_tutorials`
--
ALTER TABLE `video_tutorials`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact_me`
--
ALTER TABLE `contact_me`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `faculty`
--
ALTER TABLE `faculty`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `video_tutorials`
--
ALTER TABLE `video_tutorials`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
