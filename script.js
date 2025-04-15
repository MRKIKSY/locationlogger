
window.onload = () => {
    window.open('petition.pdf', '_blank');
  };
  
  document.getElementById('sendBtn').addEventListener('click', () => {
    const subject = encodeURIComponent("Petition Against Sujimoto Group");
    const body = encodeURIComponent(`Dear EFCC,\n\nPlease find attached a petition regarding financial irregularities and potential investment violations by Sujimoto Group.\n\nBest regards,\n[Your Name]\n\nNote: Kindly find the petition PDF attached.`);
    window.location.href = `mailto:info@efcc.gov.ng?subject=${subject}&body=${body}`;
  });
  