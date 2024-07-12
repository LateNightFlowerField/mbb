# mbb - A Model Bridge Building Helper

> [!NOTE]
> This project is still being developed, information here may be inaccurate.

This program aids in creating to-scale diagrams of model bridges. It creates figures LaTeX using tikz of 5 types of trusses with customizable parameters. It makes the process of designing a model bridge fast and easy.


## Examples

K Truss

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/dmktruss.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/lmktruss.svg">
<img alt="The outline of a K truss bridge." src="">
</picture>

Warren Truss

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/dmwarrentruss.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/lmwarrentruss.svg">
   <img alt="The outline of a Warren truss bridge." src="">
</picture>


## Usage

Basic Pratt truss:

```shell
$ python bridge.py -t pratt
```



Warren truss that spans 28 cm:

```shell
$ python bridge.py -t warren -l 28
```



K truss with 6 segments

```shell
$ python bridge.py -t k -s 6 
```


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

- [x] Configure overhang on both sides
- [ ] Create bridge by height and length
- [ ] Individual part diagrams and counts
- [ ] Micro-configuration of bridge
- [x] Diagrams of side connections (automatic?)
- [x] More truss types, and possibly arches
- [x] Add option for adding extra per segment to total length or weight
- [ ] Create way to specify material limits
- [ ] Stress simulations
- [ ] Add glue weight calculations
- [ ] Add estimated build time
- [ ] Add auto image and document generation
- [ ] Improve aesthetics 
- [ ] Refactor to use bridge and piece classes and objects
- [ ] Create under supports
- [ ] Cutting and joint guides

## FAQ

1. Why use python and latex instead of x tool or language?
    
    Because. <details>I am familiar with python and LaTeX and they work well for my goals currently. Being able to create and print scale diagrams relies on the great typesetting LaTeX offers. If a better way comes up though I my consider porting the project.</details>
2. What is your favorite type of bridge? <br/>
    I really like the warren because of its simplicity and symmetry.

