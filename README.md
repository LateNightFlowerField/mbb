# mbb - A Model Bridge Building Helper

This porgram aids in creating to-scale diagrams of model bridges. It creates figures LaTeX using tikz of 5 types of trusses with customizable parameters. It makes the process of desinging a model bridge fast and easy.


## Examples

![](docs/ktruss.svg)

![](docs/warrentruss.svg)

## Configuration

mbb has a number of configurable options with more to come.

- Truss type (Warren, Howe, Pratt, Bailey, K)
- Length of bridge
- Number of segments
- Overhang
- Show simple stats
- Width of material
- Style options for tikz lines
- Writing to an image
- Material density

## Plans

- [ ] Configure overhang on both sides
- [ ] Create bridge by height and length
- [ ] Individul part diagrams and counts
- [ ] Micro-configuration of bridge
- [ ] Diagrams of side connections (automatic?)
- [ ] More truss types, and possibly arches
- [ ] Add option for adding extra per segment to total length
- [ ] Create way to specify material limits
- [ ] Stress simulations
- [ ] Add glue weight calculations
- [ ] Add estimated build time
- [ ] Add auto image and document genoration
- [ ] Improve asethtics  

