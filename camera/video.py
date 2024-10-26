import cv2 as cv
import time

cap = cv.VideoCapture(0)
image_dir_path = "N_images"
n = 0

while True:
	ret, frame = cap.read()
	if not ret:
		break
	cv.imshow("frame", frame)
	
	key = cv.waitKey(1)
	
	if key == ord("q"):
		break

	if n < 500:
		cv.imwrite(f"{image_dir_path}/image{n}.png", frame)
		print(f"Saved image number {n}")
		n += 1  # Increment the image counter
		time.sleep(0.1)
	else:
		print("Reached the limit of 500 images.")
		break  # Exit the loop after saving 30 images
# To delete all png images in a directory: rm -r *.png

cap.release()
cv.destroyAllWindows()
