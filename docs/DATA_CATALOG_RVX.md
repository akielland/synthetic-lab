# RVX Data Catalog

**Generated:** 2026-02-04 11:58:18

Complete inventory and documentation of all datasets in the RVX folders.

## Overview

The RVX folder contains two main data sources:

1. **traveling_survey/** - National travel survey (RVU - Reisevaneundersøkelsen)
2. **zonal_register_data/** - Zonal statistical data (SDAT files) from Statistics Norway

## Folder Structure


### traveling_survey/

**National Travel Survey Data (RVU)**

Contains survey responses about travel behavior of Norwegian households.
- **Format:** SPSS (.sav), ZIP archives, documentation (.docx)
- **Source:** Statistics Norway (SSB)
- **Coverage:** Years 2019-2025

**Statistics:**
- Total files: 8
- Total size: 713.47 MB

**Files:**

| Filename | Size (MB) | Type | Rows | Columns |
|----------|-----------|------|------|---------|
| `Filemail.com - Nasjonal RVU akkumulert data.zip` | 228.44 | .zip | n/a | n/a |
| `Filemail.com - RVU 2025.zip` | 128.01 | .zip | n/a | n/a |
| `Filemail.com - RVU 2025/Nasjonal_RVU_PERSON_Nov26_0901.sav` | 63.65 | .sav | 51330 | 453 |
| `Filemail.com - RVU 2025/Nasjonal_RVU_REISER_Nov26_0901.sav` | 64.36 | .sav | 127115 | 226 |
| `Oppdatert skjema RVU_2025.docx` | 0.37 | .docx | n/a | n/a |
| `Filemail.com - Nasjonal RVU akkumulert data/RVU 2019-2024 Personfil Vektet 251125.sav` | 93.56 | .sav | n/a | n/a |
| `Filemail.com - Nasjonal RVU akkumulert data/RVU 2019_2024 Reisefil 251107.sav` | 134.88 | .sav | 597747 | 103 |
| `Spørreskjema_RVU_2021_2024.docx` | 0.20 | .docx | n/a | n/a |


### zonal_register_data/

**Zonal Statistical Data (SDAT)**

Grid-based statistical data at different geographic resolutions.
- **Format:** DBF (dBase), XLSX
- **Source:** Statistics Norway (TRAMOD/RVX)
- **Coverage:** Multiple grid resolutions (grunnkrets, delomr, etc.)
- **Data years:** 2020-2024

**Statistics:**
- Total files: 28
- Total size: 79.42 MB

**Files:**

| Filename | Size (MB) | Type | Rows | Columns |
|----------|-----------|------|------|---------|
| `sdat1_* (4 files)` | 17.70 | .dbf | 14097–14101 | 41 |
| `sdat3_* (4 files)` | 9.52 | .dbf | 14097–14101 | 18 |
| `sdat4_* (4 files)` | 10.40 | .dbf | 14097–14101 | 24 |
| `sdat5_* (4 files)` | 2.20 | .dbf | 14097–14101 | 5 |
| `sdat7_* (4 files)` | 2.64 | .dbf | 14097–14101 | 6 |
| `sdat71_* (1 files)` | 0.39 | .dbf | 14097 | 4 |
| `sdat8_* (4 files)` | 3.48 | .dbf | 14097–14101 | 8 |
| `sdat_6_* (1 files)` | 3.98 | .dbf | 14097 | 20 |
| `sdat2_data2020_delomr.xlsx` | 3.42 | .xlsx | n/a | n/a |
| `sdat2_data2020_grunnkrets.xlsx` | 25.69 | .xlsx | n/a | n/a |

## Dataset Schemas

### traveling_survey/

#### Nasjonal_RVU_PERSON_Nov26_0901.sav

- **Path:** `Filemail.com - RVU 2025/Nasjonal_RVU_PERSON_Nov26_0901.sav`
- **Type:** SAV (SPSS)
- **Rows:** 51330
- **Columns:** 453

**Column details:**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| altid | object | 2225kj96(0.0%), qya3d2ub(0.0%), qy5vzxaj(0.0%) ... (51330 unique) | — |
| respid | object | 529507ea-efa4-4a0a-b39a-381f6ff2d9ae(0.0%), 7eec8b79-5c4b-4240-ba92-172e0093600c(0.0%), 89adc908-4288-4970-b6ab-0868f832fd6c(0.0%) ... (51330 unique) | — |
| altid_1 | object | 2225kj96(0.0%), qya3d2ub(0.0%), qy5vzxaj(0.0%) ... (51330 unique) | — |
| altidNumeric | float64 | 0.0 – 0.0 (μ=0.0) | — |
| PublishedVersion | float64 | 4.0 – 108.0 (μ=62.26) | — |
| date_time_start_1 | float64 | 20250213.0 – 20251126.0 (μ=20250612.82) | — |
| date_time_start_2 | float64 | 29.0 – 235903.0 (μ=141113.77) | — |
| postnummer | object | 4790(0.6%), 9020(0.6%), 4631(0.5%) ... (2381 unique) | — |
| alder | float64 | 15.0 – 101.0 (μ=44.86) | — |
| Aldersgruppe | float64 | 1.0 – 7.0 (μ=3.99) | — |
| kjonn_kat | float64 | 1.0 – 2.0 (μ=1.49) | 48.6% |
| kjonn | object | 1(31.4%), 2(30.5%), kvinne(19.1%) ... (4 unique) | — |
| kommune | float64 | 301.0 – 5636.0 (μ=3185.08) | — |
| kommunenummer | float64 | 301.0 – 5636.0 (μ=3185.08) | — |
| grunnkrets | float64 | 3010102.0 – 56360108.0 (μ=31850732.17) | — |
| fylkesnummer | float64 | 3.0 – 56.0 (μ=31.77) | — |
| fylke | float64 | 3.0 – 56.0 (μ=31.77) | — |
| fodeland | object | (100.0%) | — |
| utsendelsesdato | object | 20250224 000000(4.2%), 20250313 000000(4.1%), 20250304 000000(4.0%) ... (78 unique) | — |
| segment | object | Oslo/Akershus(27.4%), Trondheim(10.7%), Bergen(10.3%) ... (13 unique) | — |
| utvalgskode | float64 | 1.0 – 13.0 (μ=4.67) | — |
| OS_BROWSER_1 | object | IOS iPhone(51.5%), Android Mobile(27.4%), Windows 10(13.7%) ... (11 unique) | — |
| OS_BROWSER_2 | object | IE(100.0%) | — |
| batch | float64 | 1.0 – 93.0 (μ=32.86) | — |
| Q_trans_1 | float64 | 0.0 – 1.0 (μ=0.81) | — |
| Q_trans_2 | float64 | 0.0 – 1.0 (μ=0.54) | — |
| Q_trans_3 | float64 | 0.0 – 1.0 (μ=0.22) | — |
| Q_trans_4 | float64 | 0.0 – 1.0 (μ=0.07) | — |
| Q_trans_5 | float64 | 0.0 – 1.0 (μ=0.03) | — |
| Q_trans_6 | float64 | 0.0 – 1.0 (μ=0.05) | — |
| Q_trans_7 | float64 | 0.0 – 1.0 (μ=0.05) | — |
| Q_trans_8 | float64 | 0.0 – 1.0 (μ=0.13) | — |
| Q_trans_9 | float64 | 0.0 – 1.0 (μ=0.08) | — |
| Q_trans_annet_1 | float64 | 0.0 – 1.0 (μ=0.01) | 87.0% |
| Q_trans_annet_2 | float64 | 0.0 – 1.0 (μ=0.03) | 87.0% |
| Q_trans_annet_3 | float64 | 0.0 – 1.0 (μ=0.2) | 87.0% |
| Q_trans_annet_4 | float64 | 0.0 – 1.0 (μ=0.81) | 87.0% |
| Q_trans_annet_5 | float64 | 0.0 – 1.0 (μ=0.2) | 87.0% |
| Q_trans_annet_6 | float64 | 0.0 – 1.0 (μ=0.33) | 87.0% |
| Q_trans_annet_98 | float64 | 0.0 – 1.0 (μ=0.08) | 87.0% |
| Q_trans_annet_7_other | object | (99.0%), Båt(0.1%), Rulleskøyter(0.1%) ... (257 unique) | — |
| Q_trans_tjenester_1 | float64 | 0.0 – 1.0 (μ=0.2) | — |
| Q_trans_tjenester_2 | float64 | 0.0 – 1.0 (μ=0.05) | — |
| Q_trans_tjenester_3 | float64 | 0.0 – 1.0 (μ=0.13) | — |
| Q_trans_tjenester_4 | float64 | 0.0 – 1.0 (μ=0.05) | — |
| Q_trans_tjenester_5 | float64 | 0.0 – 1.0 (μ=0.08) | — |
| Q_trans_tjenester_6 | float64 | 0.0 – 1.0 (μ=0.16) | — |
| Q_trans_tjenester_7 | float64 | 0.0 – 1.0 (μ=0.56) | — |
| FORERKORT | float64 | 1.0 – 3.0 (μ=1.12) | 5.9% |
| BOSTEDSJEKK | float64 | 1.0 – 3.0 (μ=1.04) | — |
| BOSTED_FEIL_12 | float64 | 0.0 – 1.0 (μ=0.01) | 98.3% |
| BOSTED_FEIL_13 | float64 | 0.0 – 0.0 (μ=0.0) | 98.3% |
| BOSTED_FEIL_4_other | object | (98.3%), Oslo(0.3%), Østfold(0.2%) ... (24 unique) | — |
| BOSTED_FEIL_5_other | object | (98.3%), Oslo kommune(0.2%), Bergen(0.1%) ... (132 unique) | — |
| BOSTED_FEIL_6_other | object | (100.0%), Sulkava(0.0%), Gmina Zabrodzie(0.0%) ... (5 unique) | — |
| BOSTED_FEIL_7_other | object | (98.3%), 9016(0.0%), 9020(0.0%) ... (619 unique) | — |
| BOSTED_FEIL_8_other | object | (98.3%), NO(1.7%), SE(0.0%) ... (6 unique) | — |
| BOSTED_FEIL_PRESISJON_UTDYP | float64 | 1.0 – 7.0 (μ=1.23) | 98.6% |
| BOSTED_FEIL_PRESISJON | float64 | 1.0 – 3.0 (μ=1.56) | 99.7% |
| BOSTED_ANNET_12 | float64 | 0.0 – 1.0 (μ=0.02) | 99.1% |
| BOSTED_ANNET_13 | float64 | 0.0 – 0.0 (μ=0.0) | 99.1% |
| BOSTED_ANNET_4_other | object | (99.1%), Oslo(0.2%), Trøndelag(0.2%) ... (24 unique) | — |
| BOSTED_ANNET_5_other | object | (99.1%), Trondheim(0.2%), Oslo kommune(0.1%) ... (83 unique) | — |
| BOSTED_ANNET_6_other | object | (100.0%), Wandsworth(0.0%), Kreisfreie Stadt Neumünster(0.0%) ... (5 unique) | — |
| BOSTED_ANNET_7_other | object | (99.1%), 7030(0.0%), 7031(0.0%) ... (313 unique) | — |
| BOSTED_ANNET_8_other | object | (99.1%), NO(0.9%), DE(0.0%) ... (9 unique) | — |
| BOSTED_ANNET_PRESISJON_UTDYP | float64 | 1.0 – 7.0 (μ=1.32) | 99.3% |
| BOSTED_ANNET_PRESISJON | float64 | 1.0 – 3.0 (μ=1.7) | 99.9% |
| BOSTED_FLERE | float64 | 1.0 – 2.0 (μ=1.96) | — |
| BOSTED_FLERE_ADRESSE_12 | float64 | 0.0 – 1.0 (μ=0.03) | 95.5% |
| BOSTED_FLERE_ADRESSE_13 | float64 | 0.0 – 0.0 (μ=0.0) | 95.5% |
| BOSTED_FLERE_ADRESSE_4_other | object | (95.6%), Vestland(0.6%), Oslo(0.5%) ... (70 unique) | — |
| BOSTED_FLERE_ADRESSE_5_other | object | (95.6%), Trondheim(0.4%), Oslo kommune(0.4%) ... (302 unique) | — |
| BOSTED_FLERE_ADRESSE_6_other | object | (99.9%), Kreisfreie Stadt Berlin(0.0%), Kraków(0.0%) ... (40 unique) | — |
| BOSTED_FLERE_ADRESSE_7_other | object | (95.6%), 7050(0.0%), 7030(0.0%) ... (1232 unique) | — |
| BOSTED_FLERE_ADRESSE_8_other | object | (95.6%), NO(4.3%), PL(0.0%) ... (29 unique) | — |
| BOSTED_FLERE_ADRESSE_PRESISJON_UTDYP | float64 | 1.0 – 7.0 (μ=1.37) | 96.2% |
| BOSTED_FLERE_ADRESSE_PRESISJON | float64 | 1.0 – 3.0 (μ=1.8) | 99.3% |
| BOSTED_SKJULT_B_1 | float64 | 0.0 – 1.0 (μ=0.0) | — |
| BOSTED_SKJULT_B_2 | float64 | 0.0 – 1.0 (μ=0.0) | — |
| BOSTED_SKJULT_B_3 | float64 | 0.0 – 1.0 (μ=0.0) | — |
| BOSTEDSLAND | float64 | 1.0 – 2.0 (μ=1.0) | — |
| BOSTED_ANTALL | float64 | 1.0 – 2.0 (μ=1.05) | — |
| Reisedag_3 | float64 | 0.0 – 1.0 (μ=0.77) | — |
| HOVED | float64 | 1.0 – 9.0 (μ=2.14) | — |
| OPPMOTE | float64 | 1.0 – 5.0 (μ=1.29) | 40.3% |
| OPPMOTE_SKOLE | float64 | 1.0 – 4.0 (μ=1.14) | 86.2% |
| OPPMOTE_ADRESSE_12 | float64 | 0.0 – 1.0 (μ=0.0) | 33.0% |
| OPPMOTE_ADRESSE_13 | float64 | 0.0 – 0.0 (μ=0.0) | 33.0% |
| OPPMOTE_ADRESSE_4_other | object | (33.1%), Oslo(15.2%), Trøndelag(7.9%) ... (74 unique) | — |
| OPPMOTE_ADRESSE_5_other | object | (33.1%), Oslo kommune(10.4%), Trondheim(6.3%) ... (384 unique) | — |
| OPPMOTE_ADRESSE_6_other | object | (100.0%), Manchester(0.0%), Warsaw(0.0%) ... (19 unique) | — |
| OPPMOTE_ADRESSE_7_other | object | (33.1%), 9019(1.4%), 7030(0.9%) ... (2117 unique) | — |
| OPPMOTE_ADRESSE_8_other | object | NO(66.9%), (33.0%), SE(0.0%) ... (24 unique) | — |
| OPPMOTE_ADRESSE_PRESISJON_UTDYP | float64 | 1.0 – 7.0 (μ=1.26) | 44.5% |
| OPPMOTE_ADRESSE_PRESISJON | float64 | 1.0 – 3.0 (μ=1.7) | 87.0% |
| ARBEID | float64 | 1.0 – 3.0 (μ=1.81) | 59.9% |
| ARBEID_TIMER | float64 | 1.0 – 7.0 (μ=2.57) | 90.9% |
| YRKESSJAFOR | float64 | 1.0 – 3.0 (μ=1.98) | 41.7% |
| TJENESTEREISE | float64 | 1.0 – 3.0 (μ=1.82) | 43.3% |
| ARBEIDSREISER | float64 | 1.0 – 4.0 (μ=1.31) | 89.5% |
| YRKESSJAFOR_NEW | float64 | 1.0 – 13.0 (μ=4.87) | 88.0% |
| BOSTED_IGAR | float64 | 1.0 – 4.0 (μ=1.3) | — |
| BOSTED_IGAR_Annet_12 | float64 | 0.0 – 1.0 (μ=0.13) | 90.7% |
| BOSTED_IGAR_Annet_13 | float64 | 0.0 – 0.0 (μ=0.0) | 90.7% |
| BOSTED_IGAR_Annet_4_other | object | (90.8%), Vestland(0.9%), Agder(0.9%) ... (204 unique) | — |
| BOSTED_IGAR_Annet_5_other | object | (90.9%), Oslo kommune(0.5%), Bergen(0.3%) ... (650 unique) | — |
| BOSTED_IGAR_Annet_6_other | object | (99.4%), Vega Baja del Segura(0.0%), Gdańsk(0.0%) ... (199 unique) | — |
| BOSTED_IGAR_Annet_7_other | object | (90.9%), 1747(0.1%), 7340(0.1%) ... (2131 unique) | — |
| BOSTED_IGAR_Annet_8_other | object | (90.8%), NO(8.0%), SE(0.3%) ... (56 unique) | — |
| BOSTED_IGAR_PRESISJON_UTDYP | float64 | 1.0 – 7.0 (μ=1.92) | 91.9% |
| BOSTED_IGAR_PRESISJON | float64 | 1.0 – 3.0 (μ=2.27) | 97.7% |
| UTLAND | float64 | 1.0 – 3.0 (μ=1.45) | 98.7% |
| null_reiser | float64 | 1.0 – 2.0 (μ=1.16) | 0.7% |
| null_reiser_kontroll | float64 | 1.0 – 2.0 (μ=1.72) | 83.8% |
| REISER | float64 | 1.0 – 2.0 (μ=1.12) | 0.7% |
| GJOREMAL_START_1 | float64 | 0.0 – 1.0 (μ=0.45) | 13.5% |
| GJOREMAL_START_2 | float64 | 0.0 – 1.0 (μ=0.13) | 13.5% |
| GJOREMAL_START_3 | float64 | 0.0 – 1.0 (μ=0.03) | 13.5% |
| GJOREMAL_START_4 | float64 | 0.0 – 1.0 (μ=0.09) | 13.5% |
| GJOREMAL_START_5 | float64 | 0.0 – 1.0 (μ=0.48) | 13.5% |
| GJOREMAL_START_6 | float64 | 0.0 – 1.0 (μ=0.18) | 13.5% |
| GJOREMAL_START_7 | float64 | 0.0 – 1.0 (μ=0.4) | 13.5% |
| GJOREMAL_START_8 | float64 | 0.0 – 1.0 (μ=0.04) | 13.5% |
| GJOREMAL_START_9 | float64 | 0.0 – 1.0 (μ=0.32) | 13.5% |
| GJOREMAL_START_10 | float64 | 0.0 – 1.0 (μ=0.08) | 13.5% |
| GJOREMAL_START_11 | float64 | 0.0 – 1.0 (μ=0.0) | 13.5% |
| TRANSPORTMIDDEL_2 | float64 | 0.0 – 1.0 (μ=0.52) | 12.2% |
| TRANSPORTMIDDEL_3 | float64 | 0.0 – 1.0 (μ=0.52) | 12.2% |
| TRANSPORTMIDDEL_4 | float64 | 0.0 – 1.0 (μ=0.18) | 12.2% |
| TRANSPORTMIDDEL_5 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_6 | float64 | 0.0 – 1.0 (μ=0.01) | 12.2% |
| TRANSPORTMIDDEL_8 | float64 | 0.0 – 1.0 (μ=0.05) | 12.2% |
| TRANSPORTMIDDEL_9 | float64 | 0.0 – 1.0 (μ=0.04) | 12.2% |
| TRANSPORTMIDDEL_10 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_11 | float64 | 0.0 – 1.0 (μ=0.01) | 12.2% |
| TRANSPORTMIDDEL_12 | float64 | 0.0 – 1.0 (μ=0.02) | 12.2% |
| TRANSPORTMIDDEL_13 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_14 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_15 | float64 | 0.0 – 1.0 (μ=0.01) | 12.2% |
| TRANSPORTMIDDEL_16 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_17 | float64 | 0.0 – 1.0 (μ=0.2) | 12.2% |
| TRANSPORTMIDDEL_18 | float64 | 0.0 – 1.0 (μ=0.03) | 12.2% |
| TRANSPORTMIDDEL_19 | float64 | 0.0 – 1.0 (μ=0.01) | 12.2% |
| TRANSPORTMIDDEL_20 | float64 | 0.0 – 1.0 (μ=0.05) | 12.2% |
| TRANSPORTMIDDEL_21 | float64 | 0.0 – 1.0 (μ=0.06) | 12.2% |
| TRANSPORTMIDDEL_22 | float64 | 0.0 – 1.0 (μ=0.01) | 12.2% |
| TRANSPORTMIDDEL_23 | float64 | 0.0 – 1.0 (μ=0.01) | 12.2% |
| TRANSPORTMIDDEL_24 | float64 | 0.0 – 1.0 (μ=0.01) | 12.2% |
| TRANSPORTMIDDEL_25 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_7 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_26 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_27 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_28 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_29 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_30 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_31 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_32 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_33 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_34 | float64 | 0.0 – 0.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_98 | float64 | 0.0 – 1.0 (μ=0.0) | 12.2% |
| TRANSPORTMIDDEL_97 | float64 | 0.0 – 1.0 (μ=0.0) | 54.6% |
| BIL_SJAFOR_ANTALL | float64 | 1.0 – 6.0 (μ=1.1) | 54.0% |
| BIL_REG_1_1 | object | (54.0%), Toyota(2.6%), Tesla(2.2%) ... (2877 unique) | — |
| BIL_REG_EIERFORM_1 | float64 | 1.0 – 7.0 (μ=1.37) | 54.0% |
| BIL_REG_TYPE_1 | float64 | 1.0 – 8.0 (μ=1.17) | 54.0% |
| BIL_REG_DRIVSTOFF_1 | float64 | 1.0 – 7.0 (μ=2.51) | 54.0% |
| BIL_REG_2_1 | object | (95.5%), Toyota(0.3%), Volkswagen(0.2%) ... (620 unique) | — |
| BIL_REG_EIERFORM_2 | float64 | 1.0 – 7.0 (μ=2.47) | 95.5% |
| BIL_REG_TYPE_2 | float64 | 1.0 – 8.0 (μ=1.52) | 95.5% |
| BIL_REG_DRIVSTOFF_2 | float64 | 1.0 – 7.0 (μ=2.51) | 95.5% |
| BIL_REG_3_1 | object | (99.8%), Mercedes(0.0%), Volkswagen(0.0%) ... (78 unique) | — |
| BIL_REG_EIERFORM_3 | float64 | 1.0 – 7.0 (μ=3.41) | 99.8% |
| BIL_REG_TYPE_3 | float64 | 1.0 – 8.0 (μ=2.02) | 99.8% |
| BIL_REG_DRIVSTOFF_3 | float64 | 1.0 – 7.0 (μ=2.6) | 99.8% |
| BIL_REG_4_1 | object | (100.0%), Ford(0.0%), BMW(0.0%) ... (17 unique) | — |
| BIL_REG_EIERFORM_4 | float64 | 1.0 – 7.0 (μ=4.12) | 100.0% |
| BIL_REG_TYPE_4 | float64 | 1.0 – 8.0 (μ=2.5) | 100.0% |
| BIL_REG_DRIVSTOFF_4 | float64 | 1.0 – 7.0 (μ=2.5) | 100.0% |
| BIL_REG_5_1 | object | (100.0%), VW Golf(0.0%), VW(0.0%) ... (7 unique) | — |
| BIL_REG_EIERFORM_5 | float64 | 1.0 – 7.0 (μ=5.33) | 100.0% |
| BIL_REG_TYPE_5 | float64 | 1.0 – 8.0 (μ=3.17) | 100.0% |
| BIL_REG_DRIVSTOFF_5 | float64 | 1.0 – 7.0 (μ=3.17) | 100.0% |
| tid_til_reiseseksjon_tidsstempel | float64 | 33.0 – 235932.0 (μ=141893.31) | 12.2% |
| sekunder_til_reise | float64 | 18.0 – 86252.0 (μ=641.56) | 12.2% |
| start_reiseseksjon | float64 | 33.0 – 235932.0 (μ=141893.34) | 12.2% |
| tid_reiseseksjon_tidsstempel | float64 | 2.0 – 235933.0 (μ=142937.57) | 12.4% |
| sekunder_reiseseksjon | float64 | 20.0 – 86194.0 (μ=722.01) | 12.4% |
| ALTERNATIV_BIL_1 | float64 | 0.0 – 1.0 (μ=0.23) | 54.0% |
| ALTERNATIV_BIL_2 | float64 | 0.0 – 1.0 (μ=0.17) | 54.0% |
| ALTERNATIV_BIL_3 | float64 | 0.0 – 1.0 (μ=0.12) | 54.0% |
| ALTERNATIV_BIL_4 | float64 | 0.0 – 1.0 (μ=0.05) | 54.0% |
| ALTERNATIV_BIL_5 | float64 | 0.0 – 1.0 (μ=0.36) | 54.0% |
| ALTERNATIV_BIL_6 | float64 | 0.0 – 1.0 (μ=0.07) | 54.0% |
| ALTERNATIV_BIL_7 | float64 | 0.0 – 1.0 (μ=0.01) | 54.0% |
| ALTERNATIV_BIL_8 | float64 | 0.0 – 1.0 (μ=0.03) | 54.0% |
| ALTERNATIV_BIL_9 | float64 | 0.0 – 1.0 (μ=0.05) | 54.0% |
| ALTERNATIV_BIL_10 | float64 | 0.0 – 1.0 (μ=0.38) | 54.0% |
| ALTERNATIV_BIL_11 | float64 | 0.0 – 1.0 (μ=0.02) | 54.0% |
| VANE_1 | float64 | 1.0 – 7.0 (μ=2.3) | 17.1% |
| VANE_2 | float64 | 1.0 – 7.0 (μ=3.7) | 0.7% |
| VANE_3 | float64 | 1.0 – 7.0 (μ=3.57) | 0.7% |
| VANE_4 | float64 | 1.0 – 7.0 (μ=4.74) | 0.7% |
| VANE_5 | float64 | 1.0 – 7.0 (μ=3.29) | 0.7% |
| KOLL_KORT | float64 | 1.0 – 4.0 (μ=2.02) | 13.8% |
| KORT_TYPE | float64 | 1.0 – 10.0 (μ=4.39) | 19.2% |
| BIL_EIE_FLERE_1 | float64 | 1.0 – 2.0 (μ=1.43) | 9.8% |
| BIL_EIE_1_1 | object | (48.5%), Toyota(3.0%), Volvo(2.6%) ... (3156 unique) | — |
| BIL_EIE_EIERFORM_1 | float64 | 1.0 – 7.0 (μ=1.21) | 48.5% |
| BIL_EIE_TYPE_1 | float64 | 1.0 – 8.0 (μ=1.22) | 48.5% |
| BIL_EIE_DRIVSTOFF_1 | float64 | 1.0 – 7.0 (μ=2.45) | 48.5% |
| BIL_EIE_FLERE_2 | float64 | 1.0 – 2.0 (μ=1.72) | 48.5% |
| BIL_EIE_2_1 | object | (85.5%), Toyota(0.8%), Volvo(0.6%) ... (1507 unique) | — |
| BIL_EIE_EIERFORM_2 | float64 | 1.0 – 7.0 (μ=1.36) | 85.5% |
| BIL_EIE_TYPE_2 | float64 | 1.0 – 8.0 (μ=1.6) | 85.5% |
| BIL_EIE_DRIVSTOFF_2 | float64 | 1.0 – 7.0 (μ=2.25) | 85.5% |
| BIL_EIE_FLERE_3 | float64 | 1.0 – 2.0 (μ=1.82) | 85.5% |
| BIL_EIE_3_1 | object | (97.4%), Toyota(0.1%), Mercedes(0.1%) ... (499 unique) | — |
| BIL_EIE_EIERFORM_3 | float64 | 1.0 – 7.0 (μ=1.4) | 97.4% |
| BIL_EIE_TYPE_3 | float64 | 1.0 – 8.0 (μ=2.0) | 97.4% |
| BIL_EIE_DRIVSTOFF_3 | float64 | 1.0 – 7.0 (μ=2.0) | 97.4% |
| BIL_EIE_FLERE_4 | float64 | 1.0 – 2.0 (μ=1.78) | 97.4% |
| BIL_EIE_4_1 | object | (99.4%), Mercedes(0.0%), Toyota(0.0%) ... (157 unique) | — |
| BIL_EIE_EIERFORM_4 | float64 | 1.0 – 7.0 (μ=1.55) | 99.4% |
| BIL_EIE_TYPE_4 | float64 | 1.0 – 8.0 (μ=2.22) | 99.4% |
| BIL_EIE_DRIVSTOFF_4 | float64 | 1.0 – 7.0 (μ=1.76) | 99.4% |
| BIL_EIE_FLERE_5 | float64 | 1.0 – 2.0 (μ=1.7) | 99.4% |
| BIL_EIE_5_1 | object | (99.8%), Ford(0.0%), Toyota(0.0%) ... (70 unique) | — |
| BIL_EIE_EIERFORM_5 | float64 | 1.0 – 5.0 (μ=1.48) | 99.8% |
| BIL_EIE_TYPE_5 | float64 | 1.0 – 7.0 (μ=1.97) | 99.8% |
| BIL_EIE_DRIVSTOFF_5 | float64 | 1.0 – 5.0 (μ=1.65) | 99.8% |
| BIL_REG_TOTAL | float64 | 0.0 – 5.0 (μ=0.51) | 0.7% |
| BIL_EIE_TOTAL | float64 | 0.0 – 5.0 (μ=0.71) | 0.7% |
| BIL_TOTAL | float64 | 0.0 – 8.0 (μ=1.21) | 0.7% |
| BIL_DEKK_1 | float64 | 1.0 – 4.0 (μ=1.82) | 55.3% |
| BIL_DEKK_2 | float64 | 1.0 – 4.0 (μ=1.86) | 96.1% |
| BIL_DEKK_3 | float64 | 1.0 – 4.0 (μ=2.03) | 99.8% |
| BIL_DEKK_4 | float64 | 1.0 – 4.0 (μ=2.3) | 100.0% |
| BIL_DEKK_5 | float64 | 4.0 – 4.0 (μ=4.0) | 100.0% |
| BIL_DEKK_6 | float64 | 1.0 – 4.0 (μ=1.87) | 48.5% |
| BIL_DEKK_7 | float64 | 1.0 – 4.0 (μ=1.93) | 85.5% |
| BIL_DEKK_8 | float64 | 1.0 – 4.0 (μ=2.13) | 97.4% |
| BIL_DEKK_9 | float64 | 1.0 – 4.0 (μ=2.22) | 99.4% |
| BIL_DEKK_10 | float64 | 1.0 – 4.0 (μ=2.24) | 99.8% |
| DRIVSTOFF_TOTAL_1 | float64 | 0.0 – 1.0 (μ=0.94) | 0.8% |
| DRIVSTOFF_TOTAL_2 | float64 | 0.0 – 1.0 (μ=0.65) | 0.8% |
| BIL_LADING | float64 | 1.0 – 6.0 (μ=1.2) | 57.2% |
| JOBB_P1 | float64 | 1.0 – 3.0 (μ=1.3) | 46.1% |
| JOBB_P2 | float64 | 1.0 – 3.0 (μ=1.35) | 60.8% |
| JOBB_P3 | float64 | 1.0 – 3.0 (μ=1.86) | 60.8% |
| JOBB_P6 | float64 | 1.0 – 3.0 (μ=1.56) | 46.1% |
| JOBB_P7 | float64 | 1.0 – 3.0 (μ=1.47) | 69.0% |
| HJEMME_P6 | float64 | 1.0 – 12.0 (μ=3.39) | 6.5% |
| HJEMME_P8 | float64 | 1.0 – 5.0 (μ=2.22) | 0.7% |
| HUSHOLDNING_TYPE | float64 | 1.0 – 6.0 (μ=3.24) | 37.9% |
| HUSHOLDNING_ANTALL_1 | float64 | 1.0 – 11.0 (μ=3.24) | 48.8% |
| HUSHOLDNING_ANTALL_2 | float64 | 1.0 – 11.0 (μ=1.78) | 48.8% |
| ALDER_BARN_1 | float64 | 1.0 – 19.0 (μ=10.95) | 79.8% |
| ALDER_BARN_2 | float64 | 1.0 – 19.0 (μ=11.16) | 88.5% |
| ALDER_BARN_3 | float64 | 1.0 – 19.0 (μ=11.52) | 97.1% |
| ALDER_BARN_4 | float64 | 1.0 – 19.0 (μ=12.18) | 99.5% |
| ALDER_BARN_5 | float64 | 1.0 – 19.0 (μ=11.94) | 99.9% |
| ALDER_BARN_6 | float64 | 1.0 – 19.0 (μ=14.89) | 100.0% |
| ALDER_BARN_7 | float64 | 8.0 – 19.0 (μ=13.2) | 100.0% |
| ALDER_BARN_8 | float64 | 17.0 – 19.0 (μ=17.67) | 100.0% |
| ALDER_BARN_9 | float64 | 16.0 – 19.0 (μ=17.33) | 100.0% |
| TRANSPORT_SKOLE_1 | float64 | 1.0 – 9.0 (μ=3.79) | 95.6% |
| TRANSPORT_SKOLE_2 | float64 | 1.0 – 9.0 (μ=3.59) | 95.8% |
| TRANSPORT_SKOLE_3 | float64 | 1.0 – 9.0 (μ=3.44) | 98.1% |
| TRANSPORT_SKOLE_4 | float64 | 1.0 – 9.0 (μ=3.35) | 99.6% |
| TRANSPORT_SKOLE_5 | float64 | 1.0 – 9.0 (μ=3.53) | 99.9% |
| TRANSPORT_SKOLE_6 | float64 | 2.0 – 5.0 (μ=3.83) | 100.0% |
| TRANSPORT_SKOLE_7 | float64 | — | 100.0% |
| TRANSPORT_SKOLE_8 | float64 | 7.0 – 7.0 (μ=7.0) | 100.0% |
| TRANSPORT_SKOLE_9 | float64 | 3.0 – 3.0 (μ=3.0) | 100.0% |
| FORERKORT_ANT | float64 | 1.0 – 2.0 (μ=1.03) | 54.7% |
| FORERKORT_ANT_1_other | object | (55.8%), 2(30.1%), 3(5.6%) ... (19 unique) | — |
| YRKESAKTIV_ANT | float64 | 1.0 – 2.0 (μ=1.04) | 51.5% |
| YRKESAKTIV_ANT_1_other | object | (53.6%), 2(25.9%), 0(7.4%) ... (19 unique) | — |
| H_INNTEKT | float64 | 1.0 – 12.0 (μ=7.2) | 23.4% |
| P_INNTEKT | float64 | 1.0 – 12.0 (μ=4.7) | 0.7% |
| UTDANNING | float64 | 1.0 – 8.0 (μ=4.41) | 0.7% |
| YRKE | float64 | 1.0 – 5.0 (μ=1.97) | 31.7% |
| LEDER | float64 | 1.0 – 6.0 (μ=2.93) | 31.7% |
| BRANSJE | float64 | 1.0 – 15.0 (μ=8.08) | 31.7% |
| HJEMMEKONTOR | float64 | 1.0 – 8.0 (μ=5.76) | 31.7% |
| ORDNING | float64 | 1.0 – 7.0 (μ=2.5) | 31.7% |
| PROBLEM | float64 | 1.0 – 3.0 (μ=1.92) | 0.7% |
| PROBLEMET_1 | float64 | 0.0 – 1.0 (μ=0.67) | 90.7% |
| PROBLEMET_2 | float64 | 0.0 – 1.0 (μ=0.48) | 90.7% |
| PROBLEMET_3 | float64 | 0.0 – 1.0 (μ=0.13) | 90.7% |
| PROBLEMET_4 | float64 | 0.0 – 1.0 (μ=0.29) | 90.7% |
| PROBLEMET_5 | float64 | 0.0 – 1.0 (μ=0.05) | 90.7% |
| PROBLEMET_6 | float64 | 0.0 – 1.0 (μ=0.17) | 90.7% |
| PROBLEMET_7 | float64 | 0.0 – 1.0 (μ=0.06) | 90.7% |
| PROBLEMET_9 | float64 | 0.0 – 1.0 (μ=0.03) | 90.7% |
| PROBLEMET_8 | float64 | 0.0 – 1.0 (μ=0.06) | 90.7% |
| LANGE_REISER_1 | float64 | 0.0 – 1.0 (μ=0.48) | 89.1% |
| LANGE_REISER_2 | float64 | 0.0 – 1.0 (μ=0.23) | 89.1% |
| LANGE_REISER_3 | float64 | 0.0 – 1.0 (μ=0.19) | 89.1% |
| LANGE_REISER_4 | float64 | 0.0 – 1.0 (μ=0.4) | 89.1% |
| LANGE_REISER_5 | float64 | 0.0 – 1.0 (μ=0.01) | 89.1% |
| kontakt_epost | float64 | 1.0 – 1.0 (μ=1.0) | 46.0% |
| kontakt_sms | float64 | 1.0 – 1.0 (μ=1.0) | 45.9% |
| VervLangeReiser | float64 | 1.0 – 5.0 (μ=1.29) | 95.3% |
| RVU_TILBAKEMELDING | object | (74.1%), Nei(3.3%), Ingen kommentar(0.5%) ... (9740 unique) | — |
| REKONTAKT | float64 | 1.0 – 2.0 (μ=1.45) | 6.6% |
| shortlink | object | (95.5%), rYYNQp2r(0.0%), ZKNLGzkl(0.0%) ... (2312 unique) | — |
| date_time_slutt_1 | float64 | 20250213.0 – 20251126.0 (μ=20250612.53) | 0.7% |
| date_time_slutt_2 | float64 | 44.0 – 235947.0 (μ=143673.42) | 0.7% |
| Tid_total | float64 | 14.0 – 86340.0 (μ=1683.54) | 0.7% |
| BIL_DETALJER | float64 | — | 100.0% |
| HJEMME_P1 | float64 | — | 100.0% |
| HJEMME_P3 | float64 | — | 100.0% |
| PERSONER | float64 | 1.0 – 99.0 (μ=3.33) | 62.9% |
| Alder_PERS_1 | float64 | 0.0 – 100.0 (μ=44.56) | 69.2% |
| Alder_PERS_2 | float64 | 0.0 – 94.0 (μ=24.13) | 83.2% |
| Alder_PERS_3 | float64 | 0.0 – 87.0 (μ=19.13) | 89.2% |
| Alder_PERS_4 | float64 | 0.0 – 91.0 (μ=20.85) | 96.4% |
| Alder_PERS_5 | float64 | 0.0 – 81.0 (μ=24.16) | 99.1% |
| Alder_PERS_6 | float64 | 0.0 – 75.0 (μ=24.29) | 99.7% |
| Alder_PERS_7 | float64 | 0.0 – 85.0 (μ=26.69) | 99.9% |
| Alder_PERS_8 | float64 | 0.0 – 72.0 (μ=27.39) | 99.9% |
| Alder_PERS_9 | float64 | 0.0 – 84.0 (μ=31.04) | 100.0% |
| Alder_PERS_10 | float64 | 0.0 – 36.0 (μ=18.0) | 100.0% |
| Alder_PERS_11 | float64 | 0.0 – 51.0 (μ=25.5) | 100.0% |
| Alder_PERS_12 | float64 | 0.0 – 41.0 (μ=20.5) | 100.0% |
| Alder_PERS_13 | float64 | 0.0 – 2.0 (μ=1.0) | 100.0% |
| Alder_PERS_14 | float64 | 0.0 – 0.0 (μ=0.0) | 100.0% |
| SLEKT_PERS_1 | float64 | 1.0 – 7.0 (μ=1.79) | 69.2% |
| SLEKT_PERS_2 | float64 | 1.0 – 7.0 (μ=2.75) | 83.2% |
| SLEKT_PERS_3 | float64 | 1.0 – 7.0 (μ=2.63) | 89.2% |
| SLEKT_PERS_4 | float64 | 1.0 – 7.0 (μ=2.85) | 96.4% |
| SLEKT_PERS_5 | float64 | 1.0 – 7.0 (μ=3.45) | 99.1% |
| SLEKT_PERS_6 | float64 | 1.0 – 7.0 (μ=3.83) | 99.7% |
| SLEKT_PERS_7 | float64 | 1.0 – 7.0 (μ=4.4) | 99.9% |
| SLEKT_PERS_8 | float64 | 2.0 – 7.0 (μ=5.45) | 99.9% |
| SLEKT_PERS_9 | float64 | 2.0 – 7.0 (μ=5.83) | 100.0% |
| SLEKT_PERS_10 | float64 | 3.0 – 6.0 (μ=4.5) | 100.0% |
| SLEKT_PERS_11 | float64 | 4.0 – 6.0 (μ=5.0) | 100.0% |
| SLEKT_PERS_12 | float64 | 1.0 – 6.0 (μ=3.5) | 100.0% |
| SLEKT_PERS_13 | float64 | 2.0 – 6.0 (μ=4.0) | 100.0% |
| SLEKT_PERS_14 | float64 | 5.0 – 6.0 (μ=5.5) | 100.0% |
| TRANSPORT_SKOLE_10 | float64 | — | 100.0% |
| TRANSPORT_SKOLE_11 | float64 | — | 100.0% |
| TRANSPORT_SKOLE_12 | float64 | — | 100.0% |
| TRANSPORT_SKOLE_13 | float64 | — | 100.0% |
| TRANSPORT_SKOLE_14 | float64 | — | 100.0% |
| FORERKORT_PERS_1 | float64 | 1.0 – 3.0 (μ=1.11) | 72.0% |
| FORERKORT_PERS_2 | float64 | 1.0 – 3.0 (μ=1.19) | 91.4% |
| FORERKORT_PERS_3 | float64 | 1.0 – 3.0 (μ=1.23) | 95.9% |
| FORERKORT_PERS_4 | float64 | 1.0 – 3.0 (μ=1.25) | 98.6% |
| FORERKORT_PERS_5 | float64 | 1.0 – 3.0 (μ=1.38) | 99.6% |
| FORERKORT_PERS_6 | float64 | 1.0 – 3.0 (μ=1.59) | 99.8% |
| FORERKORT_PERS_7 | float64 | 1.0 – 3.0 (μ=1.66) | 99.9% |
| FORERKORT_PERS_8 | float64 | 1.0 – 3.0 (μ=1.92) | 99.9% |
| FORERKORT_PERS_9 | float64 | 1.0 – 3.0 (μ=1.95) | 100.0% |
| FORERKORT_PERS_10 | float64 | 2.0 – 2.0 (μ=2.0) | 100.0% |
| FORERKORT_PERS_11 | float64 | 2.0 – 2.0 (μ=2.0) | 100.0% |
| FORERKORT_PERS_12 | float64 | 3.0 – 3.0 (μ=3.0) | 100.0% |
| FORERKORT_PERS_13 | float64 | — | 100.0% |
| FORERKORT_PERS_14 | float64 | — | 100.0% |
| ARBEID_PERS_OLD | float64 | — | 100.0% |
| ARBEID_PERS_1 | float64 | 1.0 – 3.0 (μ=1.26) | 72.0% |
| ARBEID_PERS_2 | float64 | 1.0 – 3.0 (μ=1.28) | 91.4% |
| ARBEID_PERS_3 | float64 | 1.0 – 3.0 (μ=1.3) | 95.9% |
| ARBEID_PERS_4 | float64 | 1.0 – 3.0 (μ=1.3) | 98.6% |
| ARBEID_PERS_5 | float64 | 1.0 – 3.0 (μ=1.43) | 99.6% |
| ARBEID_PERS_6 | float64 | 1.0 – 3.0 (μ=1.47) | 99.8% |
| ARBEID_PERS_7 | float64 | 1.0 – 3.0 (μ=1.66) | 99.9% |
| ARBEID_PERS_8 | float64 | 1.0 – 3.0 (μ=1.73) | 99.9% |
| ARBEID_PERS_9 | float64 | 1.0 – 3.0 (μ=1.9) | 100.0% |
| ARBEID_PERS_10 | float64 | 3.0 – 3.0 (μ=3.0) | 100.0% |
| ARBEID_PERS_11 | float64 | 2.0 – 2.0 (μ=2.0) | 100.0% |
| ARBEID_PERS_12 | float64 | 2.0 – 2.0 (μ=2.0) | 100.0% |
| ARBEID_PERS_13 | float64 | — | 100.0% |
| ARBEID_PERS_14 | float64 | — | 100.0% |
| valid_cases | float64 | 0.0 – 1.0 (μ=0.98) | — |
| BOSTED_kommune | float64 | 301.0 – 5636.0 (μ=3182.47) | — |
| BOSTED_fylke | float64 | 3.0 – 56.0 (μ=31.74) | — |
| BOSTED_2_kommune | float64 | 301.0 – 5630.0 (μ=3323.69) | 94.9% |
| BOSTED_3_kommune | float64 | 301.0 – 5501.0 (μ=3293.79) | 99.9% |
| Start_reisedag_kommune | float64 | 301.0 – 5636.0 (μ=3194.15) | 1.5% |
| utvalgskode_valid | float64 | 1.0 – 13.0 (μ=4.71) | 1.9% |
| utvalgskode_fakturering | float64 | 1.0 – 13.0 (μ=4.66) | 1.9% |
| kommuner_Osloomradet | float64 | 301.0 – 3242.0 (μ=1745.45) | 73.0% |
| kommuner_Trondheimsregionen | float64 | 5001.0 – 5059.0 (μ=5011.96) | 89.5% |
| kommuner_Bergensregionen | float64 | 4601.0 – 4632.0 (μ=4610.81) | 89.9% |
| kommuner_Region_NordJaeren | float64 | 1103.0 – 1130.0 (μ=1110.86) | 90.9% |
| kommuner_Nedre_Glomma | float64 | 3105.0 – 3107.0 (μ=3106.19) | 93.1% |
| kommuner_Kristiansandsregionen | float64 | 4204.0 – 4223.0 (μ=4207.18) | 90.9% |
| kommuner_Grenland | float64 | 4001.0 – 4012.0 (μ=4003.72) | 96.4% |
| kommuner_Buskerudbyen | float64 | 3301.0 – 3314.0 (μ=3304.33) | 95.4% |
| kommuner_RestOstfold_inkl_Moss_og_Halden | float64 | 3101.0 – 3124.0 (μ=3106.93) | 96.1% |
| utvalg_fra_kommune | float64 | 2.0 – 99.0 (μ=8.29) | — |
| BVA | float64 | 2.0 – 8.0 (μ=4.15) | 24.9% |
| BVA_samlet | float64 | 0.0 – 1.0 (μ=0.75) | — |
| rapportomraade | float64 | 1.0 – 13.0 (μ=4.72) | 5.1% |
| storbykommune_filter | float64 | 0.0 – 1.0 (μ=0.47) | — |
| bykommuner_filter | float64 | 0.0 – 1.0 (μ=0.66) | — |
| bykommune | float64 | 301.0 – 5501.0 (μ=3038.77) | 34.1% |
| omegnskommune_filter | float64 | 0.0 – 1.0 (μ=0.31) | — |
| by_omegn | float64 | 301.0 – 9999.0 (μ=5265.66) | 3.1% |
| kommuner_tilleggsutvalg | float64 | 301.0 – 5501.0 (μ=3191.79) | 9.7% |
| aldersgrupper_2 | float64 | 1.0 – 8.0 (μ=4.93) | — |
| Alderskategorier_RVU_2 | float64 | 1.0 – 7.0 (μ=4.4) | — |
| alder_vekting | float64 | 1.0 – 7.0 (μ=4.4) | — |
| gender | float64 | 1.0 – 2.0 (μ=1.5) | — |
| REK_YRKESSTATUS | float64 | 1.0 – 4.0 (μ=1.76) | — |
| date_datetime | datetime64[ns] | 2025-11-24 18:47:00(0.0%), 2025-03-18 15:16:00(0.0%), 2025-03-17 16:05:00(0.0%) ... (44320 unique) | — |
| date_ukenummer | float64 | 7.0 – 48.0 (μ=24.39) | — |
| Month | float64 | 2.0 – 11.0 (μ=5.98) | — |
| Quarter | float64 | 1.0 – 4.0 (μ=2.27) | — |
| response_date | datetime64[ns] | 2025-11-24 18:47:00(0.0%), 2025-03-18 15:16:00(0.0%), 2025-03-17 16:05:00(0.0%) ... (44320 unique) | — |
| datetime_slutt | datetime64[ns] | 2025-03-19 15:15:00(0.0%), 2025-03-04 16:53:00(0.0%), 2025-03-11 16:24:00(0.0%) ... (44108 unique) | 0.7% |
| reisedag_ukedag | float64 | 1.0 – 7.0 (μ=3.67) | — |
| PublishedVersion_gruppert | float64 | 4.0 – 106.0 (μ=60.85) | — |
| ANTALL_BILER | float64 | 0.0 – 7.0 (μ=1.28) | 49.7% |
| EIER_DISP_BIL | float64 | 0.0 – 1.0 (μ=0.81) | 49.7% |
| EIER_DISP_ELBIL | float64 | 0.0 – 1.0 (μ=0.4) | 49.7% |
| EIER_DISP_HYBRID | float64 | 0.0 – 1.0 (μ=0.09) | 49.7% |
| EIER_DISP_EL_HYBRID | float64 | 0.0 – 1.0 (μ=0.47) | 49.7% |
| EL_BIL | float64 | 1.0 – 3.0 (μ=1.72) | 49.7% |
| antall_reiser | float64 | 0.0 – 15.0 (μ=2.48) | — |
| har_reiser | float64 | 0.0 – 1.0 (μ=0.88) | — |
| GJOREMAL_MULTI_1 | float64 | 0.0 – 1.0 (μ=0.37) | — |
| GJOREMAL_MULTI_2 | float64 | 0.0 – 1.0 (μ=0.09) | — |
| GJOREMAL_MULTI_3 | float64 | 0.0 – 1.0 (μ=0.03) | — |
| GJOREMAL_MULTI_4 | float64 | 0.0 – 1.0 (μ=0.07) | — |
| GJOREMAL_MULTI_5 | float64 | 0.0 – 1.0 (μ=0.34) | — |
| GJOREMAL_MULTI_6 | float64 | 0.0 – 1.0 (μ=0.12) | — |
| GJOREMAL_MULTI_7 | float64 | 0.0 – 1.0 (μ=0.3) | — |
| GJOREMAL_MULTI_8 | float64 | 0.0 – 1.0 (μ=0.01) | — |
| GJOREMAL_MULTI_9 | float64 | 0.0 – 1.0 (μ=0.65) | — |
| GJOREMAL_MULTI_98 | float64 | 0.0 – 1.0 (μ=0.06) | — |
| TRM_BRUK_PERSON_02 | float64 | 0.0 – 1.0 (μ=0.5) | 0.1% |
| TRM_BRUK_PERSON_03 | float64 | 0.0 – 1.0 (μ=0.44) | 0.1% |
| TRM_BRUK_PERSON_04 | float64 | 0.0 – 1.0 (μ=0.14) | 0.1% |
| TRM_BRUK_PERSON_06 | float64 | 0.0 – 1.0 (μ=0.01) | 0.1% |
| TRM_BRUK_PERSON_08 | float64 | 0.0 – 1.0 (μ=0.07) | 0.1% |
| TRM_BRUK_PERSON_11 | float64 | 0.0 – 1.0 (μ=0.02) | 0.1% |
| TRM_BRUK_PERSON_14 | float64 | 0.0 – 1.0 (μ=0.01) | 0.1% |
| TRM_BRUK_PERSON_17 | float64 | 0.0 – 1.0 (μ=0.15) | 0.1% |
| TRM_BRUK_PERSON_18 | float64 | 0.0 – 1.0 (μ=0.03) | 0.1% |
| TRM_BRUK_PERSON_20 | float64 | 0.0 – 1.0 (μ=0.04) | 0.1% |
| TRM_BRUK_PERSON_21 | float64 | 0.0 – 1.0 (μ=0.05) | 0.1% |
| TRM_BRUK_PERSON_22 | float64 | 0.0 – 1.0 (μ=0.01) | 0.1% |
| TRM_BRUK_PERSON_23 | float64 | 0.0 – 1.0 (μ=0.01) | 0.1% |
| TRM_BRUK_PERSON_97 | float64 | 0.0 – 1.0 (μ=0.02) | 0.1% |
| TRM_BRUK_PERSON_70 | float64 | 0.0 – 1.0 (μ=0.2) | 0.1% |
| TRM_BRUK_PERSON_71 | float64 | 0.0 – 1.0 (μ=0.22) | 0.1% |
| utvalgsvekt_kombinert_Q1_Q3 | float64 | 0.2783992611431127 – 4.082536603570237 (μ=1.0) | 18.3% |
| utvalgsvekt_nasjonal_Q1_Q3 | float64 | 0.49432875432777196 – 2.872838775951457 (μ=1.0) | 94.1% |

#### Nasjonal_RVU_REISER_Nov26_0901.sav

- **Path:** `Filemail.com - RVU 2025/Nasjonal_RVU_REISER_Nov26_0901.sav`
- **Type:** SAV (SPSS)
- **Rows:** 127115
- **Columns:** 226

**Column details:**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| trip_id | object | zwv6jb_R1(0.0%), 3845zrm8_R1(0.0%), a8tyk75b_R1(0.0%) ... (127115 unique) | — |
| altid | object | ks4raf(0.0%), uymq68(0.0%), wccsmj(0.0%) ... (45056 unique) | — |
| Reise | object | R1(35.4%), R2(28.7%), R3(16.9%) ... (15 unique) | — |
| Reisenr | float64 | 1.0 – 15.0 (μ=2.38) | — |
| utvalgskode_valid | float64 | 1.0 – 13.0 (μ=4.67) | 1.4% |
| PublishedVersion | float64 | 4.0 – 108.0 (μ=62.9) | — |
| response_date | datetime64[ns] | 2025-03-18 15:16:00(0.0%), 2025-08-14 12:50:00(0.0%), 2025-03-11 15:11:00(0.0%) ... (39489 unique) | — |
| GJOREMAL | float64 | 1.0 – 98.0 (μ=8.62) | — |
| FORMAL_SUB | float64 | 1.0 – 98.0 (μ=22.78) | — |
| BOSTED_IGAR_NEW | float64 | 1.0 – 98.0 (μ=10.63) | 98.6% |
| DESTINASJON | float64 | 1.0 – 99.0 (μ=45.45) | 0.6% |
| DESTINASJON_5_other | object | (100.0%) | — |
| DESTINASJON_KART_12 | float64 | 0.0 – 1.0 (μ=0.01) | 55.5% |
| DESTINASJON_KART_13 | float64 | 0.0 – 0.0 (μ=0.0) | 55.5% |
| DESTINASJON_KART_4_other | object | (55.5%), Oslo(7.3%), Akershus(5.9%) ... (112 unique) | — |
| DESTINASJON_KART_5_other | object | (55.6%), Oslo kommune(4.8%), Trondheim(3.7%) ... (504 unique) | — |
| DESTINASJON_KART_6_other | object | (100.0%), City of Westminster(0.0%), Arrondissement Dendermonde(0.0%) ... (41 unique) | — |
| DESTINASJON_KART_7_other | object | (55.6%), 9008(0.4%), 4636(0.4%) ... (2787 unique) | — |
| DESTINASJON_KART_8_other | object | (55.5%), NO(44.2%), SE(0.2%) ... (26 unique) | — |
| DEST_PRESISJON_UTDYP | float64 | 1.0 – 7.0 (μ=1.47) | 73.9% |
| DEST_PRESISJON | float64 | 1.0 – 3.0 (μ=1.82) | 91.7% |
| STARTTID | object | 99:99(4.7%), 16:00(3.6%), 15:00(3.1%) ... (1194 unique) | — |
| TRANSPORTMIDLER_2 | float64 | 0.0 – 1.0 (μ=0.35) | 1.2% |
| TRANSPORTMIDLER_3 | float64 | 0.0 – 1.0 (μ=0.47) | 1.2% |
| TRANSPORTMIDLER_4 | float64 | 0.0 – 1.0 (μ=0.1) | 1.2% |
| TRANSPORTMIDLER_5 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_6 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_8 | float64 | 0.0 – 1.0 (μ=0.03) | 1.2% |
| TRANSPORTMIDLER_9 | float64 | 0.0 – 1.0 (μ=0.03) | 1.2% |
| TRANSPORTMIDLER_10 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_11 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_12 | float64 | 0.0 – 1.0 (μ=0.01) | 1.2% |
| TRANSPORTMIDLER_13 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_14 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_15 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_16 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_17 | float64 | 0.0 – 1.0 (μ=0.11) | 1.2% |
| TRANSPORTMIDLER_18 | float64 | 0.0 – 1.0 (μ=0.01) | 1.2% |
| TRANSPORTMIDLER_19 | float64 | 0.0 – 1.0 (μ=0.01) | 1.2% |
| TRANSPORTMIDLER_20 | float64 | 0.0 – 1.0 (μ=0.03) | 1.2% |
| TRANSPORTMIDLER_21 | float64 | 0.0 – 1.0 (μ=0.03) | 1.2% |
| TRANSPORTMIDLER_22 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_23 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_24 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_25 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_7 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_26 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_27 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_28 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_29 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_30 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_31 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_32 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_33 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_34 | float64 | 0.0 – 0.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_98 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRANSPORTMIDLER_97 | float64 | 0.0 – 1.0 (μ=0.01) | 48.2% |
| TRANSPORTMIDDEL_D_1 | float64 | 2.0 – 98.0 (μ=4.51) | 1.2% |
| TRANSPORTMIDDEL_FLY_D_1 | float64 | 3.0 – 44.0 (μ=30.27) | 99.9% |
| KOLL_HOLDEPLASS_D_1_1 | object | (96.1%), Oslo S, Oslo(0.1%), Jernbanetorget, Oslo(0.0%) ... (2206 unique) | — |
| KOLL_HOLDEPLASS_D_1_2 | object | (96.5%), NSR:StopPlace:59872(0.1%), NSR:StopPlace:58366(0.0%) ... (1806 unique) | — |
| KOLL_HOLDEPLASS_D_1_3 | object | (96.4%), 1 - Bergen sentrum(0.0%), 1 - Bergen lufthavn(0.0%) ... (1431 unique) | — |
| KOLL_HOLDEPLASS_D_1_4 | object | (97.0%), SKY:Line:1(0.1%), RUT:Line:5(0.1%) ... (515 unique) | — |
| KOLL_HOLDEPLASS_D_1_5 | object | (96.1%), Jernbanetorget(0.1%), Majorstuen(0.1%) ... (2069 unique) | — |
| KOLL_HOLDEPLASS_D_1_6 | object | (96.4%), NSR:StopPlace:337(0.0%), NSR:StopPlace:58404(0.0%) ... (1781 unique) | — |
| BIL_SJOFOR_D_1 | float64 | 1.0 – 5.0 (μ=1.05) | 67.6% |
| BIL_PASSASJER_DRIVSTOFF_D_1 | float64 | 1.0 – 7.0 (μ=2.64) | 94.7% |
| TRANSPORTMIDDEL_RUTE_D_1 | float64 | 1.0 – 2.0 (μ=1.22) | 99.9% |
| TRANSPORTMIDDEL_FORSINKET_D_1 | float64 | 3.0 – 5.0 (μ=4.76) | 100.0% |
| LASTESYKKEL_D_1 | float64 | 1.0 – 5.0 (μ=1.27) | 98.0% |
| TRANSPORTMIDDEL_D_2 | float64 | 2.0 – 99.0 (μ=55.41) | 37.7% |
| TRANSPORTMIDDEL_FLY_D_2 | float64 | 1.0 – 44.0 (μ=29.4) | 99.8% |
| KOLL_HOLDEPLASS_D_2_1 | object | (89.0%), Nationaltheatret, Oslo(0.3%), Oslo S, Oslo(0.3%) ... (3799 unique) | — |
| KOLL_HOLDEPLASS_D_2_2 | object | (89.9%), NSR:StopPlace:58404(0.3%), NSR:StopPlace:59872(0.3%) ... (2954 unique) | — |
| KOLL_HOLDEPLASS_D_2_3 | object | (89.9%), 1 - Bergen lufthavn(0.1%), 1 - Bergen sentrum(0.1%) ... (2288 unique) | — |
| KOLL_HOLDEPLASS_D_2_4 | object | (91.4%), RUT:Line:5(0.3%), RUT:Line:4(0.3%) ... (688 unique) | — |
| KOLL_HOLDEPLASS_D_2_5 | object | (89.1%), Jernbanetorget(0.3%), Oslo S(0.3%) ... (3572 unique) | — |
| KOLL_HOLDEPLASS_D_2_6 | object | (89.7%), NSR:StopPlace:337(0.3%), NSR:StopPlace:3990(0.2%) ... (2898 unique) | — |
| BIL_SJOFOR_D_2 | float64 | 1.0 – 3.0 (μ=1.04) | 90.2% |
| BIL_PASSASJER_DRIVSTOFF_D_2 | float64 | 1.0 – 7.0 (μ=2.66) | 98.8% |
| TRANSPORTMIDDEL_RUTE_D_2 | float64 | 1.0 – 3.0 (μ=1.2) | 99.8% |
| TRANSPORTMIDDEL_FORSINKET_D_2 | float64 | 1.0 – 5.0 (μ=4.5) | 100.0% |
| LASTESYKKEL_D_2 | float64 | 1.0 – 5.0 (μ=1.19) | 99.7% |
| TRANSPORTMIDDEL_D_3 | float64 | 2.0 – 99.0 (μ=46.49) | 69.3% |
| TRANSPORTMIDDEL_FLY_D_3 | float64 | 1.0 – 45.0 (μ=31.29) | 99.9% |
| KOLL_HOLDEPLASS_D_3_1 | object | (96.9%), Nationaltheatret, Oslo(0.2%), Jernbanetorget, Oslo(0.2%) ... (1088 unique) | — |
| KOLL_HOLDEPLASS_D_3_2 | object | (97.2%), NSR:StopPlace:58404(0.2%), NSR:StopPlace:58366(0.2%) ... (778 unique) | — |
| KOLL_HOLDEPLASS_D_3_3 | object | (97.1%), 1 - Bergen lufthavn(0.0%), R12 - Eidsvoll(0.0%) ... (1125 unique) | — |
| KOLL_HOLDEPLASS_D_3_4 | object | (97.7%), RUT:Line:5(0.1%), RUT:Line:4(0.1%) ... (406 unique) | — |
| KOLL_HOLDEPLASS_D_3_5 | object | (96.9%), Oslo S(0.1%), Majorstuen(0.1%) ... (1794 unique) | — |
| KOLL_HOLDEPLASS_D_3_6 | object | (97.1%), NSR:StopPlace:337(0.1%), NSR:StopPlace:59872(0.0%) ... (1596 unique) | — |
| BIL_SJOFOR_D_3 | float64 | 1.0 – 3.0 (μ=1.04) | 95.8% |
| BIL_PASSASJER_DRIVSTOFF_D_3 | float64 | 1.0 – 7.0 (μ=2.69) | 99.5% |
| TRANSPORTMIDDEL_RUTE_D_3 | float64 | 1.0 – 3.0 (μ=1.21) | 99.9% |
| TRANSPORTMIDDEL_FORSINKET_D_3 | float64 | 3.0 – 5.0 (μ=4.74) | 100.0% |
| LASTESYKKEL_D_3 | float64 | 1.0 – 5.0 (μ=1.24) | 99.9% |
| TRANSPORTMIDDEL_D_4 | float64 | 2.0 – 99.0 (μ=52.0) | 82.5% |
| TRANSPORTMIDDEL_FLY_D_4 | float64 | 4.0 – 44.0 (μ=29.41) | 99.9% |
| KOLL_HOLDEPLASS_D_4_1 | object | (98.8%), Nationaltheatret, Oslo(0.1%), Jernbanetorget, Oslo(0.1%) ... (593 unique) | — |
| KOLL_HOLDEPLASS_D_4_2 | object | (99.0%), NSR:StopPlace:58404(0.1%), NSR:StopPlace:58366(0.1%) ... (456 unique) | — |
| KOLL_HOLDEPLASS_D_4_3 | object | (99.0%), 1 - Bergkrystallen(0.0%), 1 - Bergen lufthavn(0.0%) ... (632 unique) | — |
| KOLL_HOLDEPLASS_D_4_4 | object | (99.2%), RUT:Line:4(0.0%), RUT:Line:5(0.0%) ... (265 unique) | — |
| KOLL_HOLDEPLASS_D_4_5 | object | (98.9%), Oslo S(0.0%), Majorstuen(0.0%) ... (938 unique) | — |
| KOLL_HOLDEPLASS_D_4_6 | object | (98.9%), NSR:StopPlace:337(0.0%), NSR:StopPlace:4452(0.0%) ... (854 unique) | — |
| BIL_SJOFOR_D_4 | float64 | 1.0 – 4.0 (μ=1.05) | 97.5% |
| BIL_PASSASJER_DRIVSTOFF_D_4 | float64 | 1.0 – 7.0 (μ=2.73) | 99.7% |
| TRANSPORTMIDDEL_RUTE_D_4 | float64 | 1.0 – 3.0 (μ=1.24) | 99.9% |
| TRANSPORTMIDDEL_FORSINKET_D_4 | float64 | 3.0 – 5.0 (μ=4.55) | 100.0% |
| LASTESYKKEL_D_4 | float64 | 1.0 – 5.0 (μ=1.3) | 99.9% |
| TRANSPORTMIDDEL_D_5 | float64 | 2.0 – 99.0 (μ=46.11) | 91.2% |
| TRANSPORTMIDDEL_FLY_D_5 | float64 | 4.0 – 44.0 (μ=30.09) | 100.0% |
| KOLL_HOLDEPLASS_D_5_1 | object | (99.6%), Jernbanetorget, Oslo(0.0%), Nationaltheatret, Oslo(0.0%) ... (302 unique) | — |
| KOLL_HOLDEPLASS_D_5_2 | object | (99.7%), NSR:StopPlace:58366(0.0%), NSR:StopPlace:58404(0.0%) ... (251 unique) | — |
| KOLL_HOLDEPLASS_D_5_3 | object | (99.7%), 4 - Vestli via Majorstuen(0.0%), 4 - Bergkrystallen(0.0%) ... (309 unique) | — |
| KOLL_HOLDEPLASS_D_5_4 | object | (99.7%), RUT:Line:4(0.0%), RUT:Line:5(0.0%) ... (171 unique) | — |
| KOLL_HOLDEPLASS_D_5_5 | object | (99.6%), Majorstuen(0.0%), Oslo S(0.0%) ... (386 unique) | — |
| KOLL_HOLDEPLASS_D_5_6 | object | (99.7%), NSR:StopPlace:337(0.0%), NSR:StopPlace:4452(0.0%) ... (347 unique) | — |
| BIL_SJOFOR_D_5 | float64 | 1.0 – 4.0 (μ=1.05) | 98.4% |
| BIL_PASSASJER_DRIVSTOFF_D_5 | float64 | 1.0 – 7.0 (μ=2.64) | 99.8% |
| TRANSPORTMIDDEL_RUTE_D_5 | float64 | 1.0 – 2.0 (μ=1.22) | 100.0% |
| TRANSPORTMIDDEL_FORSINKET_D_5 | float64 | 3.0 – 5.0 (μ=3.4) | 100.0% |
| LASTESYKKEL_D_5 | float64 | 1.0 – 5.0 (μ=1.45) | 99.9% |
| TRANSPORTMIDDEL_D_6 | float64 | 2.0 – 99.0 (μ=37.98) | 95.1% |
| TRANSPORTMIDDEL_FLY_D_6 | float64 | 6.0 – 44.0 (μ=27.89) | 100.0% |
| KOLL_HOLDEPLASS_D_6_1 | object | (99.8%), Nationaltheatret, Oslo(0.0%), Jernbanetorget, Oslo(0.0%) ... (190 unique) | — |
| KOLL_HOLDEPLASS_D_6_2 | object | (99.8%), NSR:StopPlace:58366(0.0%), NSR:StopPlace:58404(0.0%) ... (166 unique) | — |
| KOLL_HOLDEPLASS_D_6_3 | object | (99.8%), 100 - Kjeller(0.0%), 34 - Ekeberg hageby(0.0%) ... (192 unique) | — |
| KOLL_HOLDEPLASS_D_6_4 | object | (99.9%), RUT:Line:5(0.0%), RUT:Line:100(0.0%) ... (114 unique) | — |
| KOLL_HOLDEPLASS_D_6_5 | object | (99.8%), Oslo S, Oslo(0.0%), Majorstuen(0.0%) ... (224 unique) | — |
| KOLL_HOLDEPLASS_D_6_6 | object | (99.8%), NSR:StopPlace:59872(0.0%), NSR:StopPlace:4452(0.0%) ... (215 unique) | — |
| BIL_SJOFOR_D_6 | float64 | 1.0 – 4.0 (μ=1.04) | 98.8% |
| BIL_PASSASJER_DRIVSTOFF_D_6 | float64 | 1.0 – 7.0 (μ=2.72) | 99.9% |
| TRANSPORTMIDDEL_RUTE_D_6 | float64 | 1.0 – 2.0 (μ=1.33) | 100.0% |
| TRANSPORTMIDDEL_FORSINKET_D_6 | float64 | 5.0 – 5.0 (μ=5.0) | 100.0% |
| LASTESYKKEL_D_6 | float64 | 1.0 – 5.0 (μ=1.35) | 99.9% |
| TRANSPORTMIDDEL_D_7 | float64 | 2.0 – 99.0 (μ=28.91) | 96.9% |
| TRANSPORTMIDDEL_FLY_D_7 | float64 | 17.0 – 38.0 (μ=26.0) | 100.0% |
| KOLL_HOLDEPLASS_D_7_1 | object | (99.9%), Jernbanetorget, Oslo(0.0%), Ski stasjon, Nordre Follo(0.0%) ... (107 unique) | — |
| KOLL_HOLDEPLASS_D_7_2 | object | (99.9%), NSR:StopPlace:58366(0.0%), NSR:StopPlace:58856(0.0%) ... (94 unique) | — |
| KOLL_HOLDEPLASS_D_7_3 | object | (99.9%), 72 - Tillerterminalen via Sandmoen(0.0%), 5 - Ringen via Tøyen(0.0%) ... (99 unique) | — |
| KOLL_HOLDEPLASS_D_7_4 | object | (99.9%), RUT:Line:5(0.0%), RUT:Line:150(0.0%) ... (73 unique) | — |
| KOLL_HOLDEPLASS_D_7_5 | object | (99.9%), Oslo S(0.0%), Nationaltheatret(0.0%) ... (108 unique) | — |
| KOLL_HOLDEPLASS_D_7_6 | object | (99.9%), NSR:StopPlace:337(0.0%), NSR:StopPlace:32632(0.0%) ... (105 unique) | — |
| BIL_SJOFOR_D_7 | float64 | 1.0 – 3.0 (μ=1.04) | 99.0% |
| BIL_PASSASJER_DRIVSTOFF_D_7 | float64 | 1.0 – 7.0 (μ=2.98) | 99.9% |
| TRANSPORTMIDDEL_RUTE_D_7 | float64 | 1.0 – 2.0 (μ=1.2) | 100.0% |
| TRANSPORTMIDDEL_FORSINKET_D_7 | float64 | 3.0 – 3.0 (μ=3.0) | 100.0% |
| LASTESYKKEL_D_7 | float64 | 1.0 – 4.0 (μ=1.32) | 100.0% |
| TRANSPORTMIDDEL_D_8 | float64 | 2.0 – 99.0 (μ=22.57) | 97.7% |
| TRANSPORTMIDDEL_FLY_D_8 | float64 | 44.0 – 44.0 (μ=44.0) | 100.0% |
| KOLL_HOLDEPLASS_D_8_1 | object | (99.9%), Oslo S, Oslo(0.0%), Tøyen, Oslo(0.0%) ... (81 unique) | — |
| KOLL_HOLDEPLASS_D_8_2 | object | (99.9%), NSR:StopPlace:59872(0.0%), NSR:StopPlace:59604(0.0%) ... (72 unique) | — |
| KOLL_HOLDEPLASS_D_8_3 | object | (99.9%), 2 - Ellingsrudåsen(0.0%), 506(0.0%) ... (75 unique) | — |
| KOLL_HOLDEPLASS_D_8_4 | object | (99.9%), RUT:Line:5(0.0%), RUT:Line:4(0.0%) ... (55 unique) | — |
| KOLL_HOLDEPLASS_D_8_5 | object | (99.9%), Storo, Oslo(0.0%), Foruskanalen, Stavanger(0.0%) ... (86 unique) | — |
| KOLL_HOLDEPLASS_D_8_6 | object | (99.9%), NSR:StopPlace:43068(0.0%), NSR:StopPlace:3986(0.0%) ... (76 unique) | — |
| BIL_SJOFOR_D_8 | float64 | 1.0 – 4.0 (μ=1.04) | 99.1% |
| BIL_PASSASJER_DRIVSTOFF_D_8 | float64 | 1.0 – 7.0 (μ=3.02) | 99.9% |
| TRANSPORTMIDDEL_RUTE_D_8 | float64 | 1.0 – 1.0 (μ=1.0) | 100.0% |
| TRANSPORTMIDDEL_FORSINKET_D_8 | float64 | — | 100.0% |
| LASTESYKKEL_D_8 | float64 | 1.0 – 5.0 (μ=1.59) | 100.0% |
| REISETID | float64 | 1.0 – 11.0 (μ=3.62) | 43.6% |
| FLOKK_REISE | float64 | 1.0 – 3.0 (μ=1.65) | 37.3% |
| FLOKK_ANTALL | float64 | 1.0 – 6.0 (μ=1.51) | 77.8% |
| FLOKK_ANTALL_5_other | object | (99.7%), 5(0.1%), 6(0.1%) ... (45 unique) | — |
| FLOKK_BARN | float64 | 1.0 – 7.0 (μ=1.43) | 77.9% |
| FLOKK_BARN_6_other | object | (100.0%), 5(0.0%), 0(0.0%) ... (21 unique) | — |
| DISTANSE_RUNDTUR | float64 | 1.0 – 11.0 (μ=5.5) | 94.3% |
| FLERE_REISE | float64 | 1.0 – 3.0 (μ=1.99) | 1.4% |
| FLOKK_D_1 | float64 | 1.0 – 5.0 (μ=1.46) | 84.6% |
| FLOKK_D_1_5_other | object | (99.9%), 5(0.1%), 6(0.0%) ... (10 unique) | — |
| TRANSPORTMIDDEL_BARN_D_1 | float64 | 1.0 – 3.0 (μ=1.57) | 94.7% |
| TRANSPORTMIDDEL_BARN_D_1_1_other | object | (97.7%), 1(1.4%), 2(0.5%) ... (8 unique) | — |
| FLOKK_D_2 | float64 | 1.0 – 5.0 (μ=1.46) | 96.0% |
| FLOKK_D_2_5_other | object | (100.0%), 5(0.0%), 1(0.0%) ... (8 unique) | — |
| TRANSPORTMIDDEL_BARN_D_2 | float64 | 1.0 – 3.0 (μ=1.6) | 98.7% |
| TRANSPORTMIDDEL_BARN_D_2_1_other | object | (99.5%), 1(0.3%), 2(0.1%) ... (6 unique) | — |
| FLOKK_D_3 | float64 | 1.0 – 5.0 (μ=1.43) | 97.9% |
| FLOKK_D_3_5_other | object | (100.0%), 5(0.0%), 6(0.0%) ... (7 unique) | — |
| TRANSPORTMIDDEL_BARN_D_3 | float64 | 1.0 – 3.0 (μ=1.6) | 99.3% |
| TRANSPORTMIDDEL_BARN_D_3_1_other | object | (99.7%), 1(0.2%), 2(0.1%) ... (6 unique) | — |
| FLOKK_D_4 | float64 | 1.0 – 5.0 (μ=1.42) | 98.5% |
| FLOKK_D_4_5_other | object | (100.0%), 5(0.0%), 2(0.0%) ... (8 unique) | — |
| TRANSPORTMIDDEL_BARN_D_4 | float64 | 1.0 – 3.0 (μ=1.62) | 99.6% |
| TRANSPORTMIDDEL_BARN_D_4_1_other | object | (99.8%), 1(0.1%), 2(0.0%) ... (5 unique) | — |
| FLOKK_D_5 | float64 | 1.0 – 5.0 (μ=1.42) | 99.0% |
| FLOKK_D_5_5_other | object | (100.0%), 1(0.0%), 5(0.0%) ... (6 unique) | — |
| TRANSPORTMIDDEL_BARN_D_5 | float64 | 1.0 – 3.0 (μ=1.61) | 99.7% |
| TRANSPORTMIDDEL_BARN_D_5_1_other | object | (99.9%), 1(0.1%), 2(0.0%) ... (5 unique) | — |
| FLOKK_D_6 | float64 | 1.0 – 5.0 (μ=1.4) | 99.2% |
| FLOKK_D_6_5_other | object | (100.0%), 5(0.0%), 50(0.0%) ... (5 unique) | — |
| TRANSPORTMIDDEL_BARN_D_6 | float64 | 1.0 – 3.0 (μ=1.63) | 99.8% |
| TRANSPORTMIDDEL_BARN_D_6_1_other | object | (99.9%), 1(0.1%), 2(0.0%) ... (5 unique) | — |
| FLOKK_D_7 | float64 | 1.0 – 5.0 (μ=1.41) | 99.3% |
| FLOKK_D_7_5_other | object | (100.0%), 1(0.0%), 50(0.0%) ... (5 unique) | — |
| TRANSPORTMIDDEL_BARN_D_7 | float64 | 1.0 – 3.0 (μ=1.6) | 99.8% |
| TRANSPORTMIDDEL_BARN_D_7_1_other | object | (99.9%), 1(0.1%), 2(0.0%) ... (5 unique) | — |
| FLOKK_D_8 | float64 | 1.0 – 5.0 (μ=1.42) | 99.4% |
| FLOKK_D_8_5_other | object | (100.0%), 1(0.0%), 5(0.0%) ... (6 unique) | — |
| TRANSPORTMIDDEL_BARN_D_8 | float64 | 1.0 – 3.0 (μ=1.56) | 99.8% |
| TRANSPORTMIDDEL_BARN_D_8_1_other | object | (99.9%), 1(0.0%), 2(0.0%) ... (5 unique) | — |
| SLUTTID | object | (57.7%), 99:99(1.4%), 16:00(0.9%) ... (1231 unique) | — |
| TRM_BRUK_REISE_02 | float64 | 0.0 – 1.0 (μ=0.42) | 1.2% |
| TRM_BRUK_REISE_03 | float64 | 0.0 – 1.0 (μ=0.47) | 1.2% |
| TRM_BRUK_REISE_04 | float64 | 0.0 – 1.0 (μ=0.1) | 1.2% |
| TRM_BRUK_REISE_06 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRM_BRUK_REISE_08 | float64 | 0.0 – 1.0 (μ=0.06) | 1.2% |
| TRM_BRUK_REISE_11 | float64 | 0.0 – 1.0 (μ=0.01) | 1.2% |
| TRM_BRUK_REISE_14 | float64 | 0.0 – 1.0 (μ=0.01) | 1.2% |
| TRM_BRUK_REISE_17 | float64 | 0.0 – 1.0 (μ=0.1) | 1.2% |
| TRM_BRUK_REISE_18 | float64 | 0.0 – 1.0 (μ=0.02) | 1.2% |
| TRM_BRUK_REISE_20 | float64 | 0.0 – 1.0 (μ=0.02) | 1.2% |
| TRM_BRUK_REISE_21 | float64 | 0.0 – 1.0 (μ=0.03) | 1.2% |
| TRM_BRUK_REISE_22 | float64 | 0.0 – 1.0 (μ=0.0) | 1.2% |
| TRM_BRUK_REISE_23 | float64 | 0.0 – 1.0 (μ=0.01) | 1.2% |
| TRM_BRUK_REISE_97 | float64 | 0.0 – 1.0 (μ=0.01) | 1.2% |
| TRM_BRUK_REISE_70 | float64 | 0.0 – 1.0 (μ=0.14) | 1.2% |
| TRM_BRUK_REISE_71 | float64 | 0.0 – 1.0 (μ=0.15) | 1.2% |
| htrm_logical | float64 | 2.0 – 999.0 (μ=32.63) | — |
| htrm_logical_grouped | float64 | 1.0 – 999.0 (μ=36.08) | — |
| htrm_logical_grouped_2 | float64 | 1.0 – 999.0 (μ=35.09) | — |
| REISETID_minutter | float64 | 0.0 – 1439.0 (μ=73.79) | 59.3% |
| REISETID_timer | float64 | 0.0 – 23.0 (μ=0.91) | 59.3% |
| STARTTID_klokketime | float64 | 0.0 – 99.0 (μ=18.38) | — |
| START | float64 | 1.0 – 99.0 (μ=40.33) | — |
| REISEHENSIKT | float64 | 1.0 – 98.0 (μ=9.56) | — |

#### RVU 2019-2024 Personfil Vektet 251125.sav

- **Path:** `Filemail.com - Nasjonal RVU akkumulert data/RVU 2019-2024 Personfil Vektet 251125.sav`
- **Type:** SAV (SPSS)
- **Error:** Unknown error

#### RVU 2019_2024 Reisefil 251107.sav

- **Path:** `Filemail.com - Nasjonal RVU akkumulert data/RVU 2019_2024 Reisefil 251107.sav`
- **Type:** SAV (SPSS)
- **Rows:** 597747
- **Columns:** 103

**Column details:**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| uuid | object | 2019_14891(0.0%), 2019_36320(0.0%), 3577_23071_31(0.0%) ... (195360 unique) | — |
| uuid_trip | object | 2019_00001_1(0.0%), rzpqw0tvz9kht4jy_1(0.0%), rzug3uxkekz76jcz_1(0.0%) ... (597747 unique) | — |
| tripNum | float64 | 1.0 – 15.0 (μ=2.53) | — |
| Year | float64 | 2019.0 – 2024.0 (μ=2021.28) | — |
| HTRM | float64 | 1.0 – 99.0 (μ=5.14) | — |
| HTRM_REK | float64 | 1.0 – 6.0 (μ=2.86) | — |
| HTRM_kollektiv | float64 | 1.0 – 99.0 (μ=3.21) | 90.0% |
| HTRM_gml | float64 | 1.0 – 99.0 (μ=5.14) | 85.3% |
| HTRM_2 | float64 | 1.0 – 99.0 (μ=5.13) | 85.3% |
| HTRM_forenklet | float64 | 1.0 – 6.0 (μ=2.87) | — |
| HOVED_delreise | float64 | 1.0 – 5.0 (μ=1.11) | 85.3% |
| HTRM_detaljert | float64 | 1.0 – 999.0 (μ=22.02) | 85.3% |
| HTRM_ny | float64 | 1.0 – 99.0 (μ=5.07) | 85.3% |
| HTRM_kollektiv_ny | float64 | 1.0 – 99.0 (μ=3.34) | 98.1% |
| test | float64 | 0.0 – 0.0 (μ=0.0) | 20.3% |
| Reiseavstand_KM | float64 | 0.0 – 723100.0 (μ=21.62) | 19.0% |
| Reiseavstand_KM_revidert | float64 | 0.0 – 22230.0 (μ=17.09) | 6.8% |
| Reiseavstand_KM_gruppert | float64 | 1.0 – 6.0 (μ=3.48) | 6.8% |
| Reiseavstand_KM_gruppert_org | float64 | 1.0 – 6.0 (μ=3.53) | 21.5% |
| ReiseavstandKM_Gruppert | float64 | 1.0 – 6.0 (μ=3.53) | 21.5% |
| Reisehastighet_KMH_total_revidert | float64 | 0.05555557613169486 – 793.9285714285714 (μ=26.1) | 86.6% |
| Reisetid_MIN_sum_revidert | float64 | 0.0 – 7220.0 (μ=30.48) | 4.4% |
| Reisetid_MIN_gruppert | float64 | 1.0 – 6.0 (μ=3.4) | 5.0% |
| ReiselengdeMIN | float64 | 0.0 – 91810.0000002 (μ=37.02) | 17.7% |
| ReiselengdeMIN_revidert | float64 | 0.0 – 60060.0 (μ=33.79) | 18.3% |
| ReiselengdeMIN_revidert_NY | float64 | 0.0 – 7220.0 (μ=29.91) | 18.4% |
| Reisetid_MIN_gruppert_NY | float64 | 1.0 – 6.0 (μ=3.36) | 19.0% |
| Reisetid_MIN_summert_revidert | float64 | — | 100.0% |
| Reisetid_MIN_summert_revidert_2023 | float64 | 1.000000000002 – 1530.16666667 (μ=34.57) | 85.9% |
| START_1 | float64 | 0.0 – 98.0 (μ=2.86) | — |
| START_Grunnkrets | object | (25.3%), 9999(1.8%), 54010304(0.2%) ... (15176 unique) | — |
| START_Kommune | float64 | 301.0 – 9999.0 (μ=3334.83) | 85.3% |
| START_PRESISJON | float64 | 1.0 – 6.0 (μ=1.22) | 85.4% |
| ENDE_1 | float64 | 0.0 – 98.0 (μ=3.35) | — |
| ENDE_Grunnkrets | object | (25.3%), 9999(1.3%), 54010304(0.2%) ... (15047 unique) | — |
| ENDE_Kommune | float64 | 301.0 – 9999.0 (μ=3338.97) | 85.3% |
| ENDE_PRESISJON | float64 | 1.0 – 6.0 (μ=1.29) | 85.4% |
| REISEHENSIKT | float64 | 1.0 – 8.0 (μ=4.35) | — |
| FORMAL_SUB_1 | float64 | 1.0 – 46.0 (μ=19.82) | 31.8% |
| STARTTID_TIMESINTERVALL | float64 | 0.0 – 99.0 (μ=17.4) | 23.1% |
| GJOREMALc1 | float64 | 1.0 – 98.0 (μ=24.82) | 14.7% |
| FORMAL_Confirm_1 | float64 | 1.0 – 2.0 (μ=1.02) | 30.3% |
| FORMAL_HOVED_1 | float64 | 1.0 – 98.0 (μ=33.18) | 98.3% |
| FORMAL_HOVED_REKODET | float64 | 0.0 – 98.0 (μ=32.39) | 53.1% |
| Gjoremal | float64 | 1.0 – 98.0 (μ=7.25) | 84.8% |
| ReisehensiktRVU | float64 | 1.0 – 8.0 (μ=4.36) | 14.7% |
| HTRM_komplett | float64 | 1.0 – 99.0 (μ=4.61) | 14.7% |
| HTRM_uten_flydrosje_enkelt | float64 | 1.0 – 6.0 (μ=2.86) | 14.7% |
| START_ADRESSE_1r1_grunnkretsnummer | float64 | 0.0 – 54440505.0 (μ=22082493.33) | 17.2% |
| START_ADRESSE_1r1_grunnkrets | object | 0(23.2%), (17.2%), 9999(1.1%) ... (11410 unique) | — |
| START_kommune_2020 | float64 | 0.0 – 9999.0 (μ=2351.77) | 17.3% |
| START_ADRESSE_START_PRES_1 | float64 | 0.0 – 6.0 (μ=0.34) | 71.9% |
| START_UTLANDET_1 | float64 | 0.0 – 8.0 (μ=0.0) | 76.7% |
| ENDE_ADRESSE_1r1_grunnkretsnummer | float64 | 0.0 – 54440505.0 (μ=22218904.64) | 17.3% |
| ENDE_ADRESSE_1r1_grunnkrets | object | 0(23.2%), (17.3%), 9999(0.7%) ... (11279 unique) | — |
| ENDE_kommune_2020 | float64 | 0.0 – 9999.0 (μ=2315.04) | 17.4% |
| ENDE_ADRESSE_START_PRES_1 | float64 | 0.0 – 6.0 (μ=0.83) | 57.1% |
| ENDE_UTLANDET_1 | float64 | 0.0 – 6.0 (μ=0.01) | 76.7% |
| Reisetid_MIN_gruppert_2023 | float64 | 1.0 – 6.0 (μ=3.54) | 85.9% |
| Reiseavstand_KM_gruppert_2023 | float64 | 1.0 – 6.0 (μ=3.61) | 86.4% |
| Total_reiser | float64 | 1.0 – 1.0 (μ=1.0) | — |
| PrimaryLast1 | float64 | 1.0 – 1.0 (μ=1.0) | 14.7% |
| Reisetid_MIN_gruppert_org | float64 | 1.0 – 6.0 (μ=3.36) | 18.7% |
| komplette_utvalg | float64 | 1.0 – 1.0 (μ=1.0) | — |
| TRANSPORTMIDDEL_ANTALL_1#1 | float64 | 0.0 – 1.0 (μ=0.21) | — |
| TRANSPORTMIDDEL_ANTALL_1#2 | float64 | 0.0 – 1.0 (μ=0.09) | — |
| TRANSPORTMIDDEL_ANTALL_1#3 | float64 | 0.0 – 1.0 (μ=0.05) | — |
| TRANSPORTMIDDEL_ANTALL_1#4 | float64 | 0.0 – 1.0 (μ=0.01) | 92.8% |
| TRANSPORTMIDDEL_ANTALL_1#5 | float64 | 0.0 – 1.0 (μ=0.0) | — |
| TRANSPORTMIDDEL_ANTALL_1#6 | float64 | 0.0 – 1.0 (μ=0.0) | — |
| TRANSPORTMIDDEL_ANTALL_1#7 | float64 | 0.0 – 1.0 (μ=0.52) | — |
| TRANSPORTMIDDEL_ANTALL_1#8 | float64 | 0.0 – 1.0 (μ=0.1) | — |
| TRANSPORTMIDDEL_ANTALL_1#9 | float64 | 0.0 – 1.0 (μ=0.11) | — |
| TRANSPORTMIDDEL_ANTALL_1#10 | float64 | 0.0 – 1.0 (μ=0.01) | — |
| TRANSPORTMIDDEL_ANTALL_1#11 | float64 | 0.0 – 1.0 (μ=0.0) | — |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_1 | float64 | 1.0 – 99.0 (μ=4.92) | 15.6% |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_2 | float64 | 1.0 – 99.0 (μ=9.61) | 90.5% |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_3 | float64 | 1.0 – 99.0 (μ=8.66) | 95.9% |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_4 | float64 | 1.0 – 99.0 (μ=10.13) | 98.6% |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_5 | float64 | 1.0 – 99.0 (μ=10.97) | 99.4% |
| SYKKEL_1_vehicle_1 | float64 | 1.0 – 99.0 (μ=1.44) | 96.0% |
| SYKKEL_1_vehicle_2 | float64 | 1.0 – 99.0 (μ=1.81) | 99.8% |
| SYKKEL_1_vehicle_3 | float64 | 1.0 – 99.0 (μ=1.91) | 99.9% |
| SYKKEL_1_vehicle_4 | float64 | 1.0 – 4.0 (μ=1.54) | 100.0% |
| SYKKEL_1_vehicle_5 | float64 | 1.0 – 99.0 (μ=3.31) | 100.0% |
| KOLLEKTIV_1_vehicle_1 | float64 | 1.0 – 99.0 (μ=2.62) | 95.4% |
| KOLLEKTIV_1_vehicle_2 | float64 | 1.0 – 99.0 (μ=3.31) | 94.8% |
| KOLLEKTIV_1_vehicle_3 | float64 | 1.0 – 99.0 (μ=4.31) | 98.8% |
| KOLLEKTIV_1_vehicle_4 | float64 | 1.0 – 99.0 (μ=5.59) | 99.6% |
| KOLLEKTIV_1_vehicle_5 | float64 | 1.0 – 99.0 (μ=6.2) | 99.9% |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_6 | float64 | 1.0 – 99.0 (μ=8.5) | 100.0% |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_7 | float64 | 1.0 – 99.0 (μ=10.72) | 100.0% |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_8 | float64 | 1.0 – 99.0 (μ=12.0) | 100.0% |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_9 | float64 | 1.0 – 99.0 (μ=11.28) | 100.0% |
| SYKKEL_1_vehicle_6 | float64 | 1.0 – 2.0 (μ=1.5) | 100.0% |
| SYKKEL_1_vehicle_7 | float64 | 1.0 – 2.0 (μ=1.5) | 100.0% |
| SYKKEL_1_vehicle_8 | float64 | 1.0 – 2.0 (μ=1.33) | 100.0% |
| SYKKEL_1_vehicle_9 | float64 | 2.0 – 2.0 (μ=2.0) | 100.0% |
| KOLLEKTIV_1_vehicle_6 | float64 | 1.0 – 11.0 (μ=4.11) | 100.0% |
| KOLLEKTIV_1_vehicle_7 | float64 | 1.0 – 11.0 (μ=3.55) | 100.0% |
| KOLLEKTIV_1_vehicle_8 | float64 | 1.0 – 11.0 (μ=4.22) | 100.0% |
| KOLLEKTIV_1_vehicle_9 | float64 | 1.0 – 11.0 (μ=3.5) | 100.0% |
| antall_trm | float64 | 1.0 – 9.0 (μ=1.1) | — |

### zonal_register_data/

#### sdat1_* (4 files)

- **Files:** sdat1_d2024_g2020.dbf, sdat1_d2024_g2021.dbf, sdat1_d2024_g2023.dbf, sdat1_d2024_g2024.dbf
- **Type:** DBF
- **Rows:** 14097–14101
- **Columns:** 41

**Column details (shared across group):**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| GRUNNKRETS | N | 3010101.0 – 54440505.0 (μ=33575886.17) | — |
| M_0_4 | N | 0.0 – 256.0 (μ=10.04) | — |
| M_5_9 | N | 0.0 – 243.0 (μ=11.12) | — |
| M_10_14 | N | 0.0 – 278.0 (μ=12.03) | — |
| M_15_19 | N | 0.0 – 270.0 (μ=12.18) | — |
| M_20_24 | N | 0.0 – 283.0 (μ=12.2) | — |
| M_25_29 | N | 0.0 – 341.0 (μ=13.4) | — |
| M_30_34 | N | 0.0 – 384.0 (μ=14.36) | — |
| M_35_39 | N | 0.0 – 300.0 (μ=13.79) | — |
| M_40_44 | N | 0.0 – 266.0 (μ=13.15) | — |
| M_45_49 | N | 0.0 – 257.0 (μ=12.87) | — |
| M_50_54 | N | 0.0 – 239.0 (μ=13.74) | — |
| M_55_59 | N | 0.0 – 203.0 (μ=13.15) | — |
| M_60_64 | N | 0.0 – 163.0 (μ=11.52) | — |
| M_65_69 | N | 0.0 – 135.0 (μ=10.32) | — |
| M_70_74 | N | 0.0 – 118.0 (μ=8.95) | — |
| M_75_79 | N | 0.0 – 111.0 (μ=7.82) | — |
| M_80_84 | N | 0.0 – 83.0 (μ=4.34) | — |
| M_85_89 | N | 0.0 – 47.0 (μ=2.15) | — |
| M_90_94 | N | 0.0 – 22.0 (μ=0.8) | — |
| M_95_UP | N | 0.0 – 9.0 (μ=0.15) | — |
| K_0_4 | N | 0.0 – 190.0 (μ=9.54) | — |
| K_5_9 | N | 0.0 – 262.0 (μ=10.45) | — |
| K_10_14 | N | 0.0 – 284.0 (μ=11.41) | — |
| K_15_19 | N | 0.0 – 226.0 (μ=11.46) | — |
| K_20_24 | N | 0.0 – 434.0 (μ=11.55) | — |
| K_25_29 | N | 0.0 – 399.0 (μ=12.77) | — |
| K_30_34 | N | 0.0 – 366.0 (μ=13.8) | — |
| K_35_39 | N | 0.0 – 282.0 (μ=13.29) | — |
| K_40_44 | N | 0.0 – 254.0 (μ=12.58) | — |
| K_45_49 | N | 0.0 – 260.0 (μ=12.43) | — |
| K_50_54 | N | 0.0 – 229.0 (μ=13.25) | — |
| K_55_59 | N | 0.0 – 197.0 (μ=12.66) | — |
| K_60_64 | N | 0.0 – 154.0 (μ=11.26) | — |
| K_65_69 | N | 0.0 – 165.0 (μ=10.48) | — |
| K_70_74 | N | 0.0 – 141.0 (μ=9.29) | — |
| K_75_79 | N | 0.0 – 147.0 (μ=8.49) | — |
| K_80_84 | N | 0.0 – 124.0 (μ=5.27) | — |
| K_85_89 | N | 0.0 – 87.0 (μ=3.18) | — |
| K_90_94 | N | 0.0 – 46.0 (μ=1.6) | — |
| K_95_UP | N | 0.0 – 18.0 (μ=0.47) | — |

#### sdat3_* (4 files)

- **Files:** sdat3_d2023x_g2020.dbf, sdat3_d2023x_g2021.dbf, sdat3_d2023x_g2023.dbf, sdat3_d2023x_g2024.dbf
- **Type:** DBF
- **Rows:** 14097–14101
- **Columns:** 18

**Column details (shared across group):**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| GRUNNKRETS | N | 3010101.0 – 54440505.0 (μ=33575886.17) | — |
| SYBLU | N | 0.0 – 0.908 (μ=0.64) | — |
| SYBMU | N | 0.0 – 0.496 (μ=0.26) | — |
| SYBHU | N | 0.0 – 0.57 (μ=0.1) | — |
| SYB | N | 0.0 – 0.0 (μ=0.0) | — |
| SYALU | N | 0.0 – 0.977 (μ=0.66) | — |
| SYAMU | N | 0.0 – 0.863 (μ=0.26) | — |
| SYAHU | N | 0.0 – 0.616 (μ=0.08) | — |
| SYA1524 | N | 0.0 – 0.598 (μ=0.13) | — |
| SYA2534 | N | 0.0 – 0.468 (μ=0.2) | — |
| SYA3554 | N | 0.0 – 0.747 (μ=0.42) | — |
| SYA5566 | N | 0.0 – 0.447 (μ=0.21) | — |
| SYA67UP | N | 0.0 – 0.197 (μ=0.04) | — |
| SYAM | N | 0.0 – 0.978 (μ=0.52) | — |
| SYAK | N | 0.0 – 0.945 (μ=0.48) | — |
| SYA | N | 0.0 – 0.0 (μ=0.0) | — |
| INNT_IDX | N | 0.0 – 1.5 (μ=0.97) | — |
| BRINNT17UP | N | 0.0 – 0.0 (μ=0.0) | — |

#### sdat4_* (4 files)

- **Files:** sdat4_d2024_g2020.dbf, sdat4_d2024_g2021.dbf, sdat4_d2024_g2023.dbf, sdat4_d2024_g2024.dbf
- **Type:** DBF
- **Rows:** 14097–14101
- **Columns:** 24

**Column details (shared across group):**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| GRUNNKRETS | N | 3010101.0 – 54440505.0 (μ=33575886.17) | — |
| A10PRI | N | 0.0 – 697.0 (μ=2.8) | — |
| A20SEK | N | 0.0 – 5708.0 (μ=47.5) | — |
| A21SEK | N | 0.0 – 341.0 (μ=0.28) | — |
| A30VH | N | 0.0 – 1845.0 (μ=11.09) | — |
| A31VH | N | 0.0 – 606.0 (μ=6.09) | — |
| A32VH | N | 0.0 – 1655.0 (μ=10.38) | — |
| A33VH | N | 0.0 – 1918.0 (μ=8.09) | — |
| A34VH | N | 0.0 – 116.0 (μ=0.11) | — |
| A40TJE | N | 0.0 – 9657.0 (μ=39.04) | — |
| A41TJE | N | 0.0 – 1123.0 (μ=3.37) | — |
| A42TJE | N | 0.0 – 700.0 (μ=1.32) | — |
| A43TJE | N | 0.0 – 4765.0 (μ=3.02) | — |
| A50OFF | N | 0.0 – 3789.0 (μ=11.67) | — |
| A60UND | N | 0.0 – 575.0 (μ=2.02) | — |
| A61UND | N | 0.0 – 367.0 (μ=8.69) | — |
| A62UND | N | 0.0 – 434.0 (μ=3.16) | — |
| A63UND | N | 0.0 – 7226.0 (μ=4.34) | — |
| A70HSOS | N | 0.0 – 5164.0 (μ=22.0) | — |
| A71HSOS | N | 0.0 – 8517.0 (μ=9.89) | — |
| A72HSOS | N | 0.0 – 210.0 (μ=8.64) | — |
| A73HSOS | N | 0.0 – 664.0 (μ=7.78) | — |
| MALINT | N | 0.0 – 6247.0 (μ=53.14) | — |
| FEMINT | N | 0.0 – 9644.0 (μ=56.17) | — |

#### sdat5_* (4 files)

- **Files:** sdat5_d2023_g2020.dbf, sdat5_d2023_g2021.dbf, sdat5_d2023_g2023.dbf, sdat5_d2023_g2024.dbf
- **Type:** DBF
- **Rows:** 14097–14101
- **Columns:** 5

**Column details (shared across group):**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| GRUNNKRETS | N | 3010101.0 – 54440505.0 (μ=33575886.17) | — |
| SBARNESK | N | 0.0 – 878.0 (μ=30.68) | — |
| SUNGDSK | N | 0.0 – 832.0 (μ=14.31) | — |
| SVGSKOLE | N | 0.0 – 2236.0 (μ=14.09) | — |
| SHOGUNI | N | 0.0 – 39418.0 (μ=20.09) | — |

#### sdat7_* (4 files)

- **Files:** sdat7_d20xx_g2020_ikke_pkost.dbf, sdat7_d20xx_g2021_ikke_pkost.dbf, sdat7_d20xx_g2023_ikke_pkost.dbf, sdat7_d20xx_g2024_ikke_pkost.dbf
- **Type:** DBF
- **Rows:** 14097–14101
- **Columns:** 6

**Column details (shared across group):**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| GRUNNKRETS | N | 3010101.0 – 54440505.0 (μ=33575886.17) | — |
| KPARK | N | 0.0 – 0.0 (μ=0.0) | — |
| LPARK | N | 0.0 – 0.0 (μ=0.0) | — |
| PKORT_ARB | N | 0.0 – 0.7 (μ=0.12) | — |
| IKKEPBOLIG | N | 0.0 – 0.79 (μ=0.03) | — |
| ANDEL_EL | N | 0.0 – 1.0 (μ=1.0) | — |

#### sdat71_* (1 files)

- **Files:** sdat71_NB2023_grk2020_2020.dbf
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 4

**Column details (shared across group):**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| GRUNNKRETS | N | 3010101.0 – 54440505.0 (μ=33575886.17) | — |
| ELBIL | N | 0.0 – 0.3269 (μ=0.11) | — |
| HYBRID | N | 0.0098 – 0.2741 (μ=0.06) | — |
| FOSSIL | N | 0.5666 – 0.9805 (μ=0.84) | — |

#### sdat8_* (4 files)

- **Files:** sdat8_d2024_g2020.dbf, sdat8_d2024_g2021.dbf, sdat8_d2024_g2023.dbf, sdat8_d2024_g2024.dbf
- **Type:** DBF
- **Rows:** 14097–14101
- **Columns:** 8

**Column details (shared across group):**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| GRUNNKRETS | N | 3010101.0 – 54440505.0 (μ=33575886.17) | — |
| AGGREGAT | N | 0.0 – 0.0 (μ=0.0) | — |
| TILFSTUD1 | N | 0.0 – 2641.0 (μ=2.5) | — |
| TILFSTUD2 | N | 0.0 – 354.0 (μ=2.32) | — |
| HOTELLER | N | 0.0 – 14.0 (μ=0.1) | — |
| HYTTER | N | 0.0 – 3563.0 (μ=34.52) | — |
| BOSTUD | N | 0.0 – 0.0 (μ=0.0) | — |
| BOINST | N | 0.0 – 0.0 (μ=0.0) | — |

#### sdat_6_* (1 files)

- **Files:** sdat_6_areal_g2020.dbf
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 20

**Column details (shared across group):**

| Column | Type | Range/Values | Nulls |
|--------|------|--------------|-------|
| Grunnkrets | N | 3010101.0 – 54440505.0 (μ=33575886.17) | — |
| Areal_1 | N | 0.0 – 212861.0 (μ=1568.3) | — |
| Areal_2 | N | 0.0 – 1353191.0 (μ=78255.97) | — |
| Areal_3 | N | 0.0 – 1335905640.0 (μ=10291650.19) | — |
| Areal_4 | N | 0.0 – 401843.0 (μ=2586.93) | — |
| Areal_5 | N | 0.0 – 5853678.0 (μ=18257.18) | — |
| Areal_6 | N | 0.0 – 7963017.0 (μ=5113.94) | — |
| Areal_7 | N | 0.0 – 2314263419.0 (μ=11737582.12) | — |
| Areal_8 | N | 0.0 – 1096178350.0 (μ=11206538.17) | — |
| Areal_9 | N | 0.0 – 275540.0 (μ=77.81) | — |
| Areal_B1 | N | 0.0 – 0.0 (μ=0.0) | — |
| Areal_B2 | N | 0.0 – 0.0 (μ=0.0) | — |
| Areal_B3 | N | 0.0 – 237914.0 (μ=3674.69) | — |
| Areal_B4 | N | 0.0 – 3597.0 (μ=2.85) | — |
| Areal_B5 | N | 0.0 – 341476.0 (μ=1946.72) | — |
| Areal_B6 | N | 0.0 – 334469.0 (μ=78.78) | — |
| Areal_B7 | N | 0.0 – 710.0 (μ=0.1) | — |
| Areal_B8 | N | 0.0 – 103137.0 (μ=607.06) | — |
| Areal_B9 | N | 0.0 – 7950.0 (μ=2.09) | — |
| Areal_Tot | N | 6167.0 – 2333835928.0 (μ=33347942.91) | — |

#### sdat2_data2020_* (2 files)

- **Files:** sdat2_data2020_delomr.xlsx, sdat2_data2020_grunnkrets.xlsx
- **Type:** XLSX
- **Sheets per file:** 1
- **Shared columns:** 361
- **Schema:** Geographic-level variations


**Column Structure & Demographics:**

The 360+ columns in each geographic area are structured as:
**24 demographic cells** (age × gender) × **15 household categories** = **360 variables**

**Age & Gender (24 cells):**
- 12 age groups × 2 genders = 24 combinations

**Household Categories (15 categories):**
- Number of adults: 1 adult / 2 adults / 3+ adults
- Household type:
  - Enslig uten barn (Single without children)
  - Enslig med barn (Single with children)
  - Par uten barn (Couple without children)
  - Par med barn (Couple with children)
  - Flere voksne (Multiple adults)

**Calculation:** 3 adult categories × 5 household types = 15 categories per age/gender group


**Common columns (subset - first 10):**

| Column | Description |
|--------|-------------|
| Delområde | Demographic × Household |
| Mann_AG13_15_1voksen_EnsligUtenBarn | Demographic × Household |
| Mann_AG13_15_1voksen_EnsligMedBarn | Demographic × Household |
| Mann_AG13_15_1voksen_ParUtenBarn | Demographic × Household |
| Mann_AG13_15_1voksen_ParMedBarn | Demographic × Household |
| Mann_AG13_15_1voksen_FlereVoksne | Demographic × Household |
| Mann_AG13_15_2voksne_EnsligUtenBarn | Demographic × Household |
| Mann_AG13_15_2voksne_EnsligMedBarn | Demographic × Household |
| Mann_AG13_15_2voksne_ParUtenBarn | Demographic × Household |
| Mann_AG13_15_2voksne_ParMedBarn | Demographic × Household |
| ... | (351 more demographic combinations) |

**Geographic-level differences:**

- **sdat2_data2020_grunnkrets.xlsx**: +grunnkrets


