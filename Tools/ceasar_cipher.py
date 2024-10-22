def cesars_chipher(string: str, shift: int = 3) -> str:
    abc = 'abcdefghijklmnopqrstuvwxyz'.upper()
    return "".join([abc[(abc.find(c) + shift) % 26] for c in string])

s = 'LTARDBT0ID0WPRZIWTQDD0ILDIWDJHPCSILTCINUDJG!0IWXH0XH0P0EGDDU0DU0RDCRTEI0ID0EGDKT0NDJ0IWPI0IWT0RPTHPG0RXEWTG0XH0XCHTRJGT0CD0BPIITG0WDL0BPCN0IXBTH0NDJ0PEEAN0XI.0IWT0HTRJGXIN0DU0P0IWDJHPCS0SXHIXCRI0HWXUIH0XH0TKTCIJPAAN0IWT0HPBT0PH0IWPI0DU0P0HXCVAT0HWXUI.0TCDJVW0BJBQAXCV,0IPZT0NDJG0UAPV0PCS0TCYDN0IWT0GTHI0DU0IWT0RDCITHI.0BPZT0HJGT0NDJ0LGPE0IWT0UDAADLXCV0ITMI0LXIW0IWT0WIQ0UAPV0UDGBPI0HTRJGXINDUPIWDJHPCSDGHTRJGXINDUPHXCVAT.'

for decrypt_key in range(1,1337):
    decrypted_text = cesars_chipher(s, decrypt_key)
    if 'HTB' in decrypted_text :
        decrypted_text = decrypted_text.replace('K', ' ')
        with open('decrypted_text.txt', 'w') as f:
            f.write(decrypted_text)
            