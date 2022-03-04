// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Sum {
    function sumTwoNumbers(int number1, int number2) public pure returns (int) {
        return number1 + number2;
    }
}