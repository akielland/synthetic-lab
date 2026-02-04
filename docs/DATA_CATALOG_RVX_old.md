# RVX Data Catalog

**Generated:** 2026-02-03 15:19:11

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
| `sdat1_d2024_g2020.dbf` | 4.42 | .dbf | 14097 | 41 |
| `sdat1_d2024_g2021.dbf` | 4.42 | .dbf | 14097 | 41 |
| `sdat1_d2024_g2023.dbf` | 4.43 | .dbf | 14101 | 41 |
| `sdat1_d2024_g2024.dbf` | 4.43 | .dbf | 14101 | 41 |
| `sdat2_data2020_delomr.xlsx` | 3.42 | .xlsx | n/a | n/a |
| `sdat2_data2020_grunnkrets.xlsx` | 25.69 | .xlsx | n/a | n/a |
| `sdat3_d2023x_g2020.dbf` | 2.38 | .dbf | 14097 | 18 |
| `sdat3_d2023x_g2021.dbf` | 2.38 | .dbf | 14097 | 18 |
| `sdat3_d2023x_g2023.dbf` | 2.38 | .dbf | 14101 | 18 |
| `sdat3_d2023x_g2024.dbf` | 2.38 | .dbf | 14101 | 18 |
| `sdat4_d2024_g2020.dbf` | 2.60 | .dbf | 14097 | 24 |
| `sdat4_d2024_g2021.dbf` | 2.60 | .dbf | 14097 | 24 |
| `sdat4_d2024_g2023.dbf` | 2.60 | .dbf | 14101 | 24 |
| `sdat4_d2024_g2024.dbf` | 2.60 | .dbf | 14101 | 24 |
| `sdat5_d2023_g2020.dbf` | 0.55 | .dbf | 14097 | 5 |
| `sdat5_d2023_g2021.dbf` | 0.55 | .dbf | 14097 | 5 |
| `sdat5_d2023_g2023.dbf` | 0.55 | .dbf | 14101 | 5 |
| `sdat5_d2023_g2024.dbf` | 0.55 | .dbf | 14101 | 5 |
| `sdat71_NB2023_grk2020_2020.dbf` | 0.39 | .dbf | 14097 | 4 |
| `sdat7_d20xx_g2020_ikke_pkost.dbf` | 0.66 | .dbf | 14097 | 6 |
| `sdat7_d20xx_g2021_ikke_pkost.dbf` | 0.66 | .dbf | 14097 | 6 |
| `sdat7_d20xx_g2023_ikke_pkost.dbf` | 0.66 | .dbf | 14101 | 6 |
| `sdat7_d20xx_g2024_ikke_pkost.dbf` | 0.66 | .dbf | 14101 | 6 |
| `sdat8_d2024_g2020.dbf` | 0.87 | .dbf | 14097 | 8 |
| `sdat8_d2024_g2021.dbf` | 0.87 | .dbf | 14097 | 8 |
| `sdat8_d2024_g2023.dbf` | 0.87 | .dbf | 14101 | 8 |
| `sdat8_d2024_g2024.dbf` | 0.87 | .dbf | 14101 | 8 |
| `sdat_6_areal_g2020.dbf` | 3.98 | .dbf | 14097 | 20 |

## Dataset Schemas

### traveling_survey/

#### Nasjonal_RVU_PERSON_Nov26_0901.sav

- **Path:** `Filemail.com - RVU 2025/Nasjonal_RVU_PERSON_Nov26_0901.sav`
- **Type:** SAV (SPSS)
- **Rows:** 51330
- **Columns:** 453

**Column details:**

