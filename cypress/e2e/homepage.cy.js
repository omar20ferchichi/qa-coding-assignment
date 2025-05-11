describe('Homepage Test', () => {
    it('Should load homepage and verify title', () => {
      cy.visit('https://www.saucedemo.com/'); // Replace with your site
      cy.title().should('include', 'Example Domain'); // Adjust as needed
    });
  });
  