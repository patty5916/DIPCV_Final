import cv2
import numpy as np
import dlib
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance


class OpencvEngine(object):
    @staticmethod
    def point_fload_to_int(point):
        return (int(point[0]), int(point[1]))

    @staticmethod
    def read_image(file_path):
        img = cv2.imread(file_path)
        h, w, c = img.shape
        # resize
        if h > 512 or w > 512:
            if h < w:
                img = cv2.resize(img, (512, int(h / (w / 512))))
            else:
                img = cv2.resize(img, (int(w / (h / 512)), 512))
        return img

    @staticmethod
    def modify_denoising(img, value1=1, value2=1):
        opacity = 0.1
        dx = value1 * 5
        fc = value1 * 12.5
        temp_img = cv2.bilateralFilter(img, dx, fc, fc)
        temp_img = temp_img - img
        temp_img = cv2.GaussianBlur(temp_img, (2 * value2 - 1, 2 * value2 - 1), 0)
        temp_img = img + temp_img
        dst = cv2.addWeighted(img, opacity, temp_img, (1 - opacity), 0)
        return dst


    @staticmethod
    def modify_brightness(img, brightness=1):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        enh_bri = ImageEnhance.Brightness(img)
        image_brightened = enh_bri.enhance(brightness)
        return cv2.cvtColor(np.array(image_brightened), cv2.COLOR_RGB2BGR)

    @staticmethod
    def modify_contrast(img, contrast=1):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        enh_con = ImageEnhance.Contrast(img)
        image_contrasted = enh_con.enhance(contrast)
        return cv2.cvtColor(np.array(image_contrasted), cv2.COLOR_RGB2BGR)

    @staticmethod
    def modify_color(img, color=1):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        enh_col = ImageEnhance.Color(img)
        image_colored = enh_col.enhance(color)
        return cv2.cvtColor(np.array(image_colored), cv2.COLOR_RGB2BGR)

    @staticmethod
    def modify_sharpness(img, sharpness=1):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        enh_sha = ImageEnhance.Sharpness(img)
        image_sharped = enh_sha.enhance(sharpness)
        return cv2.cvtColor(np.array(image_sharped), cv2.COLOR_RGB2BGR)

    @staticmethod
    def modify_rgb(img, r=0, g=0, b=0):
        (B, G, R) = cv2.split(img)
        B = np.array(B + b, dtype='uint8')
        G = np.array(G + g, dtype='uint8')
        R = np.array(R + r, dtype='uint8')
        merged = cv2.merge([B, G, R])
        return merged


    @staticmethod
    def modify_white(img, value1=1, value2=1):
        dx = value1 * 5
        fc = value1 * 12.5
        p = 0.1

        temp1 = cv2.bilateralFilter(img, dx, fc, fc)
        temp2 = cv2.subtract(temp1, img)
        temp2 = cv2.add(temp2, (10, 10, 10, 128))

        temp3 = cv2.GaussianBlur(temp2, (2 * value2 - 1, 2 * value2 - 1), 0)
        temp4 = cv2.add(img, temp3)
        dst = cv2.addWeighted(img, p, temp4, 1 - p, 0.0)
        dst = cv2.add(dst, (10, 10, 10, 255))
        return dst

    @staticmethod
    def modify_lipstick(img, r):
        dlib_path = 'shape_predictor_81_face_landmarks.dat'
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(dlib_path)

        jaw_point = list(range(0, 17)) + list(range(68, 81))
        left_eye = list(range(42, 48))
        right_eye = list(range(36, 42))
        left_brow = list(range(22, 27))
        right_brow = list(range(17, 22))
        mouth = list(range(48, 61))
        nose = list(range(27, 35))
        align = (left_brow + right_eye + left_eye + right_brow + nose + mouth)

        def get_landmark(img):
            faces = detector(img, 1)
            shape = predictor(img, faces[0]).parts()
            return np.matrix([[p.x, p.y] for p in shape])

        def draw_convex_hull(img, points, color):
            hull = cv2.convexHull(points)
            cv2.fillConvexPoly(img, hull, color=color)

        def get_organ_mask(img, tag):
            landmarks = get_landmark(img)
            mask = np.zeros(img.shape[:2])
            if tag == 'eye':
                white = [right_eye, left_eye]
            if tag == 'nose':
                white = [nose]
            if tag == 'mouth':
                white = [mouth]
            if tag == 'eyebrow':
                white = [left_brow, right_brow]
            for group in white:
                points = landmarks[group]
                draw_convex_hull(mask, points, 1)
            mask = np.array([mask] * 3).transpose(1, 2, 0)
            mask = (cv2.GaussianBlur(mask, (11, 11), 0) > 0) * 1.0
            mask = cv2.GaussianBlur(mask, (11, 11), 0)
            return mask

        # 紅唇 (r越大越紅，1~255)
        def rouge(image, r):
            image_cp = image.copy()
            rouge_color = (0, 0, r)
            landmarks = get_landmark(img)
            points = landmarks[48:68]
            hull = cv2.convexHull(points)
            cv2.drawContours(image, [hull], -1, rouge_color, -1)
            cv2.addWeighted(image, 0.2, image_cp, 0.9, 0, image_cp)
            return image_cp

        return rouge(img, r)


    @staticmethod
    def modify_thin(img, right=0, left=0):
        predictor_path = 'shape_predictor_68_face_landmarks.dat'
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(predictor_path)

        def landmark_dec_dlib_fun(img_src):
            img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
            land_marks = []
            rects = detector(img_gray, 0)
            for i in range(len(rects)):
                land_marks_node = np.matrix([[p.x, p.y] for p in predictor(img_gray, rects[i]).parts()])
                land_marks.append(land_marks_node)
            return land_marks

        # 方法： Interactive Image Warping 局部平移算法
        def localTranslationWarp(srcImg, startX, startY, endX, endY, radius):
            ddradius = float(radius * radius)
            copyImg = np.zeros(srcImg.shape, np.uint8)
            copyImg = srcImg.copy()
            # 计算公式中的|m-c|^2
            ddmc = (endX - startX) * (endX - startX) + (endY - startY) * (endY - startY)
            H, W, C = srcImg.shape
            for i in range(W):
                for j in range(H):
                    # 计算该点是否在形变圆的范围之内
                    # 优化，第一步，直接判断是会在（startX,startY)的矩阵框中
                    if math.fabs(i - startX) > radius and math.fabs(j - startY) > radius:
                        continue
                    distance = (i - startX) * (i - startX) + (j - startY) * (j - startY)
                    if (distance < ddradius):
                        # 计算出（i,j）坐标的原坐标
                        # 计算公式中右边平方号里的部分
                        ratio = (ddradius - distance) / (ddradius - distance + ddmc)
                        ratio = ratio * ratio
                        # 映射原位置
                        UX = i - ratio * (endX - startX)
                        UY = j - ratio * (endY - startY)
                        # 根据双线性插值法得到UX，UY的值
                        value = BilinearInsert(srcImg, UX, UY)
                        # 改变当前 i ，j的值
                        copyImg[j, i] = value
            return copyImg

        # 双线性插值法
        def BilinearInsert(src, ux, uy):
            w, h, c = src.shape
            if c == 3:
                x1 = int(ux)
                x2 = x1 + 1
                y1 = int(uy)
                y2 = y1 + 1
                part1 = src[y1, x1].astype(np.float) * (float(x2) - ux) * (float(y2) - uy)
                part2 = src[y1, x2].astype(np.float) * (ux - float(x1)) * (float(y2) - uy)
                part3 = src[y2, x1].astype(np.float) * (float(x2) - ux) * (uy - float(y1))
                part4 = src[y2, x2].astype(np.float) * (ux - float(x1)) * (uy - float(y1))
                insertValue = part1 + part2 + part3 + part4
                return insertValue.astype(np.int8)

        def face_thin_auto(src, right, left):
            landmarks = landmark_dec_dlib_fun(src)
            # 如果未检测到人脸关键点，就不进行瘦脸
            if len(landmarks) == 0:
                return
            for landmarks_node in landmarks:
                left_landmark = landmarks_node[3]
                left_landmark_down = landmarks_node[5]
                right_landmark = landmarks_node[13]
                right_landmark_down = landmarks_node[15]
                endPt = landmarks_node[30]
                r_left = left
                r_right = right
                # 瘦左边脸
                thin_image = localTranslationWarp(src, left_landmark[0, 0], left_landmark[0, 1], endPt[0, 0],
                                                  endPt[0, 1], r_left)
                # 瘦右边脸
                thin_image = localTranslationWarp(thin_image, right_landmark[0, 0], right_landmark[0, 1], endPt[0, 0],
                                                  endPt[0, 1], r_right)
                return thin_image

        return face_thin_auto(img, right, left)


    @staticmethod
    def modify_bigeye(img, right=0, left=0):
        predictor_path = 'shape_predictor_68_face_landmarks.dat'
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(predictor_path)

        def landmark_dec_dlib_fun(img_src):
            img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
            land_marks = []
            rects = detector(img_gray, 0)
            for i in range(len(rects)):
                land_marks_node = np.matrix([[p.x, p.y] for p in predictor(img_gray, rects[i]).parts()])
                land_marks.append(land_marks_node)
            return land_marks

        # 圖像局部縮法算法
        def localZoomWarp(srcImg, point, radius, strength):
            ddradius = float(radius * radius)
            copyImg = np.zeros(srcImg.shape, np.uint8)
            copyImg = srcImg.copy()
            H, W, C = srcImg.shape
            for y in range(W):
                for x in range(H):
                    distance = (x - point[0, 0]) * (x - point[0, 0]) + (y - point[0, 1]) * (y - point[0, 1])
                    if (distance < ddradius):
                        ratio = 1 - distance / ddradius
                        ratio = 1 - strength / 100 * ratio
                        UX = (x - point[0, 0]) * ratio + point[0, 0]
                        UY = (y - point[0, 1]) * ratio + point[0, 1]
                        value = BilinearInsert(srcImg, UX, UY)
                        copyImg[y, x] = value
            return copyImg

        def BilinearInsert(src, ux, uy):
            w, h, c = src.shape
            if c == 3:
                x1 = int(ux)
                x2 = x1 + 1
                y1 = int(uy)
                y2 = y1 + 1
                part1 = src[y1, x1].astype(np.float) * (float(x2) - ux) * (float(y2) - uy)
                part2 = src[y1, x2].astype(np.float) * (ux - float(x1)) * (float(y2) - uy)
                part3 = src[y2, x1].astype(np.float) * (float(x2) - ux) * (uy - float(y1))
                part4 = src[y2, x2].astype(np.float) * (ux - float(x1)) * (uy - float(y1))
                insertValue = part1 + part2 + part3 + part4
                return insertValue.astype(np.int8)

        def big_eye(src, left_radius, right_radius, strength):
            # radius眼睛放大範圍半徑.strength眼睛放大程度
            landmarks = landmark_dec_dlib_fun(src)
            if len(landmarks) == 0:
                return
            for landmarks_node in landmarks:
                left_landmark = landmarks_node[37]
                left_landmark_down = landmarks_node[41]
                left_center = (left_landmark + left_landmark_down) / 2
                right_landmark = landmarks_node[43]
                right_landmark_down = landmarks_node[47]
                right_center = (right_landmark + right_landmark_down) / 2
                left_radius = left_radius
                right_radius = right_radius
                strength = strength
                eye_image = localZoomWarp(src, left_center, left_radius, strength)
                eye_image = localZoomWarp(eye_image, right_center, right_radius, strength)
            return eye_image

        return big_eye(img, left, right, strength)


    @staticmethod
    def old_pic(img):
        rows, cols, channals = img.shape
        for r in range(rows):
            for c in range(cols):
                B = img.item(r, c, 0)
                G = img.item(r, c, 1)
                R = img.item(r, c, 2)
                img[r, c, 0] = np.uint8(min(max(0.272 * R + 0.534 * G + 0.131 * B, 0), 255))
                img[r, c, 1] = np.uint8(min(max(0.349 * R + 0.686 * G + 0.168 * B, 0), 255))
                img[r, c, 2] = np.uint8(min(max(0.393 * R + 0.769 * G + 0.189 * B, 0), 255))
        return img


    @staticmethod
    def pencil(img):
        dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=100, sigma_r=0.1, shade_factor=0.03)
        return dst_gray


    @staticmethod
    def cartoon(img):
        dst_comic = cv2.stylization(img, sigma_s=150, sigma_r=0.25)
        return dst_comic
