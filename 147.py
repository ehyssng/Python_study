# 그루핑된 문자열에 이름 붙이기 ?P<name>
import re
p = re.compile(r"(?P<word>\w+)\s+(?P=word)")
print(p.search("Paris in the the Spring").group())