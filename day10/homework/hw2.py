""" აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი."""

#შევქმენით სხვადასხვა ტიპის ცვლადები
name = "nata"
surname = "abuladze"
age = 15

#type ფუნქციით ვიგებ შექმნილი ცვლადების ტიპებს
type_value_1 = type(name)
type_value_2 = type(surname)
type_value_3 = type(age)

#დავპრინტე ტიპების გასაგებად შექმნილი ცვლადები რათა გამეგო პირველად შექმნილი ცვლადების ტიპები
print(type(name))
print(type(age))
print(type(surname))

