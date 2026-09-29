# 🚚 GreenTech Logistics System

A Python console-based shipment order management system developed for the **GreenTech Logistics** scenario.

The application demonstrates practical use of **Stacks, Queues, recursion, searching, priority-based order processing, and route selection** to manage urgent and standard shipment orders.

---

## 🖥️ Application Preview

<table>
  <tr>
    <td width="55%">
      <img width="100%" alt="GreenTech Logistics welcome screen" src="https://github.com/user-attachments/assets/c31eaf56-3ae0-4a56-a112-e4679dc31f43" />
    </td>
    <td width="45%">
      <img width="100%" alt="GreenTech Logistics login screen" src="https://github.com/user-attachments/assets/ec5ef443-6558-4d23-965c-c50168316588" />
    </td>
  </tr>
</table>

<p align="center">
  <img width="65%" alt="GreenTech Logistics main menu" src="https://github.com/user-attachments/assets/18e26db7-a989-40d5-9e45-12390b5ff5af" />
</p>

---

## 📌 Overview

GreenTech Logistics handles eco-friendly shipment distribution with different levels of order priority.

The system separates shipments into:

- **Urgent Orders (U)** — handled using **LIFO**
- **Standard Orders (S)** — handled using **FIFO**

The application provides a menu-driven console interface where an administrator can create and manage shipment orders, search existing orders, view order summaries, process urgent shipments through a fast-track workflow, and perform route optimisation.

---

## ✨ Key Features

### Urgent Order Management

Urgent shipments are stored using a **Stack** and processed using the **Last-In, First-Out (LIFO)** principle.

The administrator can:

- Add urgent orders
- View the latest order
- Remove the latest order
- View all urgent orders
- Count current orders
- Search by order ID

Urgent orders are automatically identified using a `U` prefix.

---

### Standard Order Management

Standard shipments use a **Queue** and follow the **First-In, First-Out (FIFO)** principle.

The administrator can:

- Add standard orders
- View the first order received
- Remove the first order
- View all standard orders
- Count current orders
- Search by order ID

Standard orders are automatically identified using an `S` prefix.

---

### Dashboard

The dashboard provides a quick overview of the current system state.

It includes:

- Urgent order count
- Standard order count
- Ready-dispatch order count
- Total active orders
- Search across urgent and standard orders
- Combined order viewing

---

### ⚡ Fast Track Delivery Line

Urgent shipments can be moved through a dedicated fast-track process.

The selected urgent order passes through four recursive stages:

```text
Urgent Order Received
        ↓
Eco Package Checked
        ↓
Priority Delivery Label Added
        ↓
Fast Track Completed
        ↓
Ready for Dispatch
```

The implementation uses a **recursive Python function**, with each stage calling the next stage until the shipment is ready for dispatch.

---

### 🗺️ Shipment Route Optimisation

After an urgent order completes fast-track processing, it is moved to the ready-dispatch list.

The system compares predefined routes using delivery time and distance.

For urgent shipments, delivery time is prioritised so the system selects the route with the **fastest available delivery time**.

Example routes used by the application:

| Route | Distance | Time |
|---|---:|---:|
| Route A | 12 km | 25 minutes |
| Route B | 8 km | 35 minutes |
| Route C | 15 km | 20 minutes |

For an urgent shipment, **Route C** is selected because it has the lowest delivery time.

---

## 🧠 Data Structures & Algorithms

The project was created to demonstrate how data structures and algorithms can be applied to a practical logistics scenario.

| Concept | Implementation |
|---|---|
| Stack | Urgent shipment orders |
| Queue | Standard shipment orders |
| LIFO | Latest urgent order processed first |
| FIFO | Earliest standard order processed first |
| Recursion | Fast Track Delivery Line |
| Linear Search | Searching shipment orders |
| Lists | Order storage |
| Conditional Logic | Menu navigation and route selection |

### Stack Operations

Urgent orders use Python list operations such as:

```python
urgent_stack.append(order)
urgent_stack[-1]
urgent_stack.pop()
```

This provides the required LIFO behaviour.

### Queue Operations

Standard orders use:

```python
standard_queue.insert(0, order)
standard_queue[-1]
standard_queue.pop()
```

This maintains FIFO processing for standard shipments.

---

## 🔑 Demo Login

The application includes demonstration administrator accounts.

```text
Username: admin
Password: 123
```

Alternative demo accounts included in the project:

```text
Username: greentech
Password: 2026

Username: madzoo
Password: 0000
```

> These credentials are included only for demonstrating the academic console application and are not intended as production authentication.

---

## ⚙️ Technologies Used

- **Python 3**
- Python Lists
- Stack and Queue concepts
- Recursion
- Conditional statements
- Loops
- Functions
- Dictionary-based login validation
- PyCharm

The project uses the Python standard library only and does not require third-party packages.

---

## 🔄 System Flow

```text
Welcome Screen
      ↓
Admin Login
      ↓
Main Menu
      │
      ├── Urgent Order Management
      │       └── Stack / LIFO
      │
      ├── Standard Order Management
      │       └── Queue / FIFO
      │
      ├── Dashboard
      │       ├── Order Summary
      │       └── Order Search
      │
      ├── Fast Track Delivery Line
      │       └── Recursive Processing
      │
      └── Shipment Route Optimisation
```

---

## 🛡️ Input & Error Handling

The system checks several common situations and provides clear console messages instead of allowing invalid operations to interrupt the program.

Examples include:

- Invalid login details
- Invalid menu selections
- Searching for an order that does not exist
- Viewing an empty stack or queue
- Removing an order when no orders are available
- Opening route optimisation without a dispatch-ready order

---

## 🧪 Testing

The application was tested manually using different order-management scenarios.

Testing included:

- Successful and unsuccessful login attempts
- Adding urgent and standard orders
- Confirming LIFO behaviour for urgent orders
- Confirming FIFO behaviour for standard orders
- Searching orders
- Order count and dashboard output
- Fast-track recursive processing
- Route optimisation
- Invalid menu selections
- Empty order handling

---

## 🚀 Running the Project

### Requirements

- Python 3.x
- Windows, macOS, or Linux
- A terminal or Python-compatible IDE

Clone the repository:

```bash
git clone https://github.com/farshadfazeen/greentech-logistics-system.git
```

Open the project folder:

```bash
cd greentech-logistics-system
```

Run:

```bash
python greentech_logistics_system.py
```

Then use one of the demo accounts to access the application.

---

## 🎓 Academic Context

This project was developed for **Unit 19: Data Structures & Algorithms** as part of a Higher National Diploma in Computing.

The project focuses on applying data structures and algorithms to a shipment-management scenario, including:

- Stack and Queue operations
- Abstract Data Types
- LIFO and FIFO processing
- Recursion
- Searching
- Algorithm efficiency
- Error handling and testing

---

## 👤 Developer

**M Farshad**

Software Developer  
Colombo, Sri Lanka

GitHub: [@farshadfazeen](https://github.com/farshadfazeen)

---

## 📄 Note

This repository is maintained as part of my software development portfolio and demonstrates the practical use of Python, data structures, algorithms, recursion, and console-based application development.
