public class countbits {
	public static short countBitsFunc(int x) {
		short cnt = 0;
		while(x != 0) {
			int bit = (x & 1);
			System.out.println("x: " + Integer.toBinaryString(x) + " bit: " + bit);
			cnt += bit;
			x >>>=1;
		}
		return cnt;
	}

	public static void main(String[] args) {
		int x = 4;
		System.out.println("result: " + countBitsFunc(x));
	}

}