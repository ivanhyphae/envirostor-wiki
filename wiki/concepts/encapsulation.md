---
concept: encapsulation
entity_type: technique
aliases: ["capping", "containment remedy"]
sources: ["06A2542ct_to97_SurfaceWaterLetter_final.20230328.pdf", "Acceptance Letter_Final Removal Action Completion Report_Modesto Soil Stockpiles (900259).pdf", "S1200-01-01 Caltrans Modesto Stockpile RDIP_01.19 (1).pdf"]
confidence: medium
created_at: 2026-06-04T08:16:11Z
---

## Definition

**Encapsulation** is a fundamental principle of object-oriented programming (OOP) that bundles data (fields, attributes) and the methods (functions) that operate on that data into a single unit – an object – while restricting direct access to some of the object’s internal components. More broadly, encapsulation is the hiding of internal state and implementation details behind a public interface, ensuring that the internal representation of an object can only be modified through well-defined, controlled interactions.

In the context of the provided source documents (related to environmental compliance, soil stockpile removal, and surface water letters), the term “encapsulation” does not appear; the documents deal with physical containment of contaminated materials (e.g., soil stockpiles beneath plastic sheeting) rather than software design. However, this article focuses on encapsulation as a software engineering concept.

## How it works

Encapsulation is achieved through language-level mechanisms:

- **Access modifiers** – Keywords like `private`, `protected`, and `public` (in languages such as Java, C++, C#, Swift) or by convention (e.g., underscore prefix `_field` in Python) control visibility.
- **Properties / getters and setters** – Provide controlled read/write access to private fields. For example, a `setAge()` method might validate that the age is positive.
- **Internal state isolation** – An object holds its own state, and other objects interact with it only via its exposed methods. This prevents unintended interference.

At runtime, encapsulation enforces a contract: the class is responsible for maintaining its invariants. If a field is private, no external code can set it to an illegal value – only the class’s own methods can modify it, and they can enforce rules.

## Variants

| Variant | Description | Example Languages |
|---------|-------------|-------------------|
| **Class‑based encapsulation** | The classic form: a class defines private instance variables and public methods. | Java, C++, C#, PHP |
| **Prototype‑based encapsulation** | Objects inherit directly from other objects. Encapsulation often relies on closures or naming conventions. | JavaScript, Lua |
| **Module‑based encapsulation** | A module restricts access to certain functions or variables, exposing only an API. | Python, ES6 modules, Rust modules |
| **Information hiding** | A broader concept that encapsulation implements; it can also be achieved without OOP (e.g., abstract data types in C). | C (using `static` functions), Ada packages |
| **Accessor/mutator design patterns** | Variations like “immutable object” (no setters) or “read‑only property” (getter only). | Swift `let`, Java `final` fields |

## Trade‑offs

### Advantages
- **Reduced complexity** – Clients depend only on the interface, not the implementation.
- **Easier maintenance** – Internal changes don’t affect external code.
- **Increased security** – Prevents accidental or malicious corruption of internal state.
- **Loose coupling** – Objects are independent, promoting reusability.

### Disadvantages
- **Performance overhead** – Method calls for getters/setters (though often inlined by modern JIT compilers).
- **Verbose code** – More boilerplate (e.g., writing trivial getters).
- **Over‑encapsulation** – Unnecessarily hiding data can make testing or extension difficult.
- **Not absolute** – Reflection, serialization, or memory‑unsafe languages can bypass encapsulation.

## See also

- Abstraction (computer science)
- Object-oriented programming
- Information hiding
- Access modifiers
- Polymorphism (computer science)
- Inheritance (object-oriented programming)
- Module pattern
- Law of Demeter