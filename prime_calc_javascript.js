let max_range = 100000;

let count = 0;

for (let dividend = 1; dividend < max_range + 1; dividend++) {

    let is_prime = true;
    for (let divisor = 2; divisor < dividend; divisor++) {
        if (dividend % divisor == 0)  {
            is_prime = false;
            break;
        }
    }

    if (!is_prime) {
        continue;
    }
    count++;
}

console.log(count);