| Column | Type |
|--------|------|
| altid | object |
| respid | object |
| altid_1 | object |
| altidNumeric | float64 |
| PublishedVersion | float64 |
| date_time_start_1 | float64 |
| date_time_start_2 | float64 |
| postnummer | object |
| alder | float64 |
| Aldersgruppe | float64 |
| kjonn_kat | float64 |
| kjonn | object |
| kommune | float64 |
| kommunenummer | float64 |
| grunnkrets | float64 |
| fylkesnummer | float64 |
| fylke | float64 |
| fodeland | object |
| utsendelsesdato | object |
| segment | object |
| utvalgskode | float64 |
| OS_BROWSER_1 | object |
| OS_BROWSER_2 | object |
| batch | float64 |
| Q_trans_1 | float64 |
| Q_trans_2 | float64 |
| Q_trans_3 | float64 |
| Q_trans_4 | float64 |
| Q_trans_5 | float64 |
| Q_trans_6 | float64 |
| Q_trans_7 | float64 |
| Q_trans_8 | float64 |
| Q_trans_9 | float64 |
| Q_trans_annet_1 | float64 |
| Q_trans_annet_2 | float64 |
| Q_trans_annet_3 | float64 |
| Q_trans_annet_4 | float64 |
| Q_trans_annet_5 | float64 |
| Q_trans_annet_6 | float64 |
| Q_trans_annet_98 | float64 |
| Q_trans_annet_7_other | object |
| Q_trans_tjenester_1 | float64 |
| Q_trans_tjenester_2 | float64 |
| Q_trans_tjenester_3 | float64 |
| Q_trans_tjenester_4 | float64 |
| Q_trans_tjenester_5 | float64 |
| Q_trans_tjenester_6 | float64 |
| Q_trans_tjenester_7 | float64 |
| FORERKORT | float64 |
| BOSTEDSJEKK | float64 |
| BOSTED_FEIL_12 | float64 |
| BOSTED_FEIL_13 | float64 |
| BOSTED_FEIL_4_other | object |
| BOSTED_FEIL_5_other | object |
| BOSTED_FEIL_6_other | object |
| BOSTED_FEIL_7_other | object |
| BOSTED_FEIL_8_other | object |
| BOSTED_FEIL_PRESISJON_UTDYP | float64 |
| BOSTED_FEIL_PRESISJON | float64 |
| BOSTED_ANNET_12 | float64 |
| BOSTED_ANNET_13 | float64 |
| BOSTED_ANNET_4_other | object |
| BOSTED_ANNET_5_other | object |
| BOSTED_ANNET_6_other | object |
| BOSTED_ANNET_7_other | object |
| BOSTED_ANNET_8_other | object |
| BOSTED_ANNET_PRESISJON_UTDYP | float64 |
| BOSTED_ANNET_PRESISJON | float64 |
| BOSTED_FLERE | float64 |
| BOSTED_FLERE_ADRESSE_12 | float64 |
| BOSTED_FLERE_ADRESSE_13 | float64 |
| BOSTED_FLERE_ADRESSE_4_other | object |
| BOSTED_FLERE_ADRESSE_5_other | object |
| BOSTED_FLERE_ADRESSE_6_other | object |
| BOSTED_FLERE_ADRESSE_7_other | object |
| BOSTED_FLERE_ADRESSE_8_other | object |
| BOSTED_FLERE_ADRESSE_PRESISJON_UTDYP | float64 |
| BOSTED_FLERE_ADRESSE_PRESISJON | float64 |
| BOSTED_SKJULT_B_1 | float64 |
| BOSTED_SKJULT_B_2 | float64 |
| BOSTED_SKJULT_B_3 | float64 |
| BOSTEDSLAND | float64 |
| BOSTED_ANTALL | float64 |
| Reisedag_3 | float64 |
| HOVED | float64 |
| OPPMOTE | float64 |
| OPPMOTE_SKOLE | float64 |
| OPPMOTE_ADRESSE_12 | float64 |
| OPPMOTE_ADRESSE_13 | float64 |
| OPPMOTE_ADRESSE_4_other | object |
| OPPMOTE_ADRESSE_5_other | object |
| OPPMOTE_ADRESSE_6_other | object |
| OPPMOTE_ADRESSE_7_other | object |
| OPPMOTE_ADRESSE_8_other | object |
| OPPMOTE_ADRESSE_PRESISJON_UTDYP | float64 |
| OPPMOTE_ADRESSE_PRESISJON | float64 |
| ARBEID | float64 |
| ARBEID_TIMER | float64 |
| YRKESSJAFOR | float64 |
| TJENESTEREISE | float64 |
| ARBEIDSREISER | float64 |
| YRKESSJAFOR_NEW | float64 |
| BOSTED_IGAR | float64 |
| BOSTED_IGAR_Annet_12 | float64 |
| BOSTED_IGAR_Annet_13 | float64 |
| BOSTED_IGAR_Annet_4_other | object |
| BOSTED_IGAR_Annet_5_other | object |
| BOSTED_IGAR_Annet_6_other | object |
| BOSTED_IGAR_Annet_7_other | object |
| BOSTED_IGAR_Annet_8_other | object |
| BOSTED_IGAR_PRESISJON_UTDYP | float64 |
| BOSTED_IGAR_PRESISJON | float64 |
| UTLAND | float64 |
| null_reiser | float64 |
| null_reiser_kontroll | float64 |
| REISER | float64 |
| GJOREMAL_START_1 | float64 |
| GJOREMAL_START_2 | float64 |
| GJOREMAL_START_3 | float64 |
| GJOREMAL_START_4 | float64 |
| GJOREMAL_START_5 | float64 |
| GJOREMAL_START_6 | float64 |
| GJOREMAL_START_7 | float64 |
| GJOREMAL_START_8 | float64 |
| GJOREMAL_START_9 | float64 |
| GJOREMAL_START_10 | float64 |
| GJOREMAL_START_11 | float64 |
| TRANSPORTMIDDEL_2 | float64 |
| TRANSPORTMIDDEL_3 | float64 |
| TRANSPORTMIDDEL_4 | float64 |
| TRANSPORTMIDDEL_5 | float64 |
| TRANSPORTMIDDEL_6 | float64 |
| TRANSPORTMIDDEL_8 | float64 |
| TRANSPORTMIDDEL_9 | float64 |
| TRANSPORTMIDDEL_10 | float64 |
| TRANSPORTMIDDEL_11 | float64 |
| TRANSPORTMIDDEL_12 | float64 |
| TRANSPORTMIDDEL_13 | float64 |
| TRANSPORTMIDDEL_14 | float64 |
| TRANSPORTMIDDEL_15 | float64 |
| TRANSPORTMIDDEL_16 | float64 |
| TRANSPORTMIDDEL_17 | float64 |
| TRANSPORTMIDDEL_18 | float64 |
| TRANSPORTMIDDEL_19 | float64 |
| TRANSPORTMIDDEL_20 | float64 |
| TRANSPORTMIDDEL_21 | float64 |
| TRANSPORTMIDDEL_22 | float64 |
| TRANSPORTMIDDEL_23 | float64 |
| TRANSPORTMIDDEL_24 | float64 |
| TRANSPORTMIDDEL_25 | float64 |
| TRANSPORTMIDDEL_7 | float64 |
| TRANSPORTMIDDEL_26 | float64 |
| TRANSPORTMIDDEL_27 | float64 |
| TRANSPORTMIDDEL_28 | float64 |
| TRANSPORTMIDDEL_29 | float64 |
| TRANSPORTMIDDEL_30 | float64 |
| TRANSPORTMIDDEL_31 | float64 |
| TRANSPORTMIDDEL_32 | float64 |
| TRANSPORTMIDDEL_33 | float64 |
| TRANSPORTMIDDEL_34 | float64 |
| TRANSPORTMIDDEL_98 | float64 |
| TRANSPORTMIDDEL_97 | float64 |
| BIL_SJAFOR_ANTALL | float64 |
| BIL_REG_1_1 | object |
| BIL_REG_EIERFORM_1 | float64 |
| BIL_REG_TYPE_1 | float64 |
| BIL_REG_DRIVSTOFF_1 | float64 |
| BIL_REG_2_1 | object |
| BIL_REG_EIERFORM_2 | float64 |
| BIL_REG_TYPE_2 | float64 |
| BIL_REG_DRIVSTOFF_2 | float64 |
| BIL_REG_3_1 | object |
| BIL_REG_EIERFORM_3 | float64 |
| BIL_REG_TYPE_3 | float64 |
| BIL_REG_DRIVSTOFF_3 | float64 |
| BIL_REG_4_1 | object |
| BIL_REG_EIERFORM_4 | float64 |
| BIL_REG_TYPE_4 | float64 |
| BIL_REG_DRIVSTOFF_4 | float64 |
| BIL_REG_5_1 | object |
| BIL_REG_EIERFORM_5 | float64 |
| BIL_REG_TYPE_5 | float64 |
| BIL_REG_DRIVSTOFF_5 | float64 |
| tid_til_reiseseksjon_tidsstempel | float64 |
| sekunder_til_reise | float64 |
| start_reiseseksjon | float64 |
| tid_reiseseksjon_tidsstempel | float64 |
| sekunder_reiseseksjon | float64 |
| ALTERNATIV_BIL_1 | float64 |
| ALTERNATIV_BIL_2 | float64 |
| ALTERNATIV_BIL_3 | float64 |
| ALTERNATIV_BIL_4 | float64 |
| ALTERNATIV_BIL_5 | float64 |
| ALTERNATIV_BIL_6 | float64 |
| ALTERNATIV_BIL_7 | float64 |
| ALTERNATIV_BIL_8 | float64 |
| ALTERNATIV_BIL_9 | float64 |
| ALTERNATIV_BIL_10 | float64 |
| ALTERNATIV_BIL_11 | float64 |
| VANE_1 | float64 |
| VANE_2 | float64 |
| VANE_3 | float64 |
| VANE_4 | float64 |
| VANE_5 | float64 |
| KOLL_KORT | float64 |
| KORT_TYPE | float64 |
| BIL_EIE_FLERE_1 | float64 |
| BIL_EIE_1_1 | object |
| BIL_EIE_EIERFORM_1 | float64 |
| BIL_EIE_TYPE_1 | float64 |
| BIL_EIE_DRIVSTOFF_1 | float64 |
| BIL_EIE_FLERE_2 | float64 |
| BIL_EIE_2_1 | object |
| BIL_EIE_EIERFORM_2 | float64 |
| BIL_EIE_TYPE_2 | float64 |
| BIL_EIE_DRIVSTOFF_2 | float64 |
| BIL_EIE_FLERE_3 | float64 |
| BIL_EIE_3_1 | object |
| BIL_EIE_EIERFORM_3 | float64 |
| BIL_EIE_TYPE_3 | float64 |
| BIL_EIE_DRIVSTOFF_3 | float64 |
| BIL_EIE_FLERE_4 | float64 |
| BIL_EIE_4_1 | object |
| BIL_EIE_EIERFORM_4 | float64 |
| BIL_EIE_TYPE_4 | float64 |
| BIL_EIE_DRIVSTOFF_4 | float64 |
| BIL_EIE_FLERE_5 | float64 |
| BIL_EIE_5_1 | object |
| BIL_EIE_EIERFORM_5 | float64 |
| BIL_EIE_TYPE_5 | float64 |
| BIL_EIE_DRIVSTOFF_5 | float64 |
| BIL_REG_TOTAL | float64 |
| BIL_EIE_TOTAL | float64 |
| BIL_TOTAL | float64 |
| BIL_DEKK_1 | float64 |
| BIL_DEKK_2 | float64 |
| BIL_DEKK_3 | float64 |
| BIL_DEKK_4 | float64 |
| BIL_DEKK_5 | float64 |
| BIL_DEKK_6 | float64 |
| BIL_DEKK_7 | float64 |
| BIL_DEKK_8 | float64 |
| BIL_DEKK_9 | float64 |
| BIL_DEKK_10 | float64 |
| DRIVSTOFF_TOTAL_1 | float64 |
| DRIVSTOFF_TOTAL_2 | float64 |
| BIL_LADING | float64 |
| JOBB_P1 | float64 |
| JOBB_P2 | float64 |
| JOBB_P3 | float64 |
| JOBB_P6 | float64 |
| JOBB_P7 | float64 |
| HJEMME_P6 | float64 |
| HJEMME_P8 | float64 |
| HUSHOLDNING_TYPE | float64 |
| HUSHOLDNING_ANTALL_1 | float64 |
| HUSHOLDNING_ANTALL_2 | float64 |
| ALDER_BARN_1 | float64 |
| ALDER_BARN_2 | float64 |
| ALDER_BARN_3 | float64 |
| ALDER_BARN_4 | float64 |
| ALDER_BARN_5 | float64 |
| ALDER_BARN_6 | float64 |
| ALDER_BARN_7 | float64 |
| ALDER_BARN_8 | float64 |
| ALDER_BARN_9 | float64 |
| TRANSPORT_SKOLE_1 | float64 |
| TRANSPORT_SKOLE_2 | float64 |
| TRANSPORT_SKOLE_3 | float64 |
| TRANSPORT_SKOLE_4 | float64 |
| TRANSPORT_SKOLE_5 | float64 |
| TRANSPORT_SKOLE_6 | float64 |
| TRANSPORT_SKOLE_7 | float64 |
| TRANSPORT_SKOLE_8 | float64 |
| TRANSPORT_SKOLE_9 | float64 |
| FORERKORT_ANT | float64 |
| FORERKORT_ANT_1_other | object |
| YRKESAKTIV_ANT | float64 |
| YRKESAKTIV_ANT_1_other | object |
| H_INNTEKT | float64 |
| P_INNTEKT | float64 |
| UTDANNING | float64 |
| YRKE | float64 |
| LEDER | float64 |
| BRANSJE | float64 |
| HJEMMEKONTOR | float64 |
| ORDNING | float64 |
| PROBLEM | float64 |
| PROBLEMET_1 | float64 |
| PROBLEMET_2 | float64 |
| PROBLEMET_3 | float64 |
| PROBLEMET_4 | float64 |
| PROBLEMET_5 | float64 |
| PROBLEMET_6 | float64 |
| PROBLEMET_7 | float64 |
| PROBLEMET_9 | float64 |
| PROBLEMET_8 | float64 |
| LANGE_REISER_1 | float64 |
| LANGE_REISER_2 | float64 |
| LANGE_REISER_3 | float64 |
| LANGE_REISER_4 | float64 |
| LANGE_REISER_5 | float64 |
| kontakt_epost | float64 |
| kontakt_sms | float64 |
| VervLangeReiser | float64 |
| RVU_TILBAKEMELDING | object |
| REKONTAKT | float64 |
| shortlink | object |
| date_time_slutt_1 | float64 |
| date_time_slutt_2 | float64 |
| Tid_total | float64 |
| BIL_DETALJER | float64 |
| HJEMME_P1 | float64 |
| HJEMME_P3 | float64 |
| PERSONER | float64 |
| Alder_PERS_1 | float64 |
| Alder_PERS_2 | float64 |
| Alder_PERS_3 | float64 |
| Alder_PERS_4 | float64 |
| Alder_PERS_5 | float64 |
| Alder_PERS_6 | float64 |
| Alder_PERS_7 | float64 |
| Alder_PERS_8 | float64 |
| Alder_PERS_9 | float64 |
| Alder_PERS_10 | float64 |
| Alder_PERS_11 | float64 |
| Alder_PERS_12 | float64 |
| Alder_PERS_13 | float64 |
| Alder_PERS_14 | float64 |
| SLEKT_PERS_1 | float64 |
| SLEKT_PERS_2 | float64 |
| SLEKT_PERS_3 | float64 |
| SLEKT_PERS_4 | float64 |
| SLEKT_PERS_5 | float64 |
| SLEKT_PERS_6 | float64 |
| SLEKT_PERS_7 | float64 |
| SLEKT_PERS_8 | float64 |
| SLEKT_PERS_9 | float64 |
| SLEKT_PERS_10 | float64 |
| SLEKT_PERS_11 | float64 |
| SLEKT_PERS_12 | float64 |
| SLEKT_PERS_13 | float64 |
| SLEKT_PERS_14 | float64 |
| TRANSPORT_SKOLE_10 | float64 |
| TRANSPORT_SKOLE_11 | float64 |
| TRANSPORT_SKOLE_12 | float64 |
| TRANSPORT_SKOLE_13 | float64 |
| TRANSPORT_SKOLE_14 | float64 |
| FORERKORT_PERS_1 | float64 |
| FORERKORT_PERS_2 | float64 |
| FORERKORT_PERS_3 | float64 |
| FORERKORT_PERS_4 | float64 |
| FORERKORT_PERS_5 | float64 |
| FORERKORT_PERS_6 | float64 |
| FORERKORT_PERS_7 | float64 |
| FORERKORT_PERS_8 | float64 |
| FORERKORT_PERS_9 | float64 |
| FORERKORT_PERS_10 | float64 |
| FORERKORT_PERS_11 | float64 |
| FORERKORT_PERS_12 | float64 |
| FORERKORT_PERS_13 | float64 |
| FORERKORT_PERS_14 | float64 |
| ARBEID_PERS_OLD | float64 |
| ARBEID_PERS_1 | float64 |
| ARBEID_PERS_2 | float64 |
| ARBEID_PERS_3 | float64 |
| ARBEID_PERS_4 | float64 |
| ARBEID_PERS_5 | float64 |
| ARBEID_PERS_6 | float64 |
| ARBEID_PERS_7 | float64 |
| ARBEID_PERS_8 | float64 |
| ARBEID_PERS_9 | float64 |
| ARBEID_PERS_10 | float64 |
| ARBEID_PERS_11 | float64 |
| ARBEID_PERS_12 | float64 |
| ARBEID_PERS_13 | float64 |
| ARBEID_PERS_14 | float64 |
| valid_cases | float64 |
| BOSTED_kommune | float64 |
| BOSTED_fylke | float64 |
| BOSTED_2_kommune | float64 |
| BOSTED_3_kommune | float64 |
| Start_reisedag_kommune | float64 |
| utvalgskode_valid | float64 |
| utvalgskode_fakturering | float64 |
| kommuner_Osloomradet | float64 |
| kommuner_Trondheimsregionen | float64 |
| kommuner_Bergensregionen | float64 |
| kommuner_Region_NordJaeren | float64 |
| kommuner_Nedre_Glomma | float64 |
| kommuner_Kristiansandsregionen | float64 |
| kommuner_Grenland | float64 |
| kommuner_Buskerudbyen | float64 |
| kommuner_RestOstfold_inkl_Moss_og_Halden | float64 |
| utvalg_fra_kommune | float64 |
| BVA | float64 |
| BVA_samlet | float64 |
| rapportomraade | float64 |
| storbykommune_filter | float64 |
| bykommuner_filter | float64 |
| bykommune | float64 |
| omegnskommune_filter | float64 |
| by_omegn | float64 |
| kommuner_tilleggsutvalg | float64 |
| aldersgrupper_2 | float64 |
| Alderskategorier_RVU_2 | float64 |
| alder_vekting | float64 |
| gender | float64 |
| REK_YRKESSTATUS | float64 |
| date_datetime | datetime64[ns] |
| date_ukenummer | float64 |
| Month | float64 |
| Quarter | float64 |
| response_date | datetime64[ns] |
| datetime_slutt | datetime64[ns] |
| reisedag_ukedag | float64 |
| PublishedVersion_gruppert | float64 |
| ANTALL_BILER | float64 |
| EIER_DISP_BIL | float64 |
| EIER_DISP_ELBIL | float64 |
| EIER_DISP_HYBRID | float64 |
| EIER_DISP_EL_HYBRID | float64 |
| EL_BIL | float64 |
| antall_reiser | float64 |
| har_reiser | float64 |
| GJOREMAL_MULTI_1 | float64 |
| GJOREMAL_MULTI_2 | float64 |
| GJOREMAL_MULTI_3 | float64 |
| GJOREMAL_MULTI_4 | float64 |
| GJOREMAL_MULTI_5 | float64 |
| GJOREMAL_MULTI_6 | float64 |
| GJOREMAL_MULTI_7 | float64 |
| GJOREMAL_MULTI_8 | float64 |
| GJOREMAL_MULTI_9 | float64 |
| GJOREMAL_MULTI_98 | float64 |
| TRM_BRUK_PERSON_02 | float64 |
| TRM_BRUK_PERSON_03 | float64 |
| TRM_BRUK_PERSON_04 | float64 |
| TRM_BRUK_PERSON_06 | float64 |
| TRM_BRUK_PERSON_08 | float64 |
| TRM_BRUK_PERSON_11 | float64 |
| TRM_BRUK_PERSON_14 | float64 |
| TRM_BRUK_PERSON_17 | float64 |
| TRM_BRUK_PERSON_18 | float64 |
| TRM_BRUK_PERSON_20 | float64 |
| TRM_BRUK_PERSON_21 | float64 |
| TRM_BRUK_PERSON_22 | float64 |
| TRM_BRUK_PERSON_23 | float64 |
| TRM_BRUK_PERSON_97 | float64 |
| TRM_BRUK_PERSON_70 | float64 |
| TRM_BRUK_PERSON_71 | float64 |
| utvalgsvekt_kombinert_Q1_Q3 | float64 |
| utvalgsvekt_nasjonal_Q1_Q3 | float64 |

#### Nasjonal_RVU_REISER_Nov26_0901.sav

- **Path:** `Filemail.com - RVU 2025/Nasjonal_RVU_REISER_Nov26_0901.sav`
- **Type:** SAV (SPSS)
- **Rows:** 127115
- **Columns:** 226

**Column details:**

