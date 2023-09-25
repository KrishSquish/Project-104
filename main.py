import cv2

img = cv2.imread("solar-system.jpg")

#sun
cv2.putText(
    img,
    "Sun",
    (50,30),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255),
)

#mercury
cv2.putText(
    img,
    "Mercury",
    (120,190),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255),
)

#venus
cv2.putText(
    img,
    "Venus",
    (190,260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255),
)
#earth
cv2.putText(
    img,
    "Earth",
    (290,260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255),
)
#Mars
cv2.putText(
    img,
    "Mars",
    (390,260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255),
)

#Jupiter
cv2.putText(
    img,
    "Jupiter",
    (540,100),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (255,255,255),
)

#Saturn
cv2.putText(
    img,
    "Saturn",
    (760,140),
    cv2.FONT_HERSHEY_COMPLEX,
    0.6,
    (255,255,255),
)

#Uranus
cv2.putText(
    img,
    "Uranus",
    (970,140),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255),
)

#Neptune
cv2.putText(
    img,
    "Neptune",
    (1110,140),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255),
)


cv2.imshow("output",img)

cv2.waitKey(0)

