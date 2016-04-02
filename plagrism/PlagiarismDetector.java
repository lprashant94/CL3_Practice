 import java.util.Scanner;
    import java.io.*;

    public class PlagiarismDetector
    {
        public static void main(String[] args) 
		{
     Scanner reader = new Scanner(System.in);
     System.out.println("What file is the first file?");
     String fileOne = reader.next();

     String stringOne = readStringFromFile(fileOne);

     System.out.println("What file is the second file?");
     String fileTwo = reader.next();
     String stringTwo = readStringFromFile(fileTwo);

     if (stringOne == null || stringTwo == null)
     {
         return;
     }

     System.out.println("Comparing the 2 files......");
     System.out.println("The result of the 2 files is ....");

     if (compareStrings(stringOne, stringTwo))
     {
      System.out.println("Plagiarism detected.!!!!");
     }
     else
     {
           System.out.println("No plagiarism detected");
           }
        }

        public static String readStringFromFile(String filename)
        {
			//enter code here
     String builder = "";
     try
     {
         Scanner fileReader = new Scanner(new File(filename));
         while (fileReader.hasNextLine())
         {
      builder = builder + fileReader.nextLine() + "\n";
         }

         return builder;
     }
     catch (Exception e)
     {
         System.out.println("An error occurred while trying to open the file " + filename + ". Is the file located inside the same folder as the .class file and with the identical name?");
         return null;
     }
        }

         public static boolean compareStrings (String a, String b)
     {
       boolean checkForPlagiarism = true;
       String[] piecesA = a.split("\\s");
       String[] piecesB = b.split("\\s");

       int count1 = 0;
       int count2 = 0;
       for (int counter = 0; counter <= piecesA.length - 1; counter++)
        {
          for(int counter2 = 0; counter2<= piecesB.length - 1; counter2++)
          {
              if(piecesA[counter].equals(piecesB[counter2]))
              {
              count1++;
              }
          }
        }
       for (int counter = 0; counter <= piecesB.length - 1; counter++)
        {
          for(int counter2 = 0; counter2 <= piecesA.length - 1; counter2++)
          {
              if(piecesA[counter2].equals(piecesB[counter]))
              {
              count2++;
              }
          }
        }
System.out.println(count1 + " "+ count2+" "+piecesA.length+" "+piecesB.length+" "+(count1/(int)piecesA.length)*100+" "+(count2/(int)piecesB.length)*100 );
       if((count1/(int)piecesA.length)*100 >= 90 && (count2/(int)piecesB.length)*100 >= 90)
       {
         checkForPlagiarism = true;
       }   
else{
	checkForPlagiarism=false;
}	   
        return checkForPlagiarism;
      }
	}