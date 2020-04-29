let labels = ['Never or very rarely true','Rarely true', 'Sometimes true', 'Often true','Very often or always true'];
let colorHex = ['#c51dbd','#EDB5DA', '#BCD96B', '#4E5DEC', '#ECAD4E'];

 //Global Options
    Chart.defaults.global.defaultFontFamily = 'Cantarell';
    Chart.defaults.global.defaultFontSize = 12;
    Chart.defaults.global.defaultFontColor = '#000'

let ctx = document.getElementById('myChart1').getContext('2d');
let myChart1 = new Chart(ctx, {
        type: 'doughnut',
        data: {
          datasets: [{
            data: [0, 2.6, 13.2, 39.5, 44.7],
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
              color: '#000',
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

let cty = document.getElementById('myChart2').getContext('2d');
let myChart2 = new Chart(cty, {
  type: 'doughnut',
  data: {
    datasets: [{
      data: [2.6, 7.9, 26.3, 39.5, 23.7],
      backgroundColor: colorHex
    }],
    labels: labels
  },
  options: {
    responsive: true,
        title: {
            display:true,
            text: 'Want to watch new content'
        },

    legend: {
      position: 'bottom'
    },
    plugins: {
      datalabels: {
        color: '#000',
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