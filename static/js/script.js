document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("diagnosis-form");
    const gejalaList = document.getElementById("gejala-list");
    const hasilDiv = document.getElementById("hasil");
    const loadingDiv = document.getElementById("loading");

    // Ambil gejala dari backend
    fetch("/gejala")
        .then(res => res.json())
        .then(data => {
            data.forEach(gejala => {
                const wrapper = document.createElement("label");
                wrapper.className = "checkbox-label";

                const checkbox = document.createElement("input");
                checkbox.type = "checkbox";
                checkbox.name = "gejala";
                checkbox.value = gejala;

                wrapper.appendChild(checkbox);
                wrapper.appendChild(document.createTextNode(gejala));
                gejalaList.appendChild(wrapper);
            });
        });

    // Saat form disubmit
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const selectedGejala = Array.from(document.querySelectorAll('input[name="gejala"]:checked'))
            .map(cb => cb.value);

        if (selectedGejala.length === 0) {
            alert("❗ Harap pilih minimal satu gejala.");
            return;
        }

        hasilDiv.style.display = "none";
        hasilDiv.innerHTML = "";
        loadingDiv.style.display = "block";

        try {
            const response = await fetch("/prediksi", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ gejala: selectedGejala })
            });

            const result = await response.json();

            hasilDiv.innerHTML = `
                <div class="hasil">
                    <p><strong>🩺 Penyakit:</strong> ${result.penyakit}</p>
                    <p><strong>📖 Deskripsi:</strong> ${result.deskripsi}</p>
                    <p><strong>⚠️ Tingkat Keparahan:</strong> ${result.tingkat_keparahan}</p>
                    <p><strong>💊 Pengobatan Awal:</strong> ${result.pengobatan_awal}</p>
                    <p><strong>🧾 Obat yang Disarankan:</strong> ${result.obat}</p>
                    <p><strong>📝 Gejala yang Dipilih:</strong></p>
                    <ul>${selectedGejala.map(g => `<li>${g}</li>`).join('')}</ul>
                </div>
            `;
        } catch (err) {
            hasilDiv.innerHTML = "<p class='error'>❌ Terjadi kesalahan. Silakan coba lagi.</p>";
        } finally {
            loadingDiv.style.display = "none";
            hasilDiv.style.display = "block";
        }
    });
});
