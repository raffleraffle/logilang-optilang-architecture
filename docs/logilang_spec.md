# LogiLang Specification

LogiLang is an append-only event language.

## Principles
- Verbatim preservation
- No semantic inference
- Immutable records

## Canonical Fields

- e    : event id
- a    : actor
- act  : action (usually "utter")
- payload : exact text
- t    : timestamp (ISO8601 UTC)
- chan : user | assistant | system
- hash : sha256(payload + metadata)
- meta : optional metadata

## Guarantees
- Payload is never modified
- Events are never deleted
- Reinterpretation happens downstream
