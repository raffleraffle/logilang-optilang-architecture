# OptiLang Specification

OptiLang is a semantic intermediate representation derived from LogiLang.

## Purpose
- Normalize meaning
- Enable reasoning
- Support agents and tools

## Core Fields

- c    : canonical frame id
- s    : subject / agent
- v    : predicate (lemma)
- o    : object / content
- tm   : time
- mod  : modality
- conf : confidence (0.0–1.0)
- src  : reference to LogiLang event

## Rules
- Always reference source LogiLang event
- Multiple OptiLang frames may derive from one event
- Frames are versioned, never overwritten
