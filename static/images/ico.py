from PIL import Image

png_path = "ico.png"      # 输入 PNG 文件
ico_path = "ico.ico"      # 输出 ICO 文件

img = Image.open(png_path).convert("RGBA")
img.save(ico_path, format="ICO", sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])

print("Done:", ico_path)
