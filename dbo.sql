CREATE TABLE IF NOT EXISTS menu (
    id_dodatku INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa_dodatku TEXT NOT NULL,
    cena_na_mala REAL NOT NULL,
    cena_na_duza REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS zamowienia (
    id_zamowienia INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    telefon_kontaktowy TEXT NOT NULL,
    adres_zamawiajacego TEXT NULL,
    dystans_dostawy REAL DEFAULT 0.0,
    kwota_do_zaplaty REAL NOT NULL,
    data_przyjecia TEXT NOT NULL,
    przewidywana_data_dostawy TEXT NOT NULL,
    status_zamowienia TEXT NOT NULL DEFAULT 'NOWE',
    opis_zamowienia TEXT NOT NULL,
    CONSTRAINT check_status_zamowienia CHECK (status_zamowienia IN ('NOWE', 'W_REALIZACJI', 'ZREALIZOWANE', 'ANULOWANE'))
);

INSERT INTO menu(nazwa_dodatku, cena_na_mala, cena_na_duza)
VALUES
('szynka', 4.00, 7.00),
('salami', 5.00, 8.00),
('kukurydza', 2.00, 5.00),
('cebula', 1.50, 4.50),
('papryka', 2.50, 5.50),
('oliwki', 3.00, 5.00),
('kielbasa', 4.50, 7.50),
('kurczak', 5.00, 8.00);

INSERT INTO zamowienia(imie, nazwisko, telefon_kontaktowy, adres_zamawiajacego, dystans_dostawy, kwota_do_zaplaty, data_przyjecia, przewidywana_data_dostawy, status_zamowienia, opis_zamowienia)
VALUES ('Pawe³', 'Nowak', '123-456-789', 'Narutowicza 55b, Lublin', 3.2, 21.37, '2024-11-27', '2077-11-27', 'NOWE', 'Fast pizza du¿a dla du¿ego cz³owieka bez dodatków ZNI¯KA -10% BO TAK');