BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `DataKandidat` (
	`id_user`	INTEGER,
	`Nama Kandidat`	TEXT,
	`Posisi Pekerjaan`	TEXT
);
INSERT INTO `DataKandidat` VALUES (1,'wd','de3');
CREATE INDEX IF NOT EXISTS `IndexDataKandidat` ON `DataKandidat` (
	`Nama Kandidat`,
	`Posisi Pekerjaan`,
	`id_user`
);
COMMIT;
