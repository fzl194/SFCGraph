---
id: UDG@20.15.2@ConfigObject@IPFARMGLOBAL
type: ConfigObject
name: IPFARMGLOBAL（IPFarm全局参数）
nf: UDG
version: 20.15.2
object_name: IPFARMGLOBAL
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# IPFARMGLOBAL（IPFarm全局参数）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置系统中的心跳检测次数和检测周期等参数，用于对每个server的网络状态进行检查，如果系统与其中的某些server无法通信，则在进行业务的时候不选择这些服务器，保证从系统出去的报文能到达一个可用的server上，以减少业务处理失败的可能性。

心跳检测的具体做法是：系统定时向IP farm中的server发送ICMP报文，server收到报文后会对系统做出应答。如果系统在一定的时间内能收到server的应答，则认为这个server的状态为up。如果系统连续几次发送的ICMP报文都收不到响应，则认为server处于down状态。不论server处于up状态还是down状态，系统都会继续不断地向其发送ICMP报文，更新server的状态。

该命令也用于配置整机的针对IP farm配置的重定向选择server的负荷分担方式。一个IP farm中的每个server都是相同的，这些server共同分担系统发出的业务，系统用一些固定的方式从一个IP farm中选取一个状态为up的server，以便在不影响业务进行的前提下保证IP farm下的server的负荷相对平衡。当一个业务到来时，系统找到对应的ip-farm1，并按配置的负荷分担方式在farm选取一个状态为up的server1，此时又有ip-farm1的业务到来时，系统会根据负荷分担方式选择状态为up的server3来处理这个业务，从而很好地保证了业务快速有效的进行。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-IPFARMGLOBAL]] · LST IPFARMGLOBAL
- [[command/UDG/20.15.2/SET-IPFARMGLOBAL]] · SET IPFARMGLOBAL

## 证据

- 原始手册：`evidence/UDG/20.15.2/IPFARMGLOBAL.md`
- 原始手册：`evidence/UDG/20.15.2/IPFARMGLOBAL.md`
