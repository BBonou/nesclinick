-- ============================================================
--  Base de données : clinique_vet
--  Moteur          : MySQL 8.x
--  Encodage        : utf8mb4
--  Créé le         : 2026-06-05
-- ============================================================

CREATE DATABASE IF NOT EXISTS `clinique_vet`
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE `clinique_vet`;

SET FOREIGN_KEY_CHECKS = 0;

-- ------------------------------------------------------------
-- Table : proprietaire
-- ------------------------------------------------------------
DROP TABLE IF EXISTS `proprietaire`;
CREATE TABLE `proprietaire` (
  `num_proprietaire` INT          NOT NULL AUTO_INCREMENT,
  `nom`              VARCHAR(30)  NOT NULL,
  `prenom`           VARCHAR(40)  NOT NULL,
  `telephone`        CHAR(15)     NOT NULL,
  `adresse`          VARCHAR(20)  NOT NULL,
  PRIMARY KEY (`num_proprietaire`)
) ENGINE=InnoDB
  AUTO_INCREMENT=13
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `proprietaire` VALUES
  (1,  'Sow',    'Aissatou', '771234567', 'Dakar, Plateau'),
  (2,  'Fall',   'Moussa',   '772345678', 'Dakar, Parcelles'),
  (3,  'Diop',   'Rokhaya',  '773456789', 'Dakar, Medina'),
  (4,  'Ndiaye', 'Cheikh',   '774567890', 'Thiès, Centre'),
  (5,  'Ba',     'Mariama',  '775678901', 'Dakar, Almadies'),
  (6,  'Kane',   'Ousmane',  '776789012', 'Saint-Louis'),
  (7,  'Sarr',   'Ndéye',    '777890123', 'Dakar, Fann'),
  (8,  'Gueye',  'Serigne',  '778901234', 'Dakar, Yoff'),
  (9,  'Thiam',  'Khady',    '779012345', 'Ziguinchor'),
  (10, 'Sy',     'Abdoulaye','770123456', 'Dakar, HLM'),
  (11, 'Camara', 'Awa',      '771122334', 'Kaolack'),
  (12, 'Diouf',  'Pape',     '772233445', 'Dakar, Sicap');

-- ------------------------------------------------------------
-- Table : veterinaire
-- ------------------------------------------------------------
DROP TABLE IF EXISTS `veterinaire`;
CREATE TABLE `veterinaire` (
  `num_vet`    INT          NOT NULL AUTO_INCREMENT,
  `nom_vet`    VARCHAR(30)  NOT NULL,
  `prenom_vet` VARCHAR(50)  NOT NULL,
  `specialite` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`num_vet`)
) ENGINE=InnoDB
  AUTO_INCREMENT=4
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `veterinaire` VALUES
  (1, 'Diallo', 'Mamadou',  'Chirurgie animale'),
  (2, 'Ndiaye', 'Fatou',    'Dermatologie vétérinaire'),
  (3, 'Mbaye',  'Ibrahima', 'Médecine générale');

-- ------------------------------------------------------------
-- Table : animal
-- (dépend de : proprietaire)
-- ------------------------------------------------------------
DROP TABLE IF EXISTS `animal`;
CREATE TABLE `animal` (
  `num_animal`       INT         NOT NULL AUTO_INCREMENT,
  `nom_animal`       VARCHAR(40) NOT NULL,
  `espece`           VARCHAR(50) NOT NULL,
  `race`             VARCHAR(30) DEFAULT NULL,
  `date_naissance`   DATE        DEFAULT NULL,
  `num_proprietaire` INT         NOT NULL
  PRIMARY KEY (`num_animal`),
  KEY `fk_num_proprietaire` (`num_proprietaire`),
  CONSTRAINT `fk_num_proprietaire`
    FOREIGN KEY (`num_proprietaire`)
    REFERENCES `proprietaire` (`num_proprietaire`)
) ENGINE=InnoDB
  AUTO_INCREMENT=21
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `animal` VALUES
  (1,  'Rex',    'Chien',     'Berger Allemand',   '2019-03-15', 1),
  (2,  'Minou',  'Chat',      'Siamois',           '2020-07-22', 1),
  (3,  'Bouba',  'Chien',     'Labrador',          '2018-11-10', 2),
  (4,  'Luna',   'Chat',      'Persan',            '2021-01-05', 3),
  (5,  'Simba',  'Chien',     'Rottweiler',        '2017-06-20', 3),
  (6,  'Lola',   'Lapin',     'Bélier',            '2022-04-12', 4),
  (7,  'Max',    'Chien',     'Caniche',           '2020-09-30', 4),
  (8,  'Nala',   'Chat',      'Maine Coon',        '2019-12-18', 5),
  (9,  'Togo',   'Chien',     'Boxer',             '2018-08-25', 5),
  (10, 'Bijou',  'Chat',      'Européen',          '2021-05-14', 6),
  (11, 'Sultan', 'Chien',     'Doberman',          '2016-02-28', 6),
  (12, 'Misty',  'Lapin',     'Angora',            '2022-07-03', 7),
  (13, 'Rocky',  'Chien',     'Bulldog',           '2019-10-11', 7),
  (14, 'Chérie', 'Chat',      'Ragdoll',           '2020-03-07', 8),
  (15, 'Titan',  'Chien',     'Husky',             '2017-11-19', 8),
  (16, 'Papi',   'Perroquet', 'Gris du Gabon',     '2015-06-01', 9),
  (17, 'Bella',  'Chien',     'Golden Retriever',  '2021-08-23', 9),
  (18, 'Félix',  'Chat',      'British Shorthair', '2020-01-30', 10),
  (19, 'Dino',   'Chien',     'Dalmatien',         '2018-04-16', 11),
  (20, 'Candy',  'Chat',      'Abyssin',           '2022-02-09', 12);

