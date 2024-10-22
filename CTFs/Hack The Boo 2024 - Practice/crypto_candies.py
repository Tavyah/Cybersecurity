from Crypto.Util.number import long_to_bytes, bytes_to_long

v1_long = 4196604293528562019178729176959696479940189487937638820300425092623669070870963842968690664766177268414970591786532318240478088400508536
v2_long = 11553755018372917030893247277947844502733193007054515695939193023629350385471097895533448484666684220755712537476486600303519342608532236
v3_long = 14943875659428467087081841480998474044007665197104764079769879270204055794811591927815227928936527971132575961879124968229204795457570030
v4_long = 6336816260107995932250378492551290960420748628

"""FLAG = b'\x41\x41\x41\x42\x42\x42'

step = len(FLAG) // 3
candies = [bytes_to_long(FLAG[i:i+step]) for i in range(0, len(FLAG), step)]

cnd1, cnd2, cnd3 = candies
print(candies)
together = cnd1 + cnd2 + cnd3
print(together)

bytes_flag = long_to_bytes(cnd1)
print(bytes_flag.decode())
"""
"""from sympy import symbols, Eq, solve

# Declare cnd1, cnd2, and cnd3 as symbolic variables
cnd1, cnd2, cnd3 = symbols('cnd1 cnd2 cnd3')

# Define the equations based on v1, v2, and v3
v1 = cnd1**3 + cnd3**2 + cnd2
v2 = cnd2**3 + cnd1**2 + cnd3
v3 = cnd3**3 + cnd2**2 + cnd1

# Assume you have values for v1, v2, and v3
v1_val = v1_long  # replace with actual value
v2_val = v2_long  # replace with actual value
v3_val = v3_long  # replace with actual value

# Set up the equations
eq1 = Eq(v1, v1_val)
eq2 = Eq(v2, v2_val)
eq3 = Eq(v3, v3_val)

# Solve the system of equations
solution = solve([eq1, eq2, eq3], (cnd1, cnd2, cnd3))

print(solution)"""

solution = [(1612993708938936929835517754497931126786454632, 2260690199455691264676123410341531247524997487, 2463132351713367737738737327711828586109296509)]
string = ''
for i in range(3):
    long = solution[0][i]
    bytes = long_to_bytes(long)
    string += bytes.decode()

print(string)