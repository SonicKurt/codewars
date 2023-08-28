/**
 * Does my number look big in this?
 * 
 * @author Kurt Campbell
 * @version 1.0
 * Created: 28 August 2023
 * 
 */

/**
 * Determine whether the given value is a narcissistic number.
 * @param {number} value The given value
 * @returns {boolean} true if the value is a nariccistic number. 
 * Otherwise, it is false.
 */
export function narcissistic(value: number): boolean {
    // 1. Convert the number into a string to easily compute the length
    // of the amount of digits.
    let valueStr: string = value.toString();
    
    // 2. Store the number of digits within the value. 
    let numOfDigits: number = valueStr.length;
    
    // 3. Start the summation by powering each digit by the number of digits
    // within the value and adding the value to a sum
    let sum: number = 0;
    
    for (let i = 0; i < numOfDigits; i++) {
      let digit: number = parseInt(valueStr[i]);
  
      // Perform the calculation for the product from this power.
      let powerProduct: number = digit;
      for (let j = 0; j < numOfDigits - 1; j++) {
        powerProduct *= digit;
      }
      
      sum += powerProduct;
    }
    
    // 4. Determine whether the summation equals to the given value.
    return sum === value;
  }
  