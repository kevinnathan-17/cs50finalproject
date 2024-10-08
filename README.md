# Store management webapp (for SN_electricals store)
#### Video Demo:  <https://youtu.be/5RbCXDr5uwQ?si=u5hh3ww2d_divkuL>
#### Description:

SN Electricals Web Application

Project Overview

SN Electricals is a web application designed to facilitate the management of a small electrical store. This application is built using Python and Flask and provides functionalities for inventory management, expenditure tracking, and a simple interface for future online shopping capabilities. The goal of this project is to streamline the operations of the store, making it easier for employees to keep track of inventory, manage sales, and monitor expenditures efficiently.

The application includes several key features:

Inventory Management: Employees can view, add, and search for items in the store's inventory, ensuring that stock levels are always up to date.
2. Expenditure Tracking: The application allows users to track daily expenditures related to store operations, providing insights into spending patterns.
3. Change Calculation: A dedicated page allows users to calculate change for transactions easily.
4. User-Friendly Interface: The design is modern and intuitive, making it accessible for employees with varying levels of technical expertise.

## File Descriptions

### `app.py`

The main file that contains the Flask application. It manages the routing for the application and handles all server-side logic. Key functions include:

- **Index Route**: Displays the homepage.
- **Inventory Management Route**: Handles inventory display and modification, including search functionality.
- **Sell Item Route**: Manages sales transactions by updating inventory and expenditures.
- **Expenditure Route**: Displays and manages daily expenditures, allowing users to add, remove, and export data.
- **Shop Route**: Provides a placeholder for future online shopping functionality.
- **Change Calculator Route**: Displays a page for users to calculate change based on transactions.

### `templates/index.html`

The homepage template for the web application. This page provides navigation links to other parts of the application and gives a brief introduction to the store's functionalities.

### `templates/inventory.html`

This template displays the store's inventory. It includes features to search for items, add new items, and view current stock levels.

### `templates/expenditures.html`

Displays a list of expenditures for the selected date. Users can add new expenditures, remove existing ones, and view total spending for each day.

### `templates/shop.html`

Currently a placeholder page that indicates online shopping capabilities will be implemented in the future.

### `templates/change_calculator.html`

This template provides an interface for users to calculate change based on transactions.

### `static/styles.css`

The CSS file that contains the styling for the web application. The design focuses on a modern and clean aesthetic, enhancing user experience. Key features include:

- A responsive layout that adjusts to different screen sizes.
- Use of background images and color schemes that align with a contemporary design approach.
- Clear navigation and interactive elements to improve usability.

### `static/images/`

This folder is intended to store image assets used in the web application. Currently, it contains the background image for the application, enhancing the visual appeal.

## Design Choices

The design of the SN Electricals web application was carefully considered to ensure it meets the needs of its users.

1. **User-Centric Design**: The interface is designed to be intuitive, allowing employees to navigate easily without extensive technical knowledge. The layout prioritizes essential features to enhance efficiency.

2. **Responsive Design**: The application is built to be responsive, ensuring it can be accessed on various devices, from desktops to mobile phones. This flexibility allows employees to manage the store's operations on the go.

3. **Future-Proofing**: Placeholder pages, such as the online shopping experience, are included to allow for future enhancements. This ensures that the application can evolve as the business grows and customer needs change.

4. **Focus on Functionality**: Each feature was implemented with the goal of streamlining store operations. For example, the expenditure tracking feature not only records spending but also provides insights that can help in budgeting and financial planning.

## Conclusion

The SN Electricals web application aims to improve the efficiency of store management by providing essential tools for inventory tracking and expenditure management. With a modern design and user-friendly interface, the application is well-suited to meet the needs of employees and facilitate the store's growth. As development continues, additional features such as online shopping will be implemented, further enhancing the store's capabilities.


