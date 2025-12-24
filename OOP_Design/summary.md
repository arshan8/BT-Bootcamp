# Q1

### HAS-A Relationships (Composition)

**Course HAS Modules:**  
Composition is used because modules are an integral part of a course.

**Module HAS Units:**  
Composition is used since units cannot exist without a module.

**Unit HAS Topics:**  
Composition is used because topics belong to and depend on a unit.

### No IS-A Relationship (Inheritance)

**IS-A not used:**  
No inheritance is applied because no entity is a specialized form of another.



--- 


# Q2

### Identified Classes

Company – sells items

Customer – places orders

RegisteredCustomer – special type of customer eligible for discounts

Order – represents a purchase made by a customer

Item – products sold by the company

Discount – special offers given to registered customer

### Relationships Used
**Association**

Company – Item:
A company sells different items.

Customer – Order:
A customer places orders.

RegisteredCustomer – Discount:
Registered customers receive special discounts.

**HAS-A Relationship** (Composition)

Order HAS Items:
An order contains multiple items, which form part of the order.

**IS-A Relationship (Inheritance)**

RegisteredCustomer IS-A Customer:
RegisteredCustomer is a specialized form of Customer with additional benefits.



### Design Decisions

Inheritance is used to represent registered customers because they have distinct behavior (discount eligibility).

Association is used where entities interact but do not own each other.

HAS-A (composition) is used for Order–Item to represent a part–whole relationship.

No unnecessary relationships are added, keeping the design simple and loosely coupled.


---

# Q3

## OO Model (Design)
Identified Classes

ExamPortal

Question (base class)

MCQQuestion (Multiple Choice)

ParagraphQuestion

Category

Topic

## Relationships Used
*** IS-A *** (Inheritance)

MCQQuestion IS-A Question

ParagraphQuestion IS-A Question

(Question can be of different types)

***HAS-A**

ExamPortal HAS Questions

Question HAS Category

Question HAS Topic