-- ------------------------------------------------------------
-- Table : medicament
-- ------------------------------------------------------------
DROP TABLE IF EXISTS `medicament`;
CREATE TABLE `medicament` (
  `reference`    VARCHAR(20)    NOT NULL,
  `nom`          VARCHAR(30)    NOT NULL,
  `dosage`       VARCHAR(50)    NOT NULL,
  `prix_unitaire` DECIMAL(10,2) NOT NULL,
  `stock`        INT            NOT NULL DEFAULT 0,
  PRIMARY KEY (`reference`),
  CONSTRAINT `medicament_chk_prix`  CHECK (`prix_unitaire` > 0),
  CONSTRAINT `medicament_chk_stock` CHECK (`stock` >= 0)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `medicament` VALUES
  ('MED001', 'Amoxicilline',    '500mg',    2500.00, 47),
  ('MED002', 'Ivermectine',     '1%',        3500.00, 29),
  ('MED003', 'Métronidazole',   '250mg',    1800.00, 44),
  ('MED004', 'Prednisolone',    '5mg',       4200.00, 18),
  ('MED005', 'Furosémide',      '40mg',      2100.00, 34),
  ('MED006', 'Vaccin Rage',     '1 dose',   8500.00,  3),
  ('MED007', 'Antiparasitaire', '10ml',     5000.00, 14),
  ('MED008', 'Vitamine B12',    '1000mcg',  1500.00, 58),
  ('MED009', 'Paracétamol vét.','500mg',    1200.00,  3),
  ('MED010', 'Oméprazole',      '20mg',     3800.00, 25);

-- ------------------------------------------------------------
-- Table : consultation
-- (dépend de : veterinaire, animal)
-- ------------------------------------------------------------
DROP TABLE IF EXISTS `consultation`;
CREATE TABLE `consultation` (
  `num_consultation` INT          NOT NULL AUTO_INCREMENT,
  `date`             DATE         NOT NULL,
  `diagnostic`       TEXT         NOT NULL,
  `montant`          DECIMAL(10,2) NOT NULL,
  `num_vet`          INT          NOT NULL,
  `num_animal`       INT          NOT NULL,
  PRIMARY KEY (`num_consultation`),
  UNIQUE KEY `unicite_consultation_jour` (`num_animal`, `date`),
  KEY `fk_num_vet` (`num_vet`),
  CONSTRAINT `fk_num_vet`
    FOREIGN KEY (`num_vet`)    REFERENCES `veterinaire` (`num_vet`)   ON DELETE CASCADE,
  CONSTRAINT `fk_num_animal`
    FOREIGN KEY (`num_animal`) REFERENCES `animal`      (`num_animal`) ON DELETE CASCADE,
  CONSTRAINT `consultation_chk_montant` CHECK (`montant` >= 0)
) ENGINE=InnoDB
  AUTO_INCREMENT=26
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `consultation` VALUES
  (1,  '2025-01-10', 'Infection bactérienne cutanée',        15000.00, 1, 1),
  (2,  '2025-01-12', 'Contrôle vaccinal annuel',              8000.00, 3, 2),
  (3,  '2025-01-15', 'Parasitose intestinale',               12000.00, 2, 3),
  (4,  '2025-01-18', 'Otite externe',                        10000.00, 3, 4),
  (5,  '2025-01-20', 'Fracture patte avant',                 45000.00, 1, 5),
  (6,  '2025-02-02', 'Bilan de santé général',                8000.00, 3, 6),
  (7,  '2025-02-05', 'Dermatite allergique',                 18000.00, 2, 7),
  (8,  '2025-02-10', 'Conjonctivite',                         9000.00, 3, 8),
  (9,  '2025-02-14', 'Gastro-entérite aiguë',                14000.00, 1, 9),
  (10, '2025-02-18', 'Stérilisation',                        35000.00, 1, 10),
  (11, '2025-02-22', 'Insuffisance cardiaque débutante',     22000.00, 2, 11),
  (12, '2025-03-01', 'Abcès dentaire',                       20000.00, 3, 12),
  (13, '2025-03-05', 'Dysplasie de la hanche',               30000.00, 1, 13),
  (14, '2025-03-10', 'Anémie légère',                        13000.00, 2, 14),
  (15, '2025-03-15', 'Toux chronique',                       11000.00, 3, 15),
  (16, '2025-03-20', 'Psittacose (infection respiratoire)',  16000.00, 2, 16),
  (17, '2025-03-25', 'Contrôle post-opératoire',              6000.00, 1, 17),
  (18, '2025-04-02', 'Hyperthyroïdie',                       19000.00, 2, 18),
  (19, '2025-04-08', 'Leishmaniose suspectée',               25000.00, 1, 19),
  (20, '2025-04-12', 'Gingivite',                            10000.00, 3, 20),
  (21, '2025-04-18', 'Diarrhée chronique',                   13000.00, 3, 1),
  (22, '2025-04-22', 'Rappel vaccinal',                       8000.00, 2, 3),
  (23, '2025-05-03', 'Plaie traumatique',                    17000.00, 1, 5),
  (24, '2025-05-10', 'Surpoids - consultation diététique',   12000.00, 3, 7),
  (25, '2025-05-15', 'Examen ophtalmologique',               14000.00, 2, 9);

-- ------------------------------------------------------------
-- Table : ordonnance
-- (dépend de : consultation, medicament)
-- ------------------------------------------------------------
DROP TABLE IF EXISTS `ordonnance`;
CREATE TABLE `ordonnance` (
  `num_consultation` INT          NOT NULL,
  `reference`        VARCHAR(20)  NOT NULL,
  `posologie`        VARCHAR(100) NOT NULL,
  `duree`            INT          NOT NULL,
  PRIMARY KEY (`num_consultation`, `reference`),
  KEY `fk_ord_medicament` (`reference`),
  CONSTRAINT `fk_ord_consultation`
    FOREIGN KEY (`num_consultation`) REFERENCES `consultation` (`num_consultation`) ON DELETE CASCADE,
  CONSTRAINT `fk_ord_medicament`
    FOREIGN KEY (`reference`)        REFERENCES `medicament`   (`reference`)        ON DELETE CASCADE,
  CONSTRAINT `ordonnance_chk_duree` CHECK (`duree` > 0)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `ordonnance` VALUES
  (1,  'MED001', '1 comprimé matin et soir',       7),
  (1,  'MED008', '1 injection par semaine',         4),
  (3,  'MED002', '1 pipette sur la nuque',         30),
  (3,  'MED003', '1 comprimé 3 fois par jour',      5),
  (5,  'MED004', '1/2 comprimé le matin',          10),
  (7,  'MED001', '1 comprimé 3 fois par jour',      7),
  (7,  'MED004', '1 comprimé matin et soir',       14),
  (9,  'MED003', '1 comprimé matin et soir',        5),
  (10, 'MED001', '1 comprimé post-opératoire',      5),
  (11, 'MED005', '1/2 comprimé par jour',          30),
  (14, 'MED008', '1 injection par semaine',         3),
  (16, 'MED001', '1 comprimé matin et soir',       10),
  (18, 'MED009', '1 comprimé le soir',             30),
  (19, 'MED002', '1 comprimé par mois',            60),
  (22, 'MED007', '1 pipette mensuelle',            30);

-- ------------------------------------------------------------
-- Table : paiement
-- (dépend de : consultation)
-- ------------------------------------------------------------
DROP TABLE IF EXISTS `paiement`;
CREATE TABLE `paiement` (
  `num_pay`          INT          NOT NULL AUTO_INCREMENT,
  `montant`          DECIMAL(10,2) NOT NULL,
  `date_pay`         DATE         NOT NULL,
  `mode_pay`         ENUM('especes','carte','virement','cheque') NOT NULL,
  `num_consultation` INT          NOT NULL,
  PRIMARY KEY (`num_pay`),
  KEY `fk_num_consultation` (`num_consultation`),
  CONSTRAINT `fk_num_consultation`
    FOREIGN KEY (`num_consultation`) REFERENCES `consultation` (`num_consultation`) ON DELETE CASCADE,
  CONSTRAINT `paiement_chk_montant` CHECK (`montant` > 0)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

-- (aucun paiement enregistré pour l'instant)

SET FOREIGN_KEY_CHECKS = 1;

-- ============================================================
--  Fin du script
-- ============================================================