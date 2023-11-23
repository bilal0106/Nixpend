document.getElementById('dataForm').addEventListener('submit', function(e) { 
    e.preventDefault();    
    const formData = new FormData(this);    
    fetch('/submit', {        
        method: 'POST',        
        body: formData 
    }).then(response => response.blob()) 
    .then(blob => {        
        const url = window.URL.createObjectURL(blob);        
        window.open(url, '_blank'); 
    }); 
});
