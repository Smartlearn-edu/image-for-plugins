# Case Study Question Type for Moodle (`qtype_casestudy`)

[![Moodle 4.0+](https://img.shields.io/badge/Moodle-4.0%2B-f37f26?style=flat-square&logo=moodle&logoColor=white)](https://moodle.org)
[![PHP 7.4 - 8.3](https://img.shields.io/badge/PHP-7.4%20--%208.3-777bb4?style=flat-square&logo=php&logoColor=white)](https://php.net)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0)
[![Built by SmartLearn Education](https://img.shields.io/badge/Built%20by-SmartLearn%20Education-00a884?style=flat-square)](https://smartlearn-edu.com)

**A powerful, enterprise-grade container question type for Moodle that allows educators to group multiple standard Moodle questions together under a single clinical case, reading passage, or descriptive scenario.**

---

## 🌟 Overview

In complex assessments—such as **medical clinical case studies**, **legal scenario evaluations**, **data science challenges**, and **reading comprehension tests**—educators frequently need to ask multiple dependent questions about a single, detailed scenario.

Traditionally in Moodle, this forced instructors to either:
1. Duplicate long scenario texts across multiple separate questions, or
2. Force students to scroll back and forth across disjointed quiz pages while losing context of the patient vitals or reference passage.

The **Case Study Question Type (`qtype_casestudy`)** solves this problem permanently by acting as a native **Container Question** within the Moodle Quiz engine. It presents a unified, highly engaging user interface where the central scenario remains persistently accessible while students navigate through structured sub-questions.

---

## ✨ Key Features

- **🚀 Native Quiz Engine Integration:** Works seamlessly with Moodle Quiz, Question Bank, Question Versioning, and standard gradebook reporting.
- **🎨 Dual Responsive Layouts:**
  - **Stacked Carousel Mode (Default):** Displays the case scenario in a sticky hero header with a smooth, interactive slide carousel below for answering sub-questions step-by-step.
  - **Split-View Mode:** An advanced desktop layout that places the case scenario in a sticky left-hand pane (`50%` width) while displaying sub-questions in a scrollable right-hand column (`50%` width)—ideal for complex clinical examinations.
- **🛡️ Bulletproof State & Grading Architecture:**
  - Uses manual sub-question rendering with namespaced form fields (`subq_{id}_{field}`).
  - Completely eliminates Moodle's "shuffle desync" and ordering mismatch bugs commonly found in multi-answer container plugins.
- **📊 Granular Feedback & Review:**
  - Full support for right/wrong answer styling, specific sub-question feedback, and general case feedback.
- **💾 Complete Backup, Restore & Duplication Support:**
  - Sub-questions and weights are automatically preserved during course backups, imports, and quiz duplicates.
- **📦 Moodle XML Export & Import:**
  - Effortlessly export and import case study questions along with their nested sub-questions.

---

## 🖥️ Layout Modes

### 1. Stacked Carousel Mode (Default)
Ideal for both desktop and mobile devices. Students read the scenario at the top of the card and use **Previous / Next** controls (or direct slide indicators) to move through each diagnostic sub-question without visual clutter.

### 2. Side-by-Side Split-View Mode
Optimized for widescreen desktop assessments. The left pane locks the clinical case, patient history, and vital signs in place (`position: sticky`), allowing students to scroll through sub-questions on the right while continuously referencing the case details.

---

## 🧩 Supported Sub-Question Types

`qtype_casestudy` allows instructors to attach standard Moodle questions directly from their Question Bank as sub-questions:

| Question Type | Status | Features Supported |
| :--- | :---: | :--- |
| **Multiple Choice (Single Answer)** | ✅ Supported | Option shuffling, custom numbering, specific feedback |
| **Multiple Choice (Multiple Answer)** | ✅ Supported | Partial credit, checkbox rendering, shuffle preservation |
| **True / False** | ✅ Supported | Standard binary evaluation & feedback |
| **Short Answer** | ✅ Supported | Case-insensitive & case-sensitive text matching |
| **Numerical** | ✅ Supported | Tolerance ranges & unit handling |
| **Matching** | ✅ Supported | Dropdown stem matching with persistent order state |
| **Calculated / Simple Calculated** | ✅ Supported | Dynamic numerical generation |
| **Calculated Multichoice** | ✅ Supported | Formula-based multiple choice |

*Coming soon in future releases: Cloze (Embedded Answers), Drag and Drop into Text, Select Missing Words, and Open-ended Essay.*

---

## 🛠️ Installation

### Method 1: ZIP Installation (Recommended)
1. Download the latest release `.zip` package.
2. Log in to your Moodle site as an Administrator.
3. Navigate to **Site administration** → **Plugins** → **Install plugins**.
4. Upload the ZIP file and select **Question type (`qtype`)** as the plugin type.
5. Follow the Moodle upgrade prompts to complete installation.

### Method 2: Manual / Git Installation
1. Clone or extract the plugin code into your Moodle installation directory under:
   ```bash
   /path/to/moodle/question/type/casestudy
   ```
2. Log in as an Administrator and visit **Site administration** → **Notifications** to trigger the database upgrade tables.

---

## 📖 Instructor User Guide

### 1. Creating a Case Study Question
1. Navigate to your course **Question Bank** or edit a **Moodle Quiz**.
2. Click **Create a new question** and select **Case Study**.
3. In the **Question name** field, enter an internal reference title (e.g., *Cardiology Case 04 - Dyspnea*).
4. In the **Question text** editor, write the comprehensive case scenario, patient vitals, reading passage, or reference data.
5. Under **Case Options**, choose your preferred **Question Layout**:
   - *Stacked Carousel (Default)*
   - *Split-View (Desktop Side-by-side)*
6. Set the **Default mark** (total aggregate points for the entire case study).

### 2. Attaching & Managing Sub-Questions
1. Once saved, click **Manage Sub-questions** on the question edit screen.
2. Click **Add from Question Bank** to attach existing Multiple Choice, True/False, Short Answer, Matching, or Numerical questions.
3. Assign custom **Weight (%)** values to each sub-question so the total sums to `100%`.
4. Use the reorder handles to arrange the sub-questions into a logical diagnostic progression.

---

## 🏗️ Technical Architecture

Unlike legacy container approaches that attempt to instantiate "phantom" `$qa->render_question()` objects (which suffer from Moodle engine shuffle-state desyncs), `qtype_casestudy` implements a robust manual rendering architecture:
- Each sub-question is rendered via custom methods inside `qtype_casestudy_renderer`.
- Input fields are namespaced (`subq_{id}_{prefix}`) so Moodle's core form processing cleanly validates and grades each sub-question independently.
- Complete question attempts are recorded cleanly in `mdl_question_attempts` without polluting `question_usages`.

---

## 🤝 Compatibility & Requirements

- **Moodle Core:** 4.0, 4.1, 4.2, 4.3, 4.4, 4.5+
- **PHP Version:** PHP 7.4, 8.0, 8.1, 8.2, 8.3
- **Database:** MySQL, PostgreSQL, MariaDB, MSSQL
- **Theme Compatibility:** Boost, Classic, Remui, Moove, and all Bootstrap 4/5 based Moodle themes.

---

## 📄 License & Credits

- **Copyright:** © 2026 SmartLearn Education (`smartlearn-edu.com`)
- **License:** GNU General Public License v3.0 or later (GPL-3.0)
- **Author:** Developed by SmartLearn Education for the global Moodle community.
