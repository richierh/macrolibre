BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `personft` (
	`idpersonft`	int,
	`nama`	text,
	`tgl_tes`	date,
	`jenis_kelamin`	text,
	`tgl_lahir`	date,
	`asal_sekolah`	text,
	`jurusan`	text,
	`kota`	text,
	`hobi`	text,
	`prestasi_akademik`	text,
	`prestasi_non`	akademik text,
	`eksul`	text,
	PRIMARY KEY(`idpersonft`)
);
CREATE TABLE IF NOT EXISTS `personfs` (
	`idpersonfs`	int,
	`no_tes`	int,
	`tgl_tes`	date,
	`nama_kandidat`	text,
	`jenis_kelamin`	text,
	`tgl_lahir`	date,
	`pendidikan_terakhir`	text,
	`jurusan`	text,
	`kota`	text,
	`perusahaanorinstansi`	text,
	`posisiorjabatan`	text,
	PRIMARY KEY(`idpersonfs`)
);
CREATE TABLE IF NOT EXISTS `kuncijawaban` (
	`idkuncijawaban`	int,
	`personfsid`	int,
	`personftid`	int,
	FOREIGN KEY(`personftid`) REFERENCES `personft`(`idpersonft`),
	PRIMARY KEY(`idkuncijawaban`),
	FOREIGN KEY(`personfsid`) REFERENCES `personfs`(`idpersonfs`)
);
COMMIT;
