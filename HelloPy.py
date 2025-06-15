#โจทย์ข้อที่ 1
#คำสั่ง: เขียนโปรแกรมที่
#ถาม "ชื่อเล่น" ของผู้ใช้ แล้วเก็บในตัวแปร
#ถาม "ปี พ.ศ. ที่เกิด" ของผู้ใช้ แล้วเก็บในตัวแปร
#คำนวณอายุของผู้ใช้จากปีที่เกิด (สมมติปีปัจจุบันคือ พ.ศ. 2568)
#แสดงผลลัพธ์เป็นข้อความ

name = input("What your nick name : ")
brith = int(input("What is your Brith years : "))

your_age = 2568 - brith

#เขียนแบบ f-String
print(f"Hello : {name} Now your age : {your_age} ") 

if your_age < 18:
    print("can not pass")
    
else: 
    print("OK")

print("End Program")