| Column | Type |
|--------|------|
| trip_id | object |
| altid | object |
| Reise | object |
| Reisenr | float64 |
| utvalgskode_valid | float64 |
| PublishedVersion | float64 |
| response_date | datetime64[ns] |
| GJOREMAL | float64 |
| FORMAL_SUB | float64 |
| BOSTED_IGAR_NEW | float64 |
| DESTINASJON | float64 |
| DESTINASJON_5_other | object |
| DESTINASJON_KART_12 | float64 |
| DESTINASJON_KART_13 | float64 |
| DESTINASJON_KART_4_other | object |
| DESTINASJON_KART_5_other | object |
| DESTINASJON_KART_6_other | object |
| DESTINASJON_KART_7_other | object |
| DESTINASJON_KART_8_other | object |
| DEST_PRESISJON_UTDYP | float64 |
| DEST_PRESISJON | float64 |
| STARTTID | object |
| TRANSPORTMIDLER_2 | float64 |
| TRANSPORTMIDLER_3 | float64 |
| TRANSPORTMIDLER_4 | float64 |
| TRANSPORTMIDLER_5 | float64 |
| TRANSPORTMIDLER_6 | float64 |
| TRANSPORTMIDLER_8 | float64 |
| TRANSPORTMIDLER_9 | float64 |
| TRANSPORTMIDLER_10 | float64 |
| TRANSPORTMIDLER_11 | float64 |
| TRANSPORTMIDLER_12 | float64 |
| TRANSPORTMIDLER_13 | float64 |
| TRANSPORTMIDLER_14 | float64 |
| TRANSPORTMIDLER_15 | float64 |
| TRANSPORTMIDLER_16 | float64 |
| TRANSPORTMIDLER_17 | float64 |
| TRANSPORTMIDLER_18 | float64 |
| TRANSPORTMIDLER_19 | float64 |
| TRANSPORTMIDLER_20 | float64 |
| TRANSPORTMIDLER_21 | float64 |
| TRANSPORTMIDLER_22 | float64 |
| TRANSPORTMIDLER_23 | float64 |
| TRANSPORTMIDLER_24 | float64 |
| TRANSPORTMIDLER_25 | float64 |
| TRANSPORTMIDLER_7 | float64 |
| TRANSPORTMIDLER_26 | float64 |
| TRANSPORTMIDLER_27 | float64 |
| TRANSPORTMIDLER_28 | float64 |
| TRANSPORTMIDLER_29 | float64 |
| TRANSPORTMIDLER_30 | float64 |
| TRANSPORTMIDLER_31 | float64 |
| TRANSPORTMIDLER_32 | float64 |
| TRANSPORTMIDLER_33 | float64 |
| TRANSPORTMIDLER_34 | float64 |
| TRANSPORTMIDLER_98 | float64 |
| TRANSPORTMIDLER_97 | float64 |
| TRANSPORTMIDDEL_D_1 | float64 |
| TRANSPORTMIDDEL_FLY_D_1 | float64 |
| KOLL_HOLDEPLASS_D_1_1 | object |
| KOLL_HOLDEPLASS_D_1_2 | object |
| KOLL_HOLDEPLASS_D_1_3 | object |
| KOLL_HOLDEPLASS_D_1_4 | object |
| KOLL_HOLDEPLASS_D_1_5 | object |
| KOLL_HOLDEPLASS_D_1_6 | object |
| BIL_SJOFOR_D_1 | float64 |
| BIL_PASSASJER_DRIVSTOFF_D_1 | float64 |
| TRANSPORTMIDDEL_RUTE_D_1 | float64 |
| TRANSPORTMIDDEL_FORSINKET_D_1 | float64 |
| LASTESYKKEL_D_1 | float64 |
| TRANSPORTMIDDEL_D_2 | float64 |
| TRANSPORTMIDDEL_FLY_D_2 | float64 |
| KOLL_HOLDEPLASS_D_2_1 | object |
| KOLL_HOLDEPLASS_D_2_2 | object |
| KOLL_HOLDEPLASS_D_2_3 | object |
| KOLL_HOLDEPLASS_D_2_4 | object |
| KOLL_HOLDEPLASS_D_2_5 | object |
| KOLL_HOLDEPLASS_D_2_6 | object |
| BIL_SJOFOR_D_2 | float64 |
| BIL_PASSASJER_DRIVSTOFF_D_2 | float64 |
| TRANSPORTMIDDEL_RUTE_D_2 | float64 |
| TRANSPORTMIDDEL_FORSINKET_D_2 | float64 |
| LASTESYKKEL_D_2 | float64 |
| TRANSPORTMIDDEL_D_3 | float64 |
| TRANSPORTMIDDEL_FLY_D_3 | float64 |
| KOLL_HOLDEPLASS_D_3_1 | object |
| KOLL_HOLDEPLASS_D_3_2 | object |
| KOLL_HOLDEPLASS_D_3_3 | object |
| KOLL_HOLDEPLASS_D_3_4 | object |
| KOLL_HOLDEPLASS_D_3_5 | object |
| KOLL_HOLDEPLASS_D_3_6 | object |
| BIL_SJOFOR_D_3 | float64 |
| BIL_PASSASJER_DRIVSTOFF_D_3 | float64 |
| TRANSPORTMIDDEL_RUTE_D_3 | float64 |
| TRANSPORTMIDDEL_FORSINKET_D_3 | float64 |
| LASTESYKKEL_D_3 | float64 |
| TRANSPORTMIDDEL_D_4 | float64 |
| TRANSPORTMIDDEL_FLY_D_4 | float64 |
| KOLL_HOLDEPLASS_D_4_1 | object |
| KOLL_HOLDEPLASS_D_4_2 | object |
| KOLL_HOLDEPLASS_D_4_3 | object |
| KOLL_HOLDEPLASS_D_4_4 | object |
| KOLL_HOLDEPLASS_D_4_5 | object |
| KOLL_HOLDEPLASS_D_4_6 | object |
| BIL_SJOFOR_D_4 | float64 |
| BIL_PASSASJER_DRIVSTOFF_D_4 | float64 |
| TRANSPORTMIDDEL_RUTE_D_4 | float64 |
| TRANSPORTMIDDEL_FORSINKET_D_4 | float64 |
| LASTESYKKEL_D_4 | float64 |
| TRANSPORTMIDDEL_D_5 | float64 |
| TRANSPORTMIDDEL_FLY_D_5 | float64 |
| KOLL_HOLDEPLASS_D_5_1 | object |
| KOLL_HOLDEPLASS_D_5_2 | object |
| KOLL_HOLDEPLASS_D_5_3 | object |
| KOLL_HOLDEPLASS_D_5_4 | object |
| KOLL_HOLDEPLASS_D_5_5 | object |
| KOLL_HOLDEPLASS_D_5_6 | object |
| BIL_SJOFOR_D_5 | float64 |
| BIL_PASSASJER_DRIVSTOFF_D_5 | float64 |
| TRANSPORTMIDDEL_RUTE_D_5 | float64 |
| TRANSPORTMIDDEL_FORSINKET_D_5 | float64 |
| LASTESYKKEL_D_5 | float64 |
| TRANSPORTMIDDEL_D_6 | float64 |
| TRANSPORTMIDDEL_FLY_D_6 | float64 |
| KOLL_HOLDEPLASS_D_6_1 | object |
| KOLL_HOLDEPLASS_D_6_2 | object |
| KOLL_HOLDEPLASS_D_6_3 | object |
| KOLL_HOLDEPLASS_D_6_4 | object |
| KOLL_HOLDEPLASS_D_6_5 | object |
| KOLL_HOLDEPLASS_D_6_6 | object |
| BIL_SJOFOR_D_6 | float64 |
| BIL_PASSASJER_DRIVSTOFF_D_6 | float64 |
| TRANSPORTMIDDEL_RUTE_D_6 | float64 |
| TRANSPORTMIDDEL_FORSINKET_D_6 | float64 |
| LASTESYKKEL_D_6 | float64 |
| TRANSPORTMIDDEL_D_7 | float64 |
| TRANSPORTMIDDEL_FLY_D_7 | float64 |
| KOLL_HOLDEPLASS_D_7_1 | object |
| KOLL_HOLDEPLASS_D_7_2 | object |
| KOLL_HOLDEPLASS_D_7_3 | object |
| KOLL_HOLDEPLASS_D_7_4 | object |
| KOLL_HOLDEPLASS_D_7_5 | object |
| KOLL_HOLDEPLASS_D_7_6 | object |
| BIL_SJOFOR_D_7 | float64 |
| BIL_PASSASJER_DRIVSTOFF_D_7 | float64 |
| TRANSPORTMIDDEL_RUTE_D_7 | float64 |
| TRANSPORTMIDDEL_FORSINKET_D_7 | float64 |
| LASTESYKKEL_D_7 | float64 |
| TRANSPORTMIDDEL_D_8 | float64 |
| TRANSPORTMIDDEL_FLY_D_8 | float64 |
| KOLL_HOLDEPLASS_D_8_1 | object |
| KOLL_HOLDEPLASS_D_8_2 | object |
| KOLL_HOLDEPLASS_D_8_3 | object |
| KOLL_HOLDEPLASS_D_8_4 | object |
| KOLL_HOLDEPLASS_D_8_5 | object |
| KOLL_HOLDEPLASS_D_8_6 | object |
| BIL_SJOFOR_D_8 | float64 |
| BIL_PASSASJER_DRIVSTOFF_D_8 | float64 |
| TRANSPORTMIDDEL_RUTE_D_8 | float64 |
| TRANSPORTMIDDEL_FORSINKET_D_8 | float64 |
| LASTESYKKEL_D_8 | float64 |
| REISETID | float64 |
| FLOKK_REISE | float64 |
| FLOKK_ANTALL | float64 |
| FLOKK_ANTALL_5_other | object |
| FLOKK_BARN | float64 |
| FLOKK_BARN_6_other | object |
| DISTANSE_RUNDTUR | float64 |
| FLERE_REISE | float64 |
| FLOKK_D_1 | float64 |
| FLOKK_D_1_5_other | object |
| TRANSPORTMIDDEL_BARN_D_1 | float64 |
| TRANSPORTMIDDEL_BARN_D_1_1_other | object |
| FLOKK_D_2 | float64 |
| FLOKK_D_2_5_other | object |
| TRANSPORTMIDDEL_BARN_D_2 | float64 |
| TRANSPORTMIDDEL_BARN_D_2_1_other | object |
| FLOKK_D_3 | float64 |
| FLOKK_D_3_5_other | object |
| TRANSPORTMIDDEL_BARN_D_3 | float64 |
| TRANSPORTMIDDEL_BARN_D_3_1_other | object |
| FLOKK_D_4 | float64 |
| FLOKK_D_4_5_other | object |
| TRANSPORTMIDDEL_BARN_D_4 | float64 |
| TRANSPORTMIDDEL_BARN_D_4_1_other | object |
| FLOKK_D_5 | float64 |
| FLOKK_D_5_5_other | object |
| TRANSPORTMIDDEL_BARN_D_5 | float64 |
| TRANSPORTMIDDEL_BARN_D_5_1_other | object |
| FLOKK_D_6 | float64 |
| FLOKK_D_6_5_other | object |
| TRANSPORTMIDDEL_BARN_D_6 | float64 |
| TRANSPORTMIDDEL_BARN_D_6_1_other | object |
| FLOKK_D_7 | float64 |
| FLOKK_D_7_5_other | object |
| TRANSPORTMIDDEL_BARN_D_7 | float64 |
| TRANSPORTMIDDEL_BARN_D_7_1_other | object |
| FLOKK_D_8 | float64 |
| FLOKK_D_8_5_other | object |
| TRANSPORTMIDDEL_BARN_D_8 | float64 |
| TRANSPORTMIDDEL_BARN_D_8_1_other | object |
| SLUTTID | object |
| TRM_BRUK_REISE_02 | float64 |
| TRM_BRUK_REISE_03 | float64 |
| TRM_BRUK_REISE_04 | float64 |
| TRM_BRUK_REISE_06 | float64 |
| TRM_BRUK_REISE_08 | float64 |
| TRM_BRUK_REISE_11 | float64 |
| TRM_BRUK_REISE_14 | float64 |
| TRM_BRUK_REISE_17 | float64 |
| TRM_BRUK_REISE_18 | float64 |
| TRM_BRUK_REISE_20 | float64 |
| TRM_BRUK_REISE_21 | float64 |
| TRM_BRUK_REISE_22 | float64 |
| TRM_BRUK_REISE_23 | float64 |
| TRM_BRUK_REISE_97 | float64 |
| TRM_BRUK_REISE_70 | float64 |
| TRM_BRUK_REISE_71 | float64 |
| htrm_logical | float64 |
| htrm_logical_grouped | float64 |
| htrm_logical_grouped_2 | float64 |
| REISETID_minutter | float64 |
| REISETID_timer | float64 |
| STARTTID_klokketime | float64 |
| START | float64 |
| REISEHENSIKT | float64 |

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

