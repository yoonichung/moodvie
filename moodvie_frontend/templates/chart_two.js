
let ctx = document.getElementById('myChart2').getContext('2d');
let labels = ['Rarely true', 'Sometimes true', 'Often true','Very often or always true'];
let colorHex = ['#EDB5DA', '#BCD96B', '#4E5DEC', '#ECAD4E'];

 //Global Options
    Chart.defaults.global.defaultFontFamily = 'Cantarell';
    Chart.defaults.global.defaultFontSize = 12;
    Chart.defaults.global.defaultFontColor = 'black'

let myChart2 = new Chart(ctx, {
  type: 'doughnut',
  data: {
    datasets: [{
      data: [2.6, 13.2, 39.5, 44.7],
      backgroundColor: colorHex
    }],
    labels: labels
  },
  options: {
    responsive: true,
        title: {
            display:true,
            text: 'Mood influences browsing and consumption behaviours'
        },

    legend: {
      position: 'bottom'
    },
    plugins: {
      datalabels: {
        color: '#fff',
        anchor: 'end',
        align: 'start',
        offset: -10,
        borderWidth: 2,
        borderColor: '#fff',
        borderRadius: 25,
        backgroundColor: (context) => {
          return context.dataset.backgroundColor;
        },
        font: {
          weight: 'bold',
          size: '10'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})