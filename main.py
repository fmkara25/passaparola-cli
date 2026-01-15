def soruyu_sor(harf, soru, dogru_cevap):
    print(f"\n{harf} harfi:")
    print(soru)

    cevap = input("Cevabın (pass yazabilirsin): ").lower()

    if cevap == "pass":
        return "PAS"
    elif cevap == dogru_cevap:
        return "DOGRU"
    else:
        return "YANLIS"


def oyunu_calistir(sorular):
    durumlar = {}

    # 1. TUR
    for harf in sorular:
        durumlar[harf] = soruyu_sor(
            harf,
            sorular[harf]["soru"],
            sorular[harf]["cevap"]
        )

    # PAS KALANLARI TEKRAR SOR
    while "PAS" in durumlar.values():
        for harf in sorular:
            if durumlar[harf] == "PAS":
                durumlar[harf] = soruyu_sor(
                    harf,
                    sorular[harf]["soru"],
                    sorular[harf]["cevap"]
                )

    # SONUÇLARI SAY
    dogru_sayisi = list(durumlar.values()).count("DOGRU")
    yanlis_sayisi = list(durumlar.values()).count("YANLIS")

    print("\nOyun bitti!")
    print("Doğru sayısı:", dogru_sayisi)
    print("Yanlış sayısı:", yanlis_sayisi)


def main():
    sorular = {
        "A": {"soru": "Türkiye'nin başkenti neresidir?", "cevap": "ankara"},
        "B": {"soru": "2015/16 sezonu Turkiye Futbol Ligi sampiyonu takimin kisaltmasi?", "cevap": "bjk"},
        "C": {"soru": "Messi'nin yillarca rekabet ettigi en buyuk rakibinin ilk ismi?", "cevap": "cristiano"},
    }

    oyunu_calistir(sorular)


if __name__ == "__main__":
    main()