| Column | Type |
|--------|------|
| uuid | object |
| uuid_trip | object |
| tripNum | float64 |
| Year | float64 |
| HTRM | float64 |
| HTRM_REK | float64 |
| HTRM_kollektiv | float64 |
| HTRM_gml | float64 |
| HTRM_2 | float64 |
| HTRM_forenklet | float64 |
| HOVED_delreise | float64 |
| HTRM_detaljert | float64 |
| HTRM_ny | float64 |
| HTRM_kollektiv_ny | float64 |
| test | float64 |
| Reiseavstand_KM | float64 |
| Reiseavstand_KM_revidert | float64 |
| Reiseavstand_KM_gruppert | float64 |
| Reiseavstand_KM_gruppert_org | float64 |
| ReiseavstandKM_Gruppert | float64 |
| Reisehastighet_KMH_total_revidert | float64 |
| Reisetid_MIN_sum_revidert | float64 |
| Reisetid_MIN_gruppert | float64 |
| ReiselengdeMIN | float64 |
| ReiselengdeMIN_revidert | float64 |
| ReiselengdeMIN_revidert_NY | float64 |
| Reisetid_MIN_gruppert_NY | float64 |
| Reisetid_MIN_summert_revidert | float64 |
| Reisetid_MIN_summert_revidert_2023 | float64 |
| START_1 | float64 |
| START_Grunnkrets | object |
| START_Kommune | float64 |
| START_PRESISJON | float64 |
| ENDE_1 | float64 |
| ENDE_Grunnkrets | object |
| ENDE_Kommune | float64 |
| ENDE_PRESISJON | float64 |
| REISEHENSIKT | float64 |
| FORMAL_SUB_1 | float64 |
| STARTTID_TIMESINTERVALL | float64 |
| GJOREMALc1 | float64 |
| FORMAL_Confirm_1 | float64 |
| FORMAL_HOVED_1 | float64 |
| FORMAL_HOVED_REKODET | float64 |
| Gjoremal | float64 |
| ReisehensiktRVU | float64 |
| HTRM_komplett | float64 |
| HTRM_uten_flydrosje_enkelt | float64 |
| START_ADRESSE_1r1_grunnkretsnummer | float64 |
| START_ADRESSE_1r1_grunnkrets | object |
| START_kommune_2020 | float64 |
| START_ADRESSE_START_PRES_1 | float64 |
| START_UTLANDET_1 | float64 |
| ENDE_ADRESSE_1r1_grunnkretsnummer | float64 |
| ENDE_ADRESSE_1r1_grunnkrets | object |
| ENDE_kommune_2020 | float64 |
| ENDE_ADRESSE_START_PRES_1 | float64 |
| ENDE_UTLANDET_1 | float64 |
| Reisetid_MIN_gruppert_2023 | float64 |
| Reiseavstand_KM_gruppert_2023 | float64 |
| Total_reiser | float64 |
| PrimaryLast1 | float64 |
| Reisetid_MIN_gruppert_org | float64 |
| komplette_utvalg | float64 |
| TRANSPORTMIDDEL_ANTALL_1#1 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#2 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#3 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#4 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#5 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#6 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#7 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#8 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#9 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#10 | float64 |
| TRANSPORTMIDDEL_ANTALL_1#11 | float64 |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_1 | float64 |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_2 | float64 |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_3 | float64 |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_4 | float64 |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_5 | float64 |
| SYKKEL_1_vehicle_1 | float64 |
| SYKKEL_1_vehicle_2 | float64 |
| SYKKEL_1_vehicle_3 | float64 |
| SYKKEL_1_vehicle_4 | float64 |
| SYKKEL_1_vehicle_5 | float64 |
| KOLLEKTIV_1_vehicle_1 | float64 |
| KOLLEKTIV_1_vehicle_2 | float64 |
| KOLLEKTIV_1_vehicle_3 | float64 |
| KOLLEKTIV_1_vehicle_4 | float64 |
| KOLLEKTIV_1_vehicle_5 | float64 |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_6 | float64 |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_7 | float64 |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_8 | float64 |
| TRANSPORTMIDDEL_DELREISE_1_vehicle_9 | float64 |
| SYKKEL_1_vehicle_6 | float64 |
| SYKKEL_1_vehicle_7 | float64 |
| SYKKEL_1_vehicle_8 | float64 |
| SYKKEL_1_vehicle_9 | float64 |
| KOLLEKTIV_1_vehicle_6 | float64 |
| KOLLEKTIV_1_vehicle_7 | float64 |
| KOLLEKTIV_1_vehicle_8 | float64 |
| KOLLEKTIV_1_vehicle_9 | float64 |
| antall_trm | float64 |

### zonal_register_data/

#### sdat1_d2024_g2020.dbf

- **Path:** `sdat1_d2024_g2020.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 41

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| M_0_4 | N |
| M_5_9 | N |
| M_10_14 | N |
| M_15_19 | N |
| M_20_24 | N |
| M_25_29 | N |
| M_30_34 | N |
| M_35_39 | N |
| M_40_44 | N |
| M_45_49 | N |
| M_50_54 | N |
| M_55_59 | N |
| M_60_64 | N |
| M_65_69 | N |
| M_70_74 | N |
| M_75_79 | N |
| M_80_84 | N |
| M_85_89 | N |
| M_90_94 | N |
| M_95_UP | N |
| K_0_4 | N |
| K_5_9 | N |
| K_10_14 | N |
| K_15_19 | N |
| K_20_24 | N |
| K_25_29 | N |
| K_30_34 | N |
| K_35_39 | N |
| K_40_44 | N |
| K_45_49 | N |
| K_50_54 | N |
| K_55_59 | N |
| K_60_64 | N |
| K_65_69 | N |
| K_70_74 | N |
| K_75_79 | N |
| K_80_84 | N |
| K_85_89 | N |
| K_90_94 | N |
| K_95_UP | N |

#### sdat1_d2024_g2021.dbf

- **Path:** `sdat1_d2024_g2021.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 41

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| M_0_4 | N |
| M_5_9 | N |
| M_10_14 | N |
| M_15_19 | N |
| M_20_24 | N |
| M_25_29 | N |
| M_30_34 | N |
| M_35_39 | N |
| M_40_44 | N |
| M_45_49 | N |
| M_50_54 | N |
| M_55_59 | N |
| M_60_64 | N |
| M_65_69 | N |
| M_70_74 | N |
| M_75_79 | N |
| M_80_84 | N |
| M_85_89 | N |
| M_90_94 | N |
| M_95_UP | N |
| K_0_4 | N |
| K_5_9 | N |
| K_10_14 | N |
| K_15_19 | N |
| K_20_24 | N |
| K_25_29 | N |
| K_30_34 | N |
| K_35_39 | N |
| K_40_44 | N |
| K_45_49 | N |
| K_50_54 | N |
| K_55_59 | N |
| K_60_64 | N |
| K_65_69 | N |
| K_70_74 | N |
| K_75_79 | N |
| K_80_84 | N |
| K_85_89 | N |
| K_90_94 | N |
| K_95_UP | N |

#### sdat1_d2024_g2023.dbf

- **Path:** `sdat1_d2024_g2023.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 41

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| M_0_4 | N |
| M_5_9 | N |
| M_10_14 | N |
| M_15_19 | N |
| M_20_24 | N |
| M_25_29 | N |
| M_30_34 | N |
| M_35_39 | N |
| M_40_44 | N |
| M_45_49 | N |
| M_50_54 | N |
| M_55_59 | N |
| M_60_64 | N |
| M_65_69 | N |
| M_70_74 | N |
| M_75_79 | N |
| M_80_84 | N |
| M_85_89 | N |
| M_90_94 | N |
| M_95_UP | N |
| K_0_4 | N |
| K_5_9 | N |
| K_10_14 | N |
| K_15_19 | N |
| K_20_24 | N |
| K_25_29 | N |
| K_30_34 | N |
| K_35_39 | N |
| K_40_44 | N |
| K_45_49 | N |
| K_50_54 | N |
| K_55_59 | N |
| K_60_64 | N |
| K_65_69 | N |
| K_70_74 | N |
| K_75_79 | N |
| K_80_84 | N |
| K_85_89 | N |
| K_90_94 | N |
| K_95_UP | N |

#### sdat1_d2024_g2024.dbf

- **Path:** `sdat1_d2024_g2024.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 41

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| M_0_4 | N |
| M_5_9 | N |
| M_10_14 | N |
| M_15_19 | N |
| M_20_24 | N |
| M_25_29 | N |
| M_30_34 | N |
| M_35_39 | N |
| M_40_44 | N |
| M_45_49 | N |
| M_50_54 | N |
| M_55_59 | N |
| M_60_64 | N |
| M_65_69 | N |
| M_70_74 | N |
| M_75_79 | N |
| M_80_84 | N |
| M_85_89 | N |
| M_90_94 | N |
| M_95_UP | N |
| K_0_4 | N |
| K_5_9 | N |
| K_10_14 | N |
| K_15_19 | N |
| K_20_24 | N |
| K_25_29 | N |
| K_30_34 | N |
| K_35_39 | N |
| K_40_44 | N |
| K_45_49 | N |
| K_50_54 | N |
| K_55_59 | N |
| K_60_64 | N |
| K_65_69 | N |
| K_70_74 | N |
| K_75_79 | N |
| K_80_84 | N |
| K_85_89 | N |
| K_90_94 | N |
| K_95_UP | N |

#### sdat2_data2020_delomr.xlsx

