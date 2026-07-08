---
id: UNC@20.15.2@ConfigObject@DNSN
type: ConfigObject
name: DNSN（DNS NAPTR记录）
nf: UNC
version: 20.15.2
object_name: DNSN
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DNSN（DNS NAPTR记录）

## 说明

**适用网元：SGSN、MME**

该命令用于配置 “FQDN” （全称标准规范域名）与网元接口的对应关系。

在Attach、建立PDN连接、TAU、Handover等流程中，都会涉及到 “S-GW” 、 “P-GW” 、 “MME” 等网元的选择，并解析出网元的地址信息。以前采用的是域名到网元地址的一对一映射机制，为了提高组网运作性能，减少信令的传输延时，提出了智能网关选择的策略。比如按照组网方式，在Attach流程中尽量选择 “S-GW” 和 “P-GW” 合一的节点，可以减少信令的传输时延。

该命令可以配置域名（FQDN）与网元节点间多对多的对应关系。当LICENSE支持激活智能网元选择功能且功能开关打开时，由于同一 “FQDN” 可以与多个 “HSINDEX” 配置对应关系，因此在查询过程中，同一 “FQDN” 对应的查询 “HSINDEX” 结果可能存在多个（ “ENTITY” 、 “INTERFACETYPE” 配置相同），这就需要利用智能网元选择策略（选择合一/选择拓扑关系最近）选择出最优的网元节点，而网元节点与IP地址的对应关系是在命令 [**ADD IPV4DNSH**](../DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) 、 [**ADD IPV6DNSH**](../DNS Hostfile管理/增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md) 中配置。当智能网元选择功能关闭或LICENSE不支持时，查询出的多个结果直接按照优先级/权重返回。

## 操作本对象的命令

- [ADD DNSN](command/UNC/20.15.2/ADD-DNSN.md)
- [LST DNSN](command/UNC/20.15.2/LST-DNSN.md)
- [MOD DNSN](command/UNC/20.15.2/MOD-DNSN.md)
- [RMV DNSN](command/UNC/20.15.2/RMV-DNSN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改DNS-NAPTR记录(MOD-DNSN)_72345491.md`
- 原始手册：`evidence/UNC/20.15.2/删除DNS-NAPTR记录(RMV-DNSN)_26305700.md`
- 原始手册：`evidence/UNC/20.15.2/增加DNS-NAPTR记录(ADD-DNSN)_72225569.md`
- 原始手册：`evidence/UNC/20.15.2/查询DNS-NAPTR记录(LST-DNSN)_26145892.md`
