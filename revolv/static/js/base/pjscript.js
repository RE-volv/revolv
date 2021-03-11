// input data
const data = [
  {
    name: 'BIPOC',
    percentage: 9, 
    value: 9, 
    color: '#0789F8',
    projects: 7,
  },
  {
    name: 'Veterans',
    percentage: 3,
    value: 3,
    color: '#F9BA00',
    projects: 2,
  },
  {
    name: 'Youth',
    percentage: 11,
    value: 11,
    color: '#74C7B8',
    projects: 8,
  },
  {
    name: 'Arts',
    percentage: 7,
    value: 7,
    color: '#00AF91',
    projects: 6,
  },
  {
    name: 'Housing',
    percentage: 19,
    value: 19,
    color: '#F8DC81',
    projects: 15,
  },
  {
    name: 'Health',
    percentage: 13,
    value: 13,
    color: '#FF8585',
    projects: 11,
  },
  {
    name: 'Animals',
    percentage: 3,
    value: 3,
    color: '#FE8C00',
    projects: 3,
  },
  {
    name: 'Faith',
    percentage: 15,
    value: 15,
    color: '#A6A8F8',
    projects: 12,
  },
  {
    name: 'Conservation',
    percentage: 1,
    value: 2,
    color: '#3ABC60',
    projects: 1,
  },
  {
    name: 'Community Development',
    percentage: 11,
    value: 11,
    color: '#47D7A8',
    projects: 8,
  },
  {
    name: 'Food/Agriculture',
    percentage: 9,
    value: 9,
    color: '#3BCB60',
    projects: 7,
  },
];

const svg = d3
  .select('svg');

const viewBox = svg.attr('viewBox');
const regexViewBox = /\d+ \d+ (\d+) (\d+)/;

const [, viewBoxWidth, viewBoxHeight] = viewBox.match(regexViewBox).map(item => Number.parseInt(item, 10));

const margin = {
  top: 20,
  right: 20,
  bottom: 20,
  left: 20,
};

const width = viewBoxWidth - (margin.left + margin.right);
const height = viewBoxHeight - (margin.top + margin.bottom);


const radius = Math.min(width, height) / 2;

const strokeWidth = 10;

const group = svg
  .append('g')
  .attr('transform', `translate(${margin.left} ${margin.top})`);


const groupDefault = group
  .append('g')
  .attr('transform', `translate(${width / 2} ${height / 2})`);


groupDefault
  .append('circle')
  .attr('cx', 0)
  .attr('cy', 0)
  .attr('r', radius)
  .attr('transform', 'rotate(-90)')
  .attr('fill', 'none')
  .attr('stroke', 'hsla(0, 0%, 0%, 0.08')
  .attr('stroke-width', strokeWidth)
  .attr('stroke-linecap', 'round')
  .attr('stroke-dasharray', radius * 3.14 * 2)
  .attr('stroke-dashoffset', radius * 3.14 * 2);


const groupText = group
  .append('svg:image')
  .attr("x", 180)
  .attr("y", 80)
  .attr('width', 200)
  .attr('height', 100)
  .attr("xlink:href", "https://re-volv.org/static/images/revolvorange.png")

      


const pie = d3
  .pie()
  .sort(null)
  .padAngle(0.12)
  .value(d => d.value);

const arc = d3
  .arc()
  .innerRadius(radius)
  .outerRadius(radius);


const groupArcs = group
  .append('g')
  .attr('transform', `translate(${width / 2} ${height / 2})`);

const groupsArcs = groupArcs
  .selectAll('g')
  .data(pie(data))
  .enter()
  .append('g');


groupsArcs
  .append('path')
  .attr('d', arc)
  .attr('fill', 'none')
  .attr('stroke', d => d.data.color)
  .attr('stroke-width', strokeWidth * 0.8)
  .attr('stroke-linecap', 'round')
  .attr('stroke-linejoin', 'round')
  .attr('stroke-dasharray', radius * 3.14 * 2)
  .attr('stroke-dashoffset', radius * 3.14 * 2);


groupsArcs
  .append('line')
  .attr('x1', 0)
  .attr('x2', (d) => {
    const [x] = arc.centroid(d);
    return x > 0 ? '25' : '-25';
  })
  .attr('y1', 0)
  .attr('y2', 0)
  .attr('stroke', ({ data: d }) => d.color)
  .attr('stroke-width', 1.5)
  .attr('transform', (d) => {
    const [x, y] = arc.centroid(d);
    const offset = x > 0 ? 20 : -20;
    return `translate(${x + offset} ${y})`;
  })
  .attr('stroke-dasharray', 25)
  .attr('stroke-dashoffset', 25);


groupsArcs
  .append('text')
  .attr('x', 0)
  .attr('y', 0)
  .attr('font-size', 8)
  .attr('text-anchor', (d) => {
    const [x] = arc.centroid(d);
    return x > 0 ? 'start' : 'end';
  })
  .attr('transform', (d) => {
    const [x, y] = arc.centroid(d);
    const offset = x > 0 ? 50 : -50;
    return `translate(${x + offset} ${y})`;
  })
  .html(({ data: d }) => `
    <tspan x="0">${d.name}:</tspan><tspan x="0" dy="10" font-size="8">${d.percentage}% / ${d.projects} Project(s)</tspan>
  `)
  .style('opacity', 0)
  .style('visibility', 'hidden');


groupDefault
  .select('circle')
  .transition()
  .ease(d3.easeExp)
  .delay(200)
  .duration(2000)
  .attr('stroke-dashoffset', '0')
  .on('end', () => {
    const paths = document.querySelectorAll('svg g g path');
    paths.forEach((path) => {
      const length = path.getTotalLength();
      path.setAttribute('stroke-dasharray', length);
      path.setAttribute('stroke-dashoffset', length);
    });

    const duration = 1000;

    d3
      .selectAll('svg g g path')
      .transition()
      .ease(d3.easeLinear)
      .delay((d, i) => i * duration)
      .duration(duration)
      .attr('stroke-dashoffset', 0);


    d3
      .selectAll('svg g g line')
      .transition()
      .ease(d3.easeLinear)
      .delay((d, i) => i * duration + duration / 2.5)
      .duration(duration / 3)
      .attr('stroke-dashoffset', 0);


    d3
      .selectAll('svg g g text')
      .transition()
      .ease(d3.easeLinear)
      .delay((d, i) => i * duration + duration / 2)
      .duration(duration / 2)
      .style('opacity', 1)
      .style('visibility', 'visible');
  });