- **Path:** `sdat2_data2020_delomr.xlsx`
- **Type:** XLSX
- **Sheets:** 1

  - **Sheet:** sdat2_data2020_delomr
    - Rows: 1548
    - Columns: 361
    - Column names: Delområde, Mann_AG13_15_1voksen_EnsligUtenBarn, Mann_AG13_15_1voksen_EnsligMedBarn, Mann_AG13_15_1voksen_ParUtenBarn, Mann_AG13_15_1voksen_ParMedBarn, Mann_AG13_15_1voksen_FlereVoksne, Mann_AG13_15_2voksne_EnsligUtenBarn, Mann_AG13_15_2voksne_EnsligMedBarn, Mann_AG13_15_2voksne_ParUtenBarn, Mann_AG13_15_2voksne_ParMedBarn, Mann_AG13_15_2voksne_FlereVoksne, Mann_AG13_15_3plussvoksne_EnsligUtenBarn, Mann_AG13_15_3plussvoksne_EnsligMedBarn, Mann_AG13_15_3plussvoksne_ParUtenBarn, Mann_AG13_15_3plussvoksne_ParMedBarn, Mann_AG13_15_3plussvoksne_FlereVoksne, Mann_AG16_17_1voksen_EnsligUtenBarn, Mann_AG16_17_1voksen_EnsligMedBarn, Mann_AG16_17_1voksen_ParUtenBarn, Mann_AG16_17_1voksen_ParMedBarn, Mann_AG16_17_1voksen_FlereVoksne, Mann_AG16_17_2voksne_EnsligUtenBarn, Mann_AG16_17_2voksne_EnsligMedBarn, Mann_AG16_17_2voksne_ParUtenBarn, Mann_AG16_17_2voksne_ParMedBarn, Mann_AG16_17_2voksne_FlereVoksne, Mann_AG16_17_3plussvoksne_EnsligUtenBarn, Mann_AG16_17_3plussvoksne_EnsligMedBarn, Mann_AG16_17_3plussvoksne_ParUtenBarn, Mann_AG16_17_3plussvoksne_ParMedBarn, Mann_AG16_17_3plussvoksne_FlereVoksne, Mann_AG18_19_1voksen_EnsligUtenBarn, Mann_AG18_19_1voksen_EnsligMedBarn, Mann_AG18_19_1voksen_ParUtenBarn, Mann_AG18_19_1voksen_ParMedBarn, Mann_AG18_19_1voksen_FlereVoksne, Mann_AG18_19_2voksne_EnsligUtenBarn, Mann_AG18_19_2voksne_EnsligMedBarn, Mann_AG18_19_2voksne_ParUtenBarn, Mann_AG18_19_2voksne_ParMedBarn, Mann_AG18_19_2voksne_FlereVoksne, Mann_AG18_19_3plussvoksne_EnsligUtenBarn, Mann_AG18_19_3plussvoksne_EnsligMedBarn, Mann_AG18_19_3plussvoksne_ParUtenBarn, Mann_AG18_19_3plussvoksne_ParMedBarn, Mann_AG18_19_3plussvoksne_FlereVoksne, Mann_AG20_24_1voksen_EnsligUtenBarn, Mann_AG20_24_1voksen_EnsligMedBarn, Mann_AG20_24_1voksen_ParUtenBarn, Mann_AG20_24_1voksen_ParMedBarn, Mann_AG20_24_1voksen_FlereVoksne, Mann_AG20_24_2voksne_EnsligUtenBarn, Mann_AG20_24_2voksne_EnsligMedBarn, Mann_AG20_24_2voksne_ParUtenBarn, Mann_AG20_24_2voksne_ParMedBarn, Mann_AG20_24_2voksne_FlereVoksne, Mann_AG20_24_3plussvoksne_EnsligUtenBarn, Mann_AG20_24_3plussvoksne_EnsligMedBarn, Mann_AG20_24_3plussvoksne_ParUtenBarn, Mann_AG20_24_3plussvoksne_ParMedBarn, Mann_AG20_24_3plussvoksne_FlereVoksne, Mann_AG25_34_1voksen_EnsligUtenBarn, Mann_AG25_34_1voksen_EnsligMedBarn, Mann_AG25_34_1voksen_ParUtenBarn, Mann_AG25_34_1voksen_ParMedBarn, Mann_AG25_34_1voksen_FlereVoksne, Mann_AG25_34_2voksne_EnsligUtenBarn, Mann_AG25_34_2voksne_EnsligMedBarn, Mann_AG25_34_2voksne_ParUtenBarn, Mann_AG25_34_2voksne_ParMedBarn, Mann_AG25_34_2voksne_FlereVoksne, Mann_AG25_34_3plussvoksne_EnsligUtenBarn, Mann_AG25_34_3plussvoksne_EnsligMedBarn, Mann_AG25_34_3plussvoksne_ParUtenBarn, Mann_AG25_34_3plussvoksne_ParMedBarn, Mann_AG25_34_3plussvoksne_FlereVoksne, Mann_AG35_44_1voksen_EnsligUtenBarn, Mann_AG35_44_1voksen_EnsligMedBarn, Mann_AG35_44_1voksen_ParUtenBarn, Mann_AG35_44_1voksen_ParMedBarn, Mann_AG35_44_1voksen_FlereVoksne, Mann_AG35_44_2voksne_EnsligUtenBarn, Mann_AG35_44_2voksne_EnsligMedBarn, Mann_AG35_44_2voksne_ParUtenBarn, Mann_AG35_44_2voksne_ParMedBarn, Mann_AG35_44_2voksne_FlereVoksne, Mann_AG35_44_3plussvoksne_EnsligUtenBarn, Mann_AG35_44_3plussvoksne_EnsligMedBarn, Mann_AG35_44_3plussvoksne_ParUtenBarn, Mann_AG35_44_3plussvoksne_ParMedBarn, Mann_AG35_44_3plussvoksne_FlereVoksne, Mann_AG45_49_1voksen_EnsligUtenBarn, Mann_AG45_49_1voksen_EnsligMedBarn, Mann_AG45_49_1voksen_ParUtenBarn, Mann_AG45_49_1voksen_ParMedBarn, Mann_AG45_49_1voksen_FlereVoksne, Mann_AG45_49_2voksne_EnsligUtenBarn, Mann_AG45_49_2voksne_EnsligMedBarn, Mann_AG45_49_2voksne_ParUtenBarn, Mann_AG45_49_2voksne_ParMedBarn, Mann_AG45_49_2voksne_FlereVoksne, Mann_AG45_49_3plussvoksne_EnsligUtenBarn, Mann_AG45_49_3plussvoksne_EnsligMedBarn, Mann_AG45_49_3plussvoksne_ParUtenBarn, Mann_AG45_49_3plussvoksne_ParMedBarn, Mann_AG45_49_3plussvoksne_FlereVoksne, Mann_AG50_54_1voksen_EnsligUtenBarn, Mann_AG50_54_1voksen_EnsligMedBarn, Mann_AG50_54_1voksen_ParUtenBarn, Mann_AG50_54_1voksen_ParMedBarn, Mann_AG50_54_1voksen_FlereVoksne, Mann_AG50_54_2voksne_EnsligUtenBarn, Mann_AG50_54_2voksne_EnsligMedBarn, Mann_AG50_54_2voksne_ParUtenBarn, Mann_AG50_54_2voksne_ParMedBarn, Mann_AG50_54_2voksne_FlereVoksne, Mann_AG50_54_3plussvoksne_EnsligUtenBarn, Mann_AG50_54_3plussvoksne_EnsligMedBarn, Mann_AG50_54_3plussvoksne_ParUtenBarn, Mann_AG50_54_3plussvoksne_ParMedBarn, Mann_AG50_54_3plussvoksne_FlereVoksne, Mann_AG55_59_1voksen_EnsligUtenBarn, Mann_AG55_59_1voksen_EnsligMedBarn, Mann_AG55_59_1voksen_ParUtenBarn, Mann_AG55_59_1voksen_ParMedBarn, Mann_AG55_59_1voksen_FlereVoksne, Mann_AG55_59_2voksne_EnsligUtenBarn, Mann_AG55_59_2voksne_EnsligMedBarn, Mann_AG55_59_2voksne_ParUtenBarn, Mann_AG55_59_2voksne_ParMedBarn, Mann_AG55_59_2voksne_FlereVoksne, Mann_AG55_59_3plussvoksne_EnsligUtenBarn, Mann_AG55_59_3plussvoksne_EnsligMedBarn, Mann_AG55_59_3plussvoksne_ParUtenBarn, Mann_AG55_59_3plussvoksne_ParMedBarn, Mann_AG55_59_3plussvoksne_FlereVoksne, Mann_AG60_64_1voksen_EnsligUtenBarn, Mann_AG60_64_1voksen_EnsligMedBarn, Mann_AG60_64_1voksen_ParUtenBarn, Mann_AG60_64_1voksen_ParMedBarn, Mann_AG60_64_1voksen_FlereVoksne, Mann_AG60_64_2voksne_EnsligUtenBarn, Mann_AG60_64_2voksne_EnsligMedBarn, Mann_AG60_64_2voksne_ParUtenBarn, Mann_AG60_64_2voksne_ParMedBarn, Mann_AG60_64_2voksne_FlereVoksne, Mann_AG60_64_3plussvoksne_EnsligUtenBarn, Mann_AG60_64_3plussvoksne_EnsligMedBarn, Mann_AG60_64_3plussvoksne_ParUtenBarn, Mann_AG60_64_3plussvoksne_ParMedBarn, Mann_AG60_64_3plussvoksne_FlereVoksne, Mann_AG67_69_1voksen_EnsligUtenBarn, Mann_AG67_69_1voksen_EnsligMedBarn, Mann_AG67_69_1voksen_ParUtenBarn, Mann_AG67_69_1voksen_ParMedBarn, Mann_AG67_69_1voksen_FlereVoksne, Mann_AG67_69_2voksne_EnsligUtenBarn, Mann_AG67_69_2voksne_EnsligMedBarn, Mann_AG67_69_2voksne_ParUtenBarn, Mann_AG67_69_2voksne_ParMedBarn, Mann_AG67_69_2voksne_FlereVoksne, Mann_AG67_69_3plussvoksne_EnsligUtenBarn, Mann_AG67_69_3plussvoksne_EnsligMedBarn, Mann_AG67_69_3plussvoksne_ParUtenBarn, Mann_AG67_69_3plussvoksne_ParMedBarn, Mann_AG67_69_3plussvoksne_FlereVoksne, Mann_AG70_89_1voksen_EnsligUtenBarn, Mann_AG70_89_1voksen_EnsligMedBarn, Mann_AG70_89_1voksen_ParUtenBarn, Mann_AG70_89_1voksen_ParMedBarn, Mann_AG70_89_1voksen_FlereVoksne, Mann_AG70_89_2voksne_EnsligUtenBarn, Mann_AG70_89_2voksne_EnsligMedBarn, Mann_AG70_89_2voksne_ParUtenBarn, Mann_AG70_89_2voksne_ParMedBarn, Mann_AG70_89_2voksne_FlereVoksne, Mann_AG70_89_3plussvoksne_EnsligUtenBarn, Mann_AG70_89_3plussvoksne_EnsligMedBarn, Mann_AG70_89_3plussvoksne_ParUtenBarn, Mann_AG70_89_3plussvoksne_ParMedBarn, Mann_AG70_89_3plussvoksne_FlereVoksne, Kvinne_AG13_15_1voksen_EnsligUtenBarn, Kvinne_AG13_15_1voksen_EnsligMedBarn, Kvinne_AG13_15_1voksen_ParUtenBarn, Kvinne_AG13_15_1voksen_ParMedBarn, Kvinne_AG13_15_1voksen_FlereVoksne, Kvinne_AG13_15_2voksne_EnsligUtenBarn, Kvinne_AG13_15_2voksne_EnsligMedBarn, Kvinne_AG13_15_2voksne_ParUtenBarn, Kvinne_AG13_15_2voksne_ParMedBarn, Kvinne_AG13_15_2voksne_FlereVoksne, Kvinne_AG13_15_3plussvoksne_EnsligUtenBarn, Kvinne_AG13_15_3plussvoksne_EnsligMedBarn, Kvinne_AG13_15_3plussvoksne_ParUtenBarn, Kvinne_AG13_15_3plussvoksne_ParMedBarn, Kvinne_AG13_15_3plussvoksne_FlereVoksne, Kvinne_AG16_17_1voksen_EnsligUtenBarn, Kvinne_AG16_17_1voksen_EnsligMedBarn, Kvinne_AG16_17_1voksen_ParUtenBarn, Kvinne_AG16_17_1voksen_ParMedBarn, Kvinne_AG16_17_1voksen_FlereVoksne, Kvinne_AG16_17_2voksne_EnsligUtenBarn, Kvinne_AG16_17_2voksne_EnsligMedBarn, Kvinne_AG16_17_2voksne_ParUtenBarn, Kvinne_AG16_17_2voksne_ParMedBarn, Kvinne_AG16_17_2voksne_FlereVoksne, Kvinne_AG16_17_3plussvoksne_EnsligUtenBarn, Kvinne_AG16_17_3plussvoksne_EnsligMedBarn, Kvinne_AG16_17_3plussvoksne_ParUtenBarn, Kvinne_AG16_17_3plussvoksne_ParMedBarn, Kvinne_AG16_17_3plussvoksne_FlereVoksne, Kvinne_AG18_19_1voksen_EnsligUtenBarn, Kvinne_AG18_19_1voksen_EnsligMedBarn, Kvinne_AG18_19_1voksen_ParUtenBarn, Kvinne_AG18_19_1voksen_ParMedBarn, Kvinne_AG18_19_1voksen_FlereVoksne, Kvinne_AG18_19_2voksne_EnsligUtenBarn, Kvinne_AG18_19_2voksne_EnsligMedBarn, Kvinne_AG18_19_2voksne_ParUtenBarn, Kvinne_AG18_19_2voksne_ParMedBarn, Kvinne_AG18_19_2voksne_FlereVoksne, Kvinne_AG18_19_3plussvoksne_EnsligUtenBarn, Kvinne_AG18_19_3plussvoksne_EnsligMedBarn, Kvinne_AG18_19_3plussvoksne_ParUtenBarn, Kvinne_AG18_19_3plussvoksne_ParMedBarn, Kvinne_AG18_19_3plussvoksne_FlereVoksne, Kvinne_AG20_24_1voksen_EnsligUtenBarn, Kvinne_AG20_24_1voksen_EnsligMedBarn, Kvinne_AG20_24_1voksen_ParUtenBarn, Kvinne_AG20_24_1voksen_ParMedBarn, Kvinne_AG20_24_1voksen_FlereVoksne, Kvinne_AG20_24_2voksne_EnsligUtenBarn, Kvinne_AG20_24_2voksne_EnsligMedBarn, Kvinne_AG20_24_2voksne_ParUtenBarn, Kvinne_AG20_24_2voksne_ParMedBarn, Kvinne_AG20_24_2voksne_FlereVoksne, Kvinne_AG20_24_3plussvoksne_EnsligUtenBarn, Kvinne_AG20_24_3plussvoksne_EnsligMedBarn, Kvinne_AG20_24_3plussvoksne_ParUtenBarn, Kvinne_AG20_24_3plussvoksne_ParMedBarn, Kvinne_AG20_24_3plussvoksne_FlereVoksne, Kvinne_AG25_34_1voksen_EnsligUtenBarn, Kvinne_AG25_34_1voksen_EnsligMedBarn, Kvinne_AG25_34_1voksen_ParUtenBarn, Kvinne_AG25_34_1voksen_ParMedBarn, Kvinne_AG25_34_1voksen_FlereVoksne, Kvinne_AG25_34_2voksne_EnsligUtenBarn, Kvinne_AG25_34_2voksne_EnsligMedBarn, Kvinne_AG25_34_2voksne_ParUtenBarn, Kvinne_AG25_34_2voksne_ParMedBarn, Kvinne_AG25_34_2voksne_FlereVoksne, Kvinne_AG25_34_3plussvoksne_EnsligUtenBarn, Kvinne_AG25_34_3plussvoksne_EnsligMedBarn, Kvinne_AG25_34_3plussvoksne_ParUtenBarn, Kvinne_AG25_34_3plussvoksne_ParMedBarn, Kvinne_AG25_34_3plussvoksne_FlereVoksne, Kvinne_AG35_44_1voksen_EnsligUtenBarn, Kvinne_AG35_44_1voksen_EnsligMedBarn, Kvinne_AG35_44_1voksen_ParUtenBarn, Kvinne_AG35_44_1voksen_ParMedBarn, Kvinne_AG35_44_1voksen_FlereVoksne, Kvinne_AG35_44_2voksne_EnsligUtenBarn, Kvinne_AG35_44_2voksne_EnsligMedBarn, Kvinne_AG35_44_2voksne_ParUtenBarn, Kvinne_AG35_44_2voksne_ParMedBarn, Kvinne_AG35_44_2voksne_FlereVoksne, Kvinne_AG35_44_3plussvoksne_EnsligUtenBarn, Kvinne_AG35_44_3plussvoksne_EnsligMedBarn, Kvinne_AG35_44_3plussvoksne_ParUtenBarn, Kvinne_AG35_44_3plussvoksne_ParMedBarn, Kvinne_AG35_44_3plussvoksne_FlereVoksne, Kvinne_AG45_49_1voksen_EnsligUtenBarn, Kvinne_AG45_49_1voksen_EnsligMedBarn, Kvinne_AG45_49_1voksen_ParUtenBarn, Kvinne_AG45_49_1voksen_ParMedBarn, Kvinne_AG45_49_1voksen_FlereVoksne, Kvinne_AG45_49_2voksne_EnsligUtenBarn, Kvinne_AG45_49_2voksne_EnsligMedBarn, Kvinne_AG45_49_2voksne_ParUtenBarn, Kvinne_AG45_49_2voksne_ParMedBarn, Kvinne_AG45_49_2voksne_FlereVoksne, Kvinne_AG45_49_3plussvoksne_EnsligUtenBarn, Kvinne_AG45_49_3plussvoksne_EnsligMedBarn, Kvinne_AG45_49_3plussvoksne_ParUtenBarn, Kvinne_AG45_49_3plussvoksne_ParMedBarn, Kvinne_AG45_49_3plussvoksne_FlereVoksne, Kvinne_AG50_54_1voksen_EnsligUtenBarn, Kvinne_AG50_54_1voksen_EnsligMedBarn, Kvinne_AG50_54_1voksen_ParUtenBarn, Kvinne_AG50_54_1voksen_ParMedBarn, Kvinne_AG50_54_1voksen_FlereVoksne, Kvinne_AG50_54_2voksne_EnsligUtenBarn, Kvinne_AG50_54_2voksne_EnsligMedBarn, Kvinne_AG50_54_2voksne_ParUtenBarn, Kvinne_AG50_54_2voksne_ParMedBarn, Kvinne_AG50_54_2voksne_FlereVoksne, Kvinne_AG50_54_3plussvoksne_EnsligUtenBarn, Kvinne_AG50_54_3plussvoksne_EnsligMedBarn, Kvinne_AG50_54_3plussvoksne_ParUtenBarn, Kvinne_AG50_54_3plussvoksne_ParMedBarn, Kvinne_AG50_54_3plussvoksne_FlereVoksne, Kvinne_AG55_59_1voksen_EnsligUtenBarn, Kvinne_AG55_59_1voksen_EnsligMedBarn, Kvinne_AG55_59_1voksen_ParUtenBarn, Kvinne_AG55_59_1voksen_ParMedBarn, Kvinne_AG55_59_1voksen_FlereVoksne, Kvinne_AG55_59_2voksne_EnsligUtenBarn, Kvinne_AG55_59_2voksne_EnsligMedBarn, Kvinne_AG55_59_2voksne_ParUtenBarn, Kvinne_AG55_59_2voksne_ParMedBarn, Kvinne_AG55_59_2voksne_FlereVoksne, Kvinne_AG55_59_3plussvoksne_EnsligUtenBarn, Kvinne_AG55_59_3plussvoksne_EnsligMedBarn, Kvinne_AG55_59_3plussvoksne_ParUtenBarn, Kvinne_AG55_59_3plussvoksne_ParMedBarn, Kvinne_AG55_59_3plussvoksne_FlereVoksne, Kvinne_AG60_64_1voksen_EnsligUtenBarn, Kvinne_AG60_64_1voksen_EnsligMedBarn, Kvinne_AG60_64_1voksen_ParUtenBarn, Kvinne_AG60_64_1voksen_ParMedBarn, Kvinne_AG60_64_1voksen_FlereVoksne, Kvinne_AG60_64_2voksne_EnsligUtenBarn, Kvinne_AG60_64_2voksne_EnsligMedBarn, Kvinne_AG60_64_2voksne_ParUtenBarn, Kvinne_AG60_64_2voksne_ParMedBarn, Kvinne_AG60_64_2voksne_FlereVoksne, Kvinne_AG60_64_3plussvoksne_EnsligUtenBarn, Kvinne_AG60_64_3plussvoksne_EnsligMedBarn, Kvinne_AG60_64_3plussvoksne_ParUtenBarn, Kvinne_AG60_64_3plussvoksne_ParMedBarn, Kvinne_AG60_64_3plussvoksne_FlereVoksne, Kvinne_AG67_69_1voksen_EnsligUtenBarn, Kvinne_AG67_69_1voksen_EnsligMedBarn, Kvinne_AG67_69_1voksen_ParUtenBarn, Kvinne_AG67_69_1voksen_ParMedBarn, Kvinne_AG67_69_1voksen_FlereVoksne, Kvinne_AG67_69_2voksne_EnsligUtenBarn, Kvinne_AG67_69_2voksne_EnsligMedBarn, Kvinne_AG67_69_2voksne_ParUtenBarn, Kvinne_AG67_69_2voksne_ParMedBarn, Kvinne_AG67_69_2voksne_FlereVoksne, Kvinne_AG67_69_3plussvoksne_EnsligUtenBarn, Kvinne_AG67_69_3plussvoksne_EnsligMedBarn, Kvinne_AG67_69_3plussvoksne_ParUtenBarn, Kvinne_AG67_69_3plussvoksne_ParMedBarn, Kvinne_AG67_69_3plussvoksne_FlereVoksne, Kvinne_AG70_89_1voksen_EnsligUtenBarn, Kvinne_AG70_89_1voksen_EnsligMedBarn, Kvinne_AG70_89_1voksen_ParUtenBarn, Kvinne_AG70_89_1voksen_ParMedBarn, Kvinne_AG70_89_1voksen_FlereVoksne, Kvinne_AG70_89_2voksne_EnsligUtenBarn, Kvinne_AG70_89_2voksne_EnsligMedBarn, Kvinne_AG70_89_2voksne_ParUtenBarn, Kvinne_AG70_89_2voksne_ParMedBarn, Kvinne_AG70_89_2voksne_FlereVoksne, Kvinne_AG70_89_3plussvoksne_EnsligUtenBarn, Kvinne_AG70_89_3plussvoksne_EnsligMedBarn, Kvinne_AG70_89_3plussvoksne_ParUtenBarn, Kvinne_AG70_89_3plussvoksne_ParMedBarn, Kvinne_AG70_89_3plussvoksne_FlereVoksne

