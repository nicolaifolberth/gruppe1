package snippets_vorlesung.sample1;

public class HelloWorld {
    public static void main(String[] args) {

        int[] PrimeNumbers = new int[100];

        int Number=3;

        for(int i=0;i<100;i++){
            boolean Exam = true;
            int Divisor=2;

            do {
                if (Number % Divisor != 0) {
                    Exam = true;
                    Divisor++;
                } else {
                    Exam = false;
                    break;
                }
            } while(Exam == true &&  Divisor<Number);

            if(Exam == true){
                PrimeNumbers[i] = Number;
                Number++;
            }
            else {
                Number++;
            }

            System.out.println(PrimeNumbers[i]);
        }

    }
}