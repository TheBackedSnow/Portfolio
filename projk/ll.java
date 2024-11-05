public class Baza {
    private String[][] daneUzytkownikow = new String[5][2];

    public void dodajUzytkownika(int indeks, String imie, String numerTelefonu) {
        if (indeks >= 0 && indeks < 5) {
            daneUzytkownikow[indeks] = new String[]{imie, numerTelefonu};
        } else {
            System.out.println("Nieprawidłowy indeks użytkownika.");
        }
    }

    public void wyswietlDaneUzytkownikow() {
        System.out.println("Książka telefoniczna:");
        for (String[] dane : daneUzytkownikow) {
            System.out.println(dane[0] + " - " + dane[1]);
        }
    }

    public static void main(String[] args) {
        Baza baza = new Baza();
        baza.dodajUzytkownika(0, "Anna", "123456789");
        baza.dodajUzytkownika(1, "Jan", "987654321");
        baza.dodajUzytkownika(2, "Ewa", "456123789");
        baza.dodajUzytkownika(3, "Piotr", "321654987");
        baza.dodajUzytkownika(4, "Katarzyna", "654987321");
        baza.wyswietlDaneUzytkownikow();
    }
}
