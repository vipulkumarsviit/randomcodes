## Java Encryption/Decryption & JavaScript Decryption/Decryption Using AES Algorithm

### Prerequisites

- For java we require javax.crypto.* package.
- For Javascript we require CryptoJS library. `npm i @types/crypto-js crypto-js`



### JAVA Code

```
package com.javacodegeeks.examples.crypto;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.Key;
import java.util.Base64;

public class EncryptionUtils {
    private static final String ALGO = "AES";

    public static String encrypt(String Data, String secret) throws Exception {
        Key key = generateKey(secret);
        Cipher c = Cipher.getInstance(ALGO);
        c.init(Cipher.ENCRYPT_MODE, key);
        byte[] encVal = c.doFinal(Data.getBytes());
        return Base64.getEncoder().encodeToString(encVal);
    }

    public static String decrypt(String strToDecrypt, String secret) {
        try {
            Key key = generateKey(secret);
            Cipher cipher = Cipher.getInstance(ALGO);
            cipher.init(Cipher.DECRYPT_MODE, key);
            return new String(cipher.doFinal(Base64.getDecoder().decode(strToDecrypt)));
        } catch (Exception e) {
            System.out.println("Error while decrypting: " + e.toString());
        }
        return null;
    }

    private static Key generateKey(String secret) {
        byte[] decoded = Base64.getDecoder().decode(secret.getBytes());
        return new SecretKeySpec(decoded, ALGO);
    }

    public static String decodeKey(String str) {
        byte[] decoded = Base64.getDecoder().decode(str.getBytes());
        return new String(decoded);
    }

    public static String encodeKey(String str) {
        byte[] encoded = Base64.getEncoder().encode(str.getBytes());
        return new String(encoded);
    }

    public static void main(String args[]) throws Exception {
        String secretKey = "mustbe16byteskey";
        String encodedBase64Key = encodeKey(secretKey);
        System.out.println("EncodedBase64Key = " + encodedBase64Key);

        String toEncrypt = "Please encrypt this message!";
        System.out.println("Plain text = " + toEncrypt);

        String encrStr = encrypt(toEncrypt, encodedBase64Key);
        System.out.println("Cipher Text: Encryption of str = " + encrStr);

        String decrStr = decrypt(encrStr, encodedBase64Key);
        System.out.println("Decryption of str = " + decrStr);
    }
}

```

### Javascript Code

```
export class UtilsService {

  secretKeyBase64 = 'bXVzdGJlMTZieXRlc2tleQ==';
  secretKey = CryptoJS.enc.Base64.parse(this.secretKeyBase64);
  encrypt(plainText: string): string {
    return CryptoJS.AES.encrypt(plainText, this.secretKey, {
      mode: CryptoJS.mode.ECB,
      padding: CryptoJS.pad.Pkcs7
    }).toString();
  }
  decrypt(encryptedText: string): string {
    return CryptoJS.AES.decrypt(encryptedText, this.secretKey, {
      mode: CryptoJS.mode.ECB,
      padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Utf8);
  }
}
  
```