#### sdat2_data2020_grunnkrets.xlsx

- **Path:** `sdat2_data2020_grunnkrets.xlsx`
- **Type:** XLSX
- **Sheets:** 1

  - **Sheet:** sdat2_data2020_delomr
    - Rows: 17684
    - Columns: 361
    - Column names: grunnkrets, Mann_AG13_15_1voksen_EnsligUtenBarn, Mann_AG13_15_1voksen_EnsligMedBarn, Mann_AG13_15_1voksen_ParUtenBarn, Mann_AG13_15_1voksen_ParMedBarn, Mann_AG13_15_1voksen_FlereVoksne, Mann_AG13_15_2voksne_EnsligUtenBarn, Mann_AG13_15_2voksne_EnsligMedBarn, Mann_AG13_15_2voksne_ParUtenBarn, Mann_AG13_15_2voksne_ParMedBarn, Mann_AG13_15_2voksne_FlereVoksne, Mann_AG13_15_3plussvoksne_EnsligUtenBarn, Mann_AG13_15_3plussvoksne_EnsligMedBarn, Mann_AG13_15_3plussvoksne_ParUtenBarn, Mann_AG13_15_3plussvoksne_ParMedBarn, Mann_AG13_15_3plussvoksne_FlereVoksne, Mann_AG16_17_1voksen_EnsligUtenBarn, Mann_AG16_17_1voksen_EnsligMedBarn, Mann_AG16_17_1voksen_ParUtenBarn, Mann_AG16_17_1voksen_ParMedBarn, Mann_AG16_17_1voksen_FlereVoksne, Mann_AG16_17_2voksne_EnsligUtenBarn, Mann_AG16_17_2voksne_EnsligMedBarn, Mann_AG16_17_2voksne_ParUtenBarn, Mann_AG16_17_2voksne_ParMedBarn, Mann_AG16_17_2voksne_FlereVoksne, Mann_AG16_17_3plussvoksne_EnsligUtenBarn, Mann_AG16_17_3plussvoksne_EnsligMedBarn, Mann_AG16_17_3plussvoksne_ParUtenBarn, Mann_AG16_17_3plussvoksne_ParMedBarn, Mann_AG16_17_3plussvoksne_FlereVoksne, Mann_AG18_19_1voksen_EnsligUtenBarn, Mann_AG18_19_1voksen_EnsligMedBarn, Mann_AG18_19_1voksen_ParUtenBarn, Mann_AG18_19_1voksen_ParMedBarn, Mann_AG18_19_1voksen_FlereVoksne, Mann_AG18_19_2voksne_EnsligUtenBarn, Mann_AG18_19_2voksne_EnsligMedBarn, Mann_AG18_19_2voksne_ParUtenBarn, Mann_AG18_19_2voksne_ParMedBarn, Mann_AG18_19_2voksne_FlereVoksne, Mann_AG18_19_3plussvoksne_EnsligUtenBarn, Mann_AG18_19_3plussvoksne_EnsligMedBarn, Mann_AG18_19_3plussvoksne_ParUtenBarn, Mann_AG18_19_3plussvoksne_ParMedBarn, Mann_AG18_19_3plussvoksne_FlereVoksne, Mann_AG20_24_1voksen_EnsligUtenBarn, Mann_AG20_24_1voksen_EnsligMedBarn, Mann_AG20_24_1voksen_ParUtenBarn, Mann_AG20_24_1voksen_ParMedBarn, Mann_AG20_24_1voksen_FlereVoksne, Mann_AG20_24_2voksne_EnsligUtenBarn, Mann_AG20_24_2voksne_EnsligMedBarn, Mann_AG20_24_2voksne_ParUtenBarn, Mann_AG20_24_2voksne_ParMedBarn, Mann_AG20_24_2voksne_FlereVoksne, Mann_AG20_24_3plussvoksne_EnsligUtenBarn, Mann_AG20_24_3plussvoksne_EnsligMedBarn, Mann_AG20_24_3plussvoksne_ParUtenBarn, Mann_AG20_24_3plussvoksne_ParMedBarn, Mann_AG20_24_3plussvoksne_FlereVoksne, Mann_AG25_34_1voksen_EnsligUtenBarn, Mann_AG25_34_1voksen_EnsligMedBarn, Mann_AG25_34_1voksen_ParUtenBarn, Mann_AG25_34_1voksen_ParMedBarn, Mann_AG25_34_1voksen_FlereVoksne, Mann_AG25_34_2voksne_EnsligUtenBarn, Mann_AG25_34_2voksne_EnsligMedBarn, Mann_AG25_34_2voksne_ParUtenBarn, Mann_AG25_34_2voksne_ParMedBarn, Mann_AG25_34_2voksne_FlereVoksne, Mann_AG25_34_3plussvoksne_EnsligUtenBarn, Mann_AG25_34_3plussvoksne_EnsligMedBarn, Mann_AG25_34_3plussvoksne_ParUtenBarn, Mann_AG25_34_3plussvoksne_ParMedBarn, Mann_AG25_34_3plussvoksne_FlereVoksne, Mann_AG35_44_1voksen_EnsligUtenBarn, Mann_AG35_44_1voksen_EnsligMedBarn, Mann_AG35_44_1voksen_ParUtenBarn, Mann_AG35_44_1voksen_ParMedBarn, Mann_AG35_44_1voksen_FlereVoksne, Mann_AG35_44_2voksne_EnsligUtenBarn, Mann_AG35_44_2voksne_EnsligMedBarn, Mann_AG35_44_2voksne_ParUtenBarn, Mann_AG35_44_2voksne_ParMedBarn, Mann_AG35_44_2voksne_FlereVoksne, Mann_AG35_44_3plussvoksne_EnsligUtenBarn, Mann_AG35_44_3plussvoksne_EnsligMedBarn, Mann_AG35_44_3plussvoksne_ParUtenBarn, Mann_AG35_44_3plussvoksne_ParMedBarn, Mann_AG35_44_3plussvoksne_FlereVoksne, Mann_AG45_49_1voksen_EnsligUtenBarn, Mann_AG45_49_1voksen_EnsligMedBarn, Mann_AG45_49_1voksen_ParUtenBarn, Mann_AG45_49_1voksen_ParMedBarn, Mann_AG45_49_1voksen_FlereVoksne, Mann_AG45_49_2voksne_EnsligUtenBarn, Mann_AG45_49_2voksne_EnsligMedBarn, Mann_AG45_49_2voksne_ParUtenBarn, Mann_AG45_49_2voksne_ParMedBarn, Mann_AG45_49_2voksne_FlereVoksne, Mann_AG45_49_3plussvoksne_EnsligUtenBarn, Mann_AG45_49_3plussvoksne_EnsligMedBarn, Mann_AG45_49_3plussvoksne_ParUtenBarn, Mann_AG45_49_3plussvoksne_ParMedBarn, Mann_AG45_49_3plussvoksne_FlereVoksne, Mann_AG50_54_1voksen_EnsligUtenBarn, Mann_AG50_54_1voksen_EnsligMedBarn, Mann_AG50_54_1voksen_ParUtenBarn, Mann_AG50_54_1voksen_ParMedBarn, Mann_AG50_54_1voksen_FlereVoksne, Mann_AG50_54_2voksne_EnsligUtenBarn, Mann_AG50_54_2voksne_EnsligMedBarn, Mann_AG50_54_2voksne_ParUtenBarn, Mann_AG50_54_2voksne_ParMedBarn, Mann_AG50_54_2voksne_FlereVoksne, Mann_AG50_54_3plussvoksne_EnsligUtenBarn, Mann_AG50_54_3plussvoksne_EnsligMedBarn, Mann_AG50_54_3plussvoksne_ParUtenBarn, Mann_AG50_54_3plussvoksne_ParMedBarn, Mann_AG50_54_3plussvoksne_FlereVoksne, Mann_AG55_59_1voksen_EnsligUtenBarn, Mann_AG55_59_1voksen_EnsligMedBarn, Mann_AG55_59_1voksen_ParUtenBarn, Mann_AG55_59_1voksen_ParMedBarn, Mann_AG55_59_1voksen_FlereVoksne, Mann_AG55_59_2voksne_EnsligUtenBarn, Mann_AG55_59_2voksne_EnsligMedBarn, Mann_AG55_59_2voksne_ParUtenBarn, Mann_AG55_59_2voksne_ParMedBarn, Mann_AG55_59_2voksne_FlereVoksne, Mann_AG55_59_3plussvoksne_EnsligUtenBarn, Mann_AG55_59_3plussvoksne_EnsligMedBarn, Mann_AG55_59_3plussvoksne_ParUtenBarn, Mann_AG55_59_3plussvoksne_ParMedBarn, Mann_AG55_59_3plussvoksne_FlereVoksne, Mann_AG60_64_1voksen_EnsligUtenBarn, Mann_AG60_64_1voksen_EnsligMedBarn, Mann_AG60_64_1voksen_ParUtenBarn, Mann_AG60_64_1voksen_ParMedBarn, Mann_AG60_64_1voksen_FlereVoksne, Mann_AG60_64_2voksne_EnsligUtenBarn, Mann_AG60_64_2voksne_EnsligMedBarn, Mann_AG60_64_2voksne_ParUtenBarn, Mann_AG60_64_2voksne_ParMedBarn, Mann_AG60_64_2voksne_FlereVoksne, Mann_AG60_64_3plussvoksne_EnsligUtenBarn, Mann_AG60_64_3plussvoksne_EnsligMedBarn, Mann_AG60_64_3plussvoksne_ParUtenBarn, Mann_AG60_64_3plussvoksne_ParMedBarn, Mann_AG60_64_3plussvoksne_FlereVoksne, Mann_AG67_69_1voksen_EnsligUtenBarn, Mann_AG67_69_1voksen_EnsligMedBarn, Mann_AG67_69_1voksen_ParUtenBarn, Mann_AG67_69_1voksen_ParMedBarn, Mann_AG67_69_1voksen_FlereVoksne, Mann_AG67_69_2voksne_EnsligUtenBarn, Mann_AG67_69_2voksne_EnsligMedBarn, Mann_AG67_69_2voksne_ParUtenBarn, Mann_AG67_69_2voksne_ParMedBarn, Mann_AG67_69_2voksne_FlereVoksne, Mann_AG67_69_3plussvoksne_EnsligUtenBarn, Mann_AG67_69_3plussvoksne_EnsligMedBarn, Mann_AG67_69_3plussvoksne_ParUtenBarn, Mann_AG67_69_3plussvoksne_ParMedBarn, Mann_AG67_69_3plussvoksne_FlereVoksne, Mann_AG70_89_1voksen_EnsligUtenBarn, Mann_AG70_89_1voksen_EnsligMedBarn, Mann_AG70_89_1voksen_ParUtenBarn, Mann_AG70_89_1voksen_ParMedBarn, Mann_AG70_89_1voksen_FlereVoksne, Mann_AG70_89_2voksne_EnsligUtenBarn, Mann_AG70_89_2voksne_EnsligMedBarn, Mann_AG70_89_2voksne_ParUtenBarn, Mann_AG70_89_2voksne_ParMedBarn, Mann_AG70_89_2voksne_FlereVoksne, Mann_AG70_89_3plussvoksne_EnsligUtenBarn, Mann_AG70_89_3plussvoksne_EnsligMedBarn, Mann_AG70_89_3plussvoksne_ParUtenBarn, Mann_AG70_89_3plussvoksne_ParMedBarn, Mann_AG70_89_3plussvoksne_FlereVoksne, Kvinne_AG13_15_1voksen_EnsligUtenBarn, Kvinne_AG13_15_1voksen_EnsligMedBarn, Kvinne_AG13_15_1voksen_ParUtenBarn, Kvinne_AG13_15_1voksen_ParMedBarn, Kvinne_AG13_15_1voksen_FlereVoksne, Kvinne_AG13_15_2voksne_EnsligUtenBarn, Kvinne_AG13_15_2voksne_EnsligMedBarn, Kvinne_AG13_15_2voksne_ParUtenBarn, Kvinne_AG13_15_2voksne_ParMedBarn, Kvinne_AG13_15_2voksne_FlereVoksne, Kvinne_AG13_15_3plussvoksne_EnsligUtenBarn, Kvinne_AG13_15_3plussvoksne_EnsligMedBarn, Kvinne_AG13_15_3plussvoksne_ParUtenBarn, Kvinne_AG13_15_3plussvoksne_ParMedBarn, Kvinne_AG13_15_3plussvoksne_FlereVoksne, Kvinne_AG16_17_1voksen_EnsligUtenBarn, Kvinne_AG16_17_1voksen_EnsligMedBarn, Kvinne_AG16_17_1voksen_ParUtenBarn, Kvinne_AG16_17_1voksen_ParMedBarn, Kvinne_AG16_17_1voksen_FlereVoksne, Kvinne_AG16_17_2voksne_EnsligUtenBarn, Kvinne_AG16_17_2voksne_EnsligMedBarn, Kvinne_AG16_17_2voksne_ParUtenBarn, Kvinne_AG16_17_2voksne_ParMedBarn, Kvinne_AG16_17_2voksne_FlereVoksne, Kvinne_AG16_17_3plussvoksne_EnsligUtenBarn, Kvinne_AG16_17_3plussvoksne_EnsligMedBarn, Kvinne_AG16_17_3plussvoksne_ParUtenBarn, Kvinne_AG16_17_3plussvoksne_ParMedBarn, Kvinne_AG16_17_3plussvoksne_FlereVoksne, Kvinne_AG18_19_1voksen_EnsligUtenBarn, Kvinne_AG18_19_1voksen_EnsligMedBarn, Kvinne_AG18_19_1voksen_ParUtenBarn, Kvinne_AG18_19_1voksen_ParMedBarn, Kvinne_AG18_19_1voksen_FlereVoksne, Kvinne_AG18_19_2voksne_EnsligUtenBarn, Kvinne_AG18_19_2voksne_EnsligMedBarn, Kvinne_AG18_19_2voksne_ParUtenBarn, Kvinne_AG18_19_2voksne_ParMedBarn, Kvinne_AG18_19_2voksne_FlereVoksne, Kvinne_AG18_19_3plussvoksne_EnsligUtenBarn, Kvinne_AG18_19_3plussvoksne_EnsligMedBarn, Kvinne_AG18_19_3plussvoksne_ParUtenBarn, Kvinne_AG18_19_3plussvoksne_ParMedBarn, Kvinne_AG18_19_3plussvoksne_FlereVoksne, Kvinne_AG20_24_1voksen_EnsligUtenBarn, Kvinne_AG20_24_1voksen_EnsligMedBarn, Kvinne_AG20_24_1voksen_ParUtenBarn, Kvinne_AG20_24_1voksen_ParMedBarn, Kvinne_AG20_24_1voksen_FlereVoksne, Kvinne_AG20_24_2voksne_EnsligUtenBarn, Kvinne_AG20_24_2voksne_EnsligMedBarn, Kvinne_AG20_24_2voksne_ParUtenBarn, Kvinne_AG20_24_2voksne_ParMedBarn, Kvinne_AG20_24_2voksne_FlereVoksne, Kvinne_AG20_24_3plussvoksne_EnsligUtenBarn, Kvinne_AG20_24_3plussvoksne_EnsligMedBarn, Kvinne_AG20_24_3plussvoksne_ParUtenBarn, Kvinne_AG20_24_3plussvoksne_ParMedBarn, Kvinne_AG20_24_3plussvoksne_FlereVoksne, Kvinne_AG25_34_1voksen_EnsligUtenBarn, Kvinne_AG25_34_1voksen_EnsligMedBarn, Kvinne_AG25_34_1voksen_ParUtenBarn, Kvinne_AG25_34_1voksen_ParMedBarn, Kvinne_AG25_34_1voksen_FlereVoksne, Kvinne_AG25_34_2voksne_EnsligUtenBarn, Kvinne_AG25_34_2voksne_EnsligMedBarn, Kvinne_AG25_34_2voksne_ParUtenBarn, Kvinne_AG25_34_2voksne_ParMedBarn, Kvinne_AG25_34_2voksne_FlereVoksne, Kvinne_AG25_34_3plussvoksne_EnsligUtenBarn, Kvinne_AG25_34_3plussvoksne_EnsligMedBarn, Kvinne_AG25_34_3plussvoksne_ParUtenBarn, Kvinne_AG25_34_3plussvoksne_ParMedBarn, Kvinne_AG25_34_3plussvoksne_FlereVoksne, Kvinne_AG35_44_1voksen_EnsligUtenBarn, Kvinne_AG35_44_1voksen_EnsligMedBarn, Kvinne_AG35_44_1voksen_ParUtenBarn, Kvinne_AG35_44_1voksen_ParMedBarn, Kvinne_AG35_44_1voksen_FlereVoksne, Kvinne_AG35_44_2voksne_EnsligUtenBarn, Kvinne_AG35_44_2voksne_EnsligMedBarn, Kvinne_AG35_44_2voksne_ParUtenBarn, Kvinne_AG35_44_2voksne_ParMedBarn, Kvinne_AG35_44_2voksne_FlereVoksne, Kvinne_AG35_44_3plussvoksne_EnsligUtenBarn, Kvinne_AG35_44_3plussvoksne_EnsligMedBarn, Kvinne_AG35_44_3plussvoksne_ParUtenBarn, Kvinne_AG35_44_3plussvoksne_ParMedBarn, Kvinne_AG35_44_3plussvoksne_FlereVoksne, Kvinne_AG45_49_1voksen_EnsligUtenBarn, Kvinne_AG45_49_1voksen_EnsligMedBarn, Kvinne_AG45_49_1voksen_ParUtenBarn, Kvinne_AG45_49_1voksen_ParMedBarn, Kvinne_AG45_49_1voksen_FlereVoksne, Kvinne_AG45_49_2voksne_EnsligUtenBarn, Kvinne_AG45_49_2voksne_EnsligMedBarn, Kvinne_AG45_49_2voksne_ParUtenBarn, Kvinne_AG45_49_2voksne_ParMedBarn, Kvinne_AG45_49_2voksne_FlereVoksne, Kvinne_AG45_49_3plussvoksne_EnsligUtenBarn, Kvinne_AG45_49_3plussvoksne_EnsligMedBarn, Kvinne_AG45_49_3plussvoksne_ParUtenBarn, Kvinne_AG45_49_3plussvoksne_ParMedBarn, Kvinne_AG45_49_3plussvoksne_FlereVoksne, Kvinne_AG50_54_1voksen_EnsligUtenBarn, Kvinne_AG50_54_1voksen_EnsligMedBarn, Kvinne_AG50_54_1voksen_ParUtenBarn, Kvinne_AG50_54_1voksen_ParMedBarn, Kvinne_AG50_54_1voksen_FlereVoksne, Kvinne_AG50_54_2voksne_EnsligUtenBarn, Kvinne_AG50_54_2voksne_EnsligMedBarn, Kvinne_AG50_54_2voksne_ParUtenBarn, Kvinne_AG50_54_2voksne_ParMedBarn, Kvinne_AG50_54_2voksne_FlereVoksne, Kvinne_AG50_54_3plussvoksne_EnsligUtenBarn, Kvinne_AG50_54_3plussvoksne_EnsligMedBarn, Kvinne_AG50_54_3plussvoksne_ParUtenBarn, Kvinne_AG50_54_3plussvoksne_ParMedBarn, Kvinne_AG50_54_3plussvoksne_FlereVoksne, Kvinne_AG55_59_1voksen_EnsligUtenBarn, Kvinne_AG55_59_1voksen_EnsligMedBarn, Kvinne_AG55_59_1voksen_ParUtenBarn, Kvinne_AG55_59_1voksen_ParMedBarn, Kvinne_AG55_59_1voksen_FlereVoksne, Kvinne_AG55_59_2voksne_EnsligUtenBarn, Kvinne_AG55_59_2voksne_EnsligMedBarn, Kvinne_AG55_59_2voksne_ParUtenBarn, Kvinne_AG55_59_2voksne_ParMedBarn, Kvinne_AG55_59_2voksne_FlereVoksne, Kvinne_AG55_59_3plussvoksne_EnsligUtenBarn, Kvinne_AG55_59_3plussvoksne_EnsligMedBarn, Kvinne_AG55_59_3plussvoksne_ParUtenBarn, Kvinne_AG55_59_3plussvoksne_ParMedBarn, Kvinne_AG55_59_3plussvoksne_FlereVoksne, Kvinne_AG60_64_1voksen_EnsligUtenBarn, Kvinne_AG60_64_1voksen_EnsligMedBarn, Kvinne_AG60_64_1voksen_ParUtenBarn, Kvinne_AG60_64_1voksen_ParMedBarn, Kvinne_AG60_64_1voksen_FlereVoksne, Kvinne_AG60_64_2voksne_EnsligUtenBarn, Kvinne_AG60_64_2voksne_EnsligMedBarn, Kvinne_AG60_64_2voksne_ParUtenBarn, Kvinne_AG60_64_2voksne_ParMedBarn, Kvinne_AG60_64_2voksne_FlereVoksne, Kvinne_AG60_64_3plussvoksne_EnsligUtenBarn, Kvinne_AG60_64_3plussvoksne_EnsligMedBarn, Kvinne_AG60_64_3plussvoksne_ParUtenBarn, Kvinne_AG60_64_3plussvoksne_ParMedBarn, Kvinne_AG60_64_3plussvoksne_FlereVoksne, Kvinne_AG67_69_1voksen_EnsligUtenBarn, Kvinne_AG67_69_1voksen_EnsligMedBarn, Kvinne_AG67_69_1voksen_ParUtenBarn, Kvinne_AG67_69_1voksen_ParMedBarn, Kvinne_AG67_69_1voksen_FlereVoksne, Kvinne_AG67_69_2voksne_EnsligUtenBarn, Kvinne_AG67_69_2voksne_EnsligMedBarn, Kvinne_AG67_69_2voksne_ParUtenBarn, Kvinne_AG67_69_2voksne_ParMedBarn, Kvinne_AG67_69_2voksne_FlereVoksne, Kvinne_AG67_69_3plussvoksne_EnsligUtenBarn, Kvinne_AG67_69_3plussvoksne_EnsligMedBarn, Kvinne_AG67_69_3plussvoksne_ParUtenBarn, Kvinne_AG67_69_3plussvoksne_ParMedBarn, Kvinne_AG67_69_3plussvoksne_FlereVoksne, Kvinne_AG70_89_1voksen_EnsligUtenBarn, Kvinne_AG70_89_1voksen_EnsligMedBarn, Kvinne_AG70_89_1voksen_ParUtenBarn, Kvinne_AG70_89_1voksen_ParMedBarn, Kvinne_AG70_89_1voksen_FlereVoksne, Kvinne_AG70_89_2voksne_EnsligUtenBarn, Kvinne_AG70_89_2voksne_EnsligMedBarn, Kvinne_AG70_89_2voksne_ParUtenBarn, Kvinne_AG70_89_2voksne_ParMedBarn, Kvinne_AG70_89_2voksne_FlereVoksne, Kvinne_AG70_89_3plussvoksne_EnsligUtenBarn, Kvinne_AG70_89_3plussvoksne_EnsligMedBarn, Kvinne_AG70_89_3plussvoksne_ParUtenBarn, Kvinne_AG70_89_3plussvoksne_ParMedBarn, Kvinne_AG70_89_3plussvoksne_FlereVoksne

