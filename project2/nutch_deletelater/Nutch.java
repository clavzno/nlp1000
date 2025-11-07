/**
 * @(#)Nutch.java
 *
 * Nutch application
 *
 * @author 
 * @version 1.00 2011/11/20
 * 
 */

import java.io.File;
import java.io.InputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.BufferedInputStream;

import org.apache.nutch.analysis.lang.*;
 
public class Nutch {
    
    public static void main(String[] args) throws Exception {
    	
	   	InputStream input = new FileInputStream("Trigram\\Bikol.txt");
		OutputStream output = new FileOutputStream("Trigram\\bik.ngp");

    	NGramProfile testing = new NGramProfile("tl",1,4);
    	testing = testing.create("tl",input,"UTF-8");
		testing.save(output);
		
	   	input = new FileInputStream("Trigram\\Cebuano.txt");
		output = new FileOutputStream("Trigram\\ceb.ngp");
    	testing = testing.create("tl",input,"UTF-8");
		testing.save(output);

	   	input = new FileInputStream("Trigram\\Hiligaynon.txt");
		output = new FileOutputStream("Trigram\\hil.ngp");
    	testing = testing.create("tl",input,"UTF-8");
		testing.save(output);

	   	input = new FileInputStream("Trigram\\Ilocano.txt");
		output = new FileOutputStream("Trigram\\ilo.ngp");
    	testing = testing.create("tl",input,"UTF-8");
		testing.save(output);

	   	input = new FileInputStream("Trigram\\Kapampangan.txt");
		output = new FileOutputStream("Trigram\\pam.ngp");
    	testing = testing.create("tl",input,"UTF-8");
		testing.save(output);

	   	input = new FileInputStream("Trigram\\Pangasinense.txt");
		output = new FileOutputStream("Trigram\\pag.ngp");
    	testing = testing.create("tl",input,"UTF-8");
		testing.save(output);

	   	input = new FileInputStream("Trigram\\Tagalog.txt");
		output = new FileOutputStream("Trigram\\tl.ngp");
    	testing = testing.create("tl",input,"UTF-8");
		testing.save(output);

	   	input = new FileInputStream("Trigram\\Waray.txt");
		output = new FileOutputStream("Trigram\\war.ngp");
    	testing = testing.create("tl",input,"UTF-8");
		testing.save(output);
    }
}
