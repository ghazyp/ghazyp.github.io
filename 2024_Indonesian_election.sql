CREATE DATABASE IF NOT EXISTS indonesian_election_db;
USE indonesian_election_db;

CREATE TABLE ElectionResults (
    Province VARCHAR(50),
    AniesBaswedan INT,
    PrabowoSubianto INT,
    GanjarPranowo INT
);

INSERT INTO ElectionResults (Province, AniesBaswedan, PrabowoSubianto, GanjarPranowo) VALUES
('Aceh', 2369534, 787024, 64677),
('North Sumatra', 2339620, 4660408, 999528),
('West Sumatra', 1744042, 1217314, 124044),
('Riau', 1400093, 1931113, 357298),
('Jambi', 532605, 1438952, 234251),
('South Sumatra', 997299, 3649651, 606681),
('Bengkulu', 229681, 893499, 145570),
('Lampung', 791892, 3554310, 764486),
('Bangka Belitung Islands', 204348, 529883, 151109),
('Riau Islands', 370671, 641388, 140733),
('Banten', 2451383, 4035052, 720275),
('Jakarta', 2653762, 2692011, 1115138),
('West Java', 9099674, 16805854, 2820995),
('Central Java', 2866373, 12096454, 7827335),
('Yogyakarta', 496280, 1269265, 741220),
('East Java', 4492652, 16716603, 4434805),
('West Kalimantan', 718641, 1964183, 534450),
('Central Kalimantan', 256811, 1097070, 158788),
('South Kalimantan', 849948, 1407684, 159950),
('East Kalimantan', 448046, 1542346, 240143),
('North Kalimantan', 72065, 284209, 51451),
('Bali', 99233, 1454640, 1127134),
('West Nusa Tenggara', 850539, 2154843, 241106),
('East Nusa Tenggara', 153446, 1798753, 958505),
('North Sulawesi', 119103, 1229069, 283796),
('Gorontalo', 227354, 504662, 41508),
('Central Sulawesi', 386743, 1251313, 160594),
('Southeast Sulawesi', 361585, 1113344, 90727),
('West Sulawesi', 223153, 533757, 62514),
('South Sulawesi', 2003081, 3010726, 265948),
('Maluku', 228557, 665371, 186395),
('North Maluku', 200459, 454943, 91293),
('Papua', 67592, 378908, 178534),
('West Papua', 37459, 172965, 120565),
('Southwest Papua', 48405, 209403, 99899),
('Central Papua', 128577, 638616, 335089),
('Highland Papua', 284184, 838382, 175956),
('South Papua', 41906, 162852, 110003),
('Overseas', 125110, 427871, 118385);

SELECT
    SUM(AniesBaswedan) AS TotalVotes_AniesBaswedan,
    SUM(PrabowoSubianto) AS TotalVotes_PrabowoSubianto,
    SUM(GanjarPranowo) AS TotalVotes_GanjarPranowo
FROM ElectionResults;

SELECT
    Province,
    AniesBaswedan,
    PrabowoSubianto,
    GanjarPranowo
FROM ElectionResults
WHERE Province = 'Jakarta';