#### sdat3_d2023x_g2020.dbf

- **Path:** `sdat3_d2023x_g2020.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 18

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| SYBLU | N |
| SYBMU | N |
| SYBHU | N |
| SYB | N |
| SYALU | N |
| SYAMU | N |
| SYAHU | N |
| SYA1524 | N |
| SYA2534 | N |
| SYA3554 | N |
| SYA5566 | N |
| SYA67UP | N |
| SYAM | N |
| SYAK | N |
| SYA | N |
| INNT_IDX | N |
| BRINNT17UP | N |

#### sdat3_d2023x_g2021.dbf

- **Path:** `sdat3_d2023x_g2021.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 18

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| SYBLU | N |
| SYBMU | N |
| SYBHU | N |
| SYB | N |
| SYALU | N |
| SYAMU | N |
| SYAHU | N |
| SYA1524 | N |
| SYA2534 | N |
| SYA3554 | N |
| SYA5566 | N |
| SYA67UP | N |
| SYAM | N |
| SYAK | N |
| SYA | N |
| INNT_IDX | N |
| BRINNT17UP | N |

#### sdat3_d2023x_g2023.dbf

- **Path:** `sdat3_d2023x_g2023.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 18

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| SYBLU | N |
| SYBMU | N |
| SYBHU | N |
| SYB | N |
| SYALU | N |
| SYAMU | N |
| SYAHU | N |
| SYA1524 | N |
| SYA2534 | N |
| SYA3554 | N |
| SYA5566 | N |
| SYA67UP | N |
| SYAM | N |
| SYAK | N |
| SYA | N |
| INNT_IDX | N |
| BRINNT17UP | N |

#### sdat3_d2023x_g2024.dbf

- **Path:** `sdat3_d2023x_g2024.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 18

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| SYBLU | N |
| SYBMU | N |
| SYBHU | N |
| SYB | N |
| SYALU | N |
| SYAMU | N |
| SYAHU | N |
| SYA1524 | N |
| SYA2534 | N |
| SYA3554 | N |
| SYA5566 | N |
| SYA67UP | N |
| SYAM | N |
| SYAK | N |
| SYA | N |
| INNT_IDX | N |
| BRINNT17UP | N |

