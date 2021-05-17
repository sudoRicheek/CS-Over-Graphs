# CS-Over-Graphs
[AIP Project] This repository contains the implementation of our course project for Advanced Image Processing [CS754] : Compressed Sensing Over Graph Structures


In this project we try to explore the utility of Compressive Sensing to identify the central nodes of information flow (i.e nodes with the highest betweenness centrality). We use the following datasets: [Facebook](https://snap.stanford.edu/data/ego-Facebook.html) and [GNUTELLA](https://snap.stanford.edu/data/p2p-Gnutella08.html) for studying the viability/performance of the **DICeNod Algorithm** as defined in the [paper](https://link.springer.com/article/10.1007/s13278-018-0506-1#:~:text=In%20this%20paper%2C%20we%20propose%20a%20compressive%20sensing%2Dbased%20framework,given%20neighborhood%20around%20each%20node).

## Network Plots with the Top 10 central nodes
#### Size of the nodes gives an idea about the amount of information flow, through it.

<table>
  <tr>
    <td> Facebook Network<strong>(Large Graph Layout)</strong> with labelled Top 10 nodes with highest information flow <img src="/DICeNOD/networkPlots/facebookTop10.png"  alt="1" width = 450 ></td>
    <td> GNUTELLA Network<strong>(Kamada Kawai)</strong> with labelled Top 10 nodes with highest information flow <img src="/DICeNOD/networkPlots/gnutellaTop10.png" alt="2" width = 450 ></td>
   </tr> 
</table>

## We also studied the change in reconstruction error with the increase in the number of measurements and other parameters.

<p align="center">
  <img src="/DICeNOD/performance_gnutella/plots/RelMSEvsM_gnu.jpg" width="420" />
  <img src="/DICeNOD/performance_gnutella/plots/RelMSEvsD_gnu.jpg" width="420" /> 
</p>

<p align="center">
  <img src="/DICeNOD/performance_gnutella/plots/CatERRvsM_gnu.jpg" width="420" />
  <img src="/DICeNOD/performance_gnutella/plots/CatERRvsD_gnu.jpg" width="420" /> 
</p>

## You can find rest of the plots/results/mathematical formulations/theoretical guarantees in the [Project Report](https://github.com/sudoRicheek/CS-Over-Graphs/blob/main/Project%20Report.pdf). You can check out the implementation in DICeNOD sub-directory.  

## Authors 

Name | Contact
------------ | -------------
[Richeek Das](https://github.com/sudoRicheek) | richeek@cse.iitb.ac.in
[Aaron Jerry Ninan](https://github.com/aaroncodebro) | 190100001@iitb.ac.in

**May 2021.**
