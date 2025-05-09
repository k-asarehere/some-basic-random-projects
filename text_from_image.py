# extract or read text from an image 

from spire.ocr import *  

try:
    # initialize an OCR object for scanning 
    scanner = OcrScanner()
    # configure OCR options (language and model path for text recognition) 
    ConfigureOptions = ConfigureOptions()
    ConfigureOptions.ModelPath = r'C:/Users/YANKEY123/Documents/win-x64/' # specify the model path of your device(different for multiple OS but same format)
    ConfigureOptions.Language = 'English' 
    scanner.ConfigureDependencies(ConfigureOptions)
    # recognize text from image 
    scanner.Scan('insert the image file path(with an extension .png or jpg etc)')

    # retrieve the recognized text and save it to a file 
    text_data = scanner.Text.ToString() + '\n'
    with open('output.txt', 'a', encoding='utf-8') as f: 
         f.write(text_data + '\n')

except Exception as e:
                print('\nError occured:', e,'\n')