#### sdat4_d2024_g2020.dbf

- **Path:** `sdat4_d2024_g2020.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 24

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| A10PRI | N |
| A20SEK | N |
| A21SEK | N |
| A30VH | N |
| A31VH | N |
| A32VH | N |
| A33VH | N |
| A34VH | N |
| A40TJE | N |
| A41TJE | N |
| A42TJE | N |
| A43TJE | N |
| A50OFF | N |
| A60UND | N |
| A61UND | N |
| A62UND | N |
| A63UND | N |
| A70HSOS | N |
| A71HSOS | N |
| A72HSOS | N |
| A73HSOS | N |
| MALINT | N |
| FEMINT | N |

#### sdat4_d2024_g2021.dbf

- **Path:** `sdat4_d2024_g2021.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 24

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| A10PRI | N |
| A20SEK | N |
| A21SEK | N |
| A30VH | N |
| A31VH | N |
| A32VH | N |
| A33VH | N |
| A34VH | N |
| A40TJE | N |
| A41TJE | N |
| A42TJE | N |
| A43TJE | N |
| A50OFF | N |
| A60UND | N |
| A61UND | N |
| A62UND | N |
| A63UND | N |
| A70HSOS | N |
| A71HSOS | N |
| A72HSOS | N |
| A73HSOS | N |
| MALINT | N |
| FEMINT | N |

#### sdat4_d2024_g2023.dbf

- **Path:** `sdat4_d2024_g2023.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 24

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| A10PRI | N |
| A20SEK | N |
| A21SEK | N |
| A30VH | N |
| A31VH | N |
| A32VH | N |
| A33VH | N |
| A34VH | N |
| A40TJE | N |
| A41TJE | N |
| A42TJE | N |
| A43TJE | N |
| A50OFF | N |
| A60UND | N |
| A61UND | N |
| A62UND | N |
| A63UND | N |
| A70HSOS | N |
| A71HSOS | N |
| A72HSOS | N |
| A73HSOS | N |
| MALINT | N |
| FEMINT | N |

#### sdat4_d2024_g2024.dbf

- **Path:** `sdat4_d2024_g2024.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 24

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| A10PRI | N |
| A20SEK | N |
| A21SEK | N |
| A30VH | N |
| A31VH | N |
| A32VH | N |
| A33VH | N |
| A34VH | N |
| A40TJE | N |
| A41TJE | N |
| A42TJE | N |
| A43TJE | N |
| A50OFF | N |
| A60UND | N |
| A61UND | N |
| A62UND | N |
| A63UND | N |
| A70HSOS | N |
| A71HSOS | N |
| A72HSOS | N |
| A73HSOS | N |
| MALINT | N |
| FEMINT | N |

#### sdat5_d2023_g2020.dbf

- **Path:** `sdat5_d2023_g2020.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 5

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| SBARNESK | N |
| SUNGDSK | N |
| SVGSKOLE | N |
| SHOGUNI | N |

#### sdat5_d2023_g2021.dbf

- **Path:** `sdat5_d2023_g2021.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 5

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| SBARNESK | N |
| SUNGDSK | N |
| SVGSKOLE | N |
| SHOGUNI | N |

#### sdat5_d2023_g2023.dbf

- **Path:** `sdat5_d2023_g2023.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 5

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| SBARNESK | N |
| SUNGDSK | N |
| SVGSKOLE | N |
| SHOGUNI | N |

#### sdat5_d2023_g2024.dbf

- **Path:** `sdat5_d2023_g2024.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 5

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| SBARNESK | N |
| SUNGDSK | N |
| SVGSKOLE | N |
| SHOGUNI | N |

#### sdat71_NB2023_grk2020_2020.dbf

- **Path:** `sdat71_NB2023_grk2020_2020.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 4

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| ELBIL | N |
| HYBRID | N |
| FOSSIL | N |

#### sdat7_d20xx_g2020_ikke_pkost.dbf

- **Path:** `sdat7_d20xx_g2020_ikke_pkost.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 6

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| KPARK | N |
| LPARK | N |
| PKORT_ARB | N |
| IKKEPBOLIG | N |
| ANDEL_EL | N |

#### sdat7_d20xx_g2021_ikke_pkost.dbf

- **Path:** `sdat7_d20xx_g2021_ikke_pkost.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 6

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| KPARK | N |
| LPARK | N |
| PKORT_ARB | N |
| IKKEPBOLIG | N |
| ANDEL_EL | N |

#### sdat7_d20xx_g2023_ikke_pkost.dbf

- **Path:** `sdat7_d20xx_g2023_ikke_pkost.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 6

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| KPARK | N |
| LPARK | N |
| PKORT_ARB | N |
| IKKEPBOLIG | N |
| ANDEL_EL | N |

#### sdat7_d20xx_g2024_ikke_pkost.dbf

- **Path:** `sdat7_d20xx_g2024_ikke_pkost.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 6

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| KPARK | N |
| LPARK | N |
| PKORT_ARB | N |
| IKKEPBOLIG | N |
| ANDEL_EL | N |

#### sdat8_d2024_g2020.dbf

- **Path:** `sdat8_d2024_g2020.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 8

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| AGGREGAT | N |
| TILFSTUD1 | N |
| TILFSTUD2 | N |
| HOTELLER | N |
| HYTTER | N |
| BOSTUD | N |
| BOINST | N |

#### sdat8_d2024_g2021.dbf

- **Path:** `sdat8_d2024_g2021.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 8

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| AGGREGAT | N |
| TILFSTUD1 | N |
| TILFSTUD2 | N |
| HOTELLER | N |
| HYTTER | N |
| BOSTUD | N |
| BOINST | N |

#### sdat8_d2024_g2023.dbf

- **Path:** `sdat8_d2024_g2023.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 8

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| AGGREGAT | N |
| TILFSTUD1 | N |
| TILFSTUD2 | N |
| HOTELLER | N |
| HYTTER | N |
| BOSTUD | N |
| BOINST | N |

#### sdat8_d2024_g2024.dbf

- **Path:** `sdat8_d2024_g2024.dbf`
- **Type:** DBF
- **Rows:** 14101
- **Columns:** 8

**Column details:**

| Column | Type |
|--------|------|
| GRUNNKRETS | N |
| AGGREGAT | N |
| TILFSTUD1 | N |
| TILFSTUD2 | N |
| HOTELLER | N |
| HYTTER | N |
| BOSTUD | N |
| BOINST | N |

#### sdat_6_areal_g2020.dbf

- **Path:** `sdat_6_areal_g2020.dbf`
- **Type:** DBF
- **Rows:** 14097
- **Columns:** 20

**Column details:**

| Column | Type |
|--------|------|
| Grunnkrets | N |
| Areal_1 | N |
| Areal_2 | N |
| Areal_3 | N |
| Areal_4 | N |
| Areal_5 | N |
| Areal_6 | N |
| Areal_7 | N |
| Areal_8 | N |
| Areal_9 | N |
| Areal_B1 | N |
| Areal_B2 | N |
| Areal_B3 | N |
| Areal_B4 | N |
| Areal_B5 | N |
| Areal_B6 | N |
| Areal_B7 | N |
| Areal_B8 | N |
| Areal_B9 | N |
| Areal_Tot | N |

