from PIL import Image, ImageTk

class Graphic():
    def enlarge(self, file_path: str, sf: float):
        image = Image.open(file_path)
        image = image.resize((int(image.width * sf), int(image.height * sf)), Image.NEAREST)
        return ImageTk.PhotoImage(image)