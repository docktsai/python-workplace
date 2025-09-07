# Scan Config Check flow diagram
``` mermaid
flowchart TD
    A(["Start"]) --> B{"Is Cloud Managed KMS key?"}
    B -- Yes --> T(["OK to scan."])
    B -- No --> C@{ label: "Is 'Wiz-Scan-Access' in tags with value 'Enabled'?" }
    C -- Yes --> G1{"Is Redshift DB and WizOrchistrator role not in policy?"}
    C -- No --> D@{ label: "Remediate KMS tags to add 'Wiz-San-Access' with 'Enablded'" }
    D --> G1
    G1 -- No --> G3{"Is root role in policy without condition?"}
    G1 -- Yes --> G2[["add WizOrchistrator role to KMS policy"]]
    G2 --> G3
    G3 -- Yes --> T
    G3 -- No --> G4{"Is WizAccess and WizScanner role in policy?"}
    G4 -- Yes --> T
    G4 -- No --> G5[["Add WizAccess and WizScanner role to KMS policy"]]
    G5 --> T
    C@{ shape: diamond}
    D@{ shape: subroutine}
