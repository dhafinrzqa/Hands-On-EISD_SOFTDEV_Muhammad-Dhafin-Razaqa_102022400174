const kuotaMaksimal = 3;
const pendaftar = ["Andi", "Budi", "Sari", "Rina", "Dodi"];

let pesertaDiterima = [];
let pesertaDitolak = [];


for (let i = 0; i < pendaftar.length; i++) {
    if (pesertaDiterima.length < kuotaMaksimal) {
        pesertaDiterima.push(pendaftar[i]);
    } else {
        pesertaDitolak.push(pendaftar[i]);
        break;
    }
}

console.log("Peserta diterima: ");
pesertaDiterima.forEach(nama => console.log("- " + nama));

console.log("\nPeserta ditolak: ");
pesertaDitolak.forEach(nama => console.log("- " + nama));