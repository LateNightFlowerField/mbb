# mbb - A Model Bridge Building Helper

> [!NOTE]
> This project is still being developed, information here may be inaccurate.

This program aids in creating to-scale diagrams of model bridges. It creates figures LaTeX using tikz of 5 types of trusses with customizable parameters. It makes the process of designing a model bridge fast and easy.


## Examples

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/LateNightFlowerField/mbb/blob/a9c18473ed23365f7afc9e6b82b49533da8a40e2/docs/dmktruss.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/LateNightFlowerField/mbb/blob/a9c18473ed23365f7afc9e6b82b49533da8a40e2/docs/lmktruss.svg">
<img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="">
</picture>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="docs/dmwarrentruss.png">
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/LateNightFlowerField/mbb/blob/71a00f5cd785470699c2842f13d1b62599967710/docs/dmwarrentruss.png">
   <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="">
</picture>


<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png">
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
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

