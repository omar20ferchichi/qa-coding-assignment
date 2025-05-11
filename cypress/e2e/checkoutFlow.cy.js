/// <reference types="cypress" />

describe('Checkout Process Test', () => {
    // Utility function to calculate total price (item total + tax)
    function calculateTotalPrice(itemPrices) {
      const itemTotal = itemPrices.reduce((acc, price) => acc + price, 0);
      const tax = itemTotal * 0.08; // 8% tax
      return +(itemTotal + tax).toFixed(2);
    }
  
    // Helper function to get the current timestamp for logs
    function getTimestamp() {
      return new Date().toISOString();
    }
  
    it('should complete the checkout process correctly', () => {
      const username = 'standard_user';
      const password = 'secret_sauce';
      const itemPrices = [];
  
      cy.log('==================== TEST STARTED ====================');
      cy.log(`Test started at: ${getTimestamp()}`);
      cy.log('Test Name: Checkout Process Test');
  
      // Step 1: Log into the site
      const step1Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 1: Logging in with credentials`);
      cy.visit('https://www.saucedemo.com/');
      cy.get('#user-name').type(username);
      cy.get('#password').type(password);
      cy.get('#login-button').click();
      cy.wait(2000); // Wait for login to complete
      cy.log(`[${getTimestamp()}] Step 1 completed in ${(Date.now() - step1Start) / 1000}s`);
      cy.log('Logged in successfully');
  
      // Step 2: Sort items by lowest price
      const step2Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 2: Sorting items by lowest price`);
      cy.get('.product_sort_container').select('lohi');
      cy.wait(2000); // Wait for items to reload with new sorting
      cy.log(`[${getTimestamp()}] Step 2 completed in ${(Date.now() - step2Start) / 1000}s`);
      cy.log('Sorted items by price (Lowest to Highest)');
  
      // Step 3: Add two or more items to the shopping cart
      const step3Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 3: Adding two items to the cart`);
      cy.get('.inventory_item').each(($el, index) => {
        if (index < 2) {
          cy.wrap($el).find('.inventory_item_price').invoke('text').then((priceText) => {
            itemPrices.push(parseFloat(priceText.replace('$', '')));
          });
          cy.wrap($el).find('button').click();
          cy.wait(1000); // Wait for item to be added to the cart
        }
      });
      cy.wait(2000);
      cy.log(`[${getTimestamp()}] Step 3 completed in ${(Date.now() - step3Start) / 1000}s`);
      cy.log('Added two items to the cart');
  
      // Step 4: Visit the shopping cart
      const step4Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 4: Navigating to the shopping cart`);
      cy.get('.shopping_cart_link').click();
      cy.wait(2000); // Wait for cart page to load
      cy.log(`[${getTimestamp()}] Step 4 completed in ${(Date.now() - step4Start) / 1000}s`);
  
      // Step 5: Assert that the items in the cart are correct
      const step5Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 5: Verifying items in the cart`);
      cy.get('.cart_item').should('have.length', 2);
      cy.get('.cart_item .inventory_item_price').then(($prices) => {
        const cartItemPrices = [...$prices].map(el => parseFloat(el.innerText.replace('$', '')));
        expect(cartItemPrices).to.deep.equal(itemPrices);
      });
      cy.log(`[${getTimestamp()}] Step 5 completed in ${(Date.now() - step5Start) / 1000}s`);
      cy.log('Verified correct items in the cart');
  
      // Step 6: Proceed to Checkout
      const step6Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 6: Clicking on Checkout button`);
      cy.get('.checkout_button').click();
      cy.wait(2000); // Wait for checkout page to load
      cy.log(`[${getTimestamp()}] Step 6 completed in ${(Date.now() - step6Start) / 1000}s`);
  
      // Step 7: Fill in Checkout details
      const step7Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 7: Filling in checkout details`);
      cy.get('#first-name').type('John');
      cy.get('#last-name').type('Doe');
      cy.get('#postal-code').type('12345');
      cy.get('.cart_button').click();
      cy.wait(2000); // Wait for the checkout overview page
      cy.log(`[${getTimestamp()}] Step 7 completed in ${(Date.now() - step7Start) / 1000}s`);
  
      // Step 8: Assert purchasing correct items
      const step8Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 8: Verifying purchased items in checkout overview`);
      cy.get('.cart_item').should('have.length', 2);
      cy.log(`[${getTimestamp()}] Step 8 completed in ${(Date.now() - step8Start) / 1000}s`);
  
      // Step 9: Assert the total price
      const step9Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 9: Verifying total price calculation`);
      cy.get('.summary_total_label').invoke('text').then((totalText) => {
        const totalPrice = parseFloat(totalText.replace('Total: $', ''));
        const expectedTotal = calculateTotalPrice(itemPrices);
        expect(totalPrice).to.eq(expectedTotal);
      });
      cy.log(`[${getTimestamp()}] Step 9 completed in ${(Date.now() - step9Start) / 1000}s`);
      cy.log('Verified total price');
  
      // Step 10: Finish checkout
      const step10Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 10: Finishing checkout`);
      cy.get('#finish').click();
      cy.wait(2000); // Wait for confirmation page
      cy.log(`[${getTimestamp()}] Step 10 completed in ${(Date.now() - step10Start) / 1000}s`);
  
      // Step 11: Assert cart is empty
      const step11Start = Date.now();
      cy.log(`[${getTimestamp()}] Step 11: Verifying cart is empty after checkout`);
      cy.get('.shopping_cart_link').click();
      cy.get('.cart_item').should('have.length', 0);
      cy.log(`[${getTimestamp()}] Step 11 completed in ${(Date.now() - step11Start) / 1000}s`);
  
      cy.log('==================== TEST FINISHED ====================');
      cy.log(`Test ended at: ${getTimestamp()}`);
    });
  });
  