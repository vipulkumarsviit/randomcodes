/**
 * Embeds an image watermark over a source image to produce
 * a watermarked one.
 * @param watermarkImageFile The image file used as the watermark.
 * @param sourceImageFile The source image file.
 * @param destImageFile The output image file.
 */
static void addImageWatermark(File watermarkImageFile, File sourceImageFile, File destImageFile) {
    try {
        BufferedImage sourceImage = ImageIO.read(sourceImageFile);
        BufferedImage watermarkImage = ImageIO.read(watermarkImageFile);
 
        // initializes necessary graphic properties
        Graphics2D g2d = (Graphics2D) sourceImage.getGraphics();
        AlphaComposite alphaChannel = AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.3f);
        g2d.setComposite(alphaChannel);
 
        // calculates the coordinate where the image is painted
        int topLeftX = (sourceImage.getWidth() - watermarkImage.getWidth()) / 2;
        int topLeftY = (sourceImage.getHeight() - watermarkImage.getHeight()) / 2;
 
        // paints the image watermark
        g2d.drawImage(watermarkImage, topLeftX, topLeftY, null);
 
        ImageIO.write(sourceImage, "png", destImageFile);
        g2d.dispose();
 
        System.out.println("The image watermark is added to the image.");
 
    } catch (IOException ex) {
        System.err.println(ex);
    }
}

public static void main(Sting[] args){
  File sourceImageFile = new File("e:/Test/Watermark/SwingEmailSender.png");
  File watermarkImageFile = new File("e:/Test/Watermark/CodeJavaLogo.png");
  File destImageFile = new File("e:/Test/Watermark/text_watermarked.png");
 
  addImageWatermark(watermarkImageFile, sourceImageFile, destImageFile);
}
