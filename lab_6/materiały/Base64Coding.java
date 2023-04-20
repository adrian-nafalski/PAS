/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.UnsupportedEncodingException;
// java 6,7
import javax.xml.bind.DatatypeConverter;

/**
 *
 * @author kasiula
 */
class Base64Coding {

    public static String base64_to_text_java6_7(String text) throws UnsupportedEncodingException {
        byte[] decoded = DatatypeConverter.parseBase64Binary(text);
        return (new String(decoded, "UTF-8"));
    }

    public static String text_to_base64_java6_7(String text) throws UnsupportedEncodingException {
        byte[] message = text.getBytes("UTF-8");
        String encoded = DatatypeConverter.printBase64Binary(message);
        return encoded;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws UnsupportedEncodingException {

        System.out.println(base64_to_text_java6_7("SGVsbG8gV29ybGQ="));
        System.out.println(text_to_base64_java6_7("Hello World"));
    }

}
