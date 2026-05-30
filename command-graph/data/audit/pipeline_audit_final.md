# Command Graph Pipeline Audit Report — Final

## Pipeline Summary

| Step | Description | Output | Quality | Iterations |
|------|-------------|--------|---------|------------|
| Step 1 | Directory scan → command inventory | 4580 files, 4577 commands | HIGH | 3 |
| Step 2 | Document parsing → command metadata | 4580 commands, 99.9% section coverage | HIGH | 3 |
| Step 3 | Parameter extraction → params + enums | 14941 params, 7930 enums | HIGH | 3 |
| Step 4 | Config object discovery | 2267 objects, 4577 group records | HIGH | 2 |
| Step 5 | LLM semantic relationship extraction | ~6500+ relationships (in progress) | MEDIUM | 1 (ongoing) |
| Step 6 | LLM review of relationships | Pending | - | - |
| Step 7 | Final merge + schema | Pending | - | - |

## Step 1 Quality (HIGH)

- 4580 files scanned from UDG MML command directory
- 4577 unique command names extracted (99.9%)
- 3 special files correctly identified (目录, MML命令声明)
- Classification paths accurately reflect directory structure
- **Fix applied**: Half-width `()` parentheses support added

## Step 2 Quality (HIGH)

- 99.9% section coverage across all commands
- Verified against 5 random source documents — all sections match
- Minor issues: image markdown in description field, multi-paragraph truncation
- These are cosmetic and don't affect downstream processing

## Step 3 Quality (HIGH — improved from MEDIUM)

### Iteration 1 → 2: Fixed markdown artifacts
- Removed 133 parameters with `**参数标识**` table header artifacts
- Added `strip("*")` check for bold markdown in header rows

### Iteration 2 → 3: Fixed value_type classification
- `other` reduced from 43.4% → 2.4%
- Added full-width wave dash `～` support for integer ranges
- Added boolean pattern `TRUE或FALSE` detection
- Added hex range detection
- Added NA stripping for not_applicable type

### Final stats:
- **14941 parameters** (133 artifacts removed)
- **7930 enum values**
- Value type distribution:
  - integer_range: 8819 (59.0%)
  - enum: 4003 (26.8%)
  - ip_address: 1039 (7.0%)
  - boolean: 392 (2.6%)
  - other: 365 (2.4%)
  - string: 314 (2.1%)
  - unknown: 9 (0.1%)
- Subfield extraction: meaning 100%, value_range 99.9%, default_value 99.9%, config_principle 72.2%

## Step 4 Quality (HIGH)

- 2267 config objects discovered
- 4577 command group records (100% command coverage)
- 392 objects with full CRUD
- Verified 3 random objects — all correct

## Step 5 Quality (MEDIUM — in progress)

- Processing 4577 commands via DeepSeek LLM
- ~6500+ relationships extracted so far
- 0 empty evidence_text (100% have source evidence)
- Type distribution: param_condition (largest) > effect_timing > cmd_reference > cmd_prerequisite
- LST/DSP commands correctly return 0 relationships

### Known issues:
- effect_timing relationships sometimes have empty `to` field (expected — timing is about the command itself)
- Some relationships may have inaccurate types (to be verified in Step 6 review)

## Recommendations

1. **Step 5**: Continue extraction, then run Step 6 LLM review
2. **Step 6**: Focus review on evidence_text accuracy and type correctness
3. **Step 7**: Generate schema from actual data statistics
