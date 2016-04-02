import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args){
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
     Scanner sc = new Scanner(System.in);
	 System.out.println("Start Generating random number");
     int i = sc.nextInt();
	 
           my_random m=new my_random(System.currentTimeMillis());				//send current time as seed.
           for(int j=0;j<i;j++){
			   System.out.println(j+" th number: "+m.next(31));
           }
    }
}

class my_random{
    private long seed;
    private static final long serialVersionUID = 3905348978240129619L;
    
    public my_random(long seed){
        setSeed(seed);
    }
    
    public synchronized void setSeed(long seed){
        this.seed = (seed ^ 0x5DEECE66DL) & ((1L << 48) - 1);
    }
    
      protected synchronized int next(int bits)
    {
      seed = (seed * 0x5DEECE66DL + 0xBL) & ((1L << 48) - 1);
      return (int) (seed >>> (48 - bits));
   }
    
     public int nextInt(int n)
    {
      if (n <= 0)
        throw new IllegalArgumentException("n must be positive");
      if ((n & -n) == n) // i.e., n is a power of 2
        return (int) ((n * (long) next(31)) >> 31);
      int bits, val;
      do
        {
          bits = next(31);
          val = bits % n;
        }
      while (bits - val + (n - 1) < 0);
      return val;
    }
    
    
}