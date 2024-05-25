# mbb - A Model Bridge Building Helper

> [!NOTE]
> This project is still being developed, information here may be inaccurate.

This program aids in creating to-scale diagrams of model bridges. It creates figures LaTeX using tikz of 5 types of trusses with customizable parameters. It makes the process of designing a model bridge fast and easy.


## Examples

<picture>
    <source media="(perfers-color-scheme: dark)" srcset="docs/dmktruss.svg">
    <source media="(perfers-color-scheme: light)" srcset="docs/lmktruss.svg">
</picture>

<picture>
    <source media="(perfers-color-scheme: dark)" srcset="docs/dmwarrentruss.svg">
    <source media="(perfers-color-scheme: light)" srcset="docs/lmwarrentruss.svg">
</picture>

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
- [ ] Individual part diagrams and counts
- [ ] Micro-configuration of bridge
- [ ] Diagrams of side connections (automatic?)
- [ ] More truss types, and possibly arches
- [ ] Add option for adding extra per segment to total length
- [ ] Create way to specify material limits
- [ ] Stress simulations
- [ ] Add glue weight calculations
- [ ] Add estimated build time
- [ ] Add auto image and document generation
- [ ] Improve aesthetics  

## FAQ

1. Why use python and latex instead of x tool or language?
    
    no.
    <details>I am familiar with python and latex and they work well for my goals currently. Being able to create and print scale diagrams relies on the great typesetting LaTeX offers. If a better way comes up though I my consider porting the project.</details>
2. What is your favorite type of bridge?
    I really like the warren because of its simplicity and symmetry.

