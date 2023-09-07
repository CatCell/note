# 1.1 Internet

## part1

节点分为主机节点，中转节点。中转节点例如路由器 工作在网络层。交换机 （switch）工作在链路层。负载均衡设备，防火墙
边分为接入链路（链接主机节点和中转节点），骨干链路（可以细分为靠近骨干和边缘）
协议允许设备之间互操作，基础是遵守相同的协议。（定义:对等层的实体在通信过程中应该遵守的协议集合，包括语义...）
互联网是 tcp/ip 协议为主的协议族中最大的网。同样遵守协议但是不开放的网络不叫 Internet,叫 intronet（企业网）。
端系统(endsystem):能够通信的网络应用进程，也叫 host，

## part2

ietf 对互联网想法公开编号
协议包括格式（语法和语义都理解相同这是互操作的基础）时序和动作（比喻为陌生人的请求帮助），
从使用角度看，互联网是分布式应用进程和为他提供通信服务的基础设施（应用进程下的实体），分布式应用是网络存在的理由。基础设施为分布式应用提供服务的方式为 api
基础设施提供的服务可以分为两种面向连接的服务（tcp）无连接的服务（udp）

# 1.2 网络边缘

互联网按照组成类型聚类，方的节点集合叫边缘系统位于网络边缘，圆的集合叫做网络核心，圆方连线叫做 acess 接入系统。于是分为三个子系统。

switch 叫做开关，瞬间的开关控制连接切换通信的开闭
应用通信模式分为**c/s 模式**（客户端服务器模式），客户端去主动请求，服务器被动响应，客户端后运行服务端先运行，是主从模式。server farm 和通信链路扩容，为解决客户端过多问题。综合来说，cs 可扩展能力差，差错会导致功能断崖式下降。
**p2p 模式**，这种分布式应用进程的特点就是每个进程既是 c 又是 s。（分布式的文件分发系统迅雷，电驴。ftp 是典型 cs 模式）
tcp 提供服务特性:可靠的（不错丢，重复，时序）。rdt（reliable data trans）流量控制能力（至强和小强通信的例子）拥塞控制能力（感知路径的堵塞程度）
udp 提供无连接的服务。特点是不可靠（时间代价小，节约经济，适合网络实时多媒体应用），无流量控制，拥塞控制。(事务性应用例如域名解析查询)