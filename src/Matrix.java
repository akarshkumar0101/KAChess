
public class Matrix {
	public static int dotProduct(int[][] a, int[][] b) {
		
		if(a.length != b.length || a[0].length != b[0].length) {
			throw new IllegalArgumentException();
		}
		
		int dotProduct = 0;
		for(int i = 0; i < a.length; i++) {
			for(int j = 0; j < a[0].length; j++) {
				dotProduct += a[i][j] * b[i][j];
			}
		}
		
		return dotProduct;
	}
}
