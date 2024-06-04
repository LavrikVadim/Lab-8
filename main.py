import cv2
import matplotlib.pyplot as plt 

def task1():
    print('Нажмите ESC для уменьшения изображения')
    img = cv2.imread('images/variant-9.png') 
    img1 = img.copy() 
    for i in range(4): 
        plt.subplot(2, 2, i + 1) 
        img1 = cv2.pyrDown(img1) 
        plt.imshow(img1) 
        cv2.imshow('img', img1) 
        cv2.waitKey(0)
    
        
def task2():
    coordinates = []
    def get_coordinates(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Левый клик мыши
            coordinates.append((x, y))
        print(f"Координата добавлена: ({x}, {y})")
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Frame")
    cv2.setMouseCallback("Frame", get_coordinates)
    while True:
        ret, frame = cap.read()
        if not ret:
            break    
        cv2.imshow("Frame", frame)   
        key = cv2.waitKey(1)
        if key == 27:  
            break
    cap.release()
    cv2.destroyAllWindows()
    if coordinates:
        avg_x = sum(x for x, y in coordinates) / len(coordinates)
        avg_y = sum(y for x, y in coordinates) / len(coordinates)
        print(f"Средняя координата: ({avg_x}, {avg_y})")
    else:
        print("Координаты не были записаны.")



if __name__ == '__main__':
    task1()
    task2()


