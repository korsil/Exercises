#include <stdio.h>
#include <string.h>

#define OUT_SIZE 30

int format(int number, int out_length, char *out)
{
    char temp[OUT_SIZE];
    sprintf(temp, "%d", number);

    int len = strlen(temp);
    int is_negative = (number < 0) ? 1 : 0;
    int digit_count = len - is_negative;
    int comma_count = (digit_count - 1) / 3;
    int len_result = len + comma_count;

    if(out_length < len_result + 1)
    {
        return -1;
    }

    out[len_result] = '\0';

    int offset = 0; // if negative, we push one to the right;
    if(number < 0)
    {
        offset = 1;
        out[0] = temp[0];
    }
    
    int current_temp_index = offset;
    for(int current_idx = offset; current_idx < len_result; ++current_idx)
    {
        // 1234567891
        // 1,234,567,891
        int len_left = (len_result - current_idx);
        int is_comma = (len_left % 4) == 0 && len_left > 0;
        // printf("Len left %d, IsComma %d\n", len_left, is_comma);

        if(is_comma)
        {
            out[current_idx] = ',';
        }
        else 
        {
            out[current_idx] = temp[current_temp_index];
           // printf("Temp[%d] = %c\n", current_temp_index, temp[current_temp_index]);
            current_temp_index++;
        }
        // printf("Current out %s\n-----------\n", out);
    }

    return 1;
}

int main() {
    int number;
    printf("Enter your number: ");
  
    scanf_s("%d", &number);
    printf("Input: %d\n", number);
    char formatted[OUT_SIZE];
    if(!format(number, OUT_SIZE, formatted))
    {
        printf("Failed to format.");
    }
    printf("Result %s\n", formatted);

    /*
    int numbers[20];
    numbers[0] = 1;
    numbers[1] = 12;
    numbers[2] = 123;
    numbers[3] = 1234;
    numbers[4] = 12345;
    numbers[5] = 123456;
    numbers[6] = 1234567;
    numbers[7] = 12345678;
    numbers[8] = 123456789;
    numbers[9] = 1234567890;
    
    numbers[10] = -1;
    numbers[11] = -12;
    numbers[12] = -123;
    numbers[13] = -1234;
    numbers[14] = -12345;
    numbers[15] = -123456;
    numbers[16] = -1234567;
    numbers[17] = -12345678;
    numbers[18] = -123456789;
    numbers[19] = -1234567890;
    
    for(int i = 0; i < 20; ++i )
    {
        char formatted[OUT_SIZE];
        if(!format(numbers[i], OUT_SIZE, formatted))
        {
            printf("Failed to format.");
        }
        printf("=========\nResult %s\n=========\n", formatted);
    }
    */
        
    
    return 0